import os
import re
import shutil
import argparse
import PyPDF2
import pdfplumber

def split_pdf(path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)

        for i in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])

            output_filename = f"{output_folder}/document_page_{i + 1}.pdf"
            with open(output_filename, "wb") as output_pdf:
                writer.write(output_pdf)

def extract_names_from_pdfs(input_folder):
    name_pattern = re.compile(r'DISTRIBUTION NOTICE(.*?)Dear', re.DOTALL)
    extracted_names = {}

    for item in os.listdir(input_folder):
        if item.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, item)

            with pdfplumber.open(pdf_path) as pdf:
                first_page = pdf.pages[0]
                text = first_page.extract_text()

                match = re.search(name_pattern, text)
                if match:
                    name = match.group(1).strip()
                    extracted_names[item] = name
                else:
                    print(f"No match found in {pdf_path}")

    return extracted_names

def rename_files(names_dict, source_folder, file_prefix):
    for old_name, new_name in names_dict.items():
        old_path = os.path.join(source_folder, old_name)
        safe_new_name = file_prefix + "_" + re.sub(r'[\\/*?:"<>|]', "", new_name)
        new_path = os.path.join(source_folder, f"{safe_new_name}.pdf")

        shutil.move(old_path, new_path)

def main(input_folder, file_prefix):
    result_folder = "result"
    input_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    if not input_files:
        print(f"No PDF files found in the input directory: {input_folder}")
        return

    for file_name in input_files:
        input_pdf = os.path.join(input_folder, file_name)
        split_pdf(input_pdf, result_folder)

        names = extract_names_from_pdfs(result_folder)

        rename_files(names, result_folder, file_prefix)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Processing")
    parser.add_argument("--input_folder", default="input", help="Directory with input PDF files")
    parser.add_argument("--prefix", required=True, help="Prefix for the output files")
    args = parser.parse_args()

    main(args.input_folder, args.prefix)
