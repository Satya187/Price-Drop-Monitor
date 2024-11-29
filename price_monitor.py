import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
 
 
# Sends an email notification when the product price drops below the threshold price
def send_email_notification(current_price, threshold_price):
    sender_email = "satyaveerubhotla187@gmail.com"
    sender_password = "YOUR_PASSWORD"
    recipient_email = "satyaveerubhotla7@gmail.com"
    product_link = "https://www.amazon.in/dp/B0D9629NJQ"
    subject = "Price Drop Alert!"
    body = (
        f"The price of your product has dropped below {threshold_price}.\n"
        f"Current Price: {current_price}\n"
        f"Product Link: {product_link}\n"
        "Buy now!"
    )
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
 
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient_email], msg.as_string())
            print("Email notification sent!")
    except Exception as e:
        print(f"Failed to send email notification: {e}")
 
 
# Retrieves the current price of the specified product from Amazon
def get_price():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
 
    try:
        URL = "https://www.amazon.in/dp/B0D9629NJQ"
        driver.get(URL)
 
        price = None
        price_xpath_options = [
            "//span[@id='priceblock_ourprice']",
            "//span[@id='priceblock_dealprice']",
            "//span[@class='a-price-whole']"
        ]
 
        for xpath in price_xpath_options:
            try:
                price = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                ).text
                break
            except:
                continue
 
        if price:
            return float(price.replace(",", "").replace("₹", "").strip())
    except Exception as e:
        print(f"Error occurred while retrieving price: {e}")
    finally:
        driver.quit()
    return None
 
 
# Main execution point for monitoring the product price
if __name__ == "__main__":
    threshold_price = 1500.0
    print("Monitoring price...")
 
    while True:
        current_price = get_price()
        if current_price is not None:
            print(f"Current Price: ₹{current_price}")
            if current_price < threshold_price:
                send_email_notification(current_price, threshold_price)
                print("Stopping monitoring as the price dropped.")
                break
            else:
                print("No price drop detected. Continuing to monitor...")
        else:
            print("Failed to retrieve the price.")
 
        time.sleep(3600)
