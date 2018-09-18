import csv

with open('time.csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['month']
    writer.writerow(header)
    for i in range(1,9):
        for j in range(1,13):
            if i==8 and j>9:
                break
            else:
                month_1='201{0}/{1:02d}'.format(i,j)
                writer.writerow([month_1])
                