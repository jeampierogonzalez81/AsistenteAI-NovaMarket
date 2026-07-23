from pathlib import Path

from pypdf import PdfReader


def load_documents() -> str:
    project_root = Path(__file__).resolve().parent.parent
    documents_directory = project_root / "documents"

    texts = []

    for pdf_path in documents_directory.glob("*.pdf"):
        reader = PdfReader(pdf_path)

        pages_text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                pages_text.append(page_text)

        document_text = "\n".join(pages_text)

        texts.append(
            f"\nDOCUMENTO: {pdf_path.name}\n{document_text}"
        )

    return "\n".join(texts)