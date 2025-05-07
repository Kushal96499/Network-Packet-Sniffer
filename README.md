# 📄 Advanced Network Packet Sniffer - README
COMPANY: CODEC TECHNOLOGIES INDIA

NAME: KUSHAL KUMAWAT

NCS ID: E19E86-0116588287923

DOMAIN: Cyber Security Intern

DURATION: 3 Months

MENTOR: Miss.Vaishali

---

## 🛡️ Project Title:

**Advanced Network Packet Sniffer**

## 👨‍💻 Developed by:

**Kushal Kumawat**

## 🎯 Objective:

To create a colorful, real-time, user-friendly packet sniffer using Python that captures and analyzes TCP, UDP, and ICMP packets on Kali Linux.

---

## 🚀 Features:

* Real-time packet sniffing
* Protocol detection: TCP, UDP, ICMP
* Color-coded output using `rich`
* Timestamps on each packet
* Stylish ASCII banner
* Works on Kali Linux (root access required)

---

## 🛠️ Requirements:

* OS: Kali Linux
* Python 3
* Python Libraries:

  ```bash
  sudo apt update
  sudo apt install python3-pip
  pip3 install scapy rich
  ```

---

## 📁 File Structure:

```
advanced_packet_sniffer/
├── sniffer.py             # Main Python script
├── README.md              # Project documentation
├── packet_capture_logs/   # (Optional) To store logs
```

---

## 🧪 How to Run:

1. Open a terminal in Kali Linux.
2. Run the script with root access:

   ```bash
   sudo python3 sniffer.py
   ```

---

## 🧪 How to Test:

Open another terminal and use these examples to generate traffic:

### ICMP Test:

```bash
ping -c 4 google.com
```

### TCP Test:

```bash
curl http://example.com
```

### Local TCP Connection:

```bash
# Terminal A:
nc -lvp 1234

# Terminal B:
nc 127.0.0.1 1234
```

---

## 💡 Advanced Tips:

* Filter by protocol:

  ```python
  sniff(prn=packet_handler, store=0, filter="tcp")
  ```
* Capture on specific interface:

  ```python
  sniff(prn=packet_handler, store=0, iface="eth0")
  ```

---

## 🔐 Important Notes:

* Run the script as root (`sudo`) to capture packets.
* This script is for educational and ethical use only.

---

## 📝 Output Example:

```
16:42:03 | ICMP | 192.168.0.5:- -> 142.250.193.206:-
16:42:04 | TCP  | 192.168.0.5:47230 -> 93.184.216.34:80
```

---

## 📜 License:

This project is open-source and free to use for educational purposes.

---

## 📧 Contact:

* Name: Kushal Kumawat
* Email: \[[tanchukumawat@gmail.com](mailto:your-email@example.com)]
* Linkedin: \[[wwww.linkedin.com/in/kushal-ku]]

---

## 🎓 Acknowledgements:

* Built using [Scapy](https://scapy.net/) and [Rich](https://rich.readthedocs.io/en/stable/)
* Inspired by real-world cybersecurity tools
