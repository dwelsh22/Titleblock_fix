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
newScr.write("filedia 0\n")
for drawing in DrawingList:
    newScr.write("open " + drawing["Project_Number"] + "-" + drawing["Drawing_Number"] + ".dwg\n")
    for key, value in drawing.items():
        newScr.write("-EDITBLOCKATTRIBUTE\n\n") 
        newScr.write("TitleInfo\n" + key +
                "\n\n54,1.6\n54,2\n54,2.5\n54,3.1\n54,3.6\n54,4\n61,1.8\n62.5,1.8\n\nV\nR\n" + value + "\n\n") 
    newScr.write("close\nyes\n")
