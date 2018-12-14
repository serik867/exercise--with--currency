def readcurrency(filename):
    currency = {}
    list1 = []
    list2 = []
    with open(filename , "r") as file_object:
        for line in file_object:
            list1.append(line.split())
            #currency.update({"symbol" : line.split()[0]})
        #print(list1)

        for i in list1:
            
        print(currency)



readcurrency("currency.txt")