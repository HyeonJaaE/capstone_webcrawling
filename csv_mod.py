import csv

title = "화학공학과"
fr = open(title + ".csv", 'r', encoding='utf-8')
tmp = csv.reader(fr)

fw = open(title + "2.csv", 'w', encoding='utf-8', newline='')
wr = csv.writer(fw)

for line in tmp:
    line[8] = line[8].replace(" ","_")
    wr.writerow(line)

fr.close()
fw.close()
