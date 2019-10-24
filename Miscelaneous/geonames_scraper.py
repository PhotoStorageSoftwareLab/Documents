import scrapy
import csv
import os
import re

class GeoNameSpider(scrapy.Spider):
    try:
        os.remove('coords.csv')
    except:
        pass

    name = 'geoname'
    allowed_domains = ['geonames.org']
    start_urls = [
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=0&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=500&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=1000&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=1500&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=2000&maxRows=500'
    ]

    def parse(self, response):
        rows = response.css('table.restable')[1].css('tr')[2:]
        with open('coords.csv', 'a+', encoding='utf16', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter='\t')
            for row in rows:
                columns = row.css('td')
                latnlong = row.css('td::text')
                if len(columns) == 6 and len(latnlong) == 8:
                    country_list = []

                    #print("Name: " + str(columns[1].css('a::text')[0].get()))
                    country_list.append(str(columns[1].css('a::text')[0].get()))

                    #print("State: " + str(latnlong[2].get())[2:])
                    country_list.append(str(latnlong[2].get())[2:])

                    #print("Country: " + str(columns[2].css('a::text')[0].get()))
                    country_list.append(str(columns[2].css('a::text')[0].get()))

                    #print("Lat: " + str(latnlong[6].get()))
                    lat = str(latnlong[6].get())
                    m = re.match("(.+) (.+)° (.+)' (.+)''", lat)
                    dir = m.group(1)
                    deg = m.group(2)
                    min = m.group(3)
                    sec = m.group(4)
                    country_list.append(dir)
                    country_list.append(deg)
                    country_list.append(min)
                    country_list.append(sec)

                    #print("Long: " + str(latnlong[7].get()))
                    long = str(latnlong[7].get())
                    m = re.match("(.+) (.+)° (.+)' (.+)''", long)
                    dir = m.group(1)
                    deg = m.group(2)
                    min = m.group(3)
                    sec = m.group(4)
                    country_list.append(dir)
                    country_list.append(deg)
                    country_list.append(min)
                    country_list.append(sec)

                    csv_writer.writerow(country_list)
                    country_list = []

