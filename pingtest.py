from pythonping import ping
import csv
import datetime

if __name__ == '__main__':
    filename = "ipaddrs.txt"
    IPaddrs = []
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        for line in reader:
            IPaddrs.append(line)

    f = open('result.txt', 'a')
    CDate = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    StringZ = "Datetime: " + CDate + "\n"
    f.write(StringZ)
    for Server in IPaddrs:
        response = ping(Server["IP"])
        Reach = "Err"
        if response.success():
            Reach = "Ok"
            ServerString = Server["Name"]+" "+ Server["IP"] + " " + Reach + "\n"
            print(ServerString)
            f.write(ServerString)
        else:
            Reach = "Error"
            ServerString = Server["Name"] + " " + Server["IP"] + " " + Reach + "\n"
            f.write(ServerString)
            print(ServerString)


