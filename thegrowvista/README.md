# The Grow Vista — website

Static multi-page site. No build step, no dependencies to run it. Open `index.html`,
or upload the folder to any host (Netlify, Vercel, cPanel, GitHub Pages).

```
thegrowvista/
├─ index.html              home
├─ services.html            all 8 services, detailed
├─ portfolio.html           work + results
├─ testimonials.html        3-up review slider
├─ about.html                story, values, process
├─ faqs.html                  full FAQ list
├─ contact.html               form + process
├─ css/
│  ├─ shared.css            tokens, buttons, header, footer, floating icons — used by every page
│  ├─ hero.css               hero + marquee (home only)
│  ├─ about.css               "about us" quote block (home + about)
│  ├─ services.css            rail (home) + detailed list (services)
│  ├─ portfolio.css           work grid (home + portfolio)
│  ├─ testimonials.css        3-up review cards (home + testimonials)
│  ├─ faqs.css                 accordion (home + faqs)
│  ├─ contact.css              contact form (contact)
│  └─ home.css / services-page.css / portfolio-page.css / testimonials-page.css /
│     about-page.css / faqs-page.css / contact-page.css
│         ↳ one real stylesheet per HTML page — each just `@import`s the pieces
│           that page actually uses, so every page loads its own file.
├─ js/main.js               shared behaviour for all pages
├─ build.py                  regenerates every .html file from one template — edit
│                             the copy or markup here, then run `python3 build.py`
└─ assets/images/            logo, hero art, page-hero backdrops, placeholder art
```

## 1. Your logo

Replace `assets/images/logo.svg` with your real file (SVG or PNG). It sits directly in
the header with no background box behind it, and it is on every page, plus the about
section and the footer. If you switch to a PNG, open `build.py`, find `logo.svg` and
change it to `logo.png`, then run `python3 build.py`.

## 2. Phone and WhatsApp

- Phone: the **Book a Call** button and the contact/footer links use
  `tel:+18622033859`. Change `PHONE_HREF` / `PHONE_TXT` at the top of `build.py`.
- WhatsApp: the number lives in **one** place, `const WHATSAPP` near the top of
  `js/main.js`, and in `build.py` as `WA`. Update both to the same number.
- The contact form does not email anything — submitting it opens WhatsApp with the
  name, email, phone, service and message already written out. Nothing sends until
  you press send inside WhatsApp.
- The floating bottom-right cluster is now a single toggle (chat-bubble icon). Tap it
  and it fans out WhatsApp (primary, pulsing), Instagram and LinkedIn above it, and the
  icon morphs into a close (×) mark; tap again, click outside, or press Escape to close
  it. The same three links also appear in the footer. Point `#` at your real profile
  links in `build.py` (`ICONS` section of `footer()`).

## 3. Brands you've worked with (home page)

The "Brands we've worked with" section under the THE GROW VISTA marquee shows your
eight client logos (`assets/images/brand-*.png`), all with transparent backgrounds.
To swap any of them for a different logo:

1. Drop the new logo file into `assets/images/` (SVG or PNG, transparent background
   works best — they're shown at roughly 42px tall).
2. Open `build.py`, find `BRAND_LOGOS` near the top of the blocks section, and replace
   the filename you want to change, e.g. `"brand-carwax.png"` → `"client-9.png"`.
3. Run `python3 build.py`.

The two rows drift slowly in opposite directions and pause on hover; each logo sits
dim/grayscale until hovered, then lifts into full colour.

## 4. Brand tokens

All colours, fonts and spacing are in `:root` at the top of `css/shared.css` — this
one block controls every page, since every page imports `shared.css`.

| Token | Value | Used for |
|---|---|---|
| `--navy-900 / 800 / 700 / 600` | `#021024` `#052659` `#052659` `#5483B3` | backgrounds |
| `--gold` | `#7DA0CA` | primary accent, italic headings |
| `--aqua` | `#5483B3` | links, highlights, focus |
| `--teal` / `--teal-bright` | `#5483B3` / `#7DA0CA` | gradients |
| `--sand` | `#C1E8FF` | borders, soft text |

Fonts: **Manrope** for structure, **Cormorant Italic** for every accent word
(`from`, `we`, `we've`, `build`, `Vista`, and the coloured phrases in the about quote —
those are sized slightly smaller than the surrounding line on purpose).

## 5. Hero and inner-page backgrounds

Home hero image: `css/hero.css` → `.hero__bg` falls back to
`assets/images/hero.svg`. Replace that file with your own photo, or pass a different
one via the `--hero-image` CSS variable.

Every inner page (About, Services, Portfolio, Testimonials, FAQs, Contact) has an
**optional** background image behind its title. `build.py` already points each one at
a soft abstract backdrop (`assets/images/hero-about.svg`, `hero-services.svg`, etc).
To swap one for a real photo, replace that file, or pass `image=None` in the
`page_hero(...)` call inside `build.py` to turn it off entirely for that page.

## 6. Swapping project and service images

The 8 service cards and 4 portfolio pieces currently use dummy placeholder photos
from picsum.photos, set as the third field in the `SERVICES` and `WORKS` lists near
the top of `build.py`:

```python
("AIO", "Artificial Intelligence Optimization", "https://picsum.photos/seed/gv-aio/800/800", ...),
("Crypto Trading Platform", "...", "https://picsum.photos/seed/gv-work-crypto/900/700", ...),
```

To use your own images, replace that URL with either:
- a full `https://` URL to your hosted image, or
- a local file basename with no extension (it resolves to
  `assets/images/<name>.svg`) — the original abstract-art SVGs are still in
  `assets/images/` (`svc-aio.svg`, `work-1.svg`, etc.) if you'd rather fall back to
  those instead of photos.

Then run `python3 build.py`. Service art is square (800×800), portfolio art roughly
9:7 (900×700). Keep the count roughly matched to the data — 8 service images, 4
portfolio images — rather than padding with extras.

## 7. Behaviour notes

- **Header** stays visible on every page at every scroll position, transparent at the
  very top, and becomes a blurred navy pill after 40px of scroll. The logo has no
  container around it. The nav links sit centred between the logo and the Book a Call
  button/burger on desktop.
- **Book a Call** button is a single line now — no phone number printed on it — but
  still calls `+1 862-203-3859` when tapped.
- **Talk to a strategist** (ghost button) fills with sand colour left-to-right on
  hover; the text colour flips from light to navy as the fill passes under it.
- **THE GROW VISTA marquee** uses thick solid letters coloured to match the section
  that follows (`--navy-700`, same as the About quote background), so it reads as a
  soft watermark rather than an outline. 52-second loop, pauses on hover.
- **Services rail** auto-scrolls on a 60-second loop and stops the moment you hover or
  tab into a card.
- **Testimonials** show three cards per slide (nine reviews → three slides), advance
  automatically every 7 seconds, pause on hover, and respond to arrows, dots and touch
  swipe. Cards use five gold stars, a quote mark, the review, then name / role /
  company — no badge, matching the layout you shared minus the coloured tag.
- **FAQ accordion** opens one panel at a time and animates real height.
- `prefers-reduced-motion` is respected everywhere.

## 8. Regenerating pages after an edit

Everything text-based — nav labels, service copy, testimonials, FAQs, phone number —
lives in `build.py`, not in the HTML files directly. Edit the relevant list or
function near the top of the file, then run:

```bash
python3 build.py
```

This rewrites all seven `.html` files in place from the shared template, so header,
footer and floating icons stay identical across every page automatically.
