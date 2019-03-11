from travelspider import TravelSpider

class NewmagzineCrawler(TravelSpider):
    """docstring for NewmagzineCrawler."""
    def __init__(self, base_url):
        super(NewmagzineCrawler, self).__init__(self, base_url)
        self.source_site = 2

def main():
    crawler = NewmagzineCrawler(base_url="https://www.newamazing.com.tw")
    
if __name__ == "__main__":
    main()
        
