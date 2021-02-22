import csv

filename = "data_weather1.csv"
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