from pypdf import PdfReader, PdfWriter

pdf = PdfReader("first_pdf.pdf")
watermark = PdfReader("second_pdf.pdf")
watermark_page = watermark.pages[0]

writer = PdfWriter()

for page in pdf.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)
  
with open("watermarked_output.pdf", "wb") as f:
    writer.write(f)

print("Watermark added successfully!")
