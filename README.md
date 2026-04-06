# 🛡️ Cybersecurity Job Scraper & WhatsApp Notifier

Automated tool to scrape **LinkedIn** for Cybersecurity Junior Hybrid roles and send notifications via **Twilio WhatsApp API**.

## 🛠 Features
- **Specific Targeting:** Filters for Cybersecurity, Entry-Level/Junior, and Hybrid positions.
- **Smart Notifications:** Sends a summary of the top 5 jobs found.
- **Background Automation:** Runs 24/7 as a system service.
- **Real-time Updates:** Checks every 4 hours for the latest postings.

## 🚀 Setup & Installation

### 1. Prerequisites
- Python 3.10+
- Twilio Account (for WhatsApp notifications)

### 2. Installation
```bash
git clone https://github.com/yourusername/linkedin-job-scraper.git
cd linkedin-job-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
YOUR_PHONE_NUMBER=whatsapp:+351...
```
Adjust keywords and location in `config.py`.

### 4. Run as a Background Service (Linux/Ubuntu)
To keep the scraper running forever:
1. Copy the service file:
   ```bash
   mkdir -p ~/.config/systemd/user/
   cp linkedin-job-scraper.service ~/.config/systemd/user/
   ```
2. Start and enable:
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable linkedin-job-scraper.service
   systemctl --user start linkedin-job-scraper.service
   ```
3. Monitor logs:
   ```bash
   journalctl --user -u linkedin-job-scraper.service -f
   ```

## 📜 License
MIT
