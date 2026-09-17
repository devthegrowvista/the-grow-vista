/* =========================================================
   THE GROW VISTA — main.js  (shared by every page)
   ========================================================= */
(function () {
  'use strict';

  const $  = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

  const WHATSAPP = '18622033859';   // change the number here

  document.addEventListener('DOMContentLoaded', init);

  function init() {
    document.body.classList.add('is-loaded');
    header();
    mobileMenu();
    marquee();
    brandsMarquee();
    floatCluster();
    servicesRail();
    reveal();
    statCounters();
    accordion();
    testimonialSlider();
    contactForm();
    const y = $('#year'); if (y) y.textContent = new Date().getFullYear();
  }

  /* ---------- 1. header — always on screen, solid after a little scroll ---------- */
  function header() {
    const el = $('#siteHeader');
    if (!el) return;
    const update = () => el.classList.toggle('is-stuck', window.scrollY > 40);
    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ---------- 2. mobile menu ---------- */
  function mobileMenu() {
    const burger = $('#burger'), nav = $('#nav');
    if (!burger || !nav) return;
    burger.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
    });
    $$('.nav__link', nav).forEach(l => l.addEventListener('click', () => {
      nav.classList.remove('is-open');
      burger.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    }));
  }

  /* ---------- 3. brand marquee — duplicate for a seamless loop ---------- */
  function marquee() {
    const track = $('#marqueeTrack');
    if (track) track.innerHTML += track.innerHTML;
  }

  /* ---------- 3b. brand logos strip — duplicate each row for a seamless loop ---------- */
  function brandsMarquee() {
    $$('.brands__track').forEach(t => { t.innerHTML += t.innerHTML; });
  }

  /* ---------- 3c. floating social cluster — single toggle fans out the icons ---------- */
  function floatCluster() {
    const cluster = $('#floatCluster'), toggle = $('#floatToggle');
    if (!cluster || !toggle) return;

    const setOpen = open => {
      cluster.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Hide social links' : 'Show social links');
    };

    toggle.addEventListener('click', e => {
      e.stopPropagation();
      setOpen(!cluster.classList.contains('is-open'));
    });
    document.addEventListener('click', e => {
      if (cluster.classList.contains('is-open') && !cluster.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') setOpen(false);
    });
  }

  /* ---------- 4. services rail — duplicate, pause on hover / focus ---------- */
  function servicesRail() {
    const track = $('#railTrack');
    if (!track) return;
    track.innerHTML += track.innerHTML;
    $$('.card', track).forEach(c => {
      c.addEventListener('focusin', () => track.style.animationPlayState = 'paused');
      c.addEventListener('focusout', () => track.style.animationPlayState = 'running');
    });
  }

  /* ---------- 5. scroll reveal ---------- */
  function reveal() {
    const targets = $$('.section-head, .card, .work, .tile, .step, .svc, .stat-card, .contact__form, .faqs__left, .slider');
    if (!('IntersectionObserver' in window)) return;
    targets.forEach(el => el.classList.add('in-view-target'));
    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach((e, i) => {
        if (!e.isIntersecting) return;
        e.target.style.transitionDelay = (i * 70) + 'ms';
        e.target.classList.add('in-view');
        obs.unobserve(e.target);
      });
    }, { threshold: 0.12 });
    targets.forEach(el => io.observe(el));
  }

  /* ---------- 5b. stat card counters — count up once the card is in view ---------- */
  function statCounters() {
    const nums = $$('.stat-card [data-count]');
    if (!nums.length) return;
    if (!('IntersectionObserver' in window)) {
      nums.forEach(el => { el.textContent = el.dataset.count + el.dataset.suffix; });
      return;
    }
    const animate = el => {
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const duration = 1400;
      const start = performance.now();
      const step = now => {
        const p = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + suffix;
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        animate(e.target);
        obs.unobserve(e.target);
      });
    }, { threshold: 0.4 });
    nums.forEach(el => io.observe(el));
  }

  /* ---------- 6. FAQ accordion ---------- */
  function accordion() {
    const accs = $$('.acc');
    if (!accs.length) return;

    const setPanel = (acc, open) => {
      const panel = $('.acc__panel', acc);
      acc.classList.toggle('is-open', open);
      panel.style.height = open ? panel.scrollHeight + 'px' : '0px';
    };

    accs.forEach(acc => {
      setPanel(acc, acc.classList.contains('is-open'));
      $('.acc__head', acc).addEventListener('click', () => {
        const willOpen = !acc.classList.contains('is-open');
        accs.forEach(a => setPanel(a, false));
        setPanel(acc, willOpen);
      });
    });

    window.addEventListener('resize', () => {
      accs.forEach(a => { if (a.classList.contains('is-open')) setPanel(a, true); });
    });
  }

  /* ---------- 7. testimonials — 3-up per slide, auto advance, swipe ---------- */
  function testimonialSlider() {
    const track = $('#slideTrack');
    if (!track) return;

    const slides = $$('.slide', track);
    const dotsBox = $('#slideDots');
    let index = 0, timer;

    slides.forEach((_, i) => {
      const b = document.createElement('button');
      b.className = 'dot-btn' + (i === 0 ? ' is-active' : '');
      b.type = 'button';
      b.setAttribute('aria-label', 'Review ' + (i + 1));
      b.addEventListener('click', () => go(i));
      dotsBox.appendChild(b);
    });
    const dots = $$('.dot-btn', dotsBox);

    function go(i) {
      index = (i + slides.length) % slides.length;
      track.style.transform = 'translateX(' + (-index * 100) + '%)';
      dots.forEach((d, n) => d.classList.toggle('is-active', n === index));
      restart();
    }

    function restart() {
      clearInterval(timer);
      timer = setInterval(() => go(index + 1), 7000);
    }

    $('#slidePrev').addEventListener('click', () => go(index - 1));
    $('#slideNext').addEventListener('click', () => go(index + 1));

    // touch swipe
    let x0 = null;
    track.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
    track.addEventListener('touchend', e => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) go(index + (dx < 0 ? 1 : -1));
      x0 = null;
    });

    const box = track.closest('.slider');
    box.addEventListener('mouseenter', () => clearInterval(timer));
    box.addEventListener('mouseleave', restart);

    restart();
  }

  /* ---------- 8. contact form → opens WhatsApp with the message ---------- */
  function contactForm() {
    const form = $('#contactForm');
    if (!form) return;
    const note = $('#formNote');

    form.addEventListener('submit', e => {
      e.preventDefault();

      const val = id => (($(id) || {}).value || '').trim();
      const name = val('#name'), email = val('#email'),
            phone = val('#phone'), service = val('#service'), message = val('#message');

      const fail = msg => { note.textContent = msg; note.style.color = '#C1E8FF'; };

      if (!name)  return fail('Add your name so we know who we are talking to.');
      if (!email) return fail('Add an email address so we can reply.');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return fail('That email address looks incomplete.');

      const text =
        'New enquiry from thegrowvista.com\n\n' +
        'Name: ' + name + '\n' +
        'Email: ' + email + '\n' +
        (phone ? 'Phone: ' + phone + '\n' : '') +
        'Service: ' + service + '\n\n' +
        (message || 'No message added.');

      window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(text), '_blank', 'noopener');

      note.textContent = 'Opening WhatsApp with your message. Press send there and we will reply shortly.';
      note.style.color = '#5483B3';
      form.reset();
    });
  }
})();
