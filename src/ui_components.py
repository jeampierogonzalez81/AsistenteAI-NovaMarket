from textwrap import dedent

import streamlit as st


def render_html(content: str) -> None:
    clean_html = "".join(
        line.strip()
        for line in dedent(content).splitlines()
        if line.strip()
    )

    st.markdown(
        clean_html,
        unsafe_allow_html=True,
    )


def load_styles() -> None:
    render_html(
        """
        <style>
            @import url(
                'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
            );

            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
            }

            .stApp {
                background:
                    radial-gradient(
                        circle at top right,
                        rgba(37, 99, 235, 0.14),
                        transparent 28%
                    ),
                    linear-gradient(
                        180deg,
                        #e8f0fa 0%,
                        #dce8f5 50%,
                        #edf3f9 100%
                    );
            }

            header[data-testid="stHeader"] {
                background: transparent;
            }

            [data-testid="stToolbar"] {
                display: none;
            }

            .block-container {
                max-width: 1450px;
                padding-top: 0.7rem;
                padding-bottom: 2rem;
            }

            .topbar {
                background: #071d3d;
                color: #e2e8f0;
                padding: 9px 25px;
                border-radius: 14px 14px 0 0;
                display: flex;
                justify-content: space-around;
                gap: 20px;
                font-size: 13px;
                font-weight: 500;
            }

            .navbar {
                background: rgba(255, 255, 255, 0.96);
                padding: 18px 25px;
                border-radius: 0 0 18px 18px;
                box-shadow: 0 10px 30px rgba(15, 39, 71, 0.10);
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 25px;
                margin-bottom: 18px;
            }

            .logo {
                font-size: 27px;
                font-weight: 800;
                color: #071d3d;
                letter-spacing: -1px;
                white-space: nowrap;
            }

            .logo span {
                color: #ff5a1f;
            }

            .nav-menu {
                color: #334155;
                font-size: 14px;
                font-weight: 600;
                text-align: center;
            }

            .nav-actions {
                color: #071d3d;
                font-size: 14px;
                font-weight: 600;
                white-space: nowrap;
            }

            .hero {
                background:
                    radial-gradient(
                        circle at 80% 40%,
                        rgba(56, 189, 248, 0.38),
                        transparent 24%
                    ),
                    linear-gradient(
                        125deg,
                        #061a39 0%,
                        #0a3266 52%,
                        #155e9b 100%
                    );
                min-height: 390px;
                padding: 55px 50px;
                border-radius: 28px;
                color: white;
                position: relative;
                overflow: hidden;
                box-shadow: 0 22px 48px rgba(4, 24, 52, 0.24);
            }

            .hero::after {
                content: "💻  🎧  ⌚  📱";
                position: absolute;
                right: 5%;
                top: 27%;
                font-size: 72px;
                letter-spacing: 12px;
                transform: rotate(-3deg);
                filter: drop-shadow(0 20px 22px rgba(0, 0, 0, 0.30));
            }

            .hero-content {
                position: relative;
                z-index: 2;
                max-width: 650px;
            }

            .hero-badge {
                display: inline-block;
                background: rgba(255, 255, 255, 0.13);
                border: 1px solid rgba(255, 255, 255, 0.20);
                padding: 8px 14px;
                border-radius: 30px;
                font-size: 13px;
                margin-bottom: 18px;
            }

            .hero h1 {
                color: white;
                font-size: 52px;
                line-height: 1.08;
                margin: 0 0 18px;
                max-width: 650px;
            }

            .hero h1 span {
                color: #ff6b2c;
                display: block;
            }

            .hero p {
                color: #dbeafe;
                font-size: 18px;
                line-height: 1.65;
                max-width: 610px;
            }

            .hero-button {
                display: inline-block;
                margin-top: 20px;
                background: #ff5a1f;
                color: white !important;
                padding: 14px 24px;
                border-radius: 11px;
                font-weight: 700;
                text-decoration: none;
                box-shadow: 0 12px 25px rgba(255, 90, 31, 0.30);
            }

            .hero-button:hover {
                background: #e84c12;
            }

            .section-heading {
                display: flex;
                justify-content: space-between;
                align-items: end;
                margin: 32px 2px 18px;
            }

            .section-heading h2 {
                color: #071d3d;
                font-size: 27px;
                margin: 0;
            }

            .section-heading p {
                color: #64748b;
                margin: 5px 0 0;
            }

            .section-link {
                color: #2563eb;
                font-size: 14px;
                font-weight: 600;
            }

            .info-card,
            .product-card,
            .testimonial-card,
            .stat-card,
            .steps-card,
            .offer-card,
            .newsletter,
            .chat-shell {
                background: rgba(255, 255, 255, 0.93);
                border: 1px solid rgba(203, 213, 225, 0.85);
                box-shadow: 0 10px 28px rgba(15, 39, 71, 0.08);
            }

            .info-card {
                padding: 22px;
                border-radius: 17px;
                min-height: 145px;
            }

            .info-icon {
                font-size: 31px;
                margin-bottom: 10px;
            }

            .info-card h3 {
                color: #071d3d;
                font-size: 17px;
                margin: 0 0 8px;
            }

            .info-card p {
                color: #64748b;
                font-size: 14px;
                line-height: 1.5;
            }

            .product-card {
                padding: 18px;
                border-radius: 18px;
                min-height: 330px;
                position: relative;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .product-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 16px 35px rgba(15, 39, 71, 0.14);
            }

            .discount {
                position: absolute;
                left: 15px;
                top: 15px;
                background: #ef4444;
                color: white;
                padding: 5px 9px;
                border-radius: 7px;
                font-size: 12px;
                font-weight: 700;
            }

            .product-image {
                background: linear-gradient(145deg, #eef4fb, #dce7f4);
                border-radius: 14px;
                height: 145px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 72px;
                margin-bottom: 16px;
            }

            .product-category {
                color: #2563eb;
                font-size: 12px;
                font-weight: 600;
            }

            .product-card h3 {
                color: #071d3d;
                font-size: 16px;
                margin: 7px 0;
            }

            .product-description {
                color: #64748b;
                font-size: 13px;
                min-height: 38px;
            }

            .product-price {
                color: #ff5a1f;
                font-size: 21px;
                font-weight: 800;
                margin-top: 10px;
            }

            .old-price {
                color: #94a3b8;
                font-size: 12px;
                text-decoration: line-through;
                margin-left: 6px;
            }

            .rating {
                color: #f59e0b;
                font-size: 13px;
                margin-top: 8px;
            }

            .offer-card {
                border-radius: 21px;
                padding: 30px;
                background:
                    radial-gradient(
                        circle at bottom right,
                        rgba(37, 99, 235, 0.42),
                        transparent 36%
                    ),
                    linear-gradient(135deg, #071d3d, #0b376d);
                color: white;
                min-height: 305px;
            }

            .offer-card h2 {
                color: white;
                font-size: 27px;
            }

            .offer-card p {
                color: #dbeafe;
                line-height: 1.6;
            }

            .offer-percent {
                font-size: 64px;
                font-weight: 800;
                color: #ff6b2c;
                margin: 15px 0;
            }

            .stat-card {
                border-radius: 17px;
                padding: 22px;
                text-align: center;
            }

            .stat-number {
                color: #071d3d;
                font-size: 29px;
                font-weight: 800;
            }

            .stat-label {
                color: #64748b;
                font-size: 13px;
                margin-top: 5px;
            }

            .testimonial-card {
                border-radius: 17px;
                padding: 22px;
                min-height: 205px;
            }

            .testimonial-stars {
                color: #f59e0b;
                font-size: 18px;
            }

            .testimonial-text {
                color: #334155;
                line-height: 1.6;
                font-size: 14px;
                min-height: 88px;
            }

            .testimonial-user {
                color: #071d3d;
                font-weight: 700;
                font-size: 14px;
            }

            .testimonial-city {
                color: #64748b;
                font-size: 12px;
            }

            .steps-card {
                border-radius: 20px;
                padding: 28px;
            }

            .step-item {
                text-align: center;
                padding: 14px;
            }

            .step-number {
                width: 34px;
                height: 34px;
                border-radius: 50%;
                margin: 0 auto 10px;
                background: #dbeafe;
                color: #1d4ed8;
                font-weight: 800;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .step-icon {
                font-size: 36px;
            }

            .step-title {
                color: #071d3d;
                font-weight: 700;
                font-size: 14px;
            }

            .step-text {
                color: #64748b;
                font-size: 12px;
                margin-top: 6px;
            }

            .newsletter {
                border-radius: 20px;
                padding: 25px 30px;
                background: #071d3d;
                color: white;
                margin-top: 32px;
            }

            .newsletter h3 {
                color: white;
                margin: 0;
            }

            .newsletter p {
                color: #cbd5e1;
                margin: 7px 0 0;
            }

            .chat-shell {
                border-radius: 22px;
                padding: 24px;
                border-top: 5px solid #ff5a1f;
                min-height: 790px;
                position: sticky;
                top: 15px;
            }

            .chat-header {
                display: flex;
                align-items: center;
                gap: 12px;
                padding-bottom: 16px;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 16px;
            }

            .bot-avatar {
                width: 48px;
                height: 48px;
                border-radius: 50%;
                background: linear-gradient(135deg, #dbeafe, #bfdbfe);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 25px;
            }

            .chat-title {
                color: #071d3d;
                font-size: 19px;
                font-weight: 800;
            }

            .chat-status {
                color: #16a34a;
                font-size: 12px;
            }

            .chat-intro {
                background: #f1f5f9;
                padding: 15px;
                border-radius: 13px;
                color: #334155;
                font-size: 13px;
                line-height: 1.55;
                margin-bottom: 15px;
            }

            .documents-box {
                background: #eff6ff;
                border: 1px solid #bfdbfe;
                padding: 14px;
                border-radius: 13px;
                font-size: 13px;
                color: #1e3a5f;
                margin-bottom: 16px;
            }

            .assistant-message {
                background: #eef2f7;
                color: #1e293b;
                padding: 14px;
                border-radius: 14px 14px 14px 4px;
                margin: 10px 0;
                line-height: 1.55;
                font-size: 14px;
            }

            .user-message {
                background: #092b58;
                color: white;
                padding: 14px;
                border-radius: 14px 14px 4px 14px;
                margin: 10px 0 10px 35px;
                line-height: 1.55;
                font-size: 14px;
            }

            .message-time {
                display: block;
                text-align: right;
                font-size: 10px;
                opacity: 0.68;
                margin-top: 7px;
            }

            .footer {
                margin-top: 25px;
                background: #061831;
                color: #cbd5e1;
                padding: 32px;
                border-radius: 22px;
                text-align: center;
                line-height: 1.8;
                font-size: 13px;
            }

            .footer strong {
                color: white;
                font-size: 18px;
            }

            div.stButton > button,
            div[data-testid="stFormSubmitButton"] > button {
                background: #ff5a1f;
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: 700;
                min-height: 42px;
                transition: all 0.2s ease;
            }

            div.stButton > button:hover,
            div[data-testid="stFormSubmitButton"] > button:hover {
                background: #e84c12;
                color: white;
                border: none;
                transform: translateY(-1px);
            }

            div[data-testid="stTextInput"] input {
                border-radius: 11px;
                border: 1px solid #cbd5e1;
                background: white;
            }

            @media (max-width: 900px) {
                .nav-menu,
                .nav-actions {
                    display: none;
                }

                .topbar {
                    flex-direction: column;
                    align-items: center;
                }

                .hero {
                    padding: 40px 28px;
                }

                .hero h1 {
                    font-size: 39px;
                }

                .hero::after {
                    opacity: 0.18;
                    right: -8%;
                }
            }
        </style>
        """
    )


def render_header() -> None:
    render_html(
        """
        <div class="topbar">
            <span>🚚 Envíos rápidos a todo Chile</span>
            <span>↩️ Devolución fácil hasta 30 días</span>
            <span>🛡️ Compra 100% segura</span>
        </div>

        <div class="navbar">
            <div class="logo">NOVA<span>MARKET</span></div>

            <div class="nav-menu">
                Inicio &nbsp;&nbsp;&nbsp;
                Productos &nbsp;&nbsp;&nbsp;
                Ofertas &nbsp;&nbsp;&nbsp;
                Categorías &nbsp;&nbsp;&nbsp;
                Seguimiento &nbsp;&nbsp;&nbsp;
                Ayuda
            </div>

            <div class="nav-actions">
                ♡ Favoritos &nbsp;&nbsp; 👤 Mi cuenta &nbsp;&nbsp; 🛒 0
            </div>
        </div>
        """
    )


def render_hero() -> None:
    render_html(
        """
        <section class="hero">
            <div class="hero-content">
                <div class="hero-badge">
                    ✨ Nuevas ofertas disponibles
                </div>

                <h1>
                    Tecnología que
                    <span>impulsa tu día a día</span>
                </h1>

                <p>
                    Descubre productos para tu hogar, trabajo y
                    entretenimiento con compra protegida, envíos rápidos
                    y atención inteligente.
                </p>

                <a class="hero-button" href="#productos">
                    Explorar productos →
                </a>
            </div>
        </section>
        """
    )


def render_section_heading(
    title: str,
    description: str,
    link_text: str = "",
) -> None:
    link = (
        f'<span class="section-link">{link_text}</span>'
        if link_text
        else ""
    )

    render_html(
        f"""
        <div class="section-heading">
            <div>
                <h2>{title}</h2>
                <p>{description}</p>
            </div>
            {link}
        </div>
        """
    )


def render_benefits() -> None:
    benefits = [
        (
            "🚚",
            "Envío gratis",
            "Disponible en compras seleccionadas sobre $39.990.",
        ),
        (
            "🔒",
            "Compra protegida",
            "Pagos procesados mediante plataformas seguras.",
        ),
        (
            "↩️",
            "Devolución fácil",
            "Solicitudes disponibles hasta 30 días.",
        ),
        (
            "🎧",
            "Atención inteligente",
            "NovaBot responde usando documentación oficial.",
        ),
    ]

    columns = st.columns(4)

    for column, benefit in zip(columns, benefits):
        icon, title, description = benefit

        with column:
            render_html(
                f"""
                <div class="info-card">
                    <div class="info-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """
            )


def render_products() -> None:
    products = [
        {
            "icon": "💻",
            "discount": "-15%",
            "category": "Notebooks",
            "name": "NovaBook Pro 15",
            "description": "Potencia para estudiar, trabajar y crear.",
            "price": "$749.990",
            "old_price": "$879.990",
            "rating": "★ 4.8 (124)",
        },
        {
            "icon": "🎧",
            "discount": "-20%",
            "category": "Audio",
            "name": "SoundAir Pro",
            "description": "Audio inmersivo y cancelación de ruido.",
            "price": "$69.990",
            "old_price": "$89.990",
            "rating": "★ 4.7 (89)",
        },
        {
            "icon": "⌚",
            "discount": "-10%",
            "category": "Wearables",
            "name": "Active One",
            "description": "Actividad, salud y notificaciones.",
            "price": "$119.990",
            "old_price": "$139.990",
            "rating": "★ 4.7 (56)",
        },
        {
            "icon": "🖨️",
            "discount": "-12%",
            "category": "Impresoras",
            "name": "NovaPrint WiFi",
            "description": "Impresión inalámbrica para hogar y oficina.",
            "price": "$129.990",
            "old_price": "$149.990",
            "rating": "★ 4.5 (34)",
        },
    ]

    columns = st.columns(4)

    for column, product in zip(columns, products):
        with column:
            render_html(
                f"""
                <div class="product-card">
                    <span class="discount">{product["discount"]}</span>

                    <div class="product-image">
                        {product["icon"]}
                    </div>

                    <div class="product-category">
                        {product["category"]}
                    </div>

                    <h3>{product["name"]}</h3>

                    <div class="product-description">
                        {product["description"]}
                    </div>

                    <div class="product-price">
                        {product["price"]}
                        <span class="old-price">
                            {product["old_price"]}
                        </span>
                    </div>

                    <div class="rating">
                        {product["rating"]}
                    </div>
                </div>
                """
            )


def render_offer() -> None:
    render_html(
        """
        <div class="offer-card">
            <div>⏱️ OFERTAS DE LA SEMANA</div>

            <h2>Descuentos especiales</h2>

            <div class="offer-percent">30%</div>

            <p>
                Hasta 30% de descuento en productos seleccionados.
                Promoción visual para fines demostrativos.
            </p>

            <a class="hero-button" href="#productos">
                Ver ofertas
            </a>
        </div>
        """
    )


def render_statistics() -> None:
    statistics = [
        ("+50.000", "Clientes satisfechos"),
        ("4,9/5", "Valoración promedio"),
        ("98%", "Entregas a tiempo"),
        ("+25.000", "Pedidos gestionados"),
    ]

    columns = st.columns(4)

    for column, statistic in zip(columns, statistics):
        value, label = statistic

        with column:
            render_html(
                f"""
                <div class="stat-card">
                    <div class="stat-number">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """
            )


def render_testimonials() -> None:
    testimonials = [
        (
            "Excelente atención y productos de muy buena calidad.",
            "María Fernanda R.",
            "Santiago, Chile",
        ),
        (
            "El envío fue rápido y el producto llegó en perfectas condiciones.",
            "Carlos M.",
            "Concepción, Chile",
        ),
        (
            "NovaBot aclaró inmediatamente mis dudas sobre la devolución.",
            "Ignacia T.",
            "Valparaíso, Chile",
        ),
    ]

    columns = st.columns(3)

    for column, testimonial in zip(columns, testimonials):
        text, name, city = testimonial

        with column:
            render_html(
                f"""
                <div class="testimonial-card">
                    <div class="testimonial-stars">
                        ★★★★★
                    </div>

                    <p class="testimonial-text">
                        “{text}”
                    </p>

                    <div class="testimonial-user">
                        👤 {name}
                    </div>

                    <div class="testimonial-city">
                        {city}
                    </div>
                </div>
                """
            )


def render_purchase_steps() -> None:
    steps = [
        ("1", "🛒", "Elige tus productos", "Explora nuestro catálogo."),
        ("2", "💳", "Realiza tu pago", "Compra mediante pago protegido."),
        ("3", "📦", "Preparamos tu pedido", "Procesamos y embalamos tu compra."),
        ("4", "🚚", "Recibe en tu domicilio", "Sigue el estado de tu entrega."),
    ]

    render_html('<div class="steps-card">')

    columns = st.columns(4)

    for column, step in zip(columns, steps):
        number, icon, title, description = step

        with column:
            render_html(
                f"""
                <div class="step-item">
                    <div class="step-number">{number}</div>
                    <div class="step-icon">{icon}</div>
                    <div class="step-title">{title}</div>
                    <div class="step-text">{description}</div>
                </div>
                """
            )

    render_html("</div>")


def render_newsletter() -> None:
    render_html(
        """
        <div class="newsletter">
            <h3>✉️ Suscríbete a nuestro newsletter</h3>
            <p>
                Recibe ofertas exclusivas, novedades y recomendaciones.
                Formulario demostrativo.
            </p>
        </div>
        """
    )


def render_chat_header() -> None:
    render_html(
        """
        <div class="chat-header">
            <div class="bot-avatar">🤖</div>

            <div>
                <div class="chat-title">NovaBot</div>
                <div class="chat-status">
                    ● Asistente disponible
                </div>
            </div>
        </div>

        <div class="chat-intro">
            Hola 👋 Estoy aquí para ayudarte con información sobre
            envíos, devoluciones, pagos, garantías y privacidad.
        </div>

        <div class="documents-box">
            <strong>📚 Documentación consultada</strong><br><br>
            ✓ Envíos y entregas<br>
            ✓ Reembolsos y devoluciones<br>
            ✓ Métodos de pago<br>
            ✓ Privacidad<br>
            ✓ Garantías
        </div>
        """
    )


def render_footer() -> None:
    render_html(
        """
        <footer class="footer">
            <strong>NovaMarket</strong><br>
            Tecnología para tu hogar, oficina y entretenimiento.<br><br>

            Productos · Ofertas · Ayuda · Privacidad ·
            Devoluciones · Garantías · Contacto<br><br>

            Facebook · Instagram · LinkedIn · YouTube · TikTok<br><br>

            © 2026 NovaMarket. Proyecto demostrativo desarrollado con
            Python, LangChain, Gemini y Streamlit.
        </footer>
        """
    )
