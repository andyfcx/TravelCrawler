from travelspider import TravelSpider

class GloriaCrawler(TravelSpider):
    """docstring for GloriaCrawler."""
    def __init__(self, base_url):
        super(GloriaCrawler, self).__init__(self, base_url)
        self.source_site = 3

def main():
    crawler = GloriaCrawler(base_url="https://www.gloriatour.com.tw")
    
if __name__ == "__main__":
    main()
        
