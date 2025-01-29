# Python Script to Send Emails with Attachments Using MailerSend

This repository contains a Python script that allows you to send emails with attachments from your custom domain using the MailerSend API. The script supports both plain text and HTML content, and it can attach files (e.g., PDFs, images) to the email.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [How to Use](#how-to-use)
   - [Step 1: Set Up MailerSend](#step-1-set-up-mailersend)
   - [Step 2: Verify Your Domain](#step-2-verify-your-domain)
   - [Step 3: Configure the Script](#step-3-configure-the-script)
   - [Step 4: Run the Script](#step-4-run-the-script)
4. [Code Overview](#code-overview)
5. [License](#license)

---

## Features
- Send emails from your custom domain (e.g., `contacto@modware.lat`).
- Attach files (e.g., PDFs, images) to your emails.
- Supports both plain text and HTML email content.
- Robust error handling for API responses and exceptions.
- Easy configuration using environment variables.

---

## Requirements
- Python 3.x
- MailerSend API Key
- Verified custom domain in MailerSend
- Python libraries: `requests`, `python-dotenv`, `base64`

---

## How to Use

### Step 1: Set Up MailerSend
1. **Sign Up for MailerSend:**
   - Go to [MailerSend](https://www.mailersend.com/) and create an account.
   - Once registered, navigate to the **API & SMTP** section to generate your API Key.

2. **Get Your API Key:**
   - Copy the API Key provided by MailerSend.
   - Save it in a `.env` file in your project directory:
     ```plaintext
     MAILERSEND_API_KEY=your_api_key_here
     ```

---

### Step 2: Verify Your Domain
1. **Add Your Domain:**
   - In the MailerSend dashboard, go to **Domains** and click **Add Domain**.
   - Enter your custom domain (e.g., `modware.lat`) and click **Add Domain**.

2. **Verify Your Domain:**
   - MailerSend will provide DNS records (SPF, DKIM, and MX) that you need to add to your domain's DNS settings.
   - Go to your domain registrar (e.g., Namecheap) and add the provided DNS records.
   - Wait for the DNS changes to propagate (this can take up to 48 hours).
   - Once verified, your domain status will change to **Verified** in the MailerSend dashboard.

---

### Step 3: Configure the Script
1. **Clone the Repository:**
   ```bash
   git clone git@github.com:paulmrg-461/self_domain_email_sender.git
   cd self_domain_email_sender
   ```

2. **install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update the script:**
Open the script and update the following variables:
- from_email: Your custom domain email (e.g., contacto@modware.lat).
- from_name: The sender's name.
- to_email: The recipient's email address.
- to_name: The recipient's name.
- attachment_path: The path to the file you want to attach (e.g., image.png).

---

### Step 4: Run the Script

1. **Execute the Script:**
   ```bash
   python mailer_send.py
   ```

2. **Check the Output:**
If the email is sent successfully, you'll see:
   ```bash
    Email sent successfully!
    Response: {"message": "Email sent successfully"}
   ```
If there's an error, the script will display the error details.

---

## Contributing
Contributions are welcome! Follow these steps to get started:

1. **Fork the Repository**

2. **Create a Feature Branch

   ```bash
     git checkout -b feature/YourFeatureName
   ```
3. **Commit Your Changes**

   ```bash
     git commit -m "Add some feature"
   ```
4. **Push to the Branch**

   ```bash
     git push origin feature/YourFeatureName
   ```
   This command will launch the portfolio in your default web browser.
5. **OPen a Pull Request**

## Contact
Developed by:
Paul Realpe

Email: co.devpaul@gmail.com
Phone: 3148580454
<a  href="https://devpaul.co">https://devpaul.co/</a>

Feel free to reach out for any inquiries or collaborations!