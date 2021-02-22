import csv

FILE_NAME = 'AverageRateOfSpreadByUSCounty.csv'
NEW_FILE_NAME = 'allCountyData.csv'

POPULATION_FILE = 'co-est2019-alldata.csv'

countyDictionary = {}

with open(POPULATION_FILE) as population_file:
	CSV_READER = csv.reader(population_file, delimiter=',')
	LINE_COUNT = 0
	for row in CSV_READER:
		if LINE_COUNT == 0:
			LINE_COUNT += 1
		else:
			fullName = row[6] + row[5] #This is because there are counties same name in dif states
			countyDictionary[fullName] = row[18]
			LINE_COUNT += 1
print 'Processed {} lines'.format(LINE_COUNT)

with open(FILE_NAME) as csv_file:
	with open(NEW_FILE_NAME, mode='w') as new_csv_file:
		CSV_READER = csv.reader(csv_file, delimiter=',')
		CSV_WRITER = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		LINE_COUNT = 0
		for row in CSV_READER:
			if LINE_COUNT == 0:
				row.append("population")
				CSV_WRITER.writerow(row)
			else:
				fullName2 = row[1] + row[2]
				if fullName2 not in countyDictionary:
					print '{} Not found in Population Dataset'.format(fullName2)
				else:
					row.append(countyDictionary[fullName2])
					CSV_WRITER.writerow(row)
			LINE_COUNT += 1
print 'Processed {} lines'.format(LINE_COUNT)
