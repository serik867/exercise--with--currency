def readcurrency(filename):
    currency = {}
    list1, list2 = [], []
    with open(filename , "r") as file_object:
        for line in file_object:
            list1 = line.split()
            currency = {"symbol": list1[0] , "rate": float(list1[1])}
            list2.append(currency)
        print(*list2, sep = "\n")

readcurrency("currency.txt")