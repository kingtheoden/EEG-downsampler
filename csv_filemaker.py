from math import sin

f = open('csv_file.csv', 'w')

for x in range(100000): # 100,000
    f.write(str(x) + "," + str(sin(x)) + "\n")
f.close()
