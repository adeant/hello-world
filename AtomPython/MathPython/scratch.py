#set up the table
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
#prepare colWidths
colWidths = [0] * len(tableData)

#loop over the lists in tableData
for index in range(len(tableData)):
    max = 0 #clear out max
    #loop over the values in each sub-list
    for index2 in tableData[index]:
        #find the legth
        length = len(index2)
        #determine new max
        if length > max: max = length
    #set the index position to the max length found
    colWidths[index] = max

#loop over the index positions
for i in range(0,len(tableData[0]),1):
    string = '' #clear out the string line
    #loop over each list in tableData
    for ii in range(len(tableData)):
        list = tableData[ii] #grab the list at this loop's position
        value = list[i] #grab the value of the sub-list
        #add the value to the string
        string = string + " " + value.rjust(colWidths[ii])
    #print out the string
    print(string)
#testing
