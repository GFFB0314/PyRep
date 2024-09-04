from fpdf import FPDF
from fpdf.enums import XPos, YPos
from sys import exit

title = "SMARTRACK"
class PDF(FPDF):
    def header(self):
        #place the image'it is on the left side'
        self.image(r"C:\Users\LENOVO\Documents\CPY_SAVES\smart.jpg", 10, 2, 70)
        #set the font of the title
        self.set_font("Times", "", 35)
        self.set_draw_color(15, 20, 25)
        self.set_text_color(250, 50, 50)
        #calculate the title width
        title_w = self.get_string_width(title)
        self.set_line_width(2)
        self.set_x((self.w - title_w) - 10)
        self.cell(title_w, 10, title, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=1, align="R")
        #add a break line
        self.ln()

    def table_vertical(self, data):
        self.set_font("Helvetica", "", 12)
        header_background_color = (200, 150, 150)

        cell_padding = 2
        self.ln(60)
        for row in data:
            for header, value in row.items():
                self.set_fill_color(*header_background_color)#'*' is used to unpacked tuple or other data set
                self.set_text_color(5, 4, 4)
                self.cell(40, 10, header, border=1, align="C", fill=True, ln=0)

                self.cell(0, 10, str(value), border=1, align="C", ln=1)
            
            self.ln(5)#adds extra spaces between dictionnaries

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "BI", 10)
        self.cell(0, 10, f"{self.page_no()} / {{nb}}", align="C")

# Collect user input
data = []
while True:
    try:
        print("Enter the following details or type 'done' to finish: ")
        object = input("Object: ")
        if object.lower() == "done":
            break
        caste_type = input("Type de boitier: ")
        serial_num = input("N° de serie: ")
        imei = int(input("IMEI: "))
        device_id = input("ID: ")
        client_name = input("Nom du client: ")
        vehi_type = input("Marque du vehicule: ")
        immat = input("Immatriculation: ")
        iccid = int(input("ICCID: "))
        nom_tech = input("Nom du technicien: ")

        data.append({
            "Object": object,
            "Caste_type": caste_type,
            "N° de serie": serial_num,
            "IMEI": imei,
            "ID": device_id,
            "Client_name": client_name,
            "Vehi_type": vehi_type,
            "IMMAT": immat,
            "ICCID": iccid,
            "Nom_tech": nom_tech
        })
    except ValueError:
        exit("Enter valid data format!")

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.alias_nb_pages()
pdf.add_page()

# Generate the table in the PDF
pdf.table_vertical(data)

location = r"C:\Users\LENOVO\Documents\CPY_SAVES\part8.pdf"
pdf.output(location)
print(f"PDF was created and saved in {location}")