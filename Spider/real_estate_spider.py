class RealEstateSpiderBayut(scrapy.Spider):
    name = 'real_estate_spider_bayut'
    start_urls = ['https://www.bayut.eg/en/egypt/properties-for-sale/?gclid=Cj0KCQiArby5BhCDARIsAIJvjIS8Z6BU1W2h03olEH7nPDxrl-LmelN7bS0EE2t3lpafIg8bB2rmnr0aAv08EALw_wcB']
    # Initialize a list to store data
    real_estate_data = []
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 32,  
        'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
        'CLOSESPIDER_PAGECOUNT': 2084,
        'LOG_FILE': 'scrapy_output.log',
        'LOG_LEVEL': 'DEBUG',
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 5,  # Number of retries for failed requests
    }
    def parse(self, response):
        # Loop through each property card and extract data
        for property_card in response.css('li[role="article"]'):
            property_details = {
                'link': response.urljoin(property_card.css('a.d40f2294::attr(href)').get()),
                'price': property_card.css('span.dc381b54::text').get(),
                'currency': property_card.css('span._06f65f02::text').get(),
                'type': property_card.css('span[aria-label="Type"]::text').get(),
                'beds': property_card.css('span[aria-label="Beds"]::text').get(),
                'baths': property_card.css('span[aria-label="Baths"]::text').get(),
                'area': property_card.css('h4.cfac7e1b._85ddb82f::text').get(),
                'location': property_card.css('h3._4402bd70::text').get(),
                'down_payment': property_card.css('span._41163454::text').getall()[-1].strip() if property_card.css('span._41163454::text').getall() else None,
                'plan_type': property_card.css('div._08c46d28 div._85a67160::text').get(),
            }
            # Append the extracted details to the list
            self.real_estate_data.append(property_details)
            yield property_details
        # Extract the link to the "Next" page and follow it
        next_page = response.css('a[title="Next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    def closed(self, reason):
        # Save data to a JSON file when scraping is complete
        with open('real_estate_data_bayut_full.json', 'w', encoding='utf-8') as f:
            json.dump(self.real_estate_data, f, ensure_ascii=False, indent=4)