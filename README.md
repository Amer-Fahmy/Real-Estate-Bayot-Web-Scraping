# Real Estate Scraper
This project is a web scraper built with Scrapy to extract real estate listings from the Bayut website. It collects information such as property price, type, location, area, number of bedrooms, and more.
the dataset is avalible on [Kaggle](https://www.kaggle.com/datasets/ameribrahim/real-estate-bayot-egypt/data)

Features
Scrapes real estate property listings from Bayut.
Extracts data such as:
Price
Location
Type (e.g., apartment, villa)
Area
Number of bedrooms and bathrooms
Saves the scraped data in JSON format for easy reuse.
Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/real_estate_scraper.git
cd real_estate_scraper
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Note: Make sure you have Python 3.10+ installed.

Usage
Run the spider using the main.py script:

bash
Copy
Edit
python main.py
The scraped data will be saved in a file named real_estate_data_bayut_full.json in the project folder.

Logs of the scraping process will be saved in scrapy_output.log.

Project Structure
bash
Copy
Edit
real_estate_scraper/
├── spiders/
│   └── real_estate_spider.py   # The Scrapy spider class
├── main.py                     # Entry point to run the spider
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Ignored files and folders
Example Output
Here’s an example of what the scraped data might look like:

json
Copy
Edit
[
  {
    "link": "https://www.bayut.eg/en/property-detail/example-link",
    "price": "3,000,000",
    "currency": "EGP",
    "type": "Apartment",
    "beds": "3",
    "baths": "2",
    "area": "150 sqm",
    "location": "New Cairo, Egypt",
    "down_payment": "10%",
    "plan_type": "off_plan"
  }
]
Customization
If you want to scrape a different category of properties or add more data fields:

Open spiders/real_estate_spider.py.
Update the selectors in the parse() and parse_detail_page() methods to target new elements.
Known Limitations
The scraper relies on the website's current structure. If the structure changes, the spider might require updates.
Limited to publicly available data; login-protected content is not scraped.
License
This project is licensed under the MIT License.

