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


    select(server)
    server.disconnect()


def shutdown_vm(server):
    datacenter = 'HUBCNSH'
    pathlist = server.get_registered_vms(datacenter = datacenter,advanced_filters={'runtime.powerState':['poweredOn', 'suspended']})
    total = 0

    for path in pathlist:
        total = total + 1
        print total, path.split('/')[1][:-4]

    print ("=" * 30)
    print ("Enter the hostname you would like to force shutdown")

    hostname=raw_input(">")
    vm_path = [path for path in pathlist if hostname in path]
    vm = server.get_vm_by_path(vm_path[0])
    vm.power_off()
    print ("Job done!")

def start_vm(server):
    datacenter = 'HUBCNSH'
    pathlist = server.get_registered_vms(datacenter = datacenter,advanced_filters={'runtime.powerState':['poweredOff']})
    total = 0
    print ("Here are the machines are off.")

    for path in pathlist:
        total = total + 1
        print total, path.split('/')[1][:-4]

    print("=" * 30)
    print ("Enter the hostname server you would like to bring it up")
    hostname=raw_input(">")
    vm_path = [path for path in pathlist if hostname in path]
    vm = server.get_vm_by_path(vm_path[0])
    vm.power_on()
    print ("Job done!")

def reset_vm(server):
    datacenter = 'HUBCNSH'
    pathlist = server.get_registered_vms(datacenter = datacenter,advanced_filters={'runtime.powerState':['poweredOn', 'suspended']})
    total = 0

    for path in pathlist:
        total = total + 1
        print total, path.split('/')[1][:-4]

    print ("=" * 30)
    print ("Enter the hostname you would like to force shutdown")

    hostname=raw_input(">")
    vm_path = [path for path in pathlist if hostname in path]
    vm = server.get_vm_by_path(vm_path[0])
    vm.reset()
    print ("Job done!")

def select(server):
    #get_vm(server)
    print ("what kind of methods you want to approach mode(start/shutdown/reset)")

    answer = raw_input(">")
    if answer == "start":
        start_vm(server)
    elif answer == "reset":
        reset_vm(server)
    elif answer == "shutdown":
        shutdown_vm(server)
    else:
        print ("We don't know what your enter is")
        sys.exit(1)


if __name__ == "__main__":
    main()



