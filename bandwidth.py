import psutil, time

def sendBandwidth():
    oldValue = 0
    while True:
        network = psutil.net_io_counters(pernic=True)
        newValue = network['lo'].bytes_sent + network['lo'].bytes_recv

        if oldValue:
            return convertToBits(newValue)
            
        oldValue = newValue
        return convertToBits(oldValue)

def convertToBits(number):
        if number > 1024*1024*1024:
            number = number/(1024*1024*1024)*8
            number = str(number) + ' GBites'
        elif number > 1024*1024:
            number = number/(1024*1024)*8
            number = str(number) + ' MBites'
        elif number > 1024:
            number = number/1024*8
            number = str(number) + ' KBites'
        else:
            number = str(number) + ' Bites'
        return number

def sendStat(value):
    print(convertToBits(value))