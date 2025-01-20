import scrapy
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import json
import re
from spiders.real_estate_spider import RealEstateSpiderBayut

# Configure logging for the Scrapy crawler
configure_logging()

# Create a CrawlerRunner instance
runner = CrawlerRunner()

# Define the crawling process using inlineCallbacks
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(RealEstateSpiderBayut)  # Run the spider
    reactor.stop()  # Stop the reactor after the spider completes

# Start the crawling process
crawl()
reactor.run()  # Keep the script running until the reactor stops
