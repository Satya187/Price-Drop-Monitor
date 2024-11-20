```markdown
# Price Drop Monitor

This project is a Python script that monitors the price of a product on Amazon and sends an email notification when the price drops below a predefined threshold. The script uses Selenium to scrape the product price and SMTP to send email notifications.

## Features
- **Price Monitoring**: Monitors the price of a specific product on Amazon.
- **Email Notifications**: Sends an email to a recipient when the price drops below the specified threshold.
- **Headless Browser**: Uses Selenium with headless Chrome to scrape the product page without opening a browser window.
- **Scheduled Checks**: The script checks the price every hour and notifies the user if the price is lower than the threshold.

## Requirements

Before running the script, you need to install the following dependencies:

- **Selenium**: To interact with the Amazon website and scrape the product price.
- **WebDriver Manager**: To automatically manage the ChromeDriver.
- **Email Libraries**: To send email notifications.

You can install the required libraries using pip:

```bash
pip install selenium
pip install webdriver-manager
```

## Setup Instructions

### 1. Email Configuration

In the `send_email_notification` function, replace the following variables with your own email credentials:

- `sender_email`: Your email address.
- `sender_password`: Your email app password (see below for how to generate one).
- `recipient_email`: The email address that will receive the price drop notification.

### 2. App Password for Gmail

If you're using Gmail, you may need to generate an App Password to use for the `sender_password`. This is due to Google's security settings. You can generate an app password by following these steps:

1. Visit [Google Account](https://myaccount.google.com/).
2. Go to **Security** and enable **2-Step Verification**.
3. Under **App passwords**, generate a new app password and use it as `sender_password` in the script.

### 3. Configure the Product Link

In the `get_price` function, set the `URL` variable to the Amazon product link you want to monitor. For example:

```python
URL = "https://www.amazon.in/dp/B0D9629NJQ"
```

### 4. Run the Script

To start monitoring the price, simply run the Python script:

```bash
python price_drop_monitor.py
```

The script will check the price every hour and send a notification if the price drops below the threshold price.

## How It Works

- **Price Scraping**: The script uses Selenium to open the Amazon product page and extracts the price using XPath selectors.
- **Price Check**: Every hour, the script compares the current price with the threshold price. If the price is lower than the threshold, an email notification is sent.
- **Email Notification**: The script sends an email to the recipient using SMTP with the current price and a link to the product.

## Example Output

```bash
Monitoring price...
Current Price: ₹1299.0
Email notification sent!
Stopping monitoring as the price dropped.
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
