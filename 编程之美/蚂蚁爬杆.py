# coding:utf-8

'''
蚂蚁爬杆问题\

'''

def calcTime(XPos,speed,stick_length):
    total_time = stick_length / float(speed)
    Max = Min =0
    for i in range(len(XPos)):

        if XPos[i]>stick_length/2.0:
            currentMax = XPos[i]/float(speed)
        else:
            currentMax = (stick_length-XPos[i])/float(speed)
        currentMin = total_time - currentMax
        if Max < currentMax:
            Max = currentMax
        if Min < currentMin:
            Min = currentMin
    return [Max,Min]


print(calcTime([3,7,20,50,66,77],2,100))