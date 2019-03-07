from travelspider import TravelSpider

class NewmagzineCrawler(TravelSpider):
    """docstring for NewmagzineCrawler."""
    pass

def main():
    crawler = NewmagzineCrawler(base_url="https://www.newamazing.com.tw")
    
if __name__ == "__main__":
    main()
        