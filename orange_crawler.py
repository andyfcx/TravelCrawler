from travelspider import TravelSpider

class OrangeCrawler(TravelSpider):
    """docstring for OrangeCrawler."""
    def __init__(self, base_url):
        super(OrangeCrawler, self).__init__(self, base_url)
        self.source_site = 1

def main():
    crawler = OrangeCrawler(base_url="http://www.orangetour.com.tw")
    
if __name__ == "__main__":
    main()
        
