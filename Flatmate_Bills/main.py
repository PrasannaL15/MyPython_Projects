from fpdf import FPDF


class Bill:
    """
    Object that contains data about the bill such as total amount and period of bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bil_variable, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return weight * bil_variable.amount


class PdfReport:
    """
    Create a PDF file that contains data about flatmate such as their names, due amount and period of bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("house.png", w=50, h=40)
        # Insert title
        pdf.set_font(family='Times', size=23, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert Period Label and Value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=200, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=200, h=40, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and due amount of first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=200, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)


bill = Bill(amount=100, period="May 2021")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print(f"{john.name} Pays {john.pays(bil_variable=bill, other_flatmate=marry)} for a period of {bill.period}")
print(f"{marry.name} Pays {marry.pays(bil_variable=bill, other_flatmate=john)} for a period of {bill.period}")

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)
