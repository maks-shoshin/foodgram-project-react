from fpdf import FPDF


def download():
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font(
        'DejaVu', '', './recipes/fonts/DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', size=14)
    pdf.cell(txt='Список покупок', center=True)
    pdf.ln(8)
