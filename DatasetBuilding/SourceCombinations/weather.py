import csv


filename = "allCountyData1.csv"
fields = []
rows = []
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

filename = "conreport2019.csv"
rows_fin = []
with open(filename, 'r') as csvfile1:
    csvreader = csv.reader(csvfile1)
    r = 1
    for row in csvreader:
        for r in rows:
            query = str(r[1]) + " County, " + str(r[3])
            if(query==str(row[1])):
                new_row = r + row
                rows_fin.append(new_row)

    # for r in rows:
    #     query = str(r[1]) + " County, " + str(r[3])
    #     print(query)
    #     for row in csvreader:
    #         if (str(row[1])==query):
    #             print('Match!')
    #             rows_fin.append(row)

with open('data_weather1.csv', 'a+', newline='') as file:
    data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row_fin in rows_fin:
        data_writer.writerow(row_fin)




