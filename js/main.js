gsap.registerPlugin(ScrollTrigger);

/* ============================================
   ANIMACIÓN DE FADE IN (IDA Y VUELTA)
   ============================================ */
gsap.utils.toArray('.fade-in').forEach(element => {
    gsap.fromTo(element, 
        { opacity: 0, y: 50 }, 
        {
            opacity: 1, 
            y: 0, 
            duration: 1,
            scrollTrigger: {
                trigger: element,
                start: "top 85%", 
                toggleActions: "play reverse play reverse"
            }
        }
    );
});

/* ============================================
   CONTADORES ANIMADOS (Sobre Mí)
   ============================================ */
gsap.utils.toArray('.contador').forEach(contador => {
    const target = parseInt(contador.getAttribute('data-target'));
    
    gsap.fromTo(contador, 
        { innerText: 0 },
        {
            innerText: target,
            duration: 2,
            ease: "power2.out",
            snap: { innerText: 1 },
            scrollTrigger: {
                trigger: contador,
                start: "top 85%",
                toggleActions: "play reverse play reverse"
            }
        }
    );
});

/* ============================================
   FRASE ROTATIVA EN EL HERO
   ============================================ */
const frases = [
    "Gobernanza Corporativa",
    "AI Governance",
    "Compliance Regulatorio",
    "Contratos & Transacciones",
    "Protección de Datos"
];

let indiceFrase = 0;
const elementoRotativo = document.querySelector('.rotativo-texto');

function rotarFrase() {
    if (!elementoRotativo) return;
    
    gsap.to(elementoRotativo, {
        opacity: 0,
        y: -10,
        duration: 0.5,
        onComplete: () => {
            indiceFrase = (indiceFrase + 1) % frases.length;
            elementoRotativo.textContent = frases[indiceFrase];
            gsap.fromTo(elementoRotativo, 
                { opacity: 0, y: 10 }, 
                { opacity: 1, y: 0, duration: 0.5 }
            );
        }
    });
}

setInterval(rotarFrase, 2500);

/* ============================================
   TRANSICIÓN DE COLOR DE FONDO
   (Amarillo cambiado por Charcoal #2B2B2B)
   ============================================ */
gsap.to('body', {
    backgroundColor: '#2B2B2B',
    scrollTrigger: {
        trigger: '#sobre-mi',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#B4F5B4',
    scrollTrigger: {
        trigger: '#transicion-servicios',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#2B2B2B',
    scrollTrigger: {
        trigger: '#servicios',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#FFFFFF',
    scrollTrigger: {
        trigger: '#experiencia',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#FAD6C5',
    scrollTrigger: {
        trigger: '#formacion',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#E65C00',
    scrollTrigger: {
        trigger: '#cita',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#2B2B2B',
    scrollTrigger: {
        trigger: '#habilidades',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#FFFFFF',
    scrollTrigger: {
        trigger: '#testimonios',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

gsap.to('body', {
    backgroundColor: '#B4F5B4',
    scrollTrigger: {
        trigger: '#contacto',
        start: 'top 50%',
        end: 'bottom 50%',
        toggleActions: 'play reverse play reverse'
    }
});

/* ============================================
   EFECTO PARALLAX EN IMÁGENES
   ============================================ */
gsap.utils.toArray('.experiencia-img img').forEach(img => {
    gsap.to(img, {
        y: -30,
        scrollTrigger: {
            trigger: img,
            start: "top bottom",
            end: "bottom top",
            scrub: true
        }
    });
});

/* ============================================
   ANIMACIÓN DEL LOGO UNIVERSIDAD PANAMERICANA
   ============================================ */
const logoUP = document.querySelector('.formacion-img-container img');

if (logoUP) {
    gsap.fromTo(logoUP,
        { 
            opacity: 0, 
            scale: 0.4, 
            rotation: -15, 
            y: 60 
        },
        {
            opacity: 1,
            scale: 1,
            rotation: 0,
            y: 0,
            duration: 1.4,
            ease: "back.out(1.5)",
            clearProps: "transform,opacity",
            scrollTrigger: {
                trigger: '#formacion',
                start: "top 70%",
                toggleActions: "play reverse play reverse"
            }
        }
    );
}

/* ============================================
   LÓGICA DEL BANNER DE AVISO DE PRIVACIDAD
   ============================================ */
document.addEventListener('DOMContentLoaded', () => {
    const banner = document.querySelector('.aviso-privacidad-banner');
    if (!banner) return;

    const consentimiento = localStorage.getItem('consentimiento-privacidad');

    if (consentimiento) {
        return;
    }

    setTimeout(() => {
        banner.classList.add('visible');
    }, 1500);

    document.getElementById('btn-aceptar-cookies').addEventListener('click', () => {
        localStorage.setItem('consentimiento-privacidad', 'aceptado');
        banner.classList.remove('visible');
        console.log('Cookies aceptadas. Inicializando scripts de análisis...');
    });

    document.getElementById('btn-rechazar-cookies').addEventListener('click', () => {
        localStorage.setItem('consentimiento-privacidad', 'rechazado');
        banner.classList.remove('visible');
        console.log('Cookies rechazadas. No se cargarán scripts de seguimiento.');
    });
});