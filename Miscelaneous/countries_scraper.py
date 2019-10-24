import scrapy
import csv
import os
import re

class CountriesSpider(scrapy.Spider):
    try:
        os.remove('countries.csv')
    except:
        pass

    name = 'countries'
    allowed_domains = ['developers.google.com']
    start_urls = [
        'https://developers.google.com/public-data/docs/canonical/countries_csv'
    ]

    def parse(self, response):
        rows = response.css('div.devsite-article-body').css('table').css('tr')[1:]
        with open('countries.csv', 'a+', encoding='utf16', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter='\t')
            for row in rows:
                country_info = []
                columns = row.css('td::text')
                if len(columns) == 4:
                    country = columns[0].get()
                    lat = columns[1].get()
                    long = columns[2].get()
                    name = columns[3].get()
                    country_info.append(name)
                    country_info.append(country)
                    country_info.append(lat)
                    country_info.append(long)
                    print("Name: " + name)
                    print("Prefix: " + country)
                    print("Lat: " + lat)
                    print("Long: " + long)
                    csv_writer.writerow(country_info)



