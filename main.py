from fpdf import FPDF
import pandas as pd

# This is not a WEB app, just a pdf template project nothing else

pdf = FPDF(orientation= "P", unit="mm", format="A4")

df = pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(111, 8, 201)
    pdf.cell(w=0, h=11, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    # set footer
    pdf.ln(244)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=11, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set footer
        pdf.ln(255)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=11, txt=row["Topic"], align="R")

pdf.output("output.pdf")


# e



