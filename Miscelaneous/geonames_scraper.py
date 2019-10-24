import scrapy

class GeoNameSpider(scrapy.Spider):
    name = 'geoname'
    allowed_domains = ['geonames.org']
    start_urls = [
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=0&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=500&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=1000&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=1500&maxRows=500',
        'http://www.geonames.org/advanced-search.html?q=populated+place%2C+cities15000&country=US&featureClass=P&continentCode=NA&startRow=0&maxRows=500'
    ]

    def parse(self, response):
        rows = response.css('table.restable')[1].css('tr')[2:]
        for row in rows:
            columns = row.css('td')
            latnlong = row.css('td::text')
            if len(columns) == 6 and len(latnlong) == 8:
                print("Name: " + str(columns[1].css('a::text')[0].get()))
                print("Country: " + str(columns[2].css('a::text')[0].get()))
                print("Lat: " + str(latnlong[6].get()))
                print("Long: " + str(latnlong[7].get()))