import re
from fpdf import FPDF
from .scrapers.apn_news_scraper import article_content as adp_info
from .scrapers.goal_com_scraper import article_content as goal_info
from .scrapers.transfermarket_scraper import article_content as transfermarket_info
import datetime

def create_pdf(adp_info,goal_info,transfermarket_info)->str:
    current_date  = datetime.date.today()

    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Soccer News Digest', 0, 1, 'C')

    pdf = PDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    adp_info = adp_info.strip()
    goal_info = goal_info.strip()
    transfermarket_info = transfermarket_info.strip()

    adp_info = re.sub(r'\s+', ' ', adp_info)
    goal_info = re.sub(r'\s+', ' ', goal_info)
    transfermarket_info = re.sub(r'\s+', ' ', transfermarket_info)


    text = goal_info + transfermarket_info + adp_info

    text = text.encode('latin1', 'replace').decode('latin1')

    pdf.multi_cell(0, 10, text)

    pdf_output = f"/Users/sohamshetty/Desktop/Projects/SoccerDigest/SoccerDigest/PL/NewsScrapers/scraper_data/Report_{current_date}.pdf"
    pdf.output(pdf_output)
    
    return pdf_output

file_path = create_pdf(adp_info,goal_info,transfermarket_info)

