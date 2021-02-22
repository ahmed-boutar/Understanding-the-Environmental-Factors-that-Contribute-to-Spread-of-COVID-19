#Script to Normalize the dates on the counties data set
#Day 1 is January 1st
#Every other day is the number of days between January 1st and that day

import csv

FILE_NAME = 'us-counties.csv'
NEW_FILE_NAME = 'usCountiesDateNormalized.csv'

with open(FILE_NAME) as csv_file:
	with open(NEW_FILE_NAME, mode='w') as new_csv_file:
		CSV_READER = csv.reader(csv_file, delimiter=',')
		CSV_WRITER = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		LINE_COUNT = 0
		for row in CSV_READER:
			if LINE_COUNT == 0:
				print 'header row'
				CSV_WRITER.writerow(row)
				LINE_COUNT += 1
			else:
				date = row[0]
				numerical = date.split('/')
				value = int(numerical[1])
				month = int(numerical[0])
				if month == 2: #February
					value += 31
				elif month == 3: #March
					value += 29
					value += 31
				elif month == 4: #April
					value += 31
					value += 29
					value += 31
				elif month == 5: #May
					value += 30
					value += 31
					value += 29
					value += 31
				elif month != 1:
					print "Erroneus Month Detected"
				row[0] = value
				LINE_COUNT += 1
				CSV_WRITER.writerow(row)

print 'Processed {} lines'.format(LINE_COUNT)
