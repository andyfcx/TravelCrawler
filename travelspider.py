# -*- coding: utf-8 -*-
import requests
import pymysql
import json
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql.expression import insert
from configparser import ConfigParser

config = ConfigParser()
config.read('./mysql_config.ini')
db_host = config.get('DB', 'host')
db_user = config.get('DB', 'user')
db_pwd = config.get('DB', 'password')
cookies = {
    'ASPSESSIONIDCCSTBTAR': 'FLEBEBNCMGILOCLPIHKKDFDE',
    '_gcl_au': '1.1.626925130.1551762831',
    '_ga': 'GA1.3.288686960.1551762831',
    '_fbp': 'fb.2.1551762831967.613430174',
    'ASPSESSIONIDCSSQSRRT': 'KKBMBCPDDFIEBFFBDBALLHDG',
    '_gid': 'GA1.3.1216805868.1551894114',
    '__lfcc': '1',
}

class TravelSpider():
    def __init__(self, base_url):
        self.base_url = base_url
        self.engine = create_engine(f"mysql://{db_user}:{db_pwd}@{db_host}", encoding='utf8')
        self.start_requests()

    def start_requests(self):
        for i in range(1, 4):
            headers = {
                'Pragma': 'no-cache',
                'Origin': self.base_url,
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept': '*/*',
                'Cache-Control': 'no-cache',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Referer': f'{self.base_url}/EW/GO/GroupList.asp'
            }

            data = {
                'displayType': 'G',
                'subCd': '',
                'orderCd': '1',
                'pageALL': i,
                'pageGO': '1',
                'pagePGO': '1',
                'waitData': 'false',
                'waitPage': 'false',
                'mGrupCd': '',
                'SrcCls': '',
                'tabList': '',
                'regmCd': '',
                'regsCd': '',
                'beginDt': '2019/03/07',
                'endDt': '2019/09/07',
                'portCd': '',
                'tdays': '',
                'bjt': '',
                'carr': '',
                'allowJoin': '1',
                'allowWait': '1',
                'ikeyword': ''
            }

            response = requests.post(f'{self.base_url}/EW/Services/SearchListData.asp',
                                     headers=headers,
                                     cookies=cookies,
                                     data=data)
            res = response.json()
            self.source_site = res['SiteTitle']
            self.json_data = res['All']
            self.parse()

    def parse(self):
        for item in self.json_data:
            Travel_item = {}
            Travel_item['name'] = item['GrupSnm']
            Travel_item['code'] = item['GrupCd']
            Travel_item['start_date'] = item['OrderDl']
            Travel_item['weekday'] = item['WeekDay']
            Travel_item['start_airport'] = item['PortNm']
            Travel_item['duration'] = item['GrupLn']
            Travel_item['url'] = item['ShareUrl']
            Travel_item['total'] = item['EstmYqt']
            Travel_item['avaliable'] = item['DoneYqt']
            Travel_item['price'] = item['SaleAm']
            Travel_item['comment'] = item['FullSts']
            Travel_item['flight'] = json.dumps(self.search_flight(Travel_item['code']))
            Travel_item['source_site'] = self.source_site

            self.pipeline(Travel_item)
            print(f"Done processing {Travel_item}\n")

    def search_flight(self, code):
        url = f'{self.base_url}/EW/Services/SearchFlight.asp?prodCd={code}&sacctNo=&flightType=1'
        res = requests.get(url)
        return res.json()

    def pipeline(self, travel_item):
        meta = MetaData(bind=self.engine)
        Travel = Table('Travel', meta, autoload=True)
        i = insert(Travel)
        self.engine.execute(i.values(travel_item))
        
# def main():
#     crawler=TravelSpider("http://www.orangetour.com.tw")

# if __name__ == "__main__":
#     main()
