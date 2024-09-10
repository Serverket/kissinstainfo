
# KISS Insta Info &middot; ![Release Status](https://img.shields.io/badge/release-v1.0.0-green) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A simple way to scrape follower details from Instagram profiles with a user-friendly web interface.

## 🌐 **Overview**

KISS Insta Info is a Python Flask web application that allows users to scrape follower information from specified Instagram profiles. This application utilizes the `instaloader` library for fetching follower data and the `Beautiful Soup` library for parsing follower names from their profiles. It is designed to be easy to use while providing accurate and comprehensive results.

## 📋 **Features**

- **🔒 Instagram Login**: Users can log into their Instagram accounts securely.
- **👥 Follower Scraping**: The application retrieves and lists followers of specified Instagram profiles, including usernames and names.
- **💻 User-Friendly Interface**: Built with HTML and Tailwind CSS, the application has an intuitive design for ease of use.
- **🚨 Error Handling**: The application includes robust error handling for login failures and scraping issues.
- **⚡ Asynchronous Processing**: The application uses threads to run scraping commands to keep the user interface responsive.
- **📊 Display Results**: Shows the retrieved followers and their names in a structured table format.

## 🔒 **Privacy Notice**

Please be assured that KISS Insta Info does not send any personal information, including usernames or passwords, when scraping data. All information is processed locally and only sent to Instagram for the purpose of scraping follower data.

## ⚠️ **Ethical Use Notice**

This application is intended for ethical use only. Users should ensure they have permission to scrape data from Instagram profiles and comply with Instagram's terms of service. Unauthorized scraping or misuse of data may lead to account suspension or legal consequences. Always respect user privacy and data protection regulations.

## :gear: Running the Application

To run the KISS Insta Info, follow these steps:

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Serverket/kissinstainfo.git
cd kissinstainfo
```

**Run the Application**:

   ```bash
   python kissinstainfo.py
   ```

   This will start the Flask development server.

### Access the Web Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

## 📜 Licensing
This work is licensed under a [MIT License](LICENSE).

## :brain: Acknowledgments

*"Whoever loves discipline loves knowledge, but whoever hates correction is stupid."*