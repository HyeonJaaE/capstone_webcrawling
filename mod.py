import csv

fr = open('test.csv', 'r', encoding='utf-8')
tmp = list(csv.reader(fr))

rdr = tmp[1:]
fr.close()

fw = open("testresult.csv", 'w', encoding='utf-8', newline='')
wr = csv.writer(fw)

check = ['월','화','수','목','금','토','셀']
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
        if len(c) > 1:
            room += c[1].replace(")", "")
        sum += c[0]

    for i in range(len(sum)):
        if sum[i] in check:
            day += sum[i] + "-"
            if sum[i] == '셀':
                time += "0_0"
            else:
                idx = i + 1
                while True:
                    if sum[idx] in check:
                        tmp = sum[i+1: idx]
                        if tmp[len(tmp)-1] == ",":
                            tmp = tmp[0:-1]
                        print(tmp)
                        tmp = tmp.split(',')
                        time += tmp[0] + "_" + tmp[len(tmp)-1] +"-"
                        break
                    elif idx+1 == len(sum):
                        tmp = sum[i+1: idx+1]
                        if tmp[len(tmp)-1] == ",":
                            tmp = tmp[0:-1]
                        print(tmp)
                        tmp = tmp.split(',')
                        time += tmp[0] + "_" + tmp[len(tmp)-1] +"-"
                        break
                    idx = idx +1

    if day[len(day)-1] == "-":
        day = day[0:-1]

    if time[len(time)-1] == "-":
        time = time[0:-1]

    tmp = [line[1], line[3], line[4], int(float(line[5])),line[6], line[9], day, time, room, line[8].replace(",","_")]
    wr.writerow(tmp)

fw.close()
