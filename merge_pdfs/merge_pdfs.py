import click
import logging
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(file_input_pdfs: list, file_output_pdf: str) -> None:
    pdf_writer = PdfWriter()

    for file_input_pdf in file_input_pdfs:
        pdf_reader = PdfReader(file_input_pdf)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF
    with open(file_output_pdf, "wb") as fd_out:
        pdf_writer.write(fd_out)
    logging.info(f"Merged PDF file written to: {file_output_pdf}")
    return


@click.command()
@click.option(
    "--file_pdf",
    "-f",
    multiple=True,
    help="full path to PDF file (multiple files can be added)",
)
def main(file_pdf: tuple) -> None:
    logging.basicConfig(level=logging.INFO)
    file_output_pdf = "merged.pdf"
    file_input_pdfs = list(file_pdf)
    logging.info(f"Input PDF files: {file_input_pdfs}")
    merge_pdfs(file_input_pdfs, file_output_pdf)
    return


if __name__ == "__main__":
    main()
