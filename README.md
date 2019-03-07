# TravelCrawler

### 檔案說明
- travelspider.py 為爬蟲核心程式，仿照scrapy架構寫成
- gloriacrawler.py 為華泰旅遊爬蟲程式
- newmagzine.py 為新魅力旅遊網爬蟲程式
- orange.py 為橙果旅遊爬蟲程式

### MySQL欄位說明
- name : 旅遊產品名稱
- code : 旅遊產品的識別碼
- start_date : 旅遊團起始日期
- duration : 天數
- url : 旅遊產品單頁的網址
- total : 總團位
- avaliable : 可售位
- price : 價錢
- comment : 旅行社附註
- flight : 此行程中的飛行路線
- source_site : 爬自旅行社網站
