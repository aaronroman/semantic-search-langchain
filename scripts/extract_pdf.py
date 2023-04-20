import fitz
import fire


def pdf_to_text(path: str) -> str:
    """Extracts text from a PDF file"""
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def save_to_disk(txt: str, path: str) -> None:
    """Saves text to a file"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)


def main(input_file_path: str, output_file_path: str) -> None:
    """Extracts text from a PDF file and saves it to a text file"""
    text = pdf_to_text(input_file_path)
    save_to_disk(text, output_file_path)


if __name__ == "__main__":
    """Run the script from the command line"""
    fire.Fire(main)
