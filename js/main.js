// Vector Logistics: the menu, the year, and the contact form (Web3Forms).
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  var y = document.getElementById('y');
  if (y) y.textContent = new Date().getFullYear();

  var form = document.getElementById('contact-form');
  if (!form) return;
  var result = document.getElementById('form-result');
  var button = form.querySelector('button[type="submit"]');
  var KEY_PLACEHOLDER = 'WEB3FORMS_ACCESS_KEY';

  function show(kind, html) {
    result.className = 'notice show ' + kind;
    result.innerHTML = html;
  }

  // "I have a question" hides the truck details; "Become my dispatcher" shows them.
  function syncChoice() {
    var picked = form.querySelector('input[name="request"]:checked');
    var dispatch = !picked || picked.value.indexOf('Dispatch') === 0;
    form.querySelectorAll('.dispatch-only').forEach(function (el) { el.hidden = !dispatch; });
  }
  form.querySelectorAll('input[name="request"]').forEach(function (r) { r.addEventListener('change', syncChoice); });
  syncChoice();

  var fallback = 'Please call or text <a href="tel:8648241536">(864) 824-1536</a>, or email <a href="mailto:rusty@vldispatching.com">rusty@vldispatching.com</a>.';

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var missing = Array.prototype.filter.call(form.querySelectorAll('[required]'), function (el) {
      return !el.value.trim() || (el.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value.trim()));
    });
    if (missing.length) {
      missing[0].focus();
      show('err', 'Please fill in your name, phone, a valid email and a message.');
      return;
    }
    var data = Object.fromEntries(new FormData(form));
    if (!data.access_key || data.access_key === KEY_PLACEHOLDER) {
      show('err', 'Our form is being set up and can\'t send yet. ' + fallback);
      return;
    }
    if (data.botcheck) return;            // filled in by a bot, not a person
    delete data.botcheck;
    data.subject = (data.request && data.request.indexOf('Dispatch') === 0 ? 'New carrier: ' : 'Question: ') +
                   (data.company || data.name) + ' (Vector Logistics website)';
    data.replyto = data.email;
    button.disabled = true;
    button.textContent = 'Sending…';
    fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) { return r.json(); }).then(function (json) {
      if (json && json.success) {
        form.reset();
        syncChoice();
        show('ok', '<strong>Thanks, your message is on its way.</strong> Rusty will get back to you shortly. If it\'s urgent, call or text <a href="tel:8648241536">(864) 824-1536</a>.');
      } else {
        show('err', 'Your message didn\'t go through' + (json && json.message ? ' (' + json.message + ')' : '') + '. ' + fallback);
      }
    }).catch(function () {
      show('err', 'Your message didn\'t go through: check your connection and try again. ' + fallback);
    }).finally(function () {
      button.disabled = false;
      button.textContent = 'Send message';
    });
  });
})();
