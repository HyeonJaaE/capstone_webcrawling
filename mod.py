import csv

fr = open('test.csv', 'r', encoding='utf-8')
tmp = list(csv.reader(fr))

rdr = tmp[1:]
fr.close()

fw = open('항공우주공학과.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fw)

check = ['월','화','수','목','금']
for line in rdr:
    day = ""
    time = ""
    room = ""

    if line[7] == " ":
        continue

    a = line[7].split('/')
    sum = ""
    for b in a:
        c = b.split('(', maxsplit=1)
        room += c[1].replace(")", "")
        sum += c[0]

    sum = sum.replace(",","")
    sumList = list(sum)

    day += sumList[0]
    time += sumList[1]

    for i in range(2, len(sumList)):
        if sumList[i] in check:
            day += ("-" + sumList[i])
            time += ("_" + sumList[i-1])
            time += ("-" + sumList[i+1])
        if i == len(sumList)-1:
            time += ("_" + sumList[i])

    tmp = [line[1], line[3], line[4], int(float(line[5])),line[6], line[9], day, time, room, line[8]]
    wr.writerow(tmp)

fw.close()
