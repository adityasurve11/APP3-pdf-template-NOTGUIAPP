from fpdf import FPDF

pdf = FPDF(orientation= "P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=11)
pdf.cell(w=0, h=11, txt="Aditya Surve", align="L", ln=1)

pdf.set_font(family="Times", style="B", size=11)
pdf.cell(w=0, h=11, txt="Aditya Surve", align="R", ln=1)

pdf.output("output.pdf")
