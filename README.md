# TravelCrawler

### 資料庫設計
需要建立搜尋的key有網站左側的篩選內容，
例如：出發日期、目的地分類、價格、天數、出發機場、行程特色、景點特色、季節性、會員獨享、旅行社優惠、主要航班、旅遊型態、航班總結、航班去程、出發星期、車程偏好、指定景點。

##### 額外的表：
- 使用者評價需要另外建一個表，該表的評價平均之後作為一個FK關聯
- 航班也需要另外建立一個表，以FK做關連式查詢
- 促銷贈品


### 檔案說明
- travelspider.py 為爬蟲核心程式，仿照scrapy架構寫成
- gloriacrawler.py 為華泰旅遊爬蟲程式
- newmagzine.py 為新魅力旅遊網爬蟲程式
- orange.py 為橙果旅遊爬蟲程式

### MySQL欄位說明
- name : 旅遊產品名稱
- code : 旅遊產品的行程號
- start_date : 旅遊團起始日期
- weekday : 出發星期
- start_airport : 起飛機場
- duration : 天數
- url : 旅遊產品單頁的網址
- total : 總團位
- avaliable : 可售位
- price : 價錢
- comment : 旅行社附註
- flight : 此行程中的飛行航班
- source_site : 爬自旅行社網站
