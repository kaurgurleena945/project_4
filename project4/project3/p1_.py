print("Welcome to the Generic Finance App!")

fromUser = -1
while True: #always true loop to print
    print("Enter '1' to see how many sectors there are.")#print info and menu to the user

    fromUser = input("Enter any other input to quit ")#get user input

    if fromUser == "1": #if user wants to see 
        compLists = []#lists needed 
        sectorList = []

        f1 = open("companyList-rev1.txt","r") # read mode
        content1=f1.readlines() # reads each line and returns list

        for line in content1:
            temp=line.split() # split the string
            compLists.append(temp[0]) #appends each index of list to proper new list
            sectorList.append(temp[1])
    
      
                           
        f1.close()##close file 

        del compLists[0]
        del sectorList[0]#delete the first index from both the lists as an edge case 

        newSet = set()#make a new set 

        for i in range(len(sectorList)): #add each index in sectorList to the New Set
            newSet.add(sectorList[i])
        j = 1#make counter var j 

        print("There are %s sectors"%str(len(newSet)))#print the length of the set found with the len function

        for i in newSet:#for each index in the set
            str(j)#make j a string
            print(j, i, sep=": ")#print with : separating 
            int(j)#turn back into int 
            j = j+1#iterate 
        i = input("Press enter to continue...")#User can press enter to continue
    elif fromUser != 0: #else exit and print for user 
        print("Exiting")
        break#breaking loop

##LIST OF THINGS NEEDED 