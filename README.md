# Website Analytics Tool 🔍

A comprehensive Python tool for analyzing websites and generating detailed reports about their structure, security headers, and technical characteristics.

## Features ✨

- **Multi-Platform User Agent Support**: Choose from 25 different user agents including browsers, mobile devices, crawlers, and command-line tools
- **Comprehensive Website Analysis**: Analyzes HTML structure, meta tags, and content elements
- **Security Headers Assessment**: Evaluates important security headers and their implementation
- **Detailed Text Reports**: Generates formatted text reports with complete analysis results
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux

## What It Analyzes 📊

### Basic Information
- HTTP status codes
- Content encoding and type
- Server information
- Page title

### Content Analysis
- Number of links (`<a>` tags)
- Number of images (`<img>` tags)
- Number of scripts (`<script>` tags)
- Number of stylesheets (CSS files)
- Number of forms (`<form>` tags)

### Security Headers
- Content-Security-Policy
- X-XSS-Protection
- X-Content-Type-Options
- X-Frame-Options
- Strict-Transport-Security
- Referrer-Policy

### Meta Tags
- Extracts and displays all meta tags with their content

## User Agent Options 🌐

The tool supports 25 different user agents:

**Browsers & Mobile:**

- iPhone (Safari)
- Macbook (Safari)
- Windows (Chrome)
- Linux (Firefox)
- Android (Chrome)
- Smart TV (Samsung Tizen Browser)
- Game Console (PlayStation 5)
- iPadOS Safari
- Edge on Windows 11
- Opera Browser
- Tor Browser
- Nintendo Switch
- Internet Explorer 11 on Win7
- Linux Desktop Chrome

**Crawlers & Bots:**

- Googlebot (Search Bot)
- Facebook Crawler
- Slackbot Link Expander
- Googlebot-Mobile
- Bixby Voice Assistant
- Facebook Mobile App WebView

**Command Line Tools:**
- curl command-line tool
- wget command-line tool
- Python Requests library

**CDN & Services:**
- Amazon CloudFront Origin Shield

**Custom:**
- Enter your own User-Agent Code

## Installation 🚀

### Prerequisites

Make sure you have Python 3.6+ installed on your system.

### Required Dependencies

Install the required packages using pip:

```bash
pip install requests beautifulsoup4
```

### Clone the Repository

```bash
git clone https://github.com/KylerChan/website-analytics.git
cd website-analytics
```

## Usage 💻

1. **Run the script:**
   ```bash
   python main.py
   ```

2. **Enter the website URL** you want to analyze when prompted

3. **Choose a User-Agent** from the list of 25 options (1-25)

4. **Enter a report name** for the generated text file

5. **View results** in the terminal and find the detailed report in the `results/` folder

### Example Usage

```
What is the URL of the website you would like to get information from?
> https://example.com

What User-Agent do you want to be?
1. iPhone (Safari)
2. Macbook (Safari)
...
25. Enter your own User-Agent Code
Input the number (1-25): 3

What is the name of the text report you would like to have?
> example_analysis
```

## Output 📄

The tool generates:

1. **Terminal Summary**: Quick overview displayed in the console
2. **Detailed Text Report**: Comprehensive analysis saved as `.txt` file in the `results/` folder

### Sample Report Structure

```
================================================================================
WEBSITE ANALYSIS REPORT
================================================================================
URL: https://example.com
Generated: 2024-01-15 14:30:25
================================================================================

BASIC INFORMATION
----------------------------------------
Status Code: 200
Encoding: utf-8
Content Type: text/html; charset=utf-8
Server: nginx/1.18.0
Page Title: Example Domain

CONTENT ANALYSIS
----------------------------------------
Number of Links: 15
Number of Images: 3
Number of Scripts: 8
Number of Stylesheets: 2
Number of Forms: 1

SECURITY HEADERS ANALYSIS
----------------------------------------
[✓] Content-Security-Policy: PRESENT - default-src 'self'
[✗] X-XSS-Protection: MISSING - Not set
...
```

## Project Structure 📁

```
website-analytics/
├── main.py              # Main application script
├── results/             # Generated reports folder
│   └── *.txt           # Analysis reports
└── README.md           # This file
```

## Dependencies 📦

- **requests**: For making HTTP requests to websites
- **beautifulsoup4**: For parsing HTML content
- **datetime**: For timestamp generation (built-in)
- **os**: For file system operations (built-in)

## Use Cases 🎯

- **Web Development**: Test how your site responds to different user agents
- **SEO Analysis**: Check how search engine crawlers see your website
- **Security Auditing**: Evaluate security header implementation
- **Compatibility Testing**: Test website behavior across different browsers and devices
- **Research**: Analyze website structure and technical characteristics

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📝

This project is open source and available under the [GNU GENERAL PUBLIC LICENSE](LICENSE).

## Author 👨‍💻

Created by [@KylerChan](https://github.com/KylerChan)

## Support 💬

If you have any questions or issues, please open an issue on GitHub.

---

**Happy analyzing! 🚀**
