# 📄 PDF Processing Script

## Overview

This script processes PDF files by:
1. Splitting them into individual pages.
2. Extracting names from the first page of each PDF.
3. Renaming the files based on the extracted names with a specified prefix.

## Requirements

- Python 3.x
- Required libraries: `os`, `re`, `shutil`, `argparse`, `PyPDF2`, `pdfplumber`

## Installation

Install the necessary Python libraries using pip:

```bash
pip install PyPDF2 pdfplumber
```

## Usage

### Command Line Arguments

- `--input_folder`: Directory containing the input PDF files. Default is "input".
- `--prefix`: Prefix for the output files. (Required)

### Running the Script

```bash
python script_name.py --input_folder <input_folder> --prefix <file_prefix>
```

### Example

```bash
python script_name.py --input_folder input --prefix renamed
```

## Functions

### `split_pdf(path, output_folder)`

Splits a PDF into individual pages and saves them in the specified output folder.

### `extract_names_from_pdfs(input_folder)`

Extracts names from the first page of each PDF in the input folder using a regex pattern and returns a dictionary of filenames and extracted names.

### `rename_files(names_dict, source_folder, file_prefix)`

Renames PDF files in the source folder based on the extracted names and given prefix.

### `main(input_folder, file_prefix)`

Main function that orchestrates the PDF splitting, name extraction, and file renaming.

## License

This project is open-source and available under the MIT License.

---

### 📂 Project Structure

- `input_folder/` - Directory containing input PDF files.
- `result/` - Directory where the split and renamed PDF files will be saved.

### 📑 Example Workflow

1. Place your PDF files in the `input` folder.
2. Run the script with the desired prefix.
3. Find the processed files in the `result` folder.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Issues

If you encounter any issues, please open an issue on GitHub.

---

Happy PDF Processing! 😊
