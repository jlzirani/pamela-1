import sh
from netaddr import *
import zmq, time, json

INTERFACE = 'en0'

def prescan():
    '''Function to execute before dumping mac adresses
    eg : nmap or broadcast ping'''
    pass

def postscan(macs):
    '''Function to execute after dumping mac adresses
    eg : clean unwanted mac adresses fo hiding routers and switches
    or fix encoding glitches'''
    newmacs = {}
    for mac in macs:
        try:
            EUI(mac)
            IPAddress(macs[mac])
            newmacs[mac] = macs[mac]
        except:
            pass
    return newmacs

def scan(pre=False):
    '''Dump mac adresses and ips.
    Returns a dict {mac:ip,...}'''
    if pre:
        prescan()
    return postscan(arp_dump())

def arp_dump():
    '''[Internal] Uses arp -a to dump mac adresses
    Returns a dict {mac:ip,...}'''
    with sh.sudo(k=True, _with=True):
        dump = sh.arp('-a')
    lines = dump.strip().split('\n')
    ret = {}
    for line in lines:
        split = line.strip().split(' ')
        ip = split[1][1:-1]
        mac = split[3]
        if split[4] == 'on':
            iface = split[5]
        else:
            iface = split[6]
        if iface == INTERFACE:
            ret[mac] = ip
    return ret


def arp_scan_dump():
    '''[Internal] Uses arp-scan to dump mac adresses
    Returns a dict {mac:ip,...}'''
    raise NotImplementedError
    arp_scan("-l", "-I", INTERFACE)

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5000")
    while True:
        socket.send(json.dumps(scan()))
        print "Sending dict"
        msg_in = socket.recv()
        print msg_in
        time.sleep(10)

if __name__ == '__main__':
    main()
