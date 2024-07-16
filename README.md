# 📄 PDF Processing Script

## Overview

The PDF Split App separates PDF files into individual pages, identifies text patterns, and renames the files accordingly, storing them in the `result` folder.

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

Add PDFs to the `input` folder.

Run the script in your terminal:

```bash
python pdf_processor.py --input_folder <path/to/input> --prefix <your_prefix>
```

### Example

```bash
python pdf_processor.py --input_folder input --prefix renamed
```

Processed files will appear in the `result` folder.

## Code Explanation

### Script Logic

#### 1. Split PDF Files

The `split_pdf(path, output_folder)` function:
- **Creates an output directory** if it doesn't exist.
- **Splits each page** of the input PDF into separate PDF files.
- **Saves each page** as a new PDF file in the specified output folder.

#### 2. Extract Names from PDFs

The `extract_names_from_pdfs(input_folder)` function:
- **Searches for a specific pattern** (`DISTRIBUTION NOTICE...Dear`) in the text of the first page of each PDF.
- **Extracts the text** between `DISTRIBUTION NOTICE` and `Dear`.
- **Returns a dictionary** with the filenames as keys and the extracted names as values.

#### 3. Rename PDF Files

The `rename_files(names_dict, source_folder, file_prefix)` function:
- **Iterates through the dictionary** of extracted names.
- **Sanitizes the extracted names** to ensure they are safe for filenames.
- **Renames the split PDF files** in the source folder using the sanitized names and the given prefix.

### Main Function

The `main(input_folder, file_prefix)` function:
- **Ensures the input folder** contains PDF files.
- **Splits each PDF** into separate pages by calling `split_pdf`.
- **Extracts names** from these pages by calling `extract_names_from_pdfs`.
- **Renames the split files** using the extracted names by calling `rename_files`.

### Argument Parsing

The script uses `argparse` to accept `input_folder` and `prefix` as command-line arguments:

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Processing")
    parser.add_argument("--input_folder", default="input", help="Directory with input PDF files")
    parser.add_argument("--prefix", required=True, help="Prefix for the output files")
    args = parser.parse_args()

    main(args.input_folder, args.prefix)
```

## Limitations

- **Text Extraction**: It extracts the text appearing between "DISTRIBUTION NOTICE" and "Dear". This method is not very robust, so ensure the name you want for the file is contained exactly between these two strings.
- **File Overwrites**: Possible file overwrites with identical names.
- **Error Handling**: Limited error handling.

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
