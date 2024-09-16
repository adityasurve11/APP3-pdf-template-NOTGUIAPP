from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation= "P", unit="mm", format="A4")

df = pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(111, 8, 201)
    pdf.cell(w=0, h=11, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")


