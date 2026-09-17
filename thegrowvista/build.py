#!/usr/bin/env python3
"""Writes every HTML page of the Grow Vista site from one shared shell."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE_HREF = "tel:+18622033859"
PHONE_TXT = "+1 862-203-3859"
WA = "https://wa.me/18622033859"

NAV = [("Home", "index.html"), ("Services", "services.html"), ("Portfolio", "portfolio.html"),
       ("Testimonials", "testimonials.html"), ("About", "about.html"),
       ("FAQs", "faqs.html"), ("Contact", "contact.html")]

ICONS = {
 "facebook": '<svg viewBox="0 0 24 24"><path d="M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H8v3h2v7h3v-7h3l1-3h-4v-2c0-.6.4-1 1-1z"/></svg>',
 "instagram": '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.3 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .3-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.3-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.3 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.1A6.7 6.7 0 1 0 18.7 12 6.7 6.7 0 0 0 12 5.3zm0 11a4.3 4.3 0 1 1 4.3-4.3A4.3 4.3 0 0 1 12 16.3zm6.9-11.2a1.6 1.6 0 1 1-1.6-1.6 1.6 1.6 0 0 1 1.6 1.6z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24"><path d="M6.9 21H3.6V9h3.3v12zM5.2 7.6a1.9 1.9 0 1 1 1.9-1.9 1.9 1.9 0 0 1-1.9 1.9zM21 21h-3.3v-6c0-1.5-.5-2.4-1.8-2.4a1.9 1.9 0 0 0-1.8 1.3 2.4 2.4 0 0 0-.1.9V21H10.7s.1-10.6 0-11.7H14v1.8a3.6 3.6 0 0 1 3.3-1.8c2.3 0 3.7 1.5 3.7 4.7V21z"/></svg>',
 "x": '<svg viewBox="0 0 24 24"><path d="M17.5 3h3.2l-7 8 8.3 10h-6.5l-5-6.1-5.8 6.1H1.5l7.5-8.6L1 3h6.6l4.6 5.6L17.5 3zm-1.2 16.2h1.8L7.8 4.7H5.9l10.4 14.5z"/></svg>',
 "whatsapp": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.6 14.2c-.2.6-1.3 1.2-1.8 1.2s-1.1.3-3.6-.8a12.6 12.6 0 0 1-5-4.6c-.4-.6-1-1.7-1-3.2a3.4 3.4 0 0 1 1.1-2.5.9.9 0 0 1 .7-.3h.5c.2 0 .4 0 .6.5l.9 2.1a.6.6 0 0 1 0 .5 6.4 6.4 0 0 1-.5.7c-.2.2-.4.4-.2.7a9.3 9.3 0 0 0 1.7 2.1 8.4 8.4 0 0 0 2.4 1.5c.3.2.5.1.7-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.6.3a2 2 0 0 1-.1 1z"/></svg>',
 "message": '<svg viewBox="0 0 24 24"><path d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg>',
 "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
}


def header(active, prefix=""):
    links = "".join(
        f'\n        <a href="{prefix}{href}" class="nav__link{" is-active" if label == active else ""}">{label}</a>'
        for label, href in NAV)
    return f'''<header class="site-header" id="siteHeader">
  <div class="header-inner">
    <a href="{prefix}index.html" class="brand">
      <img src="{prefix}assets/images/logo.svg" alt="The Grow Vista logo" class="brand__logo" />
      <span class="brand__text">THE GROW <em>Vista</em></span>
    </a>

    <nav class="nav" id="nav">{links}
    </nav>

    <div class="header-actions">
      <a href="{PHONE_HREF}" class="btn btn--pill header-cta">
        <span class="btn__label">Book a Call</span>
      </a>

      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>'''


def footer(prefix=""):
    nav_links = "".join(f'<a href="{prefix}{h}">{l}</a>' for l, h in NAV)
    svc = ["AIO", "Local SEO", "Social Media Marketing", "Google Ads",
           "Reputation Management", "Website Development"]
    svc_links = "".join(f'<a href="{prefix}services.html">{s}</a>' for s in svc)
    socials = "".join(
        f'<a href="#" aria-label="{n.capitalize()}">{ICONS[n]}</a>'
        for n in ("facebook", "instagram", "linkedin", "x"))
    return f'''<footer class="site-footer">
  <div class="footer__top">
    <a href="{prefix}index.html" class="brand">
      <img src="{prefix}assets/images/logo.svg" alt="The Grow Vista logo" class="brand__logo" />
      <span class="brand__text">THE GROW <em>Vista</em></span>
    </a>
    <p class="footer__tag">&mdash; Guiding businesses to digital wins.</p>
  </div>

  <div class="footer__cols">
    <div><h4>Navigate</h4>{nav_links}</div>
    <div><h4>Services</h4>{svc_links}</div>
    <div>
      <h4>Contact</h4>
      <a href="{PHONE_HREF}">{PHONE_TXT}</a>
      <a href="mailto:info@thegrowvista.com">info@thegrowvista.com</a>
      <a href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
    <div>
      <h4>Follow</h4>
      <div class="socials">
        <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICONS["whatsapp"]}</a>
        <a href="#" aria-label="Instagram">{ICONS["instagram"]}</a>
        <a href="#" aria-label="LinkedIn">{ICONS["linkedin"]}</a>
      </div>
    </div>
  </div>

  <div class="footer__bottom">
    <span>&copy; <span id="year">2026</span> The Grow Vista. All rights reserved.</span>
    <a href="#top" class="to-top">Back to top</a>
  </div>
</footer>

<div class="float-cluster" id="floatCluster">
  <div class="float-cluster__panel">
    <a href="#" class="fc-linkedin" aria-label="LinkedIn">{ICONS["linkedin"]}</a>
    <a href="#" class="fc-instagram" aria-label="Instagram">{ICONS["instagram"]}</a>
    <a href="{WA}" class="fc-whatsapp" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ICONS["whatsapp"]}</a>
  </div>
  <button type="button" class="fc-toggle" id="floatToggle" aria-label="Show social links" aria-expanded="false">
    <span class="fc-toggle__icon fc-toggle__icon--msg">{ICONS["message"]}</span>
    <span class="fc-toggle__icon fc-toggle__icon--close">{ICONS["close"]}</span>
  </button>
</div>'''


def page(filename, title, desc, active, body, page_css, prefix=""):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="{prefix}assets/images/logo.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@1,300;1,400;1,500;1,600;1,700&family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{prefix}css/{page_css}" />
</head>
<body id="top">

{header(active, prefix)}

{body}

{footer(prefix)}

<script src="{prefix}js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(doc)


def img_url(img, prefix=""):
    """SERVICES/WORKS image field accepts either a local file basename (no
    extension, resolved against assets/images/<name>.svg) or a full URL —
    used right now for the picsum.photos dummy placeholder photos."""
    return img if img.startswith("http") else f"{prefix}assets/images/{img}.svg"


# ------------------------------------------------------------------ data
# Service and portfolio art below points at picsum.photos placeholder
# photos (seeded, so each stays the same image on every rebuild) so the
# cards look like a finished site instead of empty boxes. Swap any of
# these for your own image — either a full URL, or a local basename
# from assets/images/ (no extension, e.g. "svc-aio" -> svc-aio.svg).
SERVICES = [
    ("AIO", "Artificial Intelligence Optimization", "https://picsum.photos/seed/gv-aio/800/800",
     ["AI Search", "LLM Visibility", "Schema"],
     "Being on page one is no longer enough. We make sure your brand is the one AI assistants quote when someone asks for a recommendation in your category.",
     ["Entity and schema markup so machines understand who you are",
      "Content structured for answer engines, not just search engines",
      "Monitoring of how ChatGPT, Gemini and AI Overviews describe you",
      "Fixing wrong or outdated facts that AI models repeat about your brand"]),
    ("Local SEO", "", "https://picsum.photos/seed/gv-seo/800/800",
     ["Google Business", "Map Pack", "Citations"],
     "Most buying decisions start with a map. We get your business into the top three results for the searches that happen within driving distance of your door.",
     ["Google Business Profile setup, optimisation and weekly posting",
      "Location and service pages that actually rank",
      "Citation building and NAP consistency across directories",
      "Review velocity strategy to hold your map position"]),
    ("Social Media Marketing", "", "https://picsum.photos/seed/gv-smm/800/800",
     ["Content", "Community", "Reels"],
     "Consistent, on-brand content that earns attention instead of buying it, plus the community management that turns followers into customers.",
     ["Monthly content calendar built around your offers",
      "Short-form video and reels production",
      "Comment and DM management within business hours",
      "Monthly performance report with what to double down on"]),
    ("Google Ads", "", "https://picsum.photos/seed/gv-ads/800/800",
     ["Search", "Performance Max", "Retargeting"],
     "Paid traffic that pays for itself. We build campaigns around profit per lead, not clicks, and cut anything that does not convert.",
     ["Keyword and competitor research before a dollar is spent",
      "Conversion tracking set up properly from day one",
      "Landing pages built to match the ad promise",
      "Weekly bid, budget and negative keyword management"]),
    ("Reputation Management", "", "https://picsum.photos/seed/gv-rep/800/800",
     ["Reviews", "Monitoring", "Recovery"],
     "Your rating is your price tag. We build a steady flow of honest reviews and handle the difficult ones before they cost you customers.",
     ["Automated review requests after every job",
      "Response templates in your brand voice",
      "Alerts across Google, Facebook and industry sites",
      "Recovery plan for damaged listings and ratings"]),
    ("Website Development", "", "https://picsum.photos/seed/gv-web/800/800",
     ["Frontend", "WordPress", "Core Web Vitals"],
     "Fast, clean, mobile-first websites that load in under a second and are built to be found, not just to look good in a portfolio.",
     ["Custom design, no recycled templates",
      "Performance budget enforced before launch",
      "On-page SEO and analytics wired in",
      "Training so your team can update it without us"]),
    ("UI/UX Designing", "", "https://picsum.photos/seed/gv-uiux/800/800",
     ["Research", "Wireframes", "Design system"],
     "Interfaces people understand on the first try. We design the flow before the pixels, so the finished product needs less explaining.",
     ["User research and journey mapping",
      "Wireframes and clickable prototypes",
      "Reusable design system with tokens and components",
      "Usability testing before development starts"]),
    ("Logo Designing", "", "https://picsum.photos/seed/gv-logo/800/800",
     ["Identity", "Marks", "Guidelines"],
     "A mark that still works at sixteen pixels and on a van door. Built with a full identity system, not just one file emailed over.",
     ["Discovery session and moodboards",
      "Three distinct directions, then refinement",
      "Full file set: SVG, PNG, EPS, favicon",
      "Brand guidelines covering colour, type and spacing"]),
]

WORKS = [
    ("Crypto Trading Platform", "UI &bull; Webdesign &bull; Development", "https://picsum.photos/seed/gv-work-crypto/900/700", "Web App",
     "3.4x increase in signup completion", "work--wide"),
    ("Online Notary Service", "UX &bull; Branding &bull; SEO", "https://picsum.photos/seed/gv-work-notary/900/700", "Branding",
     "Ranked top 3 in 11 cities", "work--tall"),
    ("Auto Detailing Chain", "Local SEO &bull; Google Ads", "https://picsum.photos/seed/gv-work-auto/900/700", "Local Growth",
     "Booked out four weeks ahead", "work--tall"),
    ("Home Services Group", "Web &bull; Reputation &bull; SMM", "https://picsum.photos/seed/gv-work-home/900/700", "Full Service",
     "From 38 to 410 reviews in a year", "work--wide"),
]

# text, name, role, company, avatar colour, initial
TESTIMONIALS = [
    ("The Grow Vista rebuilt our entire digital acquisition pipeline. Within 90 days of implementing their AIO and paid search framework, our inbound pipeline tripled without expanding ad spend.",
     "Alexander Vance", "Managing Partner", "Vance & Sterling Capital", "#5483B3", "A"),
    ("Their design sensibility is in a completely different tier. They created an aesthetic that our industry competitors are now desperately trying to copy. Exceptional typography and micro-interactions.",
     "Elena Rostova", "Chief Creative Officer", "Aura Spatial Systems", "#7DA0CA", "E"),
    ("Local SEO and reputation management by The Grow Vista placed our 7 regional clinics into the #1 Google Map 3-pack across every target zip code. Direct phone inquiries are up over 200%.",
     "Marcus Thorne", "Founder & CEO", "Veritas Medical Group", "#7DA0CA", "M"),
    ("We had been burned by two agencies before. This team actually picks up the phone and explains things in plain English, and the numbers back up everything they say.",
     "Angela Voss", "Practice Manager", "Brightside Dental", "#C1E8FF", "A"),
    ("Google Ads spend dropped by a third and leads went up. That combination is rare and I did not believe it until I saw the dashboard myself.",
     "Omar Saleh", "Owner", "Coastal HVAC", "#5483B3", "O"),
    ("The brand system they built still looks right two years on. Everything we print or post feels like one company now, across every location.",
     "Rebecca Lin", "Co-founder", "Roast & Reserve", "#7DA0CA", "R"),
    ("Their reporting is the part I value most. No fluff, no vanity metrics. Just what moved, what it cost, and what we are doing next month.",
     "Daniel Reyes", "Director", "Reyes Legal Group", "#7DA0CA", "D"),
    ("Our new site loads in under a second and converts twice as well as the old one. It paid for itself inside the first quarter.",
     "Priya Kapoor", "Founder", "Lumen Wellness", "#C1E8FF", "P"),
    ("They understood AI search before anyone else we spoke to. We now show up inside the answers, not just the links listed below them.",
     "Marcus Tan", "CMO", "Fieldstack SaaS", "#5483B3", "M"),
]

FAQS = [
    ("What services does The Grow Vista provide?",
     "AI optimization, local SEO, social media marketing, Google Ads, reputation management, website development, UI/UX design and logo design. You can take one service or let us run the whole growth system."),
    ("Who are your typical clients?",
     "Local businesses, startups and growing brands across many industries that want a stronger digital presence and consistent, measurable online growth."),
    ("Do you work with international clients?",
     "Yes. Our digital-first approach lets us deliver effective strategies and smooth communication regardless of location or time zone."),
    ("How do you start a project with new clients?",
     "We begin with a discovery call to understand your goals, then send a tailored proposal covering approach, timeline and deliverables before any work starts."),
    ("Can you help with both branding and performance marketing?",
     "Absolutely. We handle creative branding and data-driven performance marketing, so your brand looks right and still delivers measurable business results."),
    ("How long does it take to see results?",
     "It depends on the service. SEO typically takes three to six months, while social and paid campaigns can show traction within weeks. We set clear expectations from day one."),
    ("Do you offer monthly retainers or one-time projects?",
     "Both. Whether you need ongoing monthly support or a single project such as a website or logo, we have flexible packages to fit your goals and budget."),
    ("How will we communicate during the project?",
     "Through whichever channel you prefer, WhatsApp, email or scheduled calls, with regular updates and reports so you are never guessing what we are working on."),
]


# ------------------------------------------------------------------ blocks
def marquee_block():
    unit = '<span>THE GROW VISTA</span><span class="dot">&bull;</span>'
    return f'''<div class="marquee" aria-hidden="true">
  <div class="marquee__track" id="marqueeTrack">{unit * 4}</div>
</div>'''


# Brands we've worked with — logo strip, two rows drifting in opposite
# directions. Real client logos — swap by replacing these files in
# assets/images/ (transparent PNG/SVG) and updating the list below,
# then run build.py again.
BRAND_LOGOS = [
    "brand-rm-mobile-auto-body.png",
    "brand-city-disc-jockeys.png",
    "brand-oras-washington-entertainment.png",
    "brand-sgf.png",
    "brand-power-house-inspection.png",
    "brand-maple-leaf-window-film.png",
    "brand-carwax.png",
    "brand-b4e.png",
]


def brands_block():
    def track(files, track_id):
        items = "".join(
            f'<span class="brands__item"><img src="assets/images/{f}" alt="Client brand logo" class="brands__logo" loading="lazy" /></span>'
            for f in files)
        return f'<div class="brands__track" id="{track_id}">{items}</div>'

    return f'''<section class="brands">
  <div class="section-head section-head--center">
    <span class="pill">Trusted by</span>
    <h2 class="split-title" style="margin-top:16px">Brands we've <em class="script script--aqua">worked</em> with</h2>
  </div>
  <div class="brands__row">
    {track(BRAND_LOGOS, "brandsTrackA")}
  </div>
  <div class="brands__row brands__row--reverse">
    {track(list(reversed(BRAND_LOGOS)), "brandsTrackB")}
  </div>
</section>'''


def services_rail(prefix=""):
    cards = ""
    for name, sub, img, tags, lead, points in SERVICES:
        tl = "".join(f"<li>{t}</li>" for t in tags)
        heading = f"{name}<br><span>{sub}</span>" if sub else name
        cards += f'''
      <article class="card">
        <div class="card__body">
          <h3>{heading}</h3>
          <ul class="tags">{tl}</ul>
          <a href="{prefix}services.html" class="btn btn--outline">View service</a>
        </div>
        <div class="card__media" style="--img:url('{img_url(img, prefix)}')"></div>
      </article>'''
    return f'''<section class="services">
  <div class="section-head section-head--center">
    <h2 class="split-title">Services <em class="script script--gold">we</em> Deliver</h2>
    <p class="section-lead">Eight disciplines, one growth system. Take the piece you need, or let us run the whole engine.</p>
  </div>

  <div class="rail">
    <div class="rail__track" id="railTrack">{cards}
    </div>
  </div>

  <div class="rail-cta">
    <a href="{prefix}services.html" class="btn btn--glow">
      <span class="btn__label">View all services</span><span class="btn__sheen"></span>
    </a>
  </div>
</section>'''


def work_grid(prefix="", limit=None):
    items = WORKS if limit is None else WORKS[:limit]
    out = ""
    for title, meta, img, tag, result, cls in items:
        out += f'''
    <a href="{prefix}contact.html" class="work {cls}" style="--img:url('{img_url(img, prefix)}')">
      <div class="work__meta">
        <span class="work__tag">{tag}</span>
        <h3>{title}</h3>
        <span>{meta}</span>
        <p class="work__result">{result}</p>
      </div>
    </a>'''
    return f'<div class="work-grid">{out}\n  </div>'


def slider_block():
    """3-up testimonial cards, grouped into slides of 3."""
    groups = [TESTIMONIALS[i:i + 3] for i in range(0, len(TESTIMONIALS), 3)]
    slides = ""
    for group in groups:
        cards = ""
        for text, who, role, company, colour, initial in group:
            cards += f'''
        <article class="t-card" style="--c2:{colour}">
          <div class="t-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <div class="t-card__quote">&#8220;&#8220;</div>
          <p>&ldquo;{text}&rdquo;</p>
          <div class="t-card__who">
            <span class="t-card__avatar">{initial}</span>
            <span><b>{who}</b><span>{role}, <em>{company}</em></span></span>
          </div>
        </article>'''
        slides += f'\n      <div class="slide">{cards}\n      </div>'
    return f'''<div class="slider">
    <div class="slider__viewport">
      <div class="slider__track" id="slideTrack">{slides}
      </div>
    </div>
    <div class="slider__ui">
      <button class="arrow" id="slidePrev" aria-label="Previous reviews">&#8592;</button>
      <div class="dots" id="slideDots"></div>
      <button class="arrow" id="slideNext" aria-label="Next reviews">&#8594;</button>
    </div>
  </div>'''


def faq_block(items):
    out = ""
    for i, (q, a) in enumerate(items):
        out += f'''
    <div class="acc{' is-open' if i == 0 else ''}">
      <button class="acc__head">{q}<i></i></button>
      <div class="acc__panel"><p>{a}</p></div>
    </div>'''
    return out


def contact_form(prefix=""):
    opts = "".join(
        f"<option>{n}{' — ' + s if s else ''}</option>" for n, s in
        [(x[0], x[1]) for x in SERVICES])
    return f'''<form class="contact__form" id="contactForm" novalidate>
    <div class="field"><label for="name">Name</label>
      <input id="name" name="name" type="text" required placeholder="Your name" /></div>
    <div class="field"><label for="email">Email</label>
      <input id="email" name="email" type="email" required placeholder="you@company.com" /></div>
    <div class="field"><label for="phone">Phone</label>
      <input id="phone" name="phone" type="tel" placeholder="+1 000 000 0000" /></div>
    <div class="field"><label for="service">Service</label>
      <select id="service" name="service">{opts}</select></div>
    <div class="field field--full"><label for="message">Message</label>
      <textarea id="message" name="message" rows="4" placeholder="What are you trying to grow?"></textarea></div>
    <button type="submit" class="btn btn--glow btn--wide">
      <span class="btn__label">Send on WhatsApp</span><span class="btn__sheen"></span>
    </button>
    <p class="form-note" id="formNote" role="status"></p>
    <p class="form-hint">Submitting opens WhatsApp with your details filled in. Nothing is sent until you press send there.</p>
  </form>'''


def contact_section(prefix=""):
    return f'''<section class="contact">
  <div class="contact__left">
    <h2 class="split-title">Let's <em class="script script--gold">build</em> Something</h2>
    <p>Tell us where you want to be in twelve months. We will map the route, then run it with you.</p>
    <ul class="contact__list">
      <li><span>Call</span><a href="{PHONE_HREF}">{PHONE_TXT}</a></li>
      <li><span>WhatsApp</span><a href="{WA}" target="_blank" rel="noopener">Message us directly</a></li>
      <li><span>Email</span><a href="mailto:info@thegrowvista.com">info@thegrowvista.com</a></li>
      <li><span>Hours</span><a href="#top">Mon to Sat, 9am to 7pm EST</a></li>
    </ul>
  </div>
  {contact_form(prefix)}
</section>'''


def cta_band(title=None, text=None, prefix=""):
    title = title or 'Ready to <em class="script script--aqua">grow</em>?'
    text = text or "Book a free thirty minute call. We will tell you what we would do first, whether or not you hire us."
    return f'''<section class="cta-band">
  <h2 class="split-title">{title}</h2>
  <p>{text}</p>
  <a href="{prefix}contact.html" class="btn btn--glow"><span class="btn__label">Start a project</span><span class="btn__sheen"></span></a>
  <a href="{PHONE_HREF}" class="btn btn--ghost">Call {PHONE_TXT}</a>
</section>'''


def page_hero(crumb, title, text, image=None):
    style = f' style="--page-hero-image:url(\'assets/images/{image}.svg\')"' if image else ""
    return f'''<section class="page-hero"{style}>
  <div class="page-hero__bg"></div>
  <div class="page-hero__veil"></div>
  <div class="shell">
    <span class="crumb">{crumb}</span>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>'''


# ================================================================== PAGES
# ---- HOME
home = f'''<section class="hero" id="home">
  <div class="hero__bg"></div>
  <div class="hero__veil"></div>

  <div class="hero__content">
    <h1 class="hero__title">
      <span class="line" data-reveal>DIGITAL</span>
      <span class="line" data-reveal>GROWTH</span>
      <span class="line line--mix" data-reveal><em class="script">from</em> ANOTHER</span>
      <span class="line" data-reveal>DIMENSION</span>
    </h1>
    <p class="hero__sub" data-reveal>Strategy, creative and performance marketing for brands that intend to be found.</p>
    <div class="hero__actions" data-reveal>
      <a href="about.html" class="btn btn--glow"><span class="btn__label">Learn more</span><span class="btn__sheen"></span></a>
      <a href="{PHONE_HREF}" class="btn btn--ghost">Talk to a strategist</a>
    </div>
  </div>

  <div class="hero__scroll"><span></span>scroll</div>
</section>

{marquee_block()}

{brands_block()}

<section class="quote">
  <div class="orb orb--left"></div>
  <div class="orb orb--right"></div>
  <div class="quote__inner">
    <span class="pill">About us</span>
    <blockquote class="quote__text">
      &laquo;We want every brand we touch to feel <span class="hl hl-aqua">unmistakable &mdash; with idea
      and presence</span>. So clients don't just find you, they <span class="hl hl-gold">remember you</span>.
      Growth should <span class="hl hl-teal">speak, engage, and stick</span>&raquo;
    </blockquote>
    <div class="quote__author">
      <img src="assets/images/logo.svg" alt="The Grow Vista logo" class="quote__logo" />
      <div><strong>The Grow Vista</strong><span>Guiding businesses to digital wins</span></div>
    </div>
    <div class="stats">
      <div class="stat"><b>15+</b><span>Years of experience</span></div>
      <div class="stat"><b>10K+</b><span>Happy clients</span></div>
      <div class="stat"><b>98%</b><span>Client retention</span></div>
      <div class="stat"><b>24/7</b><span>Dedicated support</span></div>
    </div>
    <a href="contact.html" class="btn btn--glow quote__cta"><span class="btn__label">Start a project</span><span class="btn__sheen"></span></a>
  </div>
</section>

{services_rail()}

<section class="portfolio">
  <div class="section-head">
    <h2 class="split-title">Missions <em class="script script--aqua">we've</em> Completed</h2>
    <p class="section-lead">Selected work across local service brands, ecommerce and B2B.</p>
  </div>
  {work_grid()}
  <div class="rail-cta"><a href="portfolio.html" class="btn btn--outline">View full portfolio</a></div>
</section>

<section class="testimonials">
  <div class="section-head section-head--center">
    <h2 class="split-title">Words <em class="script script--sand">from</em> Our Clients</h2>
    <p class="section-lead">Nine of them, rotating three at a time.</p>
  </div>
  {slider_block()}
</section>

<section class="faqs" id="faqs">
  <div class="faqs__left">
    <span class="bracket">[ &nbsp;FAQ'S&nbsp; ]</span>
    <h2 class="faqs__title">GOT<br />QUESTIONS?</h2>
    <p>Still unsure? Call us and we will answer it in five minutes.</p>
    <a href="{PHONE_HREF}" class="btn btn--glow"><span class="btn__label">Book a Call</span><span class="btn__sheen"></span></a>
  </div>
  <div class="faqs__right">{faq_block(FAQS[:6])}
  </div>
</section>

{cta_band()}'''

page("index.html", "The Grow Vista — Digital Growth Partners",
     "The Grow Vista builds visibility, engagement and long-term growth through AI optimization, local SEO, paid media, web development and design.",
     "Home", home, "home.css")

# ---- SERVICES
svc_items = ""
for i, (name, sub, img, tags, lead, points) in enumerate(SERVICES, 1):
    pl = "".join(f"<li>{p}</li>" for p in points)
    subtitle = f" <em class='script script--gold'>{sub}</em>" if sub else ""
    svc_items += f'''
  <article class="svc" id="{name.lower().replace(' ', '-').replace('/', '-')}">
    <div class="svc__body">
      <span class="svc__num">{i:02d}</span>
      <h2>{name}{subtitle}</h2>
      <p class="svc__lead">{lead}</p>
      <ul class="svc__points">{pl}</ul>
      <a href="contact.html" class="btn btn--outline">Start a project</a>
    </div>
    <div class="svc__art" style="--img:url('{img_url(img)}')"></div>
  </article>'''

services_body = f'''{page_hero("Services", "Everything we do, <em class='script script--aqua'>in</em> detail",
  "Eight services, built to work together. Each one can run on its own, but they compound when combined.", "hero-services")}

<section class="svc-list">{svc_items}
</section>

<section class="prose">
  <div class="section-head section-head--center">
    <h2 class="split-title">How we <em class="script script--gold">work</em></h2>
  </div>
  <div class="steps">
    <div class="step"><b>01</b><h3>Discovery</h3><p>A call to understand the business, the margins and what growth actually means for you.</p></div>
    <div class="step"><b>02</b><h3>Audit</h3><p>We pull the data, review competitors and find the gaps that are costing you customers.</p></div>
    <div class="step"><b>03</b><h3>Build</h3><p>Strategy, assets and campaigns go live in the order that produces results fastest.</p></div>
    <div class="step"><b>04</b><h3>Report</h3><p>Monthly numbers in plain English, plus what we are changing next and why.</p></div>
  </div>
</section>

{cta_band()}'''

page("services.html", "Services — The Grow Vista",
     "AIO, local SEO, social media marketing, Google Ads, reputation management, web development, UI/UX and logo design, explained in detail.",
     "Services", services_body, "services-page.css")

# ---- PORTFOLIO
portfolio_body = f'''{page_hero("Portfolio", "Missions <em class='script script--aqua'>we've</em> completed",
  "A look at what we built, what changed, and the numbers that followed.", "hero-portfolio")}

<section class="portfolio">
  {work_grid()}
</section>

<section class="prose">
  <div class="section-head section-head--center">
    <h2 class="split-title">What the work <em class="script script--gold">produced</em></h2>
  </div>
  <div class="prose__grid">
    <div class="tile"><span class="tile__k">3.4x</span><h3>Signup completion</h3><p>Rebuilt onboarding for a trading platform, cutting the flow from nine steps to four.</p></div>
    <div class="tile"><span class="tile__k">11</span><h3>Cities ranked</h3><p>Multi-location local SEO took a notary service into the map pack across eleven metros.</p></div>
    <div class="tile"><span class="tile__k">-34%</span><h3>Cost per lead</h3><p>Restructured Google Ads for an HVAC company while lead volume climbed.</p></div>
    <div class="tile"><span class="tile__k">410</span><h3>Reviews earned</h3><p>An automated review flow took a home services group from 38 to 410 in twelve months.</p></div>
  </div>
</section>

{cta_band("Want results like <em class='script script--aqua'>these</em>?")}'''

page("portfolio.html", "Portfolio — The Grow Vista",
     "Selected projects from The Grow Vista across web apps, branding, local SEO and paid media, with the results each one produced.",
     "Portfolio", portfolio_body, "portfolio-page.css")

# ---- TESTIMONIALS
testi_body = f'''{page_hero("Testimonials", "Words <em class='script script--sand'>from</em> our clients",
  "No edited quotes, no stock photos. These are the people who pay us every month.", "hero-testimonials")}

<section class="testimonials">
  {slider_block()}
</section>

<section class="prose">
  <div class="section-head section-head--center">
    <h2 class="split-title">Why they <em class="script script--gold">stay</em></h2>
  </div>
  <div class="prose__grid">
    <div class="tile"><h3>Plain <em>English</em></h3><p>Reports you can read in five minutes, with no jargon used to hide a bad month.</p></div>
    <div class="tile"><h3>One <em>team</em></h3><p>The people you meet on the discovery call are the people doing the work.</p></div>
    <div class="tile"><h3>No <em>lock-in</em></h3><p>Month to month after the first term. We keep the account by earning it.</p></div>
    <div class="tile"><h3>Fast <em>replies</em></h3><p>WhatsApp during business hours. Most messages get an answer within the hour.</p></div>
  </div>
</section>

{cta_band()}'''

page("testimonials.html", "Testimonials — The Grow Vista",
     "What clients of The Grow Vista say about working with us across SEO, paid media, web design and branding.",
     "Testimonials", testi_body, "testimonials-page.css")

# ---- ABOUT
about_body = f'''{page_hero("About us", "Empowering brands through <em class='script script--gold'>digital</em> excellence",
  "We partner with brands to build a powerful online presence through strategies that drive visibility, engagement and long-term growth.", "hero-about")}

<section class="quote">
  <div class="orb orb--left"></div>
  <div class="orb orb--right"></div>
  <div class="quote__inner">
    <span class="pill">Our belief</span>
    <blockquote class="quote__text">
      &laquo;We want every brand we touch to feel <span class="hl hl-aqua">unmistakable &mdash; with idea
      and presence</span>. So clients don't just find you, they <span class="hl hl-gold">remember you</span>.
      Growth should <span class="hl hl-teal">speak, engage, and stick</span>&raquo;
    </blockquote>
    <div class="quote__author">
      <img src="assets/images/logo.svg" alt="The Grow Vista logo" class="quote__logo" />
      <div><strong>The Grow Vista</strong><span>Guiding businesses to digital wins</span></div>
    </div>
    <div class="stats">
      <div class="stat"><b>15+</b><span>Years of experience</span></div>
      <div class="stat"><b>10K+</b><span>Happy clients</span></div>
      <div class="stat"><b>98%</b><span>Client retention</span></div>
      <div class="stat"><b>24/7</b><span>Dedicated support</span></div>
    </div>
  </div>
</section>

<section class="prose">
  <div class="section-head section-head--center">
    <h2 class="split-title">What you get <em class="script script--aqua">with</em> us</h2>
    <p class="section-lead">Eight things we hold ourselves to on every account, from the first week onward.</p>
  </div>
  <div class="prose__grid">
    <div class="tile"><h3>Proven <em>expertise</em></h3><p>Years of hands-on work delivering strategies that help brands grow and hold their position.</p></div>
    <div class="tile"><h3>Data-driven <em>results</em></h3><p>Every decision is backed by real numbers, so your budget goes where it actually performs.</p></div>
    <div class="tile"><h3>Creative <em>excellence</em></h3><p>Original work that captures attention, tells your story and leaves a lasting impression.</p></div>
    <div class="tile"><h3>End-to-end <em>solutions</em></h3><p>Strategy, design, build and marketing under one roof, so nothing falls between vendors.</p></div>
    <div class="tile"><h3>Client-centric <em>approach</em></h3><p>Every strategy is shaped around your goals, your market and your margins.</p></div>
    <div class="tile"><h3>Transparent <em>process</em></h3><p>Clear reporting and open communication. You can always see what we are doing.</p></div>
    <div class="tile"><h3>Dedicated <em>support</em></h3><p>A named point of contact who knows your account, not a rotating ticket queue.</p></div>
    <div class="tile"><h3>Global <em>perspective</em></h3><p>We apply insights from international markets to grow brands wherever they operate.</p></div>
  </div>
</section>

<section class="prose">
  <div class="section-head section-head--center">
    <h2 class="split-title">How a project <em class="script script--gold">runs</em></h2>
  </div>
  <div class="steps">
    <div class="step"><b>01</b><h3>Discovery call</h3><p>Thirty minutes to understand the business, the goals and the constraints.</p></div>
    <div class="step"><b>02</b><h3>Proposal</h3><p>Scope, timeline and price, with the reasoning behind each line item.</p></div>
    <div class="step"><b>03</b><h3>Execution</h3><p>Work begins in the order that produces visible results the fastest.</p></div>
    <div class="step"><b>04</b><h3>Review</h3><p>Monthly reporting call, then we adjust the plan for the next cycle.</p></div>
  </div>
</section>

{cta_band()}'''

page("about.html", "About — The Grow Vista",
     "Who we are, what we believe and how we run projects at The Grow Vista.",
     "About", about_body, "about-page.css")

# ---- FAQS
faqs_body = f'''{page_hero("FAQs", "Got <em class='script script--aqua'>questions</em>?",
  "The things people ask us most often, answered properly.", "hero-faqs")}

<section class="faqs">
  <div class="faqs__left">
    <span class="bracket">[ &nbsp;FAQ'S&nbsp; ]</span>
    <h2 class="faqs__title">GOT<br />QUESTIONS?</h2>
    <p>If yours is not here, message us on WhatsApp and you will get a real answer, not a brochure.</p>
    <a href="{WA}" target="_blank" rel="noopener" class="btn btn--glow"><span class="btn__label">Ask on WhatsApp</span><span class="btn__sheen"></span></a>
  </div>
  <div class="faqs__right">{faq_block(FAQS)}
  </div>
</section>

{cta_band()}'''

page("faqs.html", "FAQs — The Grow Vista",
     "Common questions about working with The Grow Vista: services, timelines, pricing models and communication.",
     "FAQs", faqs_body, "faqs-page.css")

# ---- CONTACT
contact_body = f'''{page_hero("Contact", "Let's <em class='script script--gold'>build</em> something",
  "Fill the form and it opens WhatsApp with your details ready to send, or just call us.", "hero-contact")}

{contact_section()}

<section class="prose">
  <div class="section-head section-head--center">
    <h2 class="split-title">What happens <em class="script script--aqua">next</em></h2>
  </div>
  <div class="steps">
    <div class="step"><b>01</b><h3>You message</h3><p>Form, WhatsApp or phone. Whichever is easiest for you.</p></div>
    <div class="step"><b>02</b><h3>We reply</h3><p>Within one business day, usually much sooner during working hours.</p></div>
    <div class="step"><b>03</b><h3>Discovery call</h3><p>Thirty minutes, no pitch deck. We ask questions and tell you what we would do.</p></div>
    <div class="step"><b>04</b><h3>Proposal</h3><p>Scope, timeline and price in writing, with nothing hidden in the footnotes.</p></div>
  </div>
</section>'''

page("contact.html", "Contact — The Grow Vista",
     "Call +1 862-203-3859, message us on WhatsApp, or send an enquiry through the form.",
     "Contact", contact_body, "contact-page.css")

print("pages written:", sorted(f for f in os.listdir(OUT) if f.endswith(".html")))
