# -*- coding: utf-8 -*-
"""
Genera privacidad.html (Aviso de Privacidad Integral) y aviso-legal.html (Aviso legal y términos de uso).
Uso (desde la raíz del sitio):   python3 tools/generar_legales.py

Cada bloque es (español, inglés). Las etiquetas HTML dentro de los textos están permitidas.
Si cambia algo del sitio (cookies, servicios externos, formularios, analítica), actualice este archivo.
"""
import os, sys, html as H
sys.path.insert(0, os.path.dirname(__file__))
from generar_articulos import head, header, footer

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
esc = lambda s: H.escape(s, quote=True)

ACTUALIZADO = ("9 de noviembre de 2026", "November 9, 2026")
CORREO = '<a href="mailto:ggv@blic.com.mx">ggv@blic.com.mx</a>'


def bloque(tag, es, en, attrs=""):
    a = f" {attrs}" if attrs else ""
    return f'<{tag}{a} data-en="{esc(en)}">{es}</{tag}>'

def seccion(id_, titulo, partes):
    """partes: lista de ('p'|'h3', es, en) o ('ul', [(es, en), ...])"""
    out = [f'<section class="privacidad-section" id="{id_}">', bloque("h2", *titulo)]
    for p in partes:
        if p[0] == "ul":
            out.append("<ul>" + "".join(bloque("li", es, en) for es, en in p[1]) + "</ul>")
        else:
            out.append(bloque(p[0], p[1], p[2]))
    out.append("</section>")
    return "\n".join(out)

def pagina(nombre, titulo, desc, h1, intro, secciones, eyebrow=("Legal", "Legal")):
    out = head(titulo, desc, nombre, "website")
    out += header("")
    indice = "".join(f'<li><a class="link" href="#{s[0]}" data-en="{esc(s[1][1])}">{s[1][0]}</a></li>' for s in secciones)
    out += f'''
<main id="main">
<div class="wrap legal">
{bloque("p", *eyebrow, attrs='class="eyebrow"')}
{bloque("h1", *h1)}
<p class="fecha-actualizacion" data-en="Last updated: {ACTUALIZADO[1]}">Última actualización: {ACTUALIZADO[0]}</p>
{"".join(bloque("p", es, en, attrs='class="legal-intro"') for es, en in intro)}
<nav class="legal-index" aria-label="Contenido" data-en-aria-label="Contents"><ol>{indice}</ol></nav>
{"".join(seccion(*s) for s in secciones)}
<a class="btn btn-line btn-volver" href="index.html" data-en="Back to home">Volver al inicio</a>
</div>
</main>
'''
    out += footer()
    open(os.path.join(ROOT, nombre), "w", encoding="utf-8").write(out)


# ====================================================================== AVISO DE PRIVACIDAD
PRIV = [
("responsable", ("1. Identidad y domicilio de la responsable", "1. Identity and address of the controller"), [
  ("p", "<strong>Gabriela L. González Vázquez</strong> (en adelante, “la Responsable”), con domicilio en la Ciudad de México, México, es responsable del tratamiento de los datos personales que se obtengan a través de este sitio web y de los medios de contacto que en él se indican.",
        "<strong>Gabriela L. González Vázquez</strong> (the “Controller”), with an address in Mexico City, Mexico, is responsible for the processing of personal data obtained through this website and the contact channels listed on it."),
  ("p", f"Para cualquier asunto relacionado con este aviso o con sus datos personales: {CORREO}.",
        f"For any matter related to this notice or your personal data: {CORREO}."),
]),
("datos", ("2. Datos personales que se tratan y cómo se obtienen", "2. Personal data processed and how it is obtained"), [
  ("p", "Este sitio <strong>no tiene formularios, registros ni cuentas de usuario</strong>. Los datos personales se obtienen únicamente en estos casos:",
        "This website <strong>has no forms, sign-ups or user accounts</strong>. Personal data is obtained only in the following cases:"),
  ("ul", [
    ("<strong>Cuando usted nos escribe</strong> por correo electrónico o WhatsApp: nombre, correo electrónico, número de teléfono, empresa, cargo y la información que decida compartir sobre su asunto.",
     "<strong>When you write to us</strong> by email or WhatsApp: name, email address, phone number, company, job title and any information you choose to share about your matter."),
    ("<strong>Datos técnicos de navegación</strong>: dirección IP, tipo de navegador, sistema operativo, fecha y hora de la visita y páginas solicitadas. Los registra el proveedor de alojamiento del sitio para fines de seguridad y funcionamiento; la Responsable no los utiliza para identificarle ni para elaborar perfiles.",
     "<strong>Technical browsing data</strong>: IP address, browser type, operating system, date and time of the visit and pages requested. They are logged by the site’s hosting provider for security and operational purposes; the Controller does not use them to identify you or to build profiles."),
  ]),
  ("p", "<strong>Contacto guiado y autoevaluación.</strong> Las opciones que usted elige en el contacto guiado y las respuestas de la autoevaluación se procesan únicamente en su navegador para armar un mensaje o mostrar un resultado. No se envían a ningún servidor ni se guardan. Si decide enviar el mensaje, este se abre en su propia aplicación de WhatsApp o de correo, y a partir de ese momento aplica lo descrito en este aviso.",
        "<strong>Guided contact and self-assessment.</strong> The options you choose in the guided contact and the answers in the self-assessment are processed only in your browser to compose a message or show a result. They are not sent to any server or stored. If you decide to send the message, it opens in your own WhatsApp or email app, and from then on this notice applies."),
  ("p", "<strong>Datos sensibles.</strong> No se solicitan datos personales sensibles a través de este sitio. Le pedimos no enviarlos por correo o WhatsApp en el primer contacto. Si para atender un asunto fuera indispensable tratarlos, se le informará previamente y se recabará su consentimiento expreso y por escrito.",
        "<strong>Sensitive data.</strong> No sensitive personal data is requested through this website. Please do not send it by email or WhatsApp in your first contact. If processing it became essential to handle a matter, you will be informed in advance and your express written consent will be obtained."),
  ("p", "<strong>Menores de edad.</strong> Este sitio no está dirigido a personas menores de 18 años y no se recaban sus datos de forma intencional.",
        "<strong>Minors.</strong> This website is not directed at persons under 18 years of age and their data is not knowingly collected."),
]),
("finalidades", ("3. Finalidades del tratamiento", "3. Purposes of processing"), [
  ("h3", "Finalidades primarias (necesarias para la relación con usted)", "Primary purposes (necessary for our relationship with you)"),
  ("ul", [
    ("Atender y responder su solicitud de información o de consulta.", "To handle and respond to your request for information or consultation."),
    ("Evaluar su asunto y, en su caso, prestarle servicios de asesoría y consultoría legal.", "To assess your matter and, where applicable, provide legal advisory and consulting services."),
    ("Elaborar propuestas, contratos y demás documentos propios de la relación profesional.", "To prepare proposals, engagement letters and other documents inherent to the professional relationship."),
    ("Cumplir obligaciones legales, fiscales y profesionales aplicables.", "To comply with applicable legal, tax and professional obligations."),
    ("Mantener la seguridad y el funcionamiento del sitio web.", "To maintain the security and operation of the website."),
  ]),
  ("h3", "Finalidades secundarias (no necesarias)", "Secondary purposes (not necessary)"),
  ("ul", [
    ("Enviarle comunicaciones, artículos o invitaciones a eventos sobre temas legales que puedan ser de su interés.", "To send you communications, articles or event invitations on legal topics that may interest you."),
  ]),
  ("p", f"Si no desea que sus datos se traten para la finalidad secundaria, puede indicarlo en cualquier momento escribiendo a {CORREO} con el asunto “Finalidades secundarias”. Su negativa no afectará la atención de su solicitud ni los servicios que contrate.",
        f"If you do not want your data processed for the secondary purpose, you may say so at any time by writing to {CORREO} with the subject line “Secondary purposes”. Your refusal will not affect the handling of your request or any services you engage."),
]),
("conservacion", ("4. Plazo de conservación", "4. Retention period"), [
  ("p", "Los datos personales se conservan solo durante el tiempo necesario para cumplir la finalidad para la que se obtuvieron y durante los plazos que exijan las disposiciones legales aplicables (por ejemplo, fiscales o de prescripción de acciones). Concluidos dichos plazos, se bloquean y posteriormente se suprimen de forma segura.",
        "Personal data is kept only for as long as necessary to fulfil the purpose for which it was obtained and for the periods required by applicable law (for example, tax rules or statutes of limitation). Once those periods end, the data is blocked and then securely deleted."),
]),
("transferencias", ("5. Encargados, transferencias y transferencias internacionales", "5. Processors, transfers and international transfers"), [
  ("p", "<strong>Sus datos no se venden ni se ceden con fines publicitarios.</strong> Para operar este sitio y comunicarnos con usted intervienen los siguientes proveedores, que tratan datos por cuenta de la Responsable o como responsables independientes de sus propios servicios:",
        "<strong>Your data is not sold or shared for advertising purposes.</strong> The following providers are involved in running this website and communicating with you; they process data on the Controller’s behalf or as independent controllers of their own services:"),
  ("ul", [
    ("<strong>GitHub, Inc.</strong> (Estados Unidos): alojamiento del sitio web y registros técnicos de acceso.", "<strong>GitHub, Inc.</strong> (United States): website hosting and technical access logs."),
    ("<strong>Proveedor de correo electrónico</strong> de la Responsable: recepción y envío de mensajes.", "The Controller’s <strong>email provider</strong>: receiving and sending messages."),
    ("<strong>WhatsApp (Meta Platforms)</strong>: solo si usted elige este canal; el servicio se rige además por las políticas de privacidad de WhatsApp.", "<strong>WhatsApp (Meta Platforms)</strong>: only if you choose this channel; the service is also governed by WhatsApp’s privacy policies."),
  ]),
  ("p", "Algunos de estos proveedores se ubican fuera de México, por lo que pueden existir transferencias internacionales. Para personas en el Espacio Económico Europeo, dichas transferencias se realizan conforme a los mecanismos previstos en el RGPD que tenga vigentes cada proveedor (como decisiones de adecuación o cláusulas contractuales tipo).",
        "Some of these providers are located outside Mexico, so international transfers may occur. For persons in the European Economic Area, such transfers take place under the GDPR mechanisms each provider has in place (such as adequacy decisions or standard contractual clauses)."),
  ("p", "Fuera de lo anterior, sus datos solo se transfieren a terceros sin su consentimiento en los supuestos permitidos por la ley, como el requerimiento fundado de una autoridad competente.",
        "Beyond the above, your data is only transferred to third parties without your consent in the cases permitted by law, such as a substantiated request from a competent authority."),
]),
("derechos", ("6. Derechos ARCO, revocación del consentimiento y limitación del uso", "6. ARCO rights, withdrawal of consent and limitation of use"), [
  ("p", "Usted puede <strong>Acceder</strong> a sus datos personales, <strong>Rectificarlos</strong> si son inexactos o incompletos, <strong>Cancelarlos</strong> cuando considere que no se requieren para alguna de las finalidades, y <strong>Oponerse</strong> a su tratamiento para fines específicos (derechos ARCO). También puede revocar el consentimiento otorgado y solicitar que se limite el uso o la divulgación de sus datos.",
        "You may <strong>Access</strong> your personal data, <strong>Rectify</strong> it if inaccurate or incomplete, <strong>Cancel</strong> it when you consider it is not needed for any of the purposes, and <strong>Object</strong> to its processing for specific purposes (ARCO rights). You may also withdraw your consent and request that the use or disclosure of your data be limited."),
  ("p", f"Para ejercerlos, envíe una solicitud a {CORREO} que contenga:", f"To exercise them, send a request to {CORREO} including:"),
  ("ul", [
    ("Su nombre completo y el medio para comunicarle la respuesta.", "Your full name and the means by which to send you the response."),
    ("Un documento que acredite su identidad o, en su caso, la representación legal de quien actúe en su nombre.", "A document proving your identity or, where applicable, the legal representation of the person acting on your behalf."),
    ("La descripción clara de los datos y del derecho que desea ejercer.", "A clear description of the data and of the right you wish to exercise."),
    ("Cualquier elemento que facilite la localización de los datos y, si solicita una rectificación, la documentación que la sustente.", "Any information that helps locate the data and, if you request a rectification, supporting documentation."),
  ]),
  ("p", "La Responsable le comunicará su determinación en un plazo máximo de veinte días hábiles contados desde la recepción de la solicitud y, si resulta procedente, la hará efectiva dentro de los quince días hábiles siguientes. El ejercicio de estos derechos es gratuito; solo podrán cobrarse, en su caso, los gastos justificados de envío o reproducción.",
        "The Controller will notify you of its decision within a maximum of twenty business days from receipt of the request and, if appropriate, will carry it out within the following fifteen business days. Exercising these rights is free of charge; only justified shipping or copying costs may be charged, where applicable."),
]),
("rgpd", ("7. Información adicional para personas en el Espacio Económico Europeo (RGPD)", "7. Additional information for persons in the European Economic Area (GDPR)"), [
  ("p", "Si usted se encuentra en el Espacio Económico Europeo, el tratamiento se basa en: la aplicación de medidas precontractuales o la ejecución de un contrato a petición suya (art. 6.1.b RGPD); el cumplimiento de obligaciones legales (art. 6.1.c); el interés legítimo en responder a sus mensajes y mantener la seguridad del sitio (art. 6.1.f); y su consentimiento para las comunicaciones de la finalidad secundaria (art. 6.1.a), que puede retirar en cualquier momento.",
        "If you are in the European Economic Area, processing is based on: taking pre-contractual steps or performing a contract at your request (Art. 6(1)(b) GDPR); compliance with legal obligations (Art. 6(1)(c)); the legitimate interest in responding to your messages and keeping the site secure (Art. 6(1)(f)); and your consent for secondary-purpose communications (Art. 6(1)(a)), which you may withdraw at any time."),
  ("p", "Además de los derechos indicados, usted puede solicitar la supresión, la limitación del tratamiento y la portabilidad de sus datos. Responderemos en el plazo de un mes, prorrogable en los términos del RGPD. No se toman decisiones basadas únicamente en tratamientos automatizados ni se elaboran perfiles.",
        "In addition to the rights above, you may request erasure, restriction of processing and portability of your data. We will respond within one month, extendable under the terms of the GDPR. No decisions based solely on automated processing are made and no profiling takes place."),
]),
("cookies", ("8. Cookies, almacenamiento local y contenido de terceros", "8. Cookies, local storage and third-party content"), [
  ("p", "<strong>Este sitio no utiliza cookies</strong>, propias ni de terceros, ni herramientas de analítica, publicidad, píxeles de seguimiento o complementos de redes sociales. Las fuentes tipográficas se sirven desde el propio sitio, por lo que al visitarlo no se establece conexión con servicios de terceros.",
        "<strong>This website does not use cookies</strong>, first- or third-party, nor analytics, advertising, tracking pixels or social media plug-ins. Typefaces are served from the site itself, so visiting it does not connect your browser to third-party services."),
  ("ul", [
    ("<strong>Almacenamiento local del navegador.</strong> Si usted cambia el idioma, el sitio guarda esa preferencia en su propio navegador (clave <code>idioma-sitio</code>). El dato no se envía a ningún servidor, es estrictamente necesario para la función que usted solicitó y puede borrarlo en cualquier momento desde la configuración de su navegador.",
     "<strong>Browser local storage.</strong> If you change the language, the site stores that preference in your own browser (key <code>idioma-sitio</code>). The value is never sent to any server, is strictly necessary for the feature you requested, and you can delete it at any time from your browser settings."),
    ("<strong>Video de YouTube.</strong> Uno de los artículos incluye un video que solo se carga si usted presiona “Reproducir video”. A partir de ese momento, YouTube (Google) puede tratar datos y almacenar cookies conforme a sus propias políticas.",
     "<strong>YouTube video.</strong> One article includes a video that only loads if you press “Play video”. From that moment, YouTube (Google) may process data and store cookies under its own policies."),
    ("<strong>Enlaces externos.</strong> Los enlaces a WhatsApp, LinkedIn u otros sitios le llevan a servicios de terceros con sus propias políticas de privacidad.",
     "<strong>External links.</strong> Links to WhatsApp, LinkedIn or other websites take you to third-party services with their own privacy policies."),
  ]),
  ("p", "Por estas razones el sitio no muestra un aviso de cookies: no existen cookies que aceptar o rechazar. Si en el futuro se incorporan, se solicitará su consentimiento previo cuando la ley lo exija y se actualizará este aviso.",
        "For these reasons the site does not display a cookie banner: there are no cookies to accept or reject. If any are added in the future, your prior consent will be requested where the law requires it and this notice will be updated."),
]),
("seguridad", ("9. Medidas de seguridad", "9. Security measures"), [
  ("p", "La Responsable aplica medidas de seguridad administrativas, técnicas y físicas razonables para proteger sus datos contra daño, pérdida, alteración, destrucción o uso, acceso o tratamiento no autorizado. El sitio se sirve únicamente mediante conexión cifrada (HTTPS).",
        "The Controller applies reasonable administrative, technical and physical security measures to protect your data against damage, loss, alteration, destruction or unauthorized use, access or processing. The site is served only over an encrypted connection (HTTPS)."),
]),
("cambios", ("10. Cambios al aviso de privacidad", "10. Changes to this privacy notice"), [
  ("p", "Este aviso puede modificarse por cambios legales, en los servicios o en el funcionamiento del sitio. Cualquier cambio se publicará en esta misma página, indicando la fecha de la última actualización.",
        "This notice may change due to legal developments or changes in services or in how the site works. Any change will be published on this page, together with the date of the last update."),
]),
("autoridad", ("11. Autoridad competente", "11. Supervisory authority"), [
  ("p", "Si considera que su derecho a la protección de datos personales ha sido vulnerado, puede acudir ante la autoridad competente en México, que a partir de 2025 es la Secretaría Anticorrupción y Buen Gobierno. Si se encuentra en el Espacio Económico Europeo, puede presentar una reclamación ante la autoridad de control de su país de residencia (por ejemplo, la Agencia Española de Protección de Datos).",
        "If you believe your right to personal data protection has been infringed, you may contact the competent authority in Mexico, which since 2025 is the Ministry of Anti-Corruption and Good Governance (Secretaría Anticorrupción y Buen Gobierno). If you are in the European Economic Area, you may lodge a complaint with the supervisory authority of your country of residence (for example, the Spanish Data Protection Agency)."),
]),
]

# ====================================================================== AVISO LEGAL
LEGAL = [
("titular", ("1. Titular del sitio", "1. Website owner"), [
  ("p", f"Este sitio web es operado por Gabriela L. González Vázquez, abogada, con domicilio en la Ciudad de México, México. Contacto: {CORREO}.",
        f"This website is operated by Gabriela L. González Vázquez, attorney, based in Mexico City, Mexico. Contact: {CORREO}."),
]),
("informativo", ("2. Contenido informativo; no constituye asesoría legal", "2. Informational content; not legal advice"), [
  ("p", "Los artículos y demás contenidos de este sitio tienen fines exclusivamente informativos y de carácter general. <strong>No constituyen asesoría jurídica</strong> ni sustituyen el análisis de un caso concreto por un profesional. La normativa cambia con frecuencia: verifique la vigencia de la información antes de tomar cualquier decisión.",
        "The articles and other content on this website are for general informational purposes only. <strong>They do not constitute legal advice</strong> and do not replace a professional analysis of a specific case. Regulations change frequently: verify that the information is current before making any decision."),
]),
("relacion", ("3. Inexistencia de relación abogado-cliente", "3. No attorney-client relationship"), [
  ("p", "La consulta de este sitio, o el envío de un mensaje por correo o WhatsApp, no crea una relación profesional abogado-cliente. Dicha relación solo existe una vez que ambas partes la acuerdan expresamente. Le pedimos no enviar información confidencial o sensible antes de ese momento.",
        "Browsing this website, or sending a message by email or WhatsApp, does not create an attorney-client relationship. Such a relationship only exists once both parties expressly agree to it. Please do not send confidential or sensitive information before then."),
]),
("propiedad", ("4. Propiedad intelectual y marcas de terceros", "4. Intellectual property and third-party trademarks"), [
  ("p", "Los textos, fotografías y el diseño de este sitio pertenecen a su titular o se usan con autorización. Se permite citar fragmentos de los artículos indicando la fuente y el enlace; cualquier otra reproducción requiere autorización previa por escrito.",
        "The text, photographs and design of this website belong to its owner or are used with permission. Quoting excerpts from the articles is allowed with attribution and a link; any other reproduction requires prior written permission."),
  ("p", "Los nombres y logotipos de instituciones y empresas que aparecen en el sitio son propiedad de sus respectivos titulares y se muestran únicamente para describir la trayectoria profesional de la titular. Su presencia no implica patrocinio, respaldo ni relación actual con dichas entidades.",
        "The names and logos of institutions and companies shown on the site belong to their respective owners and are displayed solely to describe the owner’s professional background. Their presence does not imply sponsorship, endorsement or a current relationship with those entities."),
]),
("testimonios", ("5. Testimonios", "5. Testimonials"), [
  ("p", "Los testimonios reflejan la experiencia individual de quienes los emitieron. Cada asunto es distinto y los resultados anteriores no garantizan resultados futuros.",
        "Testimonials reflect the individual experience of those who gave them. Every matter is different and past results do not guarantee future outcomes."),
]),
("enlaces", ("6. Enlaces a sitios de terceros", "6. Links to third-party websites"), [
  ("p", "Este sitio puede contener enlaces a sitios de terceros. La titular no controla ni es responsable de su contenido, disponibilidad o políticas de privacidad.",
        "This website may contain links to third-party websites. The owner does not control and is not responsible for their content, availability or privacy policies."),
]),
("responsabilidad", ("7. Limitación de responsabilidad", "7. Limitation of liability"), [
  ("p", "La titular procura que la información del sitio sea exacta y esté actualizada, pero no garantiza que esté libre de errores u omisiones. En la medida en que lo permita la ley aplicable, no será responsable de los daños derivados del uso de la información publicada ni de interrupciones en la disponibilidad del sitio.",
        "The owner endeavors to keep the site’s information accurate and up to date but does not guarantee it is free of errors or omissions. To the extent permitted by applicable law, the owner shall not be liable for damages arising from the use of the published information or from interruptions in the site’s availability."),
]),
("privacidad", ("8. Datos personales", "8. Personal data"), [
  ("p", "El tratamiento de datos personales se rige por el <a href=\"privacidad.html\">Aviso de Privacidad Integral</a>.",
        "The processing of personal data is governed by the <a href=\"privacidad.html\">Comprehensive Privacy Notice</a>."),
]),
("ley", ("9. Legislación aplicable y jurisdicción", "9. Governing law and jurisdiction"), [
  ("p", "Este aviso se rige por las leyes de los Estados Unidos Mexicanos. Para cualquier controversia, las partes se someten a los tribunales competentes de la Ciudad de México, salvo que una norma imperativa disponga otra cosa.",
        "This notice is governed by the laws of the United Mexican States. For any dispute, the parties submit to the competent courts of Mexico City, unless a mandatory rule provides otherwise."),
]),
]

if __name__ == "__main__":
    pagina("privacidad.html",
           ("Aviso de Privacidad — Gabriela L. González Vázquez", "Privacy Notice — Gabriela L. González Vázquez"),
           ("Aviso de Privacidad Integral conforme a la LFPDPPP y, en lo aplicable, al RGPD.", "Comprehensive Privacy Notice under Mexico’s LFPDPPP and, where applicable, the GDPR."),
           ("Aviso de Privacidad Integral", "Comprehensive Privacy Notice"),
           [("Este aviso se emite en cumplimiento de la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (publicada en el Diario Oficial de la Federación el 20 de marzo de 2025) y demás normativa aplicable y, para personas que se encuentren en el Espacio Económico Europeo, del Reglamento (UE) 2016/679 (RGPD).",
             "This notice is issued in compliance with Mexico’s Federal Law on the Protection of Personal Data Held by Private Parties (published in the Official Gazette on March 20, 2025) and other applicable regulations and, for persons located in the European Economic Area, Regulation (EU) 2016/679 (GDPR).")],
           PRIV)
    pagina("aviso-legal.html",
           ("Aviso Legal — Gabriela L. González Vázquez", "Legal Notice — Gabriela L. González Vázquez"),
           ("Aviso legal y términos de uso del sitio.", "Legal notice and terms of use of the website."),
           ("Aviso legal y términos de uso", "Legal notice and terms of use"),
           [("Al utilizar este sitio usted acepta los siguientes términos. Si no está de acuerdo con ellos, le pedimos no utilizarlo.",
             "By using this website you accept the following terms. If you do not agree with them, please do not use it.")],
           LEGAL)
    print("OK: privacidad.html + aviso-legal.html")
