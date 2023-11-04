import csv
with open("demo.csv","r") as demo:
    demoread=csv.reader(demo)
    next(demoread)
    #k=input("enter slno ")
    k=input("enter slno ")
    for i in demoread:
        if k in i:
            print(i)

