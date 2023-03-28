print("Welcome to the Generic Finance App!")##printing welcome 

reportDict = {}#initializing dictionary

def print_report(sector, price, recommendation = None):#print report methods takes sector price and optional recommendation
    if recommendation != None:#if there is a rec
        if price > 0:#if positive
            print("Sector: %s | Marketprice: +%.4s | Recommendation: %s"%(sector, price, recommendation))#print all of the parameters for users
        else: #if negative print neg sign (already included in number)
            print("Sector: %s | Marketprice: %.4s | Recommendation: %s"%(sector, price, recommendation))
    else:#else print parameters wihout rec for the users 
        if price > 0: #if positive
            print("Sector: %s | Marketprice: +%.4s"%((sector, price)))
        else: #else (negitave) print neg sign
            print("Sector: %s | Marketprice: %.4s"%((sector, price)))

def make_float(input): ##make float function that adds all prices in list to be added 
    if input[0] == "+": ##if the first index is positive (ie change is positive)
        input = input.lstrip("+")##get rid of first index so can convert to float 
        input = float(input)#make float
        posList.append(input)#append to positive number list
    elif input[0] == "-": ##do same but add all negative prices to its own negative list 
        input = input.lstrip("-")
        input = float(input)
        negList.append(input)

fromUser = -1
while True: ##infinite loop
    print("Enter '1' to see how many sectors there are.")##printing menu

    fromUser = input("Enter any other input to quit ")##getting input from user 

    negList = []
    posList = []##defining variables and lists to be used later 
    

    if fromUser == "1": ##if user wants to see sectors 
        compLists = []#define lists and directories needed 
        sectorList = []
        exchangeList = []
        company_dict = {}

        f1 = open("companyList-rev1.txt","r") # read mode
        content1=f1.readlines() # reads each line and returns list

        for line in content1:#read each line of the file
            temp=line.split() # split the string
            compLists.append(temp[0]) #appends each index of list to proper new list
            sectorList.append(temp[1])
            exchangeList.append(temp[2])                         
        f1.close()##close file 

        del compLists[0]
        del sectorList[0]##delete the first element of each list due to the edge case to get clean lists 
        del exchangeList[0]

        newSet = set()#create a new set 


        for values in range(len(sectorList)): #for each value in the sector list add the value to the new set
            newSet.add(sectorList[values])
    
    
        for i in range(len(sectorList)): #for each company 
            tup1 = (sectorList[i], exchangeList[i]) ##make a tuple of the sector and the price
            company_dict[compLists[i]] = tup1##add tup1 to the directory value with the company as the key


        print("There are %s sectors"%str(len(newSet)))#print the number of sectors to the user using the len function
    
        j = 1#j counter var 
    

        counterList = []#new list for counting what order the sectors are in 
        for i in newSet:#for each index of the set
            str(j)#make j a string so it can be printed 
            counterList.append(i)#add the sectors in the order that they are in the new set
            print(j, i, sep=": ")#print j and i with : separating them in a clearly formatted list
            int(j)#return j to an int
            j = j+1#increment j 
        print()#new line


        print('To exit the program, type "EXIT"')##get sector
        print('To print generated reports, type "REPORTS"')
        sector = input("Select a sector to see its companies and its current stock market status: ")

        counter = 0#declaring variables
        average = 0
        for i in range(len(counterList)): #for i in range of the counterList
            if str(i) == str(sector):#if the string of i is equal to the user input (order of list has order of set, so finds corresponding sector)
                sector = counterList[i-1]#print index -1 

        if sector  == "EXIT": ##if you want to exit, exit
            print("Exiting")
            break #break from loop
        elif sector == "Finance": #else if you want finance
            print("\nSelected Sector: Finance")#print
            for key,values in company_dict.items(): #going through company_dict
                if values[0] == "Finance": #if the first value in tuple is finance
                    print(key, "| stock:", values[1])#print the info to the user
                    make_float(values[1])#user make floar method to initialize the lists with the prices
                    counter = counter+1#add the counter to count the number of companies
            for i in range(len(posList)): #add all of the values from posList using a for loop to iterate 
                average = average + float(posList[i])
            for i in range(len(negList)): #subtract all the numbers from negList using for loop to access each index of the loop
                average = average - float(negList[i])
            average = average / counter#divide by counter to get the average 
            if average > 0:#if average is postive print positive sign for user with info 
                print("Average change of +%.4s"%str(average))
            if average < 0: # if average is negative print neg sign for user with info (sign already included in number)
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")#Asking user if the want to buy or sell
            if buysell == "Hold": #if they want to hold
                buysell = None #set var to None
            tup1 = (average, buysell) #then make a tuple with vars from before 
            reportDict[sector] = tup1#add to reportDict
            
       
        elif sector == "Conglomerate": #Same for conglomerate sector as finance sector
            print("\nSelected Sector: Conglomerate")
            for key,values in company_dict.items(): 
                if values[0] == "Conglomerate": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None 
            tup1 = (average, buysell) 
            reportDict[sector] = tup1
    
        elif sector == "Oil": 
            print("\nSelected Sector: Oil")#same for oil sector as finance sector
            for key,values in company_dict.items(): 
                if values[0] == "Oil": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None 
            tup1 = (average, buysell) 
            reportDict[sector] = tup1

        elif sector == "Retail": 
            print("\nSelected Sector: Retail")#same for retail sector
            for key,values in company_dict.items(): 
                if values[0] == "Retail": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None 
            tup1 = (average, buysell) 
            reportDict[sector] = tup1
    
        elif sector == "FMCG": 
            print("\nSelected Sector: FMCG")#same for FMCG Sector 
            for key,values in company_dict.items(): 
                if values[0] == "FMCG": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None 
            tup1 = (average, buysell) 
            reportDict[sector] = tup1
    
        elif sector == "Semiconductor": #Same for semiconductor sector 
            print("\nSelected Sector: Semiconductor")
            for key,values in company_dict.items(): 
                if values[0] == "Semiconductor": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))

            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None 
            tup1 = (average, buysell) 
            reportDict[sector] = tup1
            
    
        elif sector == "Defense": #same for defense sector
            print("\nSelected Sector: Defense")
            for key,values in company_dict.items(): 
                if values[0] == "Defense": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None 
            tup1 = (average, buysell) 
            reportDict[sector] = tup1

        elif sector == "Software": #Same for software sector 
            print("\nSelected Sector: Software")
            for key,values in company_dict.items(): 
                if values[0] == "Software": 
                    print(key, "| stock:", values[1])
                    make_float(values[1])
                    counter = counter+1
            for i in range(len(posList)): 
                average = average + float(posList[i])
            for i in range(len(negList)): 
                average = average - float(negList[i])
            average = average / counter
            if average > 0:
                print("Average change of +%.4s"%str(average))
            if average < 0: 
                print("Average change of %.4s"%str(average))
            buysell = input("Should they buy, sell, or hold?")
            if buysell == "Hold": 
                buysell = None
            tup1 = (average, buysell) 
            reportDict[sector] = tup1
        elif sector == "REPORTS": #if sector is equal to reports 
            print("Printing reports...")
            if str(reportDict.values()) == "dict_values([])": #if there are no values in dictionary
                    print("There are no reports to print")#print to user
            for keys, values in reportDict.items():  #for each index of the dictionary
                print_report(keys, values[0], values[1])#call print report function for each index to print to user
            i = input("Press enter to continue...")#will continue loop

    else: #else if user doesn't want to see the list 
        print("Exiting")#print exiting
        break #break loop

