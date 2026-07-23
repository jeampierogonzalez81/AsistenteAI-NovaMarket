from pathlib import Path

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


STORE_NAME = "NovaMarket"

DOCUMENTS = {
    "politica_reembolsos_devoluciones.pdf": {
        "title": "Política de Reembolsos y Devoluciones",
        "sections": [
            (
                "1. Objetivo",
                """
                Esta política explica las condiciones aplicables a las devoluciones,
                cambios y reembolsos de productos comprados en NovaMarket. Su objetivo
                es ofrecer un proceso claro, seguro y transparente para todos los clientes.
                """,
            ),
            (
                "2. Plazo para solicitar una devolución",
                """
                El cliente dispone de 30 días corridos desde la fecha de recepción del
                pedido para solicitar una devolución. Las solicitudes realizadas después
                de este plazo podrán ser rechazadas, salvo que exista una garantía legal
                o un defecto de fabricación comprobable.
                """,
            ),
            (
                "3. Condiciones del producto",
                """
                El producto debe conservar sus accesorios, manuales, embalaje original
                y comprobante de compra. No debe presentar daños provocados por uso
                inadecuado, golpes, humedad, alteraciones, reparaciones no autorizadas
                o desgaste excesivo.
                """,
            ),
            (
                "4. Productos que no admiten devolución",
                """
                No se aceptan devoluciones de software activado, licencias digitales,
                tarjetas de regalo, productos personalizados, artículos de higiene
                abiertos ni productos cuyo sello de seguridad haya sido retirado.
                """,
            ),
            (
                "5. Procedimiento",
                """
                Para iniciar el proceso, el cliente debe contactar al soporte de NovaMarket,
                indicar su número de pedido, explicar el motivo y adjuntar fotografías
                cuando exista daño visible. El equipo de soporte responderá dentro de
                dos días hábiles con las instrucciones de envío.
                """,
            ),
            (
                "6. Reembolsos",
                """
                Una vez recibido e inspeccionado el producto, NovaMarket informará el
                resultado dentro de cinco días hábiles. Los reembolsos aprobados se
                procesarán mediante el mismo medio de pago utilizado en la compra.
                El tiempo de acreditación puede variar entre cinco y diez días hábiles.
                """,
            ),
            (
                "7. Costos de devolución",
                """
                Si la devolución se debe a un error de NovaMarket, producto defectuoso
                o daño durante el transporte, la empresa cubrirá el costo. Si el cliente
                cambia de opinión, el costo del envío de devolución será de su responsabilidad.
                """,
            ),
        ],
    },
    "guia_envios_entregas.pdf": {
        "title": "Guía de Envíos y Entregas",
        "sections": [
            (
                "1. Preparación del pedido",
                """
                Los pedidos son preparados dentro de uno a dos días hábiles después de
                confirmarse el pago. Los pedidos realizados durante fines de semana o
                feriados comienzan a procesarse el siguiente día hábil.
                """,
            ),
            (
                "2. Modalidades de envío",
                """
                NovaMarket ofrece envío estándar y envío express. El envío estándar
                demora entre tres y cinco días hábiles. El envío express demora entre
                uno y dos días hábiles, según la ciudad y disponibilidad logística.
                """,
            ),
            (
                "3. Costos",
                """
                El envío estándar tiene un costo fijo de 4.990 pesos chilenos. El envío
                express tiene un costo de 8.990 pesos. Las compras superiores a
                60.000 pesos incluyen envío estándar gratuito.
                """,
            ),
            (
                "4. Seguimiento",
                """
                Cuando el pedido sea despachado, el cliente recibirá por correo electrónico
                un número de seguimiento y un enlace para consultar el estado de la entrega.
                La actualización del transportista puede tardar hasta 24 horas.
                """,
            ),
            (
                "5. Intentos de entrega",
                """
                El transportista realizará hasta dos intentos de entrega. Si no encuentra
                a una persona autorizada, el pedido podrá regresar al centro de distribución.
                Un nuevo despacho puede generar un costo adicional.
                """,
            ),
            (
                "6. Retrasos",
                """
                Pueden ocurrir retrasos por condiciones climáticas, alta demanda, errores
                en la dirección o situaciones operacionales del transportista. NovaMarket
                notificará al cliente cuando exista información confirmada sobre la demora.
                """,
            ),
            (
                "7. Producto dañado durante el transporte",
                """
                Si el paquete llega con daños visibles, el cliente debe tomar fotografías
                del embalaje y del producto y comunicarse con soporte dentro de las primeras
                48 horas posteriores a la recepción.
                """,
            ),
        ],
    },
    "preguntas_frecuentes_metodos_pago.pdf": {
        "title": "Preguntas Frecuentes y Métodos de Pago",
        "sections": [
            (
                "1. ¿Qué medios de pago acepta NovaMarket?",
                """
                Se aceptan tarjetas de crédito y débito, transferencias bancarias y pagos
                mediante plataformas electrónicas autorizadas. La disponibilidad puede
                variar según la región o la entidad financiera.
                """,
            ),
            (
                "2. ¿Puedo pagar en cuotas?",
                """
                Sí. Las compras con tarjeta de crédito pueden pagarse en cuotas cuando
                el banco emisor lo permita. Los intereses y condiciones dependen de la
                institución financiera del cliente.
                """,
            ),
            (
                "3. ¿Cómo sé si mi pago fue aprobado?",
                """
                Después del pago, NovaMarket envía una confirmación por correo electrónico.
                Si el pago queda pendiente, el pedido no será preparado hasta que la
                plataforma confirme la transacción.
                """,
            ),
            (
                "4. ¿Puedo modificar un pedido?",
                """
                Solo es posible modificar o cancelar un pedido antes de que ingrese al
                proceso de preparación. El cliente debe contactar al soporte lo antes posible.
                """,
            ),
            (
                "5. ¿Cómo obtengo mi comprobante?",
                """
                El comprobante de compra se envía al correo registrado y también puede
                descargarse desde la sección Mis pedidos de la cuenta del cliente.
                """,
            ),
            (
                "6. ¿Qué hago si el pago fue cobrado dos veces?",
                """
                El cliente debe enviar el comprobante y los últimos cuatro dígitos del medio
                de pago. NovaMarket revisará el caso con la plataforma correspondiente y
                responderá dentro de cinco días hábiles.
                """,
            ),
            (
                "7. ¿NovaMarket almacena los datos de mi tarjeta?",
                """
                NovaMarket no almacena directamente los datos completos de tarjetas.
                Los pagos son procesados mediante proveedores certificados y conexiones seguras.
                """,
            ),
        ],
    },
    "politica_privacidad.pdf": {
        "title": "Política de Privacidad",
        "sections": [
            (
                "1. Información recopilada",
                """
                NovaMarket puede recopilar nombre, correo electrónico, teléfono, dirección
                de envío, historial de compras, consultas de soporte y datos técnicos
                necesarios para operar la plataforma.
                """,
            ),
            (
                "2. Uso de la información",
                """
                Los datos se utilizan para procesar pedidos, gestionar entregas, responder
                consultas, prevenir fraudes, mejorar el servicio y cumplir obligaciones legales.
                """,
            ),
            (
                "3. Proveedores externos",
                """
                La información puede compartirse únicamente con proveedores necesarios,
                como empresas de transporte, plataformas de pago, servicios de alojamiento
                y herramientas de atención al cliente.
                """,
            ),
            (
                "4. Seguridad",
                """
                NovaMarket aplica medidas técnicas y administrativas razonables para proteger
                la información contra acceso no autorizado, pérdida, alteración o divulgación.
                """,
            ),
            (
                "5. Derechos del usuario",
                """
                El usuario puede solicitar acceso, corrección, actualización o eliminación
                de sus datos personales, cuando la legislación aplicable lo permita.
                """,
            ),
            (
                "6. Conservación",
                """
                Los datos se conservarán durante el tiempo necesario para prestar el servicio,
                cumplir obligaciones legales, resolver disputas y prevenir actividades fraudulentas.
                """,
            ),
            (
                "7. Contacto",
                """
                Las solicitudes relacionadas con privacidad pueden enviarse a
                privacidad@novamarket.cl. NovaMarket responderá dentro de un plazo máximo
                de diez días hábiles.
                """,
            ),
        ],
    },
    "manual_garantia_productos.pdf": {
        "title": "Manual de Garantía de Productos",
        "sections": [
            (
                "1. Cobertura general",
                """
                Los productos comercializados por NovaMarket cuentan con una garantía
                comercial de 12 meses desde la fecha de compra, salvo que el fabricante
                indique un plazo diferente.
                """,
            ),
            (
                "2. Qué cubre la garantía",
                """
                La garantía cubre fallas de fabricación, defectos de materiales y problemas
                de funcionamiento ocurridos durante un uso normal del producto.
                """,
            ),
            (
                "3. Exclusiones",
                """
                No cubre daños por golpes, caídas, humedad, voltaje incorrecto, uso comercial
                no autorizado, desgaste normal, instalación incorrecta, software malicioso,
                manipulación interna o reparación por servicios no autorizados.
                """,
            ),
            (
                "4. Cómo solicitar la garantía",
                """
                El cliente debe presentar comprobante de compra, número de pedido, descripción
                de la falla y evidencia fotográfica o audiovisual cuando corresponda.
                """,
            ),
            (
                "5. Evaluación técnica",
                """
                NovaMarket o el servicio técnico autorizado evaluará el producto dentro de
                diez días hábiles desde su recepción. En casos complejos, el plazo puede
                extenderse con aviso previo al cliente.
                """,
            ),
            (
                "6. Soluciones disponibles",
                """
                Si la garantía es aceptada, NovaMarket podrá reparar el producto, reemplazarlo
                por uno equivalente o emitir un reembolso, según disponibilidad y resultado técnico.
                """,
            ),
            (
                "7. Productos reparados o reemplazados",
                """
                Un producto reparado mantiene el plazo restante de la garantía original.
                Un producto reemplazado contará con una garantía mínima de seis meses o con
                el plazo restante original, aplicándose el periodo más favorable.
                """,
            ),
        ],
    },
}


def build_pdf(file_path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        leading=25,
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=13,
        leading=17,
        spaceBefore=10,
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontSize=10.5,
        leading=16,
        spaceAfter=10,
    )

    document = SimpleDocTemplate(
        str(file_path),
        pagesize=A4,
        rightMargin=2.2 * cm,
        leftMargin=2.2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=title,
        author=STORE_NAME,
    )

    content = [
        Paragraph(STORE_NAME, title_style),
        Paragraph(title, title_style),
        Spacer(1, 0.3 * cm),
        Paragraph(
            "Documento informativo oficial para clientes de NovaMarket.",
            body_style,
        ),
        PageBreak(),
    ]

    for heading, text in sections:
        content.append(Paragraph(heading, heading_style))
        content.append(Paragraph(" ".join(text.split()), body_style))

    document.build(content)


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    documents_directory = project_root / "documents"
    documents_directory.mkdir(exist_ok=True)

    for filename, data in DOCUMENTS.items():
        output_path = documents_directory / filename
        build_pdf(output_path, data["title"], data["sections"])
        print(f"PDF generado: {output_path}")


if __name__ == "__main__":
    main()