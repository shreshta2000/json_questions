import json
filename = 'employess_details.txt'
mydict = {} 
list1 = ["name","designation","age","salary"]
with open(filename) as details: 
    for line in details:

        # for words in line:
            # print(words)
        # key = line.strip().split(None,1)
        print(line)
        # print(key)
        # for i in line: 

        # print(key)
        # for i in description:
            # for j in i:
                # print([i][j])
        # i = 0
        # while i < len(list1):
        #     print(list1[i])
            # i = i + 1
        #     j=0
        #     while j in (description[i]):

        #     # print(i,line[i])
        #         print(description[i][j])
        #         j= j + 1
            # i = i + 1
            # description = list( line.strip().split(None, 4))
        # mydict[list1[line]] = value
        # print(value)
# print(mydict)