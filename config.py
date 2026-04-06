import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# WhatsApp Settings (Twilio)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')
YOUR_PHONE_NUMBER = os.getenv('YOUR_PHONE_NUMBER')

# Scraper Settings
SEARCH_KEYWORDS = "Cybersecurity"
LOCATION = "Portugal"  # Changed to a specific location as Hybrid requires a region
CHECK_INTERVAL_HOURS = 4  # Checking 6 times a day is realistic for new postings
# Experience Level: 2 = Junior/Entry Level
# Work Type: 1 = On-site, 2 = Remote, 3 = Hybrid
EXPERIENCE_LEVEL = "2"
WORK_TYPE = "3"
