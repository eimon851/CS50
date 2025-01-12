SELECT * FROM VIEW;
from fpdf import FPDF

# # Prompt user to enter name
name = input("Name: ")

# define class PDF
class PDF(FPDF):
    # header on top, image center and text is center of image
    def header(self):
        # text above shirt
        self.set_font("helvetica", "B", 40)
        self.cell(80)
        self.cell(30,30,"CS50 Shirtificate", border=None, align="C")


        # rendering image, centered at page
        self.image("shirtificate.png", 30, 50, 150)

        # text center of shirt
        self.set_xy(70,90)
        self.set_font("helvetica", "B", 15)
        self.set_text_color(255,255,255)
        self.cell(30,30, f"{name} took CS50")



        # setting font detail
# create instance of object
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.output("shirtificate.pdf")


