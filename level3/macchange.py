import subprocess

def change_mac_address(interface,mac):
 
    subprocess.call(['sudo','ifconfig',interface,'down'])
    subprocess.call(['sudo','ifconfig',interface,'hw','ether',mac])
    subprocess.call(['sudo','ifconfig',interface,'up'])

def main():
    interface = str(input("enter Interface to change Mac Address to:"))
    new_mac_address = input('Enter the mac address to change to')

    before_change = subprocess.check_output(['ifconfig',interface])
    change_mac_address(interface,new_mac_address)
    after_change = subprocess.check_output(['ifconfig',interface])

    if before_change==after_change:
        print('Failed to change the Mac address to',new_mac_address)
    else:
        print('Mac Address Changed to',new_mac_address,'on Interface',interface)
main()

