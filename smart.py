from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 14)
        self.set_text_color(50, 50, 50)  # Darker text color for the header
        self.cell(0, 10, 'Device Installation Report', ln=True, align='C')
        self.ln(10)

    def table_vertical(self, data):
        # Set font for the table
        self.set_font('Arial', '', 12)

        # Background color for headers
        header_background_color = (200, 200, 200)

        # Padding for cells
        cell_padding = 2

        for row in data:
            for header, value in row.items():
                # Header cell
                self.set_fill_color(*header_background_color)
                self.set_text_color(0, 0, 0)
                self.cell(40, 10, header, border=1, align='C', fill=True, ln=0)
                
                # Value cell
                self.cell(0, 10, str(value), border=1, align='C', ln=1)
                
            # Add a line break between entries
            self.ln(5)

# Collect user input
data = []
while True:
    print("Enter the following details or type 'done' to finish:")
    objet = input("Objet: ")
    if objet.lower() == 'done':
        break
    type_de_boitier = input("Type de Boitier: ")
    numero_serie = input("N° de serie: ")
    imei = input("IMEI: ")
    device_id = input("ID: ")
    nom_client = input("Nom du Client: ")
    marque_vehicule = input("Marque du vehicule: ")
    immatriculation = input("Immatriculation: ")
    iccid = input("ICCID: ")
    nom_technicien = input("Nom du technicien: ")

    # Store data in dictionary format
    data.append({
        'Objet': objet,
        'Type de Boitier': type_de_boitier,
        'N° de serie': numero_serie,
        'IMEI': imei,
        'ID': device_id,
        'Nom du Client': nom_client,
        'Marque du vehicule': marque_vehicule,
        'Immatriculation': immatriculation,
        'ICCID': iccid,
        'Nom du technicien': nom_technicien
    })

# Create a PDF object
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Generate the table in the PDF
pdf.table_vertical(data)

# Save the PDF
pdf_file_name = r"C:\Users\LENOVO\Documents\CPY_SAVES\part7.pdf"
pdf.output(pdf_file_name)

print(f"PDF created successfully and saved as {pdf_file_name}")