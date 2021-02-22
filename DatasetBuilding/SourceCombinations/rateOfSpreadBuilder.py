import csv

FILE_NAME = 'usCountiesDateNormalized.csv'
NEW_FILE_NAME = 'AverageRateOfSpreadByUSCounty.csv'

with open(FILE_NAME) as csv_file:
	with open(NEW_FILE_NAME, mode='w') as new_csv_file:
		CSV_READER = csv.reader(csv_file, delimiter=',')
		CSV_WRITER = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		LINE_COUNT = 0
		prev = "temp"
		startDate = 0
		testCount = 0
		previousRow = []
		for row in CSV_READER:
			newRow = []
			if LINE_COUNT == 0:
				print 'header row'
				newRow.append("daysSinceInfection1")
				newRow.append(row[1])
				newRow.append(row[2])
				newRow.append(row[4])
				newRow.append(row[5])
				newRow.append("avg rate of infection")
				newRow.append("avg rate of death")
				CSV_WRITER.writerow(newRow)
				LINE_COUNT += 1
			else:
				if row[1] != prev:
					if LINE_COUNT >= 2:
						totalDays = (int(previousRow[0]) - startDate) + 1.0
						if totalDays >= 25: #Only include counties that have been infected for at least 25 days
							if int(previousRow[4]) >= 50: #only include counties with more than 50 infections
								avgRateOfInfect = float(previousRow[4])/totalDays
								avgRateOfDeath = float(previousRow[5])/totalDays
								newRow.append(totalDays)
								newRow.append(previousRow[1])
								newRow.append(previousRow[2])
								newRow.append(previousRow[4])
								newRow.append(previousRow[5])
								newRow.append(avgRateOfInfect)
								newRow.append(avgRateOfDeath)
								CSV_WRITER.writerow(newRow)

					startDate = int(row[0])
				prev = row[1]
				LINE_COUNT += 1
			previousRow = row
print 'Processed {} lines'.format(LINE_COUNT)
