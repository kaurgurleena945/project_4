print("Welcome to the Generic Finance App!")#prints welcome

fromUser = -1
while True: #always true loop
    print("Enter '1' to see how many sectors there are.")#print menu to user

    fromUser = input("Enter any other input to quit ")#gets value from user 
    if fromUser != "1": 
        print("Exiting")#else print exiting
        break#break loop
    if fromUser == "1": #if user prints 1 
        compLists = []
        sectorList = []#lists to be used later and the dictionary
        exchangeList = []
        company_dict = {}

        f1 = open("companyList-rev1.txt","r") # read mode
        content1=f1.readlines() # reads each line and returns list

        for line in content1:
            temp=line.split() # split the string
            compLists.append(temp[0]) #appends each index of list to proper new list
            sectorList.append(temp[1])
            exchangeList.append(temp[2])
    
      
                           
        f1.close()##close file 

        del compLists[0]
        del sectorList[0]#delete the first edge case from the lists
        del exchangeList[0]

    newSet = set()#make a new set


    for values in range(len(sectorList)): #read the values from sectorList and add them to set
        newSet.add(sectorList[values])
    
    
    for i in range(len(sectorList)): #interate through lists and make a tuple with relevant info, then add that tup to dict with company as key
        tup1 = (sectorList[i], exchangeList[i]) 
        company_dict[compLists[i]] = tup1


    print("There are %s sectors"%str(len(newSet)))#print the number of sectors using len function
    
    j = 1#set counter equal to 1 

    counterList = []#make a counterList
    for i in newSet:#iterate thru set
        str(j)#make j a string
        counterList.append(i)#add the i to counterList (to get order of the set)
        print(j, i, sep=": ")#print seperating by a :
        int(j)#return j to an int
        j = j+1#increment j


    useri = input('To exit the program, type "EXIT"\nSelect a sector to see its companies and its current stock market status: ')
    #exit program or select sector

    for i in range(len(counterList)): #for i in range of the counterList
        if str(i) == str(useri):#if the string of i is equal to the user input (order of list has order of set, so finds corresponding sector)
            useri = counterList[i-1]#print index -1 
    if useri == "EXIT": # if input is exit print exit
            print("Exiting")
            break#from loop
    elif useri == "Finance": #else if user says Finance
        print("\nSelected Sector: Finance")#print sector to user
        for key,values in company_dict.items(): #go thru dictionary items
            if values[0] == "Finance": #if the sector is finance
                print(key, "| stock:", values[1])#print out the key (company) and stock for user
        useri = input("Press enter to continue...")   #press enter to continue
    elif useri == "Conglomerate": #same as finance but with conglomerate
        print("\nSelected Sector: Conglomerate")
        for key,values in company_dict.items(): 
            if values[0] == "Conglomerate": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")
    elif useri == "Oil": #same but for oil
        print("\nSelected Sector: Oil")
        for key,values in company_dict.items(): 
            if values[0] == "Oil": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")
    elif useri == "Retail": #same but for retail
        print("\nSelected Sector: Retail")
        for key,values in company_dict.items(): 
            if values[0] == "Retail": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")
    elif useri == "FMCG": #same but for FMCG
        print("\nSelected Sector: FMCG")
        for key,values in company_dict.items(): 
            if values[0] == "FMCG": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")
    elif useri == "Semiconductor": #Same but for semiconductor
        print("\nSelected Sector: Semiconductor")
        for key,values in company_dict.items(): 
            if values[0] == "Semiconductor": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")
    elif useri == "Defense": #same for defense
        print("\nSelected Sector: Defense")
        for key,values in company_dict.items(): 
            if values[0] == "Defense": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")
    elif useri == "Software": #same for software
        print("\nSelected Sector: Software")
        for key,values in company_dict.items(): 
            if values[0] == "Software": 
                print(key, "| stock:", values[1])
        useri = input("Press enter to continue...")