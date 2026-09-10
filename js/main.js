// ============================================
// GGLV - Gabriela L. González Vázquez
// Main JavaScript File
// ============================================

// ------------------------------------------------
// Inject styles needed for the scroll animations.
// Self-contained here so this file works even if
// styles.css hasn't been updated separately.
// ------------------------------------------------
(function injectScrollAnimationStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .scroll-progress {
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            width: 0%;
            background: linear-gradient(90deg, var(--color-accent, #cda35a), var(--color-accent-dark, #b98c40));
            z-index: 2000;
            transition: width 0.12s ease-out;
            pointer-events: none;
        }

        .fade-in-section {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: opacity, transform;
        }

        .fade-in-section.in-view {
            opacity: 1;
            transform: translateY(0);
        }

        .fade-in-left {
            opacity: 0;
            transform: translateX(-35px);
            transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .fade-in-left.in-view {
            opacity: 1;
            transform: translateX(0);
        }

        .fade-in-right {
            opacity: 0;
            transform: translateX(35px);
            transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .fade-in-right.in-view {
            opacity: 1;
            transform: translateX(0);
        }

        /* Respect people who prefer reduced motion */
        @media (prefers-reduced-motion: reduce) {
            .fade-in-section,
            .fade-in-left,
            .fade-in-right {
                opacity: 1 !important;
                transform: none !important;
                transition: none !important;
            }
            .scroll-progress {
                transition: none;
            }
        }
    `;
    document.head.appendChild(style);
})();

// ------------------------------------------------
// Scroll Progress Bar
// Always visible and always updating while the
// page is scrolled, in either direction.
// ------------------------------------------------
const progressBar = document.createElement('div');
progressBar.className = 'scroll-progress';
document.body.appendChild(progressBar);

function updateScrollProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = progress + '%';
}

window.addEventListener('scroll', updateScrollProgress, { passive: true });
updateScrollProgress();

// ------------------------------------------------
// Mobile Menu Toggle
// ------------------------------------------------
const menuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');

if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', () => {
        navLinks.classList.toggle('active');

        // Animate hamburger to X
        const spans = menuBtn.querySelectorAll('span');
        spans.forEach(span => span.classList.toggle('active'));
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!menuBtn.contains(e.target) && !navLinks.contains(e.target)) {
            navLinks.classList.remove('active');
            const spans = menuBtn.querySelectorAll('span');
            spans.forEach(span => span.classList.remove('active'));
        }
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            const spans = menuBtn.querySelectorAll('span');
            spans.forEach(span => span.classList.remove('active'));
        });
    });
}

// ------------------------------------------------
// Smooth Scroll for Anchor Links
// ------------------------------------------------
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');

        if (targetId === '#') return;

        const target = document.querySelector(targetId);

        if (target) {
            e.preventDefault();
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ------------------------------------------------
// Header Scroll Effect
// ------------------------------------------------
const header = document.querySelector('.header');

if (header) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

// ------------------------------------------------
// Form Submission (Formspree)
// Requires a real Formspree form ID in the <form
// action="..."> attribute in index.html — see the
// HTML comment right above the form for setup steps.
// ------------------------------------------------
const contactForm = document.querySelector('.contact-form form');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Basic validation
        const nombre = document.getElementById('nombre');
        const email = document.getElementById('email');
        const mensaje = document.getElementById('mensaje');

        let isValid = true;

        if (nombre && nombre.value.trim() === '') {
            isValid = false;
            nombre.style.borderColor = '#ff4444';
        }

        if (email && (email.value.trim() === '' || !email.value.includes('@'))) {
            isValid = false;
            email.style.borderColor = '#ff4444';
        }

        if (mensaje && mensaje.value.trim() === '') {
            isValid = false;
            mensaje.style.borderColor = '#ff4444';
        }

        if (!isValid) return;

        const submitBtn = contactForm.querySelector('.btn-submit');
        const originalText = submitBtn.textContent;

        submitBtn.textContent = 'Enviando...';
        submitBtn.disabled = true;

        try {
            const formData = new FormData(contactForm);
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            });

            if (response.ok) {
                submitBtn.textContent = '¡Mensaje enviado! ✓';
                submitBtn.style.background = '#4CAF50';
                submitBtn.style.borderColor = '#4CAF50';
                contactForm.reset();
            } else {
                throw new Error('Formspree respondió con un error');
            }
        } catch (err) {
            submitBtn.textContent = 'Error al enviar, intenta de nuevo';
            submitBtn.style.background = '#ff4444';
            submitBtn.style.borderColor = '#ff4444';
            console.error('Error enviando el formulario:', err);
        } finally {
            setTimeout(() => {
                submitBtn.textContent = originalText;
                submitBtn.style.background = '';
                submitBtn.style.borderColor = '';
                submitBtn.disabled = false;
            }, 3500);
        }
    });

    // Remove error styling on input
    const formInputs = contactForm.querySelectorAll('input, textarea, select');
    formInputs.forEach(input => {
        input.addEventListener('input', () => {
            input.style.borderColor = '';
        });
    });
}

// ------------------------------------------------
// Scroll Animations
// Elements fade/slide in every time they enter the
// viewport, and reset every time they leave it, so
// the effect keeps replaying whether you scroll down
// or back up — it never "runs out".
// ------------------------------------------------
function initScrollAnimations() {
    const upTargets = document.querySelectorAll(
        '.practice-card, .education-card, .timeline-item, .project, .stat, .language-tag, .testimonial-card, .collaborator-badge'
    );
    const leftTargets = document.querySelectorAll(
        '.about-text, .contact-info'
    );
    const rightTargets = document.querySelectorAll(
        '.about-image, .contact-form, .experience-visual'
    );

    const applyClass = (list, className) => {
        list.forEach((el, index) => {
            el.classList.add(className);
            // small stagger so groups of cards/items don't all move at once
            el.style.transitionDelay = `${(index % 4) * 0.08}s`;
        });
    };

    applyClass(upTargets, 'fade-in-section');
    applyClass(leftTargets, 'fade-in-left');
    applyClass(rightTargets, 'fade-in-right');

    const allTargets = [...upTargets, ...leftTargets, ...rightTargets];

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            } else {
                // Removing the class resets the element so the
                // animation plays again next time it scrolls into view.
                entry.target.classList.remove('in-view');
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -10% 0px'
    });

    allTargets.forEach((el) => observer.observe(el));
}

initScrollAnimations();

// ------------------------------------------------
// Update copyright year
// ------------------------------------------------
const yearSpan = document.querySelector('.footer-bottom p:first-child');
if (yearSpan) {
    const currentYear = new Date().getFullYear();
    yearSpan.innerHTML = yearSpan.innerHTML.replace('2026', currentYear);
}
