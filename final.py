from bs4 import BeautifulSoup as bs
import requests
import csv
import os
"""------------------------------------------------------------------------------------------"""
URL = 'https://volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201'
CSV = 'benesov'
"""------------------------------------------------------------------------------------------"""


"""try URL and name of CSV from user"""
try:
    wrong_keys = "~ # % & * : < > ? / \ { | }."
    page = requests.get(URL)
    soup = bs(page.content, 'html.parser')
    for i in soup.find_all('td', {'class': 'cislo'}):
        link = i.find('a', href=True)
    if len(CSV) == 0 or any(c in wrong_keys for c in CSV):
        exit()
    if len(link) > 0:
        CSV = CSV + '_2017.csv'
        print("Vše je v pořádku, stahuji data.")
except:
    print("Zkontroluj správnost odkazu či jména CSV. Nesmí být zakázané znaky!) (~ # % & * : < > ? / \ { | }.)")
    exit()


""""get middle links and get cities, codes and parties for first row in csv"""
links = []
main_url = 'https://volby.cz/pls//ps2017nss/'
for i in soup.find_all('td', {'class': 'cislo'}): # get middle links and combine them with main_url
    link = i.find('a', href=True)
    links.append(main_url + link['href'])

cities, codes = [], []
for x in soup.find_all('td', class_='overflow_name'): # get cities and codes
    cities.append(x.text)
    for c in soup.find_all('td', {'class': 'cislo'}):
        code = c.find('a', href=True)
        codes.append(code.text)

parties = []
page = requests.get(links[0])
soup = bs(page.content, 'html.parser') # get from first middle link parties
soup.find_all('div', {'class': 't2_470'})
for party in soup.find_all('td', class_='overflow_name'):
    parties.append(party.text)


def up_to_1k(o): # Getting data from each "middle link", editing and save them to list named "done".
    up_k = "\xa0"
    m = o.text
    for character in up_k:
        m = m.replace(character, "")
        done.append(m)
        return done


def data(): # get registered, envelopes, correct envelopes and party votes
    o = soup.find('td', {'headers': 'sa2'})
    up_to_1k(o)
    o = soup.find('td', {'headers': 'sa3'})
    up_to_1k(o)
    o = soup.find('td', {'headers': 'sa6'})
    up_to_1k(o)
    for o in soup.find_all('td', {'headers': 't1sa2 t1sb3'}):
        up_to_1k(o)
    for o in soup.find_all('td', {'headers': 't2sa2 t2sb3'}):
        up_to_1k(o)


""""Fce to writes data to CSV"""
fw = ["kód", "město", "registrováno", "vydané obálky", "platné obálky"]
with open(CSV, "w", newline="", encoding="windows-1250") as csv_file:
    write = csv.writer(csv_file)
    write.writerow(fw+parties)

def write_to_csv():
    with open(CSV, "a", newline="", encoding="windows-1250") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(done)
        done.clear()

def final(): # Fce which opens directory of program (where is saved .cls)
    directory = os.getcwd()
    path = os.path.realpath(directory)
    if os.name == "Windows":
        os.startfile(path)
    else:
        os.system('xdg-open "%s"' % path)
    print("Data stáhnuty ve složce programu. ", CSV)


""""starting program"""
done = []
j = 0
for site in links:
    page = requests.get(site)
    soup = bs(page.content, 'html.parser')
    done.append(codes[j])
    done.append(cities[j])
    print("Stahuji", j+1, "z", len(cities), " ", cities[j])
    j = j + 1
    data()
    write_to_csv()
final()
