import csv

FILE_NAME = 'allCountyData2.csv'
NEW_FILE_NAME = 'allCountyData.csv'

POPULATION_FILE = 'tempAverages.csv'

countyDictionary = {}

with open(POPULATION_FILE) as population_file:
	CSV_READER = csv.reader(population_file, delimiter=',')
	LINE_COUNT = 0
	for row in CSV_READER:
		if LINE_COUNT == 0:
			LINE_COUNT += 1
		else:
			countyDictionary[row[0]] = row[1]
			LINE_COUNT += 1
print 'Processed {} lines'.format(LINE_COUNT)

with open(FILE_NAME) as csv_file:
	with open(NEW_FILE_NAME, mode='w') as new_csv_file:
		CSV_READER = csv.reader(csv_file, delimiter=',')
		CSV_WRITER = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		LINE_COUNT = 0
		for row in CSV_READER:
			if LINE_COUNT == 0:
				row.append("avgPrecip")
				CSV_WRITER.writerow(row)
			else:
				if row[2] not in countyDictionary:
					print '{} Not found in Population Dataset'.format(row[2])
				else:
					row.append(countyDictionary[row[2]])
					CSV_WRITER.writerow(row)
			LINE_COUNT += 1
print 'Processed {} lines'.format(LINE_COUNT)
