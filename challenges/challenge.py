import datetime as dt

localTime = dt.datetime.now()


lonChange = dt.timedelta(hours=8)
nycChange = dt.timedelta(hours=3)

lon = localTime + lonChange
nyc = localTime + nycChange

openTime = localTime.replace(hour=9, minute=0, second=0,microsecond=0)
closeTime = localTime.replace(hour=17, minute=0, second=0, microsecond=0)


def checkOpen():
     if localTime > openTime and localTime < closeTime:
         print("In Portland, Oregon, it is currently: " + localTime.strftime("%X"))
         print("The Portland Office is currently open")
     elif localTime > closeTime:
         print("In Portland, Oregon, it is currently: " + localTime.strftime("%X"))
         print("The Portland Office is currently closed")

def checkNYCOpen():
    if nyc > openTime and localTime < closeTime:
        print("In New York City, New York, it is currently: " + nyc.strftime("%X"))
        print("The New York Office is currently open")
    elif nyc > closeTime:
        print("In New York City, New York, it is currently: " + nyc.strftime("%X"))
        print("The New York Office is currently closed")

def checkLONOpen():
    if lon > openTime and lon < closeTime:
        print("In London, England, it is currently: " + lon.strftime("%X"))
        print("The London Office is currently open")
    elif lon > closeTime:
        print("In London, England, it is currently: " + lon.strftime("%X"))
        print("The London Office is currently closed")


if __name__ == "__main__":
    checkOpen()
    print("\n")
    checkNYCOpen()
    print("\n")
    checkLONOpen()

