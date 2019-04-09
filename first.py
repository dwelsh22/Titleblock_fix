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
    newScr.write("open ~\" + drawing[Project_Number] + "-" + drawing[Drawing_Number] + ".dwg\n")
    newScr.write("-EDITBLOCKATTRIBUTE\n\n") 
    for key, value in drawing.items():
        newScr.write("TitleInfo\n*\n\n0,0\n300,50\n\nV\nR\n" + "dictionary key and value") 
        #newScr.write("Fix the parameter " + key + " to " + value + "\n")
    newScr.write("\nclose")
