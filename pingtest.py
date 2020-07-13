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
        if "IP" in Server.keys():
            Ip = Server["IP"].split("-")
            IpAddress = []
            if len(Ip) == 2:
                IpOctetsFirst = Ip[0].split(".")
                if len(IpOctetsFirst) < 4:
                    break
                lastdigitinipfirst = IpOctetsFirst[3]
                lastipaddrlastdigit = Ip[1]
                for Digit1 in range(int(lastdigitinipfirst),int(lastipaddrlastdigit)):
                    IpAddrTmp = "%s.%s.%s.%d"%(IpOctetsFirst[0],IpOctetsFirst[1],IpOctetsFirst[2],Digit1)
                    IpAddress.append(IpAddrTmp)

            else:
                IpAddress.append(Server["IP"])

            print(IpAddress)


            for IpAddressEach in IpAddress:
                response = ping(IpAddressEach)
                Reach = "Err"
                if response.success():
                    Reach = "Ok"
                    ServerString = Server["Name"]+" "+ IpAddressEach + " " + Reach + "\n"
                    print(ServerString)
                    f.write(ServerString)
                else:
                    Reach = "Error"
                    ServerString = Server["Name"] + " " + IpAddressEach + " " + Reach + "\n"
                    f.write(ServerString)
                    print(ServerString)
