# -*- coding: utf-8 -*-
"""
Diccionario ES → EN de los textos de index.html y privacidad.html.
La clave es el texto en español (sin etiquetas, espacios normalizados).
Si el valor EN contiene etiquetas HTML, reemplaza el contenido completo del elemento.
Ya aplicado en los HTML como atributos data-en="..."; este archivo queda como referencia
para revisar/editar traducciones.
"""
UI = {
# ---- navegación / comunes
"Inicio": "Home",
"Sobre mí": "About me",
"Áreas": "Areas",
"Experiencia": "Experience",
"Formación": "Education",
"Habilidades": "Skills",
"Perspectivas": "Insights",
"Contacto": "Contact",

# ---- hero
"Abogada Corporativa & Compliance": "Corporate & Compliance Attorney",
"Experta en Regulación, Contratos, Technology & AI Governance. Más de 12 años construyendo soluciones legales para el futuro.":
    "Expert in Regulation, Contracts, Technology & AI Governance. Over 12 years building legal solutions for the future.",
"Hablemos": "Let’s talk",
"Ver trayectoria": "View my track record",

# ---- sobre mí
"Sobre Mí": "About Me",
"Estrategia legal para la era digital": "Legal strategy for the digital age",
"Resumen Profesional": "Professional Summary",
"Abogada con más de 12 años de experiencia en gobernanza corporativa, inteligencia estratégica y gestión integral de riesgos. Especializada en la resolución de problemas operativos, cumplimiento normativo y fortalecimiento institucional en sectores público y privado, con aplicación de Inteligencia Artificial a procesos legales, contractuales y regulatorios.":
    "Attorney with over 12 years of experience in corporate governance, strategic intelligence and comprehensive risk management. Specialized in solving operational problems, regulatory compliance and institutional strengthening in the public and private sectors, applying Artificial Intelligence to legal, contractual and regulatory processes.",
"Años de experiencia": "Years of experience",
"Países LATAM": "LATAM countries",
"Sistemas jurídicos": "Legal systems",
"Sectores industriales": "Industry sectors",
"+ Proyectos legales": "+ Legal projects",

# ---- áreas de práctica
"Áreas de Práctica": "Practice Areas",
"Servicios especializados": "Specialized services",
"Gobernanza Corporativa": "Corporate Governance",
"Estructuración de órganos de gobierno, políticas internas y mejores prácticas para empresas en crecimiento.":
    "Design of governing bodies, internal policies and best practices for growing companies.",
"Asesoría en implementación ética y legal de Inteligencia Artificial en procesos empresariales.":
    "Advice on the ethical and legal implementation of Artificial Intelligence in business processes.",
"Compliance Regulatorio": "Regulatory Compliance",
"Diseño e implementación de programas de cumplimiento normativo nacional e internacional.":
    "Design and implementation of domestic and international regulatory compliance programs.",
"Contratos & Transacciones": "Contracts & Transactions",
"Negociación, redacción y gestión de contratos complejos para sectores público y privado.":
    "Negotiation, drafting and management of complex contracts for the public and private sectors.",
"Protección de Datos": "Data Protection",
"Cumplimiento con LFPDPPP, GDPR y marcos regulatorios de privacidad en LATAM.":
    "Compliance with the LFPDPPP, the GDPR and privacy regulatory frameworks across LATAM.",
"Propiedad Intelectual": "Intellectual Property",
"Protección de activos intangibles, patentes, marcas y secretos industriales para innovación.":
    "Protection of intangible assets, patents, trademarks and trade secrets for innovation.",

# ---- experiencia
"Trayectoria profesional": "Professional track record",
"Agosto 2018 — Presente": "August 2018 — Present",
"Agosto 2018 — Septiembre 2025": "August 2018 — September 2025",
"Febrero 2020 — Enero 2023": "February 2020 — January 2023",
"Agosto 2012 — Enero 2018": "August 2012 — January 2018",
"Enero 2009 — Agosto 2012": "January 2009 — August 2012",
"Firma tech especializada en gobernanza corporativa, compliance y propiedad intelectual para nuevos modelos de negocio \"tech & AI startups\", con experiencia en sistemas jurídicos de Estados Unidos y Latinoamérica (Colombia, Perú y Guatemala).":
    "Tech firm specialized in corporate governance, compliance and intellectual property for new business models (“tech & AI startups”), with experience in the legal systems of the United States and Latin America (Colombia, Peru and Guatemala).",
"Proyecto destacado: Atarraya, Inc — Legal Manager / Sector Privado (Biotecnología) / Agosto 2018 – Septiembre 2025. Responsable in-house de transacciones corporativas, laborales, propiedad intelectual y cumplimiento regulatorio en México y Estados Unidos.":
    "<strong>Featured project:</strong> Atarraya, Inc — Legal Manager / Private Sector (Biotechnology) / August 2018 – September 2025. In-house lead for corporate transactions, labor matters, intellectual property and regulatory compliance in Mexico and the United States.",
"Legal Manager — Sector Privado (Biotecnología)": "Legal Manager — Private Sector (Biotechnology)",
"Responsable in-house de las transacciones corporativas, laborales, propiedad intelectual y cumplimiento regulatorio de la empresa en México y Estados Unidos. Desarrollo de estrategias legales alineadas con las áreas financiera, operativa y de expansión, apoyando levantamiento de capital, alianzas estratégicas y crecimiento internacional.":
    "In-house lead for the company’s corporate transactions, labor matters, intellectual property and regulatory compliance in Mexico and the United States. Development of legal strategies aligned with the finance, operations and expansion teams, supporting capital raising, strategic alliances and international growth.",
"INAI — Instituto Nacional de Transparencia": "INAI — National Institute of Transparency",
"Asesora Externa — Sector Público (Protección de Datos y Privacidad)": "External Advisor — Public Sector (Data Protection and Privacy)",
"Asesora externa del órgano garante federal en materia de auditoría de cuentas, gestión contractual, control normativo y protección de datos personales. Responsable de supervisar el cumplimiento legal, regulatorio y de propiedad intelectual conforme a la normativa aplicable.":
    "External advisor to the federal oversight body on account auditing, contract management, regulatory control and personal data protection. Responsible for overseeing legal, regulatory and intellectual property compliance under applicable regulations.",
"Coordinadora Jurídica — Sector Energía": "Legal Coordinator — Energy Sector",
"Negociación, gestión de riesgos y administración de contratos para el sector de transformación industrial de hidrocarburos, logística y refinerías, incluyendo servicios integrales, obra pública, mantenimiento y servicios especializados. Vinculación y aplicación de políticas internas con el marco jurídico del sector energético.":
    "Negotiation, risk management and contract administration for the hydrocarbon industrial transformation, logistics and refining sector, including integrated services, public works, maintenance and specialized services. Alignment and application of internal policies with the legal framework of the energy sector.",
"Comisión Nacional de los Derechos Humanos (CNDH)": "National Human Rights Commission (CNDH)",
"Subdirectora de Consultoría en Asuntos Jurídicos": "Deputy Director of Legal Affairs Consulting",
"Desarrollo y aprobación de reglamentos internos y normas públicas (innovación digital de KPI), elaborando y aprobando normativas internas y estándares públicos del organismo, supervisando la implementación y cumplimiento de las mismas.":
    "Development and approval of internal regulations and public standards (digital KPI innovation), drafting and approving the agency’s internal rules and public standards, and overseeing their implementation and compliance.",

# ---- formación
"Formación Académica": "Academic Background",
"Universidad Panamericana (CDMX Campus)": "Universidad Panamericana (Mexico City Campus)",
"Abril 2026 — Abril 2028": "April 2026 — April 2028",
"Doctorado en Derecho": "PhD in Law",
"Defensa de Protocolo en Technology & AI Governance": "Research proposal defense in Technology & AI Governance",
"Enero 2012 — Diciembre 2013": "January 2012 — December 2013",
"Maestría en Derecho Administrativo": "Master’s Degree in Administrative Law",
"Especialización en Instituciones de Derecho Administrativo": "Postgraduate Specialization in Administrative Law Institutions",
"Licenciatura en Derecho": "Bachelor of Laws (LL.B.)",

# ---- filosofía
"Filosofía de Trabajo": "Work Philosophy",
"\"Apasionada por construir y colaborar con equipos legales e internos para mejorar procesos, siempre bajo un entorno amable, dinámico y de respeto mutuo.\"":
    "“Passionate about building and collaborating with legal and in-house teams to improve processes, always in a friendly, dynamic environment of mutual respect.”",

# ---- habilidades e idiomas
"Habilidades & Idiomas": "Skills & Languages",
"Las competencias que me representan": "The competencies that define me",
"Habilidades que me representan": "Skills that define me",
"Liderazgo": "Leadership",
"Comunicación": "Communication",
"Trabajo en equipo": "Teamwork",
"Organización": "Organization",
"Gestión analítica": "Analytical management",
"Práctica resolutiva": "Problem-solving practice",
"Idiomas": "Languages",
"Inglés": "English",
"100% — First Certificate Cambridge": "100% — Cambridge First Certificate",
"Francés": "French",
"40% — B1 en curso (UNAM - CELE)": "40% — B1 in progress (UNAM - CELE)",

# ---- perspectivas (inicio)
"Análisis legal para la era digital": "Legal analysis for the digital age",
"Ver todas las publicaciones": "View all articles",

# ---- testimonios
"Testimonios": "Testimonials",
"Lo que dicen quienes han trabajado conmigo": "What people who have worked with me say",
"\"Gabriela entendió desde el primer día los riesgos regulatorios de nuestro modelo de negocio. Su asesoría en compliance nos permitió cerrar una ronda de inversión sin contratiempos legales.\"":
    "“Gabriela understood the regulatory risks of our business model from day one. Her compliance advice allowed us to close an investment round without any legal setbacks.”",
"\"Trabajar con Gabriela en temas de AI Governance fue clave para estructurar nuestras políticas internas antes de escalar el producto a otros países de la región.\"":
    "“Working with Gabriela on AI Governance was key to structuring our internal policies before scaling the product to other countries in the region.”",
"\"Su capacidad para explicar temas legales complejos de forma clara hizo toda la diferencia en la negociación de nuestros contratos internacionales.\"":
    "“Her ability to explain complex legal matters clearly made all the difference in negotiating our international contracts.”",
"CEO, Startup Tech": "CEO, Tech Startup",
"Directora de Operaciones": "Director of Operations",
"Fundador, Consultora Regional": "Founder, Regional Consultancy",

# ---- contacto
"Hablemos de su proyecto": "Let’s talk about your project",
"¿Necesita asesoría legal para su empresa tech o requiere apoyo en cumplimiento normativo? Estoy aquí para ayudarle.":
    "Do you need legal advice for your tech company or support with regulatory compliance? I am here to help.",
"ENVIAR MENSAJE": "SEND MESSAGE",

# ---- footer / banner
"© 2026 Gabriela L. González Vázquez. Todos los derechos reservados.": "© 2026 Gabriela L. González Vázquez. All rights reserved.",
"Aviso de Privacidad": "Privacy Notice",
"Términos de servicio": "Terms of Service",
"Utilizamos cookies para mejorar tu experiencia. Al continuar navegando, aceptas nuestro Aviso de Privacidad.":
    "We use cookies to improve your experience. By continuing to browse, you accept our <a href=\"privacidad.html\" target=\"_blank\">Privacy Notice</a>.",
"Rechazar": "Decline",
"Aceptar": "Accept",

# ---- video slot
"Tu video aquí": "Your video here",

# ================= PRIVACIDAD =================
"Aviso de Privacidad Integral": "Comprehensive Privacy Notice",
"Última actualización: 13 de enero de 2026": "Last updated: January 13, 2026",
"1. Identidad y Domicilio del Responsable": "1. Identity and Address of the Data Controller",
"Gabriela L. González Vázquez (en adelante, \"la Responsable\"), con domicilio en Ciudad de México, es la entidad responsable del tratamiento de sus datos personales, en términos de la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP).":
    "<strong>Gabriela L. González Vázquez</strong> (hereinafter, “the Controller”), domiciled in Mexico City, is the party responsible for the processing of your personal data, pursuant to the Federal Law on the Protection of Personal Data Held by Private Parties (LFPDPPP).",
"Para cualquier duda o aclaración relacionada con este aviso, puede contactarnos a través de los correos electrónicos: ggv@blic.com.mx y gapiso@gmail.com.":
    "For any questions or clarifications regarding this notice, you may contact us at the following email addresses: <a href=\"mailto:ggv@blic.com.mx\">ggv@blic.com.mx</a> and <a href=\"mailto:gapiso@gmail.com\">gapiso@gmail.com</a>.",
"2. Datos Personales que se Recaban": "2. Personal Data Collected",
"Para llevar a cabo las finalidades descritas en el presente aviso de privacidad, se podrán recabar las siguientes categorías de datos personales:":
    "To carry out the purposes described in this privacy notice, the following categories of personal data may be collected:",
"Datos de identificación: Nombre completo, correo electrónico, teléfono.":
    "<strong>Identification data:</strong> Full name, email address, telephone number.",
"Datos profesionales: Cargo, empresa, sector industrial.":
    "<strong>Professional data:</strong> Job title, company, industry sector.",
"No se recaban datos personales sensibles. Sin embargo, si en el futuro se llegaran a tratar, se le informará y se solicitará su consentimiento expreso y por escrito.":
    "No sensitive personal data is collected. However, should such data be processed in the future, you will be informed and your express written consent will be requested.",
"3. Finalidades del Tratamiento": "3. Purposes of Processing",
"Sus datos personales serán tratados para las siguientes finalidades:": "Your personal data will be processed for the following purposes:",
"Finalidades Necesarias (requieren su consentimiento):": "Necessary Purposes (require your consent):",
"Proporcionar los servicios de asesoría legal y consultoría solicitados.": "To provide the legal advisory and consulting services requested.",
"Establecer contacto comercial y responder a sus solicitudes de información.": "To establish business contact and respond to your information requests.",
"Elaborar contratos, convenios y cualquier otro documento legal necesario para la prestación de servicios.":
    "To prepare contracts, agreements and any other legal document necessary for the provision of services.",
"Finalidades Voluntarias (no requieren su consentimiento para la relación jurídica):": "Voluntary Purposes (do not require your consent for the legal relationship):",
"Enviar comunicaciones informativas, boletines, invitaciones a eventos y material promocional sobre temas legales de su interés.":
    "To send informational communications, newsletters, event invitations and promotional material on legal topics of interest to you.",
"Realizar encuestas de satisfacción y estudios de mercado para mejorar la calidad de nuestros servicios.":
    "To conduct satisfaction surveys and market studies to improve the quality of our services.",
"Usted puede manifestar su negativa para el tratamiento de sus datos personales para las finalidades voluntarias enviando un correo electrónico a las direcciones proporcionadas.":
    "You may object to the processing of your personal data for the voluntary purposes by sending an email to the addresses provided.",
"4. Mecanismos para Ejercer los Derechos ARCO": "4. Mechanisms to Exercise ARCO Rights",
"Usted tiene derecho a conocer qué datos personales tenemos de usted, para qué los utilizamos y las condiciones del uso que les damos (Acceso). Asimismo, es su derecho solicitar la corrección de su información personal en caso de que esté desactualizada, sea inexacta o incompleta (Rectificación); que la eliminemos de nuestros registros o bases de datos cuando considere que la misma no está siendo utilizada adecuadamente (Cancelación); así como oponerse al uso de sus datos personales para fines específicos (Oposición). Estos derechos se conocen como derechos ARCO.":
    "You have the right to know what personal data we hold about you, what we use it for and the conditions of that use (Access). You also have the right to request the correction of your personal information if it is outdated, inaccurate or incomplete (Rectification); to have it deleted from our records or databases when you consider that it is not being used properly (Cancellation); and to object to the use of your personal data for specific purposes (Opposition). These rights are known as ARCO rights.",
"Para ejercer cualquiera de los derechos ARCO, usted deberá enviar una solicitud a los correos electrónicos ggv@blic.com.mx y gapiso@gmail.com, que contenga:":
    "To exercise any of the ARCO rights, you must send a request to the email addresses <a href=\"mailto:ggv@blic.com.mx\">ggv@blic.com.mx</a> and <a href=\"mailto:gapiso@gmail.com\">gapiso@gmail.com</a>, containing:",
"Nombre completo y correo electrónico para comunicarle la respuesta.": "Full name and email address to communicate our response.",
"Documento que acredite su identidad o, en su caso, la representación legal.": "A document proving your identity or, where applicable, legal representation.",
"Descripción clara y precisa de los datos personales respecto de los que se busca ejercer alguno de los derechos ARCO.":
    "A clear and precise description of the personal data with respect to which you seek to exercise any of the ARCO rights.",
"Cualquier otro elemento o documento que facilite la localización de los datos personales.":
    "Any other element or document that helps locate the personal data.",
"La Responsable le comunicará la determinación adoptada en un plazo máximo de veinte días hábiles contados desde la fecha en que se recibió la solicitud.":
    "The Controller will notify you of its decision within a maximum of twenty business days from the date the request was received.",
"5. Transferencia de Datos Personales": "5. Transfer of Personal Data",
"Sus datos personales no serán transferidos a terceros sin su consentimiento, salvo en los casos previstos por la ley.":
    "Your personal data will not be transferred to third parties without your consent, except in the cases provided for by law.",
"6. Uso de Cookies y Tecnologías de Rastreo": "6. Use of Cookies and Tracking Technologies",
"Este sitio web utiliza cookies y otras tecnologías de rastreo para mejorar la experiencia del usuario, analizar el tráfico del sitio y personalizar el contenido. Puede gestionar sus preferencias de cookies en cualquier momento a través de la configuración de su navegador.":
    "This website uses cookies and other tracking technologies to improve the user experience, analyze site traffic and personalize content. You can manage your cookie preferences at any time through your browser settings.",
"7. Cambios al Aviso de Privacidad": "7. Changes to the Privacy Notice",
"La Responsable se reserva el derecho de efectuar en cualquier momento modificaciones o actualizaciones al presente aviso de privacidad. Estas modificaciones estarán disponibles al público a través de nuestro sitio web en la sección de aviso de privacidad.":
    "The Controller reserves the right to make modifications or updates to this privacy notice at any time. Such modifications will be made available to the public through our website in the privacy notice section.",
"8. Autoridad de Control": "8. Supervisory Authority",
"Si usted considera que sus derechos de protección de datos han sido vulnerados, puede presentar una queja o denuncia ante la autoridad de control competente en México, que a partir de 2025 es la Secretaría Anticorrupción y Buen Gobierno, o ante la autoridad de control de su país de residencia si se encuentra en el Espacio Económico Europeo (por ejemplo, la Agencia Española de Protección de Datos).":
    "If you believe your data protection rights have been infringed, you may file a complaint with the competent supervisory authority in Mexico, which since 2025 is the Ministry of Anti-Corruption and Good Governance, or with the supervisory authority of your country of residence if you are located in the European Economic Area (for example, the Spanish Data Protection Agency).",
"Volver al Inicio": "Back to Home",
}

# Atributos (alt, aria-label, etc.): (atributo, valor ES) → valor EN
ATTRS = {
    ("alt", "Servicios legales corporativos"): "Corporate legal services",
    ("alt", "Gabriela L. González Vázquez"): "Gabriela L. González Vázquez",
    ("alt", "BLIC - Business Legal Intelligence Consulting"): "BLIC - Business Legal Intelligence Consulting",
    ("alt", "INAI - Instituto Nacional de Transparencia"): "INAI - National Institute of Transparency",
    ("alt", "Pemex - Petróleos Mexicanos"): "Pemex - Petróleos Mexicanos",
    ("alt", "CNDH - Comisión Nacional de los Derechos Humanos"): "CNDH - National Human Rights Commission",
    ("alt", "Universidad Panamericana"): "Universidad Panamericana",
    ("aria-label", "Contactar por WhatsApp"): "Contact via WhatsApp",
}
WA_ES = "https://wa.me/525537179626?text=Hola%20Gabriela,%20me%20gustar%C3%ADa%20agendar%20una%20consulta."
WA_EN = "https://wa.me/525537179626?text=Hello%20Gabriela,%20I%20would%20like%20to%20schedule%20a%20consultation."
META_ES = {"title": "Gabriela L. González Vázquez - Abogada Corporativa & Compliance"}
META_EN_TITLE = "Gabriela L. González Vázquez - Corporate & Compliance Attorney"
META_EN_DESC = "Corporate & Compliance Attorney. Expert in Regulation, Contracts, Technology & AI Governance. Over 12 years building legal solutions for the future."
PRIV_TITLE_EN = "Privacy Notice - Gabriela L. González Vázquez"
