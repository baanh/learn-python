'''
Created on Feb 22, 2019

@author: Luke Nguyen
The program produces an order summary from the list containing data of order quantities at different timestamps.
The program takes item type, length of interval, and starting date as input. Then, it will print out the number
of purchases of the selected item type for 7 days starting from the chosen day of Jan, 2019.
'''
import orderlog
import datetime
ORDERS = orderlog.orderlst

'''
The method helps convert minute into HH:mm format
'''
def toHour(minute):
    h = minute // 60
    m = minute % 60
    return str(h) + ':' + str(m).zfill(2)

'''
The method helps convert HH:mm into minute,
the SECOND is skipped because in this case orders at 6:59:30 are still
counted to the summary of interval 6:00 - 6:59
'''
def toMinute(time): # skip the second
    partitions = time.split(':')
    return int(partitions[0]) * 60 + int(partitions[1])

'''
The method should create and return a two-dimensional list [[interval 1 summary][interval 2 summary]...] 
representing the order summary matrix. The length of each row equals to the number of days.
'''
def composeOrderMatrix(startDay, itemType, openingTime, closingTime, intervalMin):
    # Count the number of intervals
    intervalCount = (closingTime - openingTime) * 60 // intervalMin
    # Use variables startMin and endMin to store interval start and interval end
    startMin = openingTime * 60
    endMin = startMin + intervalMin - 1
    orderCount = 0
    orderCounts = []
    orderMatrix = []
    
    for i in range(0, intervalCount):
        # Calculate the number of orders in the timeframe
        for d in range(startDay, startDay + 7):
            for row in ORDERS:
                if (row[0] == str(d)):
                    time = row[1] # 23:59:03
                    if startMin <= toMinute(time) <= endMin:
                        orderCount += row[4 + itemType]
            orderCounts.append(orderCount)
            orderCount = 0
        orderMatrix.append(orderCounts.copy())
        orderCounts.clear()
        orderCount = 0
        startMin = endMin + 1
        endMin = startMin + intervalMin - 1
    return orderMatrix

'''
The method produces a string label shown in the leftmost column of the
output in the form of STARTTIME - ENDTIME
'''
def labelString(intervalNum, openingTime, intervalMin):
    startMin = openingTime * 60 + intervalMin * intervalNum
    endMin = startMin + intervalMin - 1
    return str(toHour(startMin)) + ' - ' + str(toHour(endMin))

'''
The method should display the content of the matrix with the format as shown
'''
def printWeek(orderMatrix, openingTime, closingTime, intervalMin, startDay):
    dayNames = []
    for i in range(0, 7):
        day = datetime.date(2019, 1, startDay + i)
        dayNames.append(day.strftime('%a'))
    title = 'TIME \ DAY    ' + ' '.join(dayNames)
    print(title.rjust(45, ' '))
    print('-' * 46)
    for i in range(0, len(orderMatrix)):
        intervalSummary = labelString(i, openingTime, intervalMin) + ' |   ' + '   '.join(str(x) for x in orderMatrix[i])
        print(intervalSummary.rjust(45, ' '))
    print('Bye!')

def main():
    itemTypes = ORDERS[0][4:]
    itemTypeCount = len(itemTypes)
    # Initialize variables
    OPENING_TIME = 6
    CLOSING_TIME = 24
    itemTypeIndex = -1
    startDay = -1
    
    print('This program presents a weekly purchase summary.')
    
    while itemTypeIndex not in range(0, itemTypeCount):
        print('Enter code to select item type:')
        itemTypeIndex = eval(input(' '.join([str(i) + '(' + itemTypes[i] + ')' for i in range(0, itemTypeCount)]) + ': '))
        
    intervalMin = eval(input('Enter the time interval in minutes: '))
    
    while (startDay not in range(1, 26)):
        startDay = eval(input('Please enter a stating date (between 1 and 25): '))
        
    startDate = datetime.date(2019, 1, startDay)
    
    print('\nDisplaying number of purchases of ', itemTypes[itemTypeIndex], ' for 7 days starting on ', \
          startDate.strftime('%A'), ', ', startDate.strftime('%b'), ' ', startDate.day, ' ', startDate.year, '\n', sep='')
    
    orderMatrix = composeOrderMatrix(startDate.day, itemTypeIndex, OPENING_TIME, CLOSING_TIME, intervalMin)
    printWeek(orderMatrix, OPENING_TIME, CLOSING_TIME, intervalMin, startDate.day)

main()
    
