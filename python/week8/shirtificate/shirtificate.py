from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=50)
        self.cell(0, 40, "CS50 Shirtificate", align="C")


pdf = PDF(orientation="P", format="A4")
pdf.set_auto_page_break(False)
pdf.add_page()
pdf.image("shirtificate.png", 5, 60, 200, 220)

name = input("User name: ")
pdf.set_font("helvetica", style="B", size=24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 120)
pdf.cell(0, 10, name, align="C")
pdf.output("shirtificate.pdf")
