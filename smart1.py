from fpdf import FPDF
from fpdf.enums import XPos, YPos

title = "SMARTRACK"


class PDF(FPDF):
    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)  # the child class 'PDF' is pass to the super class 'FPDF' as argument
        # object.add_font(font_name, font_style, font_location, uni=True)
        self.add_font("Blackadder ITC Regular", "", r"C:\Windows\Fonts\ITCBLKAD.ttf", uni="DEPRECATED")

    def header(self):
        self.set_font("Times", "", 25)
        self.set_draw_color(15, 20, 25)  # the range is from 0 to 255
        self.set_text_color(134, 237, 235)
        title_w = self.get_string_width(title)
        doc_w = self.w
        self.set_line_width(2)
        self.set_x((doc_w - title_w) / 2)
        self.cell(title_w, 10, title, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=1, align="C")
        self.ln()
        
    #def table_vertical(self):

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "BI", 10)
        self.cell(0, 10, f"{self.page_no()} / {{nb}}", align="C")


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font("Blackadder ITC Regular", "", 15)
pdf.cell(0, 10, "I SHALL MAKE IT !!", border=1, align="C")
pdf.output(r"C:\Users\LENOVO\Documents\CPY_SAVES\part8.pdf")
