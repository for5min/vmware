from pysphere import VIServer
import sys

def main():

    if len(sys.argv) <> 3:
        print ("Usage:")
        print (sys.argv[0], "<username> <password")

    username = sys.argv[1]
    password = sys.argv[2]

    vcenter = "ecnshmw1001.sh.cn.ao.ericsson.se"


    server = VIServer()
    server.connect( vcenter, username, password )
    print ("Login .....")
    type = server.get_api_type()
    version = server.get_api_version()

    print ("You are now connecting with {0} with API version {1}".format(type, version))


if __name__ == "__main__":
    main()



