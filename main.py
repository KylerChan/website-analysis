import requests as r
import os 
import time as t
from bs4 import BeautifulSoup
import datetime

def main():
    print("What is the URL of the website you would like to get information from?")
    url = input("> ")
    
    print("---------------- \n")
    
    print("What User-Agent do you want to be?")
    print("A User-Agent header is a header that the website will identify you as.")
    print("1. Iphone (Safari)")
    print("2. Macbook (Safari)")
    print("3. Windows (Chrome)")
    print("4. Linux (Firefox)")
    print("5. Andriod (Chrome)")
    print("6. Smart TV (Samsung Tizen Browser)")
    print("7. Game Console (Playstation 5)")
    print("8. iPadOS Safari")
    print("9. Googlebot (Search Bot)")
    print("10. Edge on Windows 11")
    print("11. Facebook Crawler")
    print("12. Slackbot Link Expander")
    print("13. Opera Browser")
    print("14. Tor Browser")
    print("15. Nintendo Switch")
    print("16. Internet Explorer 11 on Win7")
    print("17. Linux Desktop Chrome")
    print("18. curl command-line tool")
    print("19. wget command-line tool")
    print("20. Python Requests library")
    print("21. Googlebot-Mobile")
    print("22. Bixby Voice Assistant")
    print("23. Facebook Mobile App WebView")
    print("24. Amazon CloudFront Origin Shield")
    print("25. Enter your own User-Agent Code")
    user_headerChoice = int(input("Input the number (1-25): "))
    
    userAgent = ""
    
    if user_headerChoice == 1:
        userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    elif user_headerChoice == 2:
        userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    elif user_headerChoice == 3:
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Safari/537.36"
    elif user_headerChoice == 4:
        userAgent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"
    elif user_headerChoice == 5:
        userAgent = "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
    elif user_headerChoice == 6: 
        userAgent = "Mozilla/5.0 (SMART-TV; Linux; Tizen 6.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 TV Safari/537.36"
    elif user_headerChoice == 7:
        userAgent = "Mozilla/5.0 (PlayStation 5 3.11) AppleWebKit/605.1.15 (KHTML, like Gecko)"
    elif user_headerChoice == 8:
        userAgent = "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    elif user_headerChoice == 9:
        userAgent = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    elif user_headerChoice == 10:
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Safari/537.36 Edg/125.0.2535.67"
    elif user_headerChoice == 11:
        userAgent = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
    elif user_headerChoice == 12:
        userAgent = "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)"
    elif user_headerChoice == 13:
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Safari/537.36 OPR/99.0.0.0"
    elif user_headerChoice == 14:
        userAgent = "Mozilla/5.0 (Windows NT 10.0; rv:115.0) Gecko/20100101 Firefox/115.0"
    elif user_headerChoice == 15:
        userAgent = "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/6.0.0.10.12 NintendoBrowser/5.1.0.13343"
    elif user_headerChoice == 16:
        userAgent = "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
    elif user_headerChoice == 17:
        userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Safari/537.36"
    elif user_headerChoice == 18:
        userAgent = "curl/8.2.0"
    elif user_headerChoice == 19:
        userAgent = "Wget/1.21.3 (linux-gnu)"
    elif user_headerChoice == 20:
        userAgent = "python-requests/2.31.0"
    elif user_headerChoice == 21:
        userAgent = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MMB29V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    elif user_headerChoice == 22:
        userAgent = "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Bixby/2.0"
    elif user_headerChoice == 23:
        userAgent = "Mozilla/5.0 (Linux; Android 13; SM-S918U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.0.0 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/437.0.0.27.118]"
    elif user_headerChoice == 24:
        userAgent = "Amazon CloudFront"
    elif user_headerChoice == 25:
        customAgent = True
        userAgent = input("Enter the user agent code here: ")
    
    headers = {
        "User-Agent": userAgent,
        "Accept-Language": "en-US"
    }
    
    response = r.get(url, headers=headers)
    
    encoding = response.encoding  
    headers_dict = dict(response.headers)
    statusCode = response.status_code
    htmlPage = response
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.text.strip() if soup.title else "No title found"
    links_count = len(soup.find_all('a'))
    images_count = len(soup.find_all('img'))
    scripts_count = len(soup.find_all('script'))
    styles_count = len(soup.find_all('style')) + len(soup.find_all('link', rel='stylesheet'))
    forms_count = len(soup.find_all('form'))
    
    meta_tags = {}
    for meta in soup.find_all('meta'):
        if meta.get('name'):
            meta_tags[meta.get('name')] = meta.get('content')
    
    security_headers = {
        'Content-Security-Policy': headers_dict.get('Content-Security-Policy', 'Not set'),
        'X-XSS-Protection': headers_dict.get('X-XSS-Protection', 'Not set'),
        'X-Content-Type-Options': headers_dict.get('X-Content-Type-Options', 'Not set'),
        'X-Frame-Options': headers_dict.get('X-Frame-Options', 'Not set'),
        'Strict-Transport-Security': headers_dict.get('Strict-Transport-Security', 'Not set'),
        'Referrer-Policy': headers_dict.get('Referrer-Policy', 'Not set')
    }
    
    t.sleep(1)
    print("----------")
    print("\n Generating report of website...")
    report_name = input("What is the name of the text report you would like to have? ")
    
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(results_dir, exist_ok=True)
    
    report_content = []
    report_content.append("=" * 40)
    report_content.append("WEBSITE ANALYSIS REPORT")
    report_content.append("=" * 40)
    report_content.append(f"URL: {url}")
    report_content.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_content.append("=" * 40)
    report_content.append("")
    
    report_content.append("BASIC INFORMATION")
    report_content.append("-" * 40)
    report_content.append(f"Status Code: {statusCode}")
    report_content.append(f"Encoding: {encoding}")
    report_content.append(f"Content Type: {headers_dict.get('Content-Type', 'Unknown')}")
    report_content.append(f"Server: {headers_dict.get('Server', 'Unknown')}")
    report_content.append(f"Page Title: {title}")
    report_content.append("")
    
    report_content.append("CONTENT ANALYSIS")
    report_content.append("-" * 40)
    report_content.append(f"Number of Links: {links_count}")
    report_content.append(f"Number of Images: {images_count}")
    report_content.append(f"Number of Scripts: {scripts_count}")
    report_content.append(f"Number of Stylesheets: {styles_count}")
    report_content.append(f"Number of Forms: {forms_count}")
    report_content.append("")
    
    report_content.append("RESPONSE HEADERS")
    report_content.append("-" * 40)
    for key, value in headers_dict.items():
        report_content.append(f"{key}: {str(value)}")
    report_content.append("")
    
    if meta_tags:
        report_content.append("META TAGS")
        report_content.append("-" * 40)
        for name, content in meta_tags.items():
            report_content.append(f"{name}: {str(content)}")
        report_content.append("")
    
    report_content.append("SECURITY HEADERS ANALYSIS")
    report_content.append("-" * 40)
    for key, value in security_headers.items():
        status = 'PRESENT' if value != 'Not set' else 'MISSING'
        status_indicator = '[✓]' if status == 'PRESENT' else '[✗]'
        report_content.append(f"{status_indicator} {key}: {status} - {str(value)}")
    report_content.append("")
    
    report_content.append("REQUEST INFORMATION")
    report_content.append("-" * 40)
    report_content.append(f"User Agent Used: {userAgent}")
    
    report_content.append("")
    
    report_content.append("SUMMARY")
    report_content.append("-" * 40)
    security_present = sum(1 for v in security_headers.values() if v != 'Not set')
    security_total = len(security_headers)
    report_content.append(f"Security Headers: {security_present}/{security_total} present")
    report_content.append(f"Total Elements: {links_count + images_count + scripts_count + styles_count + forms_count}")
    report_content.append(f"Analysis completed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_content.append("")
    report_content.append("=" * 40)
    report_content.append("END OF REPORT - Tool made by @KylerChan on GitHub")
    report_content.append("=" * 40)
    
    report_path = os.path.join(results_dir, f"{report_name}.txt")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_content))
    
    print(f"\nText report has been generated and saved to: {report_path}")
    print("\nReport Summary:")
    print(f"URL: {url}")
    print(f"Status Code: {statusCode}")
    print(f"Content Type: {headers_dict.get('Content-Type', 'Unknown')}")
    print(f"Page Title: {title}")
    print(f"Links: {links_count}, Images: {images_count}, Scripts: {scripts_count}")
    print(f"Security Headers: {security_present}/{security_total} present")

if __name__ == "__main__":
    main()
