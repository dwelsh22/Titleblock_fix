import csv
#Creates dictionary to store values in
DrawingList = []

with open('test.csv', "r", newline='' ) as csvfile:
    csvreader = csv.reader(csvfile, dialect='excel')
    headerlist = csvreader.__next__()
    for rows in csvreader:
        #print(rows)
        i = 0
        TitleNames = {}
        for item in rows:
            TitleNames[headerlist[i]] = item
            i += 1
        DrawingList.append(TitleNames)

print(DrawingList)

newScr = open("new_script_file.scr", "w")
for drawing in DrawingList:
    for key, value in drawing.items():
        newScr.write("Fix the parameter " + key + " to " + value + "\n")
    newScr.write("\n")
