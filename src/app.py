from datetime import datetime

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate

from agent import create_llm
from document_loader import load_documents
from ui_components import (
    load_styles,
    render_benefits,
    render_chat_header,
    render_footer,
    render_header,
    render_hero,
    render_newsletter,
    render_offer,
    render_products,
    render_purchase_steps,
    render_section_heading,
    render_statistics,
    render_testimonials,
)

st.set_page_config(
    page_title="NovaMarket | Tecnología para tu vida",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_styles()


@st.cache_resource
def get_llm():
    return create_llm()


@st.cache_data
def get_documents():
    return load_documents()


def get_current_time() -> str:
    return datetime.now().strftime("%H:%M")


def initialize_chat() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def clear_chat() -> None:
    st.session_state.messages = []


def generate_answer(question: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        """
        Eres NovaBot, el asistente virtual oficial de NovaMarket.

        Responde siempre en español con un tono amable, claro,
        natural y profesional.

        No te presentes al comenzar cada respuesta.
        Responde directamente la consulta.

        Utiliza exclusivamente la información contenida
        en la documentación oficial proporcionada.

        No inventes condiciones, precios, plazos,
        políticas ni procedimientos.

        No menciones nombres de archivos ni agregues fuentes.

        Si la información no aparece en los documentos, responde exactamente:

        "Lamentablemente, no encontré esa información en la
        documentación oficial disponible de NovaMarket."

        DOCUMENTACIÓN OFICIAL:
        {documents}

        PREGUNTA DEL CLIENTE:
        {question}
        """
    )

    chain = prompt | get_llm()

    response = chain.invoke(
        {
            "documents": get_documents(),
            "question": question,
        }
    )

    return response.content


def render_chat_messages() -> None:
    for message in st.session_state.messages:
        css_class = (
            "user-message"
            if message["role"] == "user"
            else "assistant-message"
        )

        icon = "👤" if message["role"] == "user" else "🤖"

        message_html = (
            f'<div class="{css_class}">'
            f'<strong>{icon}</strong><br>'
            f'{message["content"]}'
            f'<span class="message-time">{message["time"]}</span>'
            f'</div>'
        )

        st.markdown(
            message_html,
            unsafe_allow_html=True,
        )


initialize_chat()
render_header()

main_column, chat_column = st.columns([3.2, 1.15], gap="large")

with main_column:
    render_hero()
    render_benefits()

    st.markdown('<div id="productos"></div>', unsafe_allow_html=True)

    render_section_heading(
        "Productos destacados",
        "Tecnología seleccionada para cada momento.",
        "Ver catálogo completo →",
    )

    product_column, offer_column = st.columns([3, 1.15], gap="large")

    with product_column:
        render_products()

    with offer_column:
        render_offer()

    render_section_heading(
        "NovaMarket en cifras",
        "Una experiencia comercial construida sobre confianza.",
    )
    render_statistics()

    render_section_heading(
        "Lo que opinan nuestros clientes",
        "Experiencias simuladas para esta demostración.",
    )
    render_testimonials()

    render_section_heading(
        "¿Cómo comprar?",
        "Una experiencia sencilla desde la selección hasta la entrega.",
    )
    render_purchase_steps()
    render_newsletter()
    render_footer()

with chat_column:
    render_chat_header()
    render_chat_messages()

    st.markdown("##### Preguntas sugeridas")

    suggested_questions = [
        "¿Cuántos días tengo para devolver un producto?",
        "¿Qué daños no cubre la garantía?",
        "¿Cuánto tarda el envío express?",
    ]

    for index, suggested_question in enumerate(suggested_questions):
        if st.button(
            suggested_question,
            key=f"suggested_{index}",
            use_container_width=True,
        ):
            st.session_state.selected_question = suggested_question

    default_question = st.session_state.pop("selected_question", "")

    with st.form("novabot_form", clear_on_submit=True):
        question = st.text_input(
            "Escribe tu pregunta",
            value=default_question,
            placeholder="Ejemplo: ¿Qué métodos de pago aceptan?",
            label_visibility="collapsed",
        )

        submit_button = st.form_submit_button(
            "Enviar consulta ➤",
            use_container_width=True,
        )

    if st.button("🗑️ Limpiar conversación", use_container_width=True):
        clear_chat()
        st.rerun()

    if submit_button:
        clean_question = question.strip()

        if not clean_question:
            st.warning("Escribe una pregunta antes de enviarla.")
        else:
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": clean_question,
                    "time": get_current_time(),
                }
            )

            with st.spinner("NovaBot está revisando la documentación..."):
                try:
                    answer = generate_answer(clean_question)
                except Exception as error:
                    answer = (
                        "No fue posible generar la respuesta. "
                        "Revisa la configuración de Gemini."
                    )
                    st.error(answer)
                    with st.expander("Detalle técnico"):
                        st.code(str(error))

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "time": get_current_time(),
                }
            )

            st.rerun()

    st.caption(
        "Las respuestas se generan únicamente con la documentación oficial."
    )
