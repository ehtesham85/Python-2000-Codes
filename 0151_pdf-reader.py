from pypdf import PdfReader

# Read the First PDF file
reader=PdfReader("first_pdf.pdf")
pages=reader.pages[0]
text=pages.extract_text()
print(text)

# Read the Second PDF file
reader2=PdfReader("second_pdf.pdf")
pages2=reader.pages[0]
gtext2=pages.extract_text()
print(gtext2)
