Description

PDF Split App separates PDF files into individual pages, identifies text patterns, and renames the files accordingly, storing them in the result folder.

		Add PDFs to the input folder.

		Run: python pdf_processor.py --prefix YourDesiredPrefix in your terminal.

		Processed files appear in the result folder.

Limitations
	•	It extracts the text appearing between "DISTRIBUTION NOTICE" and "Dear" (not very robust). So make sure the name you want for the file is contained exactly between these two strings
	•	Possible file overwrites with identical names.
	•	Limited error handling
