from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

class csvtolist:

    def __init__(self, filename):
         self.filename = filename
         self.arr = []

    def read_csv(self):
        # csv file reader
        with open(self.filename,'r') as csv_file:
            csv_reader = csv.reader(csv_file)

        # appends every line read by the reader into an array (arr)
            for line in csv_reader:
                self.arr.append(line)

    def get_data(self):
        return self.arr

def list_to_csv(data_list, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["NAME"])
        for data in data_list:
            csv_writer.writerow([data])
url_to_scrape = "https://www.britannica.com/topic/list-of-countries-1993160"

req = Request(
    url= url_to_scrape, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
request_page = urlopen(req)

page_html = request_page.read()

request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')
print(type(html_soup))
f = []

for k in html_soup.find_all("ul", class_="topic-list"):
    for z in k.find_all("a", class_ = "md-crosslink"):
        f.append(z.get_text())
    

print(f)
list_to_csv(f, "countries.csv")

filename = "countries.csv"
csv_processor = csvtolist(filename)
csv_processor.read_csv()
result = csv_processor.get_data()
print(result)