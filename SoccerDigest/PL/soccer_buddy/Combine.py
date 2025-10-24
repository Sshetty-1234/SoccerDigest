import re
import os
from fpdf import FPDF
import datetime
from .scrapers.apn_news_scraper import article_content as adp_info
from .scrapers.goal_com_scraper import article_content as goal_info
from .scrapers.transfermarket_scraper import article_content as transfermarket_info

def create_pdf(adp_info, goal_info, transfermarket_info) -> str:
    current_date = datetime.date.today()

    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Soccer News Digest', 0, 1, 'C')

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Clean and process text
    adp_info = re.sub(r'\s+', ' ', adp_info.strip())
    goal_info = re.sub(r'\s+', ' ', goal_info.strip())
    transfermarket_info = re.sub(r'\s+', ' ', transfermarket_info.strip())

    # Combine all text
    text = f"{goal_info}\n\n{transfermarket_info}\n\n{adp_info}"

    # Encode for PDF compatibility
    text = text.encode('latin1', 'replace').decode('latin1')

    # Add content to PDF
    pdf.multi_cell(0, 10, text)

    # Save PDF
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_output = os.path.join(base_dir, "data",'summary', f"Report_{current_date}.pdf")
    pdf.output(pdf_output)
    print(f"PDF created at: {pdf_output}")
    
    

if __name__ == "__main__":
    # Dummy data for testing purposes
    

    create_pdf(adp_info, goal_info, transfermarket_info)
