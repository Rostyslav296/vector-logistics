"""Builds the three pages of the Vector Logistics site (index, about, contact) from one header and footer,
so they stay alike. Edit the text here, then run:  python3 tools/build_site.py
(The Web3Forms access key goes in the contact form below: WEB3FORMS_ACCESS_KEY.)"""
import os, sys, json
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE, TEL, EMAIL = "(864) 824-1536", "8648241536", "rusty@vldispatching.com"
ICON = {
 "star": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 1 7 7c0 5-7 13-7 13S5 14 5 9a7 7 0 0 1 7-7zm0 4.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z"/></svg>',
 "pct": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.5 4a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zm0 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm9 7a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zm0 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zM18.4 4l1.5 1.5L5.6 19.9 4.1 18.4z"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5zm-1.2 13.6-3.5-3.5 1.4-1.4 2.1 2.1 4.8-4.8 1.4 1.4z"/></svg>',
 "truck": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h12v10H3zM15 9h3.6L22 12.6V16h-7zM7 19.5a2 2 0 1 1 0-4 2 2 0 0 1 0 4zM18 19.5a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/></svg>',
 "trend": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 17.5l6-6 4 4 6.6-7.4V12H22V4h-8v2.4h3.8L13 11.8l-4-4-7.5 7.5z"/></svg>',
 "route": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3a3 3 0 0 1 3 3c0 2-3 5.5-3 5.5S3 8 3 6a3 3 0 0 1 3-3zM18 12.5a3 3 0 0 1 3 3c0 2-3 5.5-3 5.5s-3-3.5-3-5.5a3 3 0 0 1 3-3zM9 18h4a2.5 2.5 0 0 0 0-5h-2.5a4 4 0 0 1 0-8H14v1.8h-3.5a2.2 2.2 0 0 0 0 4.4H13a4.3 4.3 0 0 1 0 8.6H9z"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6zM14 3.5V8h4.5zM9 12h8v1.6H9zM9 15.5h8v1.6H9z"/></svg>',
 "cash": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 6h20v12H2zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM5 8.5v1.6h1.6V8.5zM17.4 13.9v1.6H19v-1.6z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3zm2 2v.5l7 4.5 7-4.5V7zm14 2.9-7 4.5-7-4.5V17h14z"/></svg>',
 "flag": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h2v18H5zM8 4h12v9H8zm2 2v1.4h3V6zm0 2.8v1.4h8V8.8zM14 6v1.4h4V6z"/></svg>',
}

def head(title, desc, page, extra=""):
    canon = "" if page == "index.html" else page
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<meta name="theme-color" content="#0f1b2d">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta property="og:image" content="https://vldispatching.com/images/og-image.png"><meta property="og:url" content="https://vldispatching.com/{canon}"><link rel="canonical" href="https://vldispatching.com/{canon}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="images/favicon.png"><link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">{extra}</head><body>
<a class="skip" href="#main">Skip to the content</a>
<div class="topbar"><div class="container"><span><span class="star">&#9733;</span>Tennessee-based, American-owned truck dispatching</span><span class="tb-right">Call or text <a href="tel:{TEL}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
<header class="header"><div class="container">
<a href="index.html" class="brand" aria-label="Vector Logistics, home"><img class="brand-mark" src="images/logo-mark.png" alt="" width="70" height="42"><img class="brand-word" src="images/logo-wordmark.png" alt="Vector Logistics" width="145" height="23"></a>
<button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
<nav id="nav" class="nav-links" aria-label="Main">{nav(page)}<a class="call" href="tel:{TEL}">Call {PHONE}</a></nav>
</div></header>
<main id="main">
"""

def nav(page):
    out = []
    for href, name in (("index.html", "Home"), ("about.html", "About"), ("contact.html", "Contact")):
        on = ' class="active" aria-current="page"' if href == page else ""
        out.append(f'<a href="{href}"{on}>{name}</a>')
    return "".join(out)

def band(title="Ready to stay loaded?", text=None):
    text = text or f'Tell us about your truck, your lanes and what you want to earn. Call or text {PHONE}, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.'
    return f"""<section class="band"><div class="container"><div><h2>{title}</h2><p>{text}</p></div>
<div class="cta"><a class="btn btn-light" href="contact.html">Become a client</a><a class="btn btn-navy" href="tel:{TEL}">{ICON['phone'].replace('<svg','<svg width="18" height="18" fill="currentColor"')} {PHONE}</a></div></div></section>
"""

FOOT = f"""</main>
<footer class="footer"><div class="container">
<div class="footer-grid">
<div><img class="footer-logo" src="images/logo-white.png" alt="Vector Logistics" width="121" height="64"><p>Truck dispatching for owner-operators and small fleets. A Tennessee-based, American-owned company: your dispatcher is in the USA, on a US phone number, during US business hours.</p></div>
<div><h4>Vector Logistics</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact and sign-up</a></li><li><a href="index.html#faq">Questions</a></li></ul></div>
<div><h4>Talk to us</h4><ul><li><a href="tel:{TEL}">{PHONE}</a> (call or text)</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Tennessee, USA</li><li>Dispatching across the lower 48</li></ul></div>
</div>
<div class="footer-bottom"><span>&copy; <span id="y">2026</span> Vector Logistics. Truck dispatching services. We are a dispatcher, not a freight broker.</span><span>Photos are illustrative.</span></div>
</div></footer>
<script src="js/main.js"></script>
</body></html>
"""

def card(icon, title, text):
    return f'<div class="card"><div class="icon">{ICON[icon]}</div><h3>{title}</h3><p>{text}</p></div>'

FAQ = [
 ("Are you a freight broker?", "No. A broker works for the shipper; a dispatcher works for you, the carrier. The rate confirmation is always between you and the broker, and we never take money from a broker or a shipper. Our only pay is our fee from you."),
 ("What does it cost?", "6% of each load's gross: the rate confirmation amount, fuel surcharge included. Detention, layover, TONU and lumper reimbursements are yours. There is no setup fee and no contract, and if we don't book you a load, you pay nothing."),
 ("Do I have to take every load you find?", "No. There is no forced dispatch. We bring you the load, the rate and the route, and you say yes or no."),
 ("Do you work with new authorities?", "Yes. The first months on a new MC are when good freight is hardest to find, because many brokers want history you don't have yet. We know which brokers work with new authorities."),
 ("What do I need to get started?", "Your MC authority letter, certificate of insurance and a W-9, plus your equipment, home base, lanes and the rate per mile you need. We send the broker setup packets for you."),
 ("How do I pay the fee?", "We invoice every Friday for the loads delivered that week, due in 7 days, by ACH, Zelle or check. If you use a factoring company, it can pay us for you when you set that up."),
 ("Where are you located?", "Vector Logistics is based in Tennessee and American-owned. We dispatch trucks across the lower 48 states, from your home base and on your lanes."),
]

def faq_html():
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

def faq_ld():
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

BUSINESS_LD = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Vector Logistics",
               "description": "Tennessee-based, American-owned truck dispatching for owner-operators and small fleets. 6% of each load's gross, no contracts.",
               "telephone": "+1-864-824-1536", "email": EMAIL, "image": "https://vldispatching.com/images/logo.png", "url": "https://vldispatching.com/",
               "address": {"@type": "PostalAddress", "addressRegion": "TN", "addressCountry": "US"},
               "areaServed": {"@type": "Country", "name": "United States"}, "priceRange": "6% of load gross"}

def ld(obj):
    return '\n<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"

# ── Home ──────────────────────────────────────────────────────────────────
index = head("Vector Logistics | Tennessee-Based Truck Dispatching for Owner-Operators",
             "Tennessee-based, American-owned truck dispatching for owner-operators and small fleets. We find top-paying loads, negotiate your rates and handle the paperwork for 6% of the load. No contracts.",
             "index.html", ld(BUSINESS_LD) + ld(faq_ld())) + f"""
<section class="hero" style="background-image:url('images/hero.jpg')"><div class="container"><div class="hero-copy">
<span class="badge">{ICON['star']} Tennessee-based &middot; American-owned</span>
<h1>You drive. We find the loads that pay.</h1>
<p>Vector Logistics is a truck dispatching company based in Tennessee and run by a former owner-operator. We find top-paying freight on the leading load boards and from shippers, negotiate your rate and handle the paperwork, for a flat 6% of the load.</p>
<div class="cta"><a class="btn btn-primary" href="contact.html">Become a client</a><a class="btn btn-outline" href="tel:{TEL}">Call Rusty: {PHONE}</a></div>
<p class="fine">No contracts &middot; No setup fees &middot; No forced dispatch</p>
</div></div></section>

<section class="trust" aria-label="Why carriers choose Vector"><div class="container">
<div class="trust-item"><div class="icon">{ICON['pct']}</div><div><strong>6% flat fee</strong><span>Of each load's gross. Nothing up front.</span></div></div>
<div class="trust-item"><div class="icon">{ICON['shield']}</div><div><strong>No contracts</strong><span>Stay because the loads are good.</span></div></div>
<div class="trust-item"><div class="icon">{ICON['route']}</div><div><strong>Every load is your call</strong><span>No forced dispatch, ever.</span></div></div>
<div class="trust-item"><div class="icon">{ICON['pin']}</div><div><strong>Based in Tennessee</strong><span>An American company with US-based dispatch.</span></div></div>
</div></section>

<section class="section"><div class="container"><h2 class="section-title">Everything off your plate but the wheel</h2><p class="section-subtitle">Searching boards and calling brokers from a truck stop costs you miles and money. Hand us the office work.</p>
<div class="grid g3">
{card('truck','Load sourcing','We work the leading load boards, including DAT, Truckstop and 123Loadboard, along with direct shippers, to find freight for your truck and your lanes.')}
{card('trend','Rate negotiation','We call the brokers and push for the best rate per mile on every load, because a good first offer is rarely the best one.')}
{card('route','Route and backhaul planning','We plan each load around the next one, cutting deadhead miles and keeping your truck headed where the freight pays.')}
{card('doc','Paperwork and setup','Broker setup packets, W-9s, certificates of insurance, MC letters and rate confirmations, filled out and sent for you.')}
{card('cash','Factoring and billing help','We send bills of lading and paperwork to your factoring company, so the money from each load reaches you without delay.')}
{card('phone','A real person on the phone','When a load changes or a broker goes quiet, you call your dispatcher, someone who knows your truck, and they handle it.')}
</div></div></section>

<section class="section dark local"><div class="container split">
<div><span class="eyebrow">Local and American</span><h2 class="section-title">A Tennessee dispatcher, not an overseas call center</h2>
<p style="color:#c9d3df">Vector Logistics is a small, American-owned business based right here in Tennessee. When you call, you get Rusty: a former owner-operator, on a US phone number, during US business hours, who talks to brokers in plain English and knows what a load is really worth.</p>
<ul class="checks"><li>Owned and run in Tennessee, USA</li><li>The same time zones as your brokers and shippers</li><li>In the middle of the country's freight: Tennessee sits on I-40, I-24, I-65, I-75 and I-81</li><li>One dispatcher who knows your truck, your lanes and your home time</li></ul>
<a class="btn btn-primary" href="about.html">Meet your dispatcher</a></div>
<div class="grid" style="gap:14px">
<div class="stat"><strong>{ICON['flag'].replace('<svg','<svg width="18" height="18" fill="#ff8a8a" style="vertical-align:-3px;margin-right:6px"')}American-owned</strong><span>A US small business, working for US carriers.</span></div>
<div class="stat"><strong>{ICON['pin'].replace('<svg','<svg width="18" height="18" fill="#ff8a8a" style="vertical-align:-3px;margin-right:6px"')}Based in Tennessee</strong><span>Dispatching owner-operators and small fleets across the lower 48.</span></div>
<div class="stat"><strong>{ICON['phone'].replace('<svg','<svg width="18" height="18" fill="#ff8a8a" style="vertical-align:-3px;margin-right:6px"')}A real dispatcher who answers</strong><span>Call or text {PHONE}.</span></div>
</div>
</div></section>

<section class="section alt"><div class="container split"><div><span class="eyebrow">Why Vector</span><h2 class="section-title">Dispatched by someone who has run the truck</h2>
<p>Rusty ran his own authority as an owner-operator, booking his own freight, handling his own bills of lading and working with factoring companies. He knows which loads are worth taking, and what a bad one costs you.</p>
<ul class="checks"><li><strong>You stay in control.</strong> No forced dispatch: every load is your call.</li><li><strong>We work for you.</strong> We represent the carrier, not the broker.</li><li><strong>A simple 6% fee.</strong> We take 6% of each load's gross, with no contract and no setup fee, so we earn when you earn.</li></ul>
<a class="btn btn-primary" href="about.html">Read Rusty's story</a></div><img src="images/highway.jpg" alt="A semi truck on the highway at sunrise" loading="lazy" width="900" height="600"></div></section>

<section class="section" id="pricing"><div class="container"><span class="eyebrow">Pricing</span><h2 class="section-title">One simple fee</h2><p class="section-subtitle">No setup fee, no monthly fee and no contract. We are paid only when you haul a load we booked.</p>
<div class="price">
<div class="price-big"><div class="pct">6%<small>of each load's gross</small></div><p>The rate confirmation amount, fuel surcharge included. Detention, layover, TONU and lumper reimbursements are yours. Invoiced every Friday for the week's delivered loads.</p></div>
<div class="examples">
<div class="example"><span>A $2,500 load</span><strong>$150 fee</strong></div>
<div class="example"><span>A week grossing $6,000</span><strong>$360 fee</strong></div>
<div class="example"><span>A week we don't book you a load</span><strong>$0</strong></div>
<div class="example"><span>Contract, setup fee, cancellation fee</span><strong>None</strong></div>
</div></div></div></section>

<section class="section dark"><div class="container"><h2 class="section-title">How it works</h2><p class="section-subtitle">Getting started takes one phone call or the form on our contact page.</p><div class="steps">
<div class="step"><h3>Tell us about your truck</h3><p>Your equipment, your lanes, your home time and what you need to earn per mile.</p></div>
<div class="step"><h3>Send your documents</h3><p>Your MC authority letter, certificate of insurance and W-9. We set you up with brokers.</p></div>
<div class="step"><h3>We find and negotiate</h3><p>We bring you the best loads we can find, at the best rate we can get. You say yes or no.</p></div>
<div class="step"><h3>You drive and get paid</h3><p>We send the rate confirmation and route, then handle the paperwork to your factoring company.</p></div></div>
<div class="cta" style="margin-top:34px"><a class="btn btn-primary" href="contact.html">Get started</a></div></div></section>

<section class="section"><div class="container split"><img src="images/loading-dock.jpg" alt="A semi truck at a loading dock" loading="lazy" width="900" height="600"><div><span class="eyebrow">Who we work with</span><h2 class="section-title">Owner-operators and small fleets</h2>
<p>If you have your own authority and would rather be driving than hunting freight, we should talk. Running one truck or ten, we dispatch it like it's our own. New to your authority? We can help you get rolling.</p>
<div class="pills" style="margin-top:18px"><span class="pill">Dry van</span><span class="pill">Box truck (26 ft)</span><span class="pill">Hotshot</span><span class="pill">New MC authorities</span><span class="pill">1 to 10 trucks</span></div></div></div></section>

<section class="section alt" id="faq"><div class="container"><div class="center"><span class="eyebrow">Questions</span><h2 class="section-title">What carriers ask us</h2><p class="section-subtitle">Something else on your mind? <a href="contact.html">Ask us</a>.</p></div>
<div class="faq">{faq_html()}</div></div></section>
""" + band() + FOOT

# ── About ─────────────────────────────────────────────────────────────────
about = head("About | Vector Logistics, Tennessee-Based Truck Dispatching",
             "Meet Rusty, the former owner-operator behind Vector Logistics: a Tennessee-based, American-owned truck dispatching service for owner-operators and small fleets.",
             "about.html", ld(BUSINESS_LD)) + f"""
<section class="hero small" style="background-image:url('images/owner-truck.jpg')"><div class="container"><div class="hero-copy">
<span class="badge">{ICON['star']} Tennessee-based &middot; American-owned</span>
<h1>From the driver's seat to your dispatch desk</h1>
<p>Vector Logistics is a truck dispatching service built in Tennessee by someone who has lived the job from your side of the windshield.</p>
</div></div></section>

<section class="section"><div class="container split"><div><span class="eyebrow">Meet Rusty</span><h2 class="section-title">I've been where you are</h2>
<p>I'm Rusty, the owner of Vector Logistics. Before I ever dispatched anyone else's truck, I was an owner-operator with my own MC and DOT numbers.</p>
<p>I found my own loads on all the top load boards and from direct shippers. I negotiated with the brokers, handled my own bills of lading and worked with factoring companies to get paid. I know what it's like to sit at a truck stop refreshing a load board when you should be sleeping.</p>
<p>That's why I started Vector Logistics: to give owner-operators a dispatcher who understands the business because he has run one, and who works to get you the best dollar per mile on every load.</p>
<a class="btn btn-primary" href="contact.html">Talk to Rusty</a></div>
<img src="images/loading-dock.jpg" alt="A semi truck at a loading dock" loading="lazy" width="900" height="600"></div></section>

<section class="section dark local"><div class="container split">
<div><span class="eyebrow">Local and American</span><h2 class="section-title">Proudly based in Tennessee</h2>
<p style="color:#c9d3df">Vector Logistics is an American-owned small business based in Tennessee. Your dispatcher isn't in an overseas call center: he's in the USA, on a US phone number, working your loads during the same hours your brokers and shippers do.</p>
<ul class="checks"><li>Owned and run in Tennessee, USA</li><li>Dispatching across the lower 48 from your home base</li><li>Straight answers in plain English, from a former owner-operator</li></ul></div>
<img src="images/logo-white.png" alt="The Vector Logistics logo" loading="lazy" width="797" height="420" style="box-shadow:none;object-fit:contain;max-height:260px">
</div></section>

<section class="section alt"><div class="container"><span class="eyebrow">How we work</span><h2 class="section-title">Plain dealing, the way I'd want to be treated as a carrier</h2><p class="section-subtitle">Everything is agreed in writing before your first load.</p>
<div class="grid g4">
{card('route','You keep the final say','There is no forced dispatch. We bring you the load and the rate, and you decide whether to take it.')}
{card('trend',"We represent you","Our job is getting you the best rate, not keeping a broker happy. We're your dispatcher, not a freight broker.")}
{card('cash','A fee you can see',"You pay 6% of each load's gross, agreed in writing before we start. No contract and no setup fee.")}
{card('pin','Local and accountable','A Tennessee business you can call, with a real person who answers and knows your truck.')}
</div></div></section>

<section class="section"><div class="container"><span class="eyebrow">What I bring to your truck</span><h2 class="section-title">Experience you can put to work</h2>
<div class="grid g2" style="margin-top:28px">
{card('truck','Hands-on experience','Real decisions made as an owner-operator: lanes, deadhead, detention, brokers and what a load really nets after fuel.')}
{card('trend','Load board know-how','Experience on the leading boards and with direct shippers, finding freight that pays beyond the first listing.')}
{card('doc','Paperwork that gets done right','Rate confirmations, bills of lading, broker packets and factoring submissions, the things that hold up your money if they are wrong.')}
{card('phone','Straight talk',"If a load is bad for you, I'll tell you, even when it would earn me a fee.")}
</div></div></section>
""" + band() + FOOT

# ── Contact ───────────────────────────────────────────────────────────────
contact = head("Contact | Vector Logistics, Tennessee-Based Truck Dispatching",
               "Get in touch with Vector Logistics: ask a question, or have us become your dispatcher. Tennessee-based, American-owned, 6% of the load, no contracts.",
               "contact.html") + f"""
<section class="hero small" style="background-image:url('images/highway.jpg')"><div class="container"><div class="hero-copy">
<span class="badge">{ICON['star']} Tennessee-based &middot; American-owned</span>
<h1>Talk to a Tennessee dispatcher</h1>
<p>Ask a question, or tell us about your truck and we'll start finding you loads. No contract, no setup fee, 6% of the load.</p>
</div></div></section>

<section class="section alt"><div class="container contact-grid">
<aside class="contact-card">
<h2>Reach Rusty directly</h2>
<p>The fastest way is a call or a text. You'll talk to the owner, a former owner-operator, not a call center.</p>
<a class="contact-line" href="tel:{TEL}"><span class="icon">{ICON['phone']}</span><span>{PHONE}<small>Call or text</small></span></a>
<a class="contact-line" href="mailto:{EMAIL}"><span class="icon">{ICON['mail']}</span><span>{EMAIL}<small>Email</small></span></a>
<div class="contact-line"><span class="icon">{ICON['pin']}</span><span>Tennessee, USA<small>Dispatching across the lower 48</small></span></div>
<h2 style="margin-top:22px">To get started, have ready</h2>
<ul class="checks"><li>Your MC authority letter</li><li>Your certificate of insurance</li><li>A W-9</li><li>Your equipment, home base, lanes and the rate per mile you need</li></ul>
</aside>

<div class="form-card">
<h2>Send us a message</h2>
<p>Fill this in and Rusty will get back to you. Fields marked * are needed.</p>
<form id="contact-form" action="https://api.web3forms.com/submit" method="POST" novalidate>
<!-- Web3Forms (web3forms.com). The access key is made to be public; paste it here once the account is set up. -->
<input type="hidden" name="access_key" value="WEB3FORMS_ACCESS_KEY">
<input type="hidden" name="subject" value="New message from the Vector Logistics website">
<input type="hidden" name="from_name" value="Vector Logistics website">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<fieldset class="choice"><legend>What can we do for you? *</legend>
<label><input type="radio" name="request" value="Dispatch my truck(s)" checked> Become my dispatcher</label>
<label><input type="radio" name="request" value="A question"> I have a question</label>
</fieldset>
<div class="fields">
<div class="field"><label for="f-name">Your name *</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-company">Company <span class="opt">(optional)</span></label><input id="f-company" name="company" autocomplete="organization"></div>
<div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
<div class="field"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div class="field dispatch-only"><label for="f-mc">MC number <span class="opt">(optional)</span></label><input id="f-mc" name="mc_number" inputmode="numeric" placeholder="MC-"></div>
<div class="field dispatch-only"><label for="f-dot">DOT number <span class="opt">(optional)</span></label><input id="f-dot" name="dot_number" inputmode="numeric"></div>
<div class="field dispatch-only"><label for="f-equipment">Equipment</label><select id="f-equipment" name="equipment"><option value="">Choose one</option><option>Dry van</option><option>Box truck (26 ft)</option><option>Hotshot</option><option>Reefer</option><option>Flatbed</option><option>Other</option></select></div>
<div class="field dispatch-only"><label for="f-trucks">Trucks</label><select id="f-trucks" name="trucks"><option value="">How many?</option><option>1</option><option>2 to 3</option><option>4 to 10</option><option>More than 10</option></select></div>
<div class="field dispatch-only full"><label for="f-base">Home base and lanes <span class="opt">(optional)</span></label><input id="f-base" name="home_base_and_lanes" placeholder="e.g. Atlanta, GA; the Southeast and Texas"></div>
<div class="field full"><label for="f-message">Message *</label><textarea id="f-message" name="message" required placeholder="Your question, or what you need from a dispatcher (home time, rate per mile, anything else)."></textarea></div>
</div>
<div class="form-foot"><small>We use your details only to answer you. Your message is delivered to our inbox by Web3Forms.</small>
<button class="btn btn-primary" type="submit">Send message</button></div>
<div id="form-result" class="notice" role="status" aria-live="polite"></div>
</form>
</div>
</div></section>
""" + band("Rather talk now?", f"Call or text Rusty at {PHONE}. A Tennessee dispatcher, on your side of the deal.") + FOOT

for name, html in (("index.html", index), ("about.html", about), ("contact.html", contact)):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(html)
print("written")
