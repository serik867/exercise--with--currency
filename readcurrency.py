def readcurrency(filename):
    currency = {}
    list1 = []
    with open(filename , "r") as file_object:
        for line in file_object:
            list1 = line.split()
            currency.update({"symbol": list1[0] , "rate": float(list1[1])})
            print(currency)
           # for element in line:

            #print(line, end = "")



readcurrency("currency.txt")