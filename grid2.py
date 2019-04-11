row0=["O","X","X","X"]
row1=["X","X","X","X"]
row2=["X","X","X","X"]
row3=["X","X","X","X"]
row4=["X","X","X","X"]
row5=["X","X","X","X"]
columns=[row0,row1,row2,row3,row4,row5]

def print_columns():
    for each in columns:
        print("")
        for eachitem in each:
            print("{0:>20}".format(eachitem),end=" ")
    print("")

def main():    
    choice = "y"
    rowChoice=0
    columnChoice=0
    while choice == "y":
        row=int(input("Please select your character row: (1,2,3,4,5,6) : "))
        column=int(input("Please select your character column: (1,2,3,4) : "))
        row-=1
        column-=1
        columns[rowChoice][columnChoice]="X"
        columns[row][column]="O"
        rowChoice=row
        columnChoice=column
        print_columns()
        choice=input("\nMove again? (y/n): ")

print_columns()
print("")
main()


