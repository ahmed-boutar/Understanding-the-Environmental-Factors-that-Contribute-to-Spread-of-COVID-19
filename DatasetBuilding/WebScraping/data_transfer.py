from selenium import webdriver
from bs4 import BeautifulSoup
import csv


def generate_links(filename):
    f = open("states.txt", encoding="utf-8")
    lines = []
    for line in f:
        new_line = line.lower().strip('\n').lower()
        lines.append(new_line)##.replace(' ', '-'))

    with open('links.txt', 'a+', newline='') as file:
        for l in lines:
            query = str('https://www.countyhealthrankings.org/app/' + l.replace(' ', '-') + '/2020/measure/factors/9/data')
            file.writelines(query.strip() + ' \n')
    return lines


filename = "allCountyData.csv"
fields = []
rows = []
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

lines = generate_links('states.txt')
f = open("links.txt", encoding="utf-8")
writer = csv.writer(csvfile)
l = 0
fin_rows = []
for link in f:
    state_url = link
    driver = webdriver.Chrome("/Users/ahmedboutar/Documents/chromedriver")
    driver.get(state_url)
    driver.implicitly_wait(300)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for row in rows:
        curr_state = str(lines[l].lower().strip())
        row_state = str(row[2].lower().strip())
        row_county = str(row[1]).lower().strip()
        perc_table = soup.find('table', attrs={'class': 'measure-data-table sticky-enabled'})
        if perc_table is None:
            print("Table not found for ", curr_state, " state!!")
            print("=====================================")
            continue
        if(row_state==curr_state):
            for tr in perc_table.tbody.findAll('tr'):
                county_name = tr.find('td', class_='name')
                percentage = tr.find('td', class_='raw_value')
                if(row_county==county_name.text.lower().strip()):
                    row[10] = percentage.text
                    fin_rows.append(row)
    l = l + 1
    driver.close()
with open('data.csv', 'a+', newline='') as file:
    data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row_fin in fin_rows:
        data_writer.writerow(row_fin)

        # if (str(row[2]).lower().strip() == curr_state):
        #     for a in soup.findAll('tr', attrs={'class':'ng-scope odd'}):
        #         for c in a.findAll('td', attrs={'class': 'raw_value'}):
        #             percentage = str(c.text)
        #             percentages_odd.append(percentage)
        #         for b in a.findAll('td', attrs={'class': 'name'}):
        #             county_name = str(b.text)
        #             dict_county.update({county_name: percentages_odd[i]})
        #             if str(county_name).lower().strip() == str(row[1]).lower().strip():
        #                 row[10] = percentages_odd[i]
        #                 fin_rows.append(row)
        #                 i = i + 1
        #
        #     for e in soup.findAll('tr', attrs={'class':'ng-scope even'}):
        #         for f in e.findAll('td', attrs={'class': 'raw_value'}):
        #             percentage = str(f.text)
        #             percentages_even.append(percentage)
        #         for g in e.findAll('td', attrs={'class': 'name'}):
        #             county_name = str(g.text)
        #             dict_county.update({county_name: percentages_even[j]})
        #             if str(county_name).lower().strip() == str(row[1]).lower().strip():
        #                 row[10] = percentages_even[j]
        #                 fin_rows.append(row)
        #                 j = j + 1;
    # l = l + 1
    # driver.close()

    # for key in dict_county:
    #     print(key)
    #     if (str(key).lower().strip() == str(row[1]).lower().strip()):
    #         row[10] = dict_county.get(key)
    #         fin_rows.append(row)
    # print(row)

# with open('data1.csv', 'a+', newline='') as file:
#     data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row_fin in fin_rows:
#         data_writer.writerow(row_fin)

            #     if (b is str(rows[1])):
            #         county_names.append(str(b))
            # for c in a.findAll('td', attrs={'class': 'raw_value'}):
            #     if(str(c) is in county_names):

# button = driver.find_element_by_id('shopping-selector-parent-process-modal-close-click')
# button.click()
# content = driver.page_source
# soup = BeautifulSoup(content, 'html.parser')
# for a in soup.findAll('div', attrs={'class': 'recipe-content-center'}):
#     name = a.find('h1', attrs={'class': 'recipe-name ng-binding'})
#     products.append(name.text)
#     for b in soup.findAll('div', attrs={'class': 'related-product-name-price'}):
#         for ingredient in b.find_all('button', attrs={'class': 'title ng-binding no-sponsor'}):
#             ingredients.append(ingredient.text)
#     with open('data.csv', 'a+', newline='') as file:
#         data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         data_writer.writerow([recipe_url, products, ingredients])
#     driver.close()
