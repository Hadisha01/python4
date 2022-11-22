import datetime
d = datetime.datetime.fromtimestamp(4567888542).strftime("%m/%d/%Y %H:%M:%S")

print("convert unix timestamp string to readable date: ",d)