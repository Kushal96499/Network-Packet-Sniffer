#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, UDP, ICMP
from rich.console import Console
from rich.table import Table
from rich import print
import datetime

console = Console()

def banner():
    console.print(r"""
███╗   ██╗███████╗██╗    ██╗███████╗██████╗ ███████╗
████╗  ██║██╔════╝██║    ██║██╔════╝██╔══██╗██╔════╝
██╔██╗ ██║█████╗  ██║ █╗ ██║█████╗  ██████╔╝███████╗
██║╚██╗██║██╔══╝  ██║███╗██║██╔══╝  ██╔═══╝ ╚════██║
██║ ╚████║███████╗╚███╔███╔╝███████╗██║     ███████║
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝     ╚══════╝
     [bold green]Advanced Packet Sniffer by Kushal Kumawat[/bold green]
    """, style="bold cyan")

def packet_handler(packet):
    time = datetime.datetime.now().strftime('%H:%M:%S')
    proto = 'Unknown'

    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if TCP in packet:
            proto = 'TCP'
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            proto = 'UDP'
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        elif ICMP in packet:
            proto = 'ICMP'
            sport = '-'
            dport = '-'
        else:
            sport = dport = '-'

        console.print(f"[bold yellow]{time}[/bold yellow] | [bold green]{proto}[/bold green] | "
                      f"[blue]{ip_src}:{sport}[/blue] -> [red]{ip_dst}:{dport}[/red]")

    else:
        console.print("[gray]Non-IP Packet Captured[/gray]")

def main():
    banner()
    console.print("\n[bold magenta]Sniffing started... Press CTRL+C to stop[/bold magenta]\n")
    sniff(prn=packet_handler, store=0)

if __name__ == "__main__":
    main()
