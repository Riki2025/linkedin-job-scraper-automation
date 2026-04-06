import time
from playwright.sync_api import sync_playwright
from twilio.rest import Client
import config

def send_whatsapp_notification(message):
    """Sends a notification via Twilio WhatsApp API."""
    if not all([config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.YOUR_PHONE_NUMBER]):
        print("⚠️ WhatsApp credentials not found in .env! Skipping notification.")
        return

    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=config.TWILIO_WHATSAPP_NUMBER,
            to=config.YOUR_PHONE_NUMBER
        )
        print(f"✅ Notification sent! SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp: {e}")

def scrape_jobs():
    """Scrapes LinkedIn for new job listings."""
    print(f"🔍 Searching for '{config.SEARCH_KEYWORDS}' jobs in '{config.LOCATION}'...")

    with sync_playwright() as p:
        # We add some common browser arguments to look more like a real user
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # LinkedIn Search URL with filters:
        # f_TPR=r14400 -> Posted in the last 4 hours (matching our interval)
        # f_E=2 -> Entry Level/Junior
        # f_WT=3 -> Hybrid
        # f_WT=2 -> Remote
        search_url = (
            f"https://www.linkedin.com/jobs/search?keywords={config.SEARCH_KEYWORDS}"
            f"&location={config.LOCATION}&f_TPR=r14400&f_E={config.EXPERIENCE_LEVEL}&f_WT={config.WORK_TYPE}"
        )

        try:
            page.goto(search_url)
            page.wait_for_selector(".jobs-search__results-list", timeout=15000)

            # Extract job data
            cards = page.locator(".base-search-card").all()
            found_jobs = []

            for card in cards[:5]:  # Get the top 5 jobs
                title = card.locator(".base-search-card__title").inner_text().strip()
                company = card.locator(".base-search-card__subtitle").inner_text().strip()
                link = card.locator("a.base-card__full-link").get_attribute("href")
                found_jobs.append(f"• *{title}* @ {company}")

            if found_jobs:
                count = len(cards)
                job_list_str = "\n".join(found_jobs)
                msg = (
                    f"🛡️ *Cybersecurity Alert!* 🛡️\n\n"
                    f"Found *{count}* new Junior Hybrid jobs in the last 4 hours!\n\n"
                    f"✨ *Top Results:* \n{job_list_str}\n\n"
                    f"🔗 *Full Results:* \n{search_url}\n\n"
                    f"Stay safe and good luck! 💻"
                )
                print(f"Found {count} jobs. Sending notification...")
                send_whatsapp_notification(msg)
            else:
                print("No new jobs found in the last 4 hours.")

        except Exception as e:
            print(f"An error occurred during scraping: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    while True:
        try:
            scrape_jobs()
        except Exception as e:
            print(f"❌ Critical error in loop: {e}")

        print(f"😴 Waiting {config.CHECK_INTERVAL_HOURS} hours for next search...")
        time.sleep(config.CHECK_INTERVAL_HOURS * 3600)
