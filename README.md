# TravelCrawler

### 資料庫設計
需要建立搜尋的key有網站左側的篩選內容，
例如：出發日期、目的地分類、價格、天數、出發機場、行程特色、景點特色、季節性、會員獨享、旅行社優惠、主要航班、旅遊型態、航班總結、航班去程、出發星期、車程偏好、指定景點。

- 其中，出發日期、價格、天數、出發機場、去程、出發星期，已經在Travel表中建好

##### 額外的表：

- 目的地分類：需要欄位有id、地區、國家名稱、區域名稱（省、州、等）

- 使用者評價需要另外建一個表，該表的評價平均之後作為一個FK關聯
```
CREATE TABLE UserFeedback (
    ID int NOT NULL PRIMARY KEY auto_increment,
    `uid` varchar(255) NOT NULL references user(id),
    `agent` varchar(255) references agent(id),
    `product_purchased` int not null references Travel(ID),
    `date` datetime,
	  `travel_arrangement_score` int, 
    `guide_service_score` int,
    `eating_arrangement_score` int,
    `housing_arrangement_score` int ,
    `transportation_score` int,
    `star` int,
    `comment` text(255)
);
```
- 旅行社的資料
```
create table agent(
id int not null primary key auto_increment,
`name` varchar(255),
`address` varchar(255),
`tel` varchar(255),
`fax` varchar(255),
`email` varchar(255),
`representative` varchar(255)
);
```

- 航班也需要另外建立一個表，以FK做關連式查詢，本次只有將航班爬取下來，需要其他資訊才比較好整理成表

- 促銷贈品


### 檔案說明
- travelspider.py 為爬蟲核心程式，仿照scrapy架構寫成
- gloriacrawler.py 為華泰旅遊爬蟲程式
- newmagzine.py 為新魅力旅遊網爬蟲程式
- orange.py 為橙果旅遊爬蟲程式

### Travel欄位說明
目前將爬完的資料儲存在 Travel表當中
- id : Primary key auto increment
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
- source_site : 爬自旅行社網站（應使用FK關聯至agent表）
