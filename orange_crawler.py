from travelspider import TravelSpider

class OrangeCrawler(TravelSpider):
    """docstring for OrangeCrawler."""
    pass

def main():
    crawler = OrangeCrawler(base_url="http://www.orangetour.com.tw")
    
if __name__ == "__main__":
    main()
        