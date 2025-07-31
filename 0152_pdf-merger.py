from pypdf import PdfWriter

merger = PdfWriter()
merger.append("first_pdf.pdf")
merger.append("second_pdf.pdf")
merger.write("merged_pdf.pdf")
merger.close()

print("PDFs merged successfully into 'merged_pdf.pdf'")
