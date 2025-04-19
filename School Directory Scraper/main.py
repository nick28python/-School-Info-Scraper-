import requests
from bs4 import BeautifulSoup
import csv

# Custom headers to act like a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

proxies = {
    "http": "http://your_proxy_here",
    "https": "http://your_proxy_here"
}

# Dummy URL (replace this with real one for actual project)
BASE_URL = "https://example.com/schools-directory?page={}"

# Total pages to loop (for demo, 3 pages)
TOTAL_PAGES = 3

# Final data list
school_data = []

for page in range(1, TOTAL_PAGES + 1):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADERS, proxies=proxies)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example HTML structure (you'll inspect actual site's tags)
    school_blocks = soup.find_all("div", class_="school-card")

    for school in school_blocks:
        name = school.find("h3", class_="school-name").text.strip()
        email_tag = school.find("a", href=True)
        email = email_tag["href"].replace("mailto:", "") if email_tag else "N/A"

        school_data.append([name, email])

# Save to CSV
with open("data/sample_site_schools.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email"])
    writer.writerows(school_data)

print("✅ Data scraped and saved!")
