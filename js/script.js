document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');

  if (hamburger) {
    hamburger.addEventListener('click', function () {
      navLinks.classList.toggle('active');
    });
  }

  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
    });
  });

  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      alert('Thank you for contacting us! We will get back to you shortly.');
      this.reset();
    });
  }

  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', function () {
      const item = this.parentElement;
      const isActive = item.classList.contains('active');
      item.closest('.faq-list').querySelectorAll('.faq-item.active').forEach(active => {
        active.classList.remove('active');
      });
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  const brandTabs = document.querySelectorAll('.brand-tab');
  const brandPanels = document.querySelectorAll('.brand-panel');

  function switchBrand(brand) {
    brandTabs.forEach(t => t.classList.toggle('active', t.dataset.brand === brand));
    brandPanels.forEach(p => p.classList.toggle('active', p.dataset.brand === brand));
    const target = document.getElementById('services-section');
    if (target) {
      const headerOffset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - headerOffset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  }

  brandTabs.forEach(tab => {
    tab.addEventListener('click', function () {
      switchBrand(this.dataset.brand);
    });
  });

  document.querySelectorAll('.brand-link').forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      switchBrand(this.dataset.brand);
    });
  });

  const urlParams = new URLSearchParams(window.location.search);
  const brandParam = urlParams.get('brand');
  if (brandParam) {
    const panel = document.querySelector(`.brand-panel[data-brand="${brandParam}"]`);
    if (panel) switchBrand(brandParam);
  }

  const statNumbers = document.querySelectorAll('.stat-number');
  if (statNumbers.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.dataset.target);
          let current = 0;
          const step = Math.ceil(target / 40);
          const timer = setInterval(() => {
            current += step;
            if (current >= target) {
              current = target;
              clearInterval(timer);
            }
            el.textContent = current;
          }, 30);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });
    statNumbers.forEach(n => observer.observe(n));
  }
});
