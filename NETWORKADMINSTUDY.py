#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import random

# --- App Metadata ---
APP_VERSION = "1.4.0"
BUILD_DATE = "August 28, 2026"
AUTHOR = "Matt-Réal Slaunwhite"

# --- Comprehensive Chapter Notes ---
CHAPTER_CONTENT = {
    "Ch 1: OSI Model": (
        "THE OSI MODEL & TCP/IP SUITE (How Data Travels)\n"
        "----------------------------------------------------------------------\n"
        "The Open Systems Interconnection (OSI) model standardizes network communication "
        "into 7 distinct functional layers. Think of it like packing and shipping an item: "
        "as data moves down the stack, headers are added (Encapsulation); as data travels up, "
        "headers are stripped away (De-encapsulation).\n\n"
        "7. APPLICATION LAYER (PDU: Data)\n"
        "• Human-computer interaction layer where applications access network services.\n"
        "• Protocols: HTTP, HTTPS, DNS, DHCP, FTP, SSH, SMTP, SNMP.\n\n"
        "6. PRESENTATION LAYER (PDU: Data)\n"
        "• Translates, formats, compresses, and encrypts/decrypts data.\n"
        "• Standards: TLS/SSL, ASCII, JPEG, GIF, MP4.\n\n"
        "5. SESSION LAYER (PDU: Data)\n"
        "• Sets up, coordinates, manages, and terminates dialogues between computers.\n"
        "• Protocols/APIs: NetBIOS, RPC, Sockets, PPTP session control.\n\n"
        "4. TRANSPORT LAYER (PDU: Segments for TCP / Datagrams for UDP)\n"
        "• Manages end-to-end data transport, flow control, and port addressing.\n"
        "• TCP (Transmission Control Protocol): Connection-oriented, reliable 3-way handshake (SYN -> SYN-ACK -> ACK), sequencing, retransmission of lost packets.\n"
        "• UDP (User Datagram Protocol): Connectionless, lightweight, best-effort (no handshake/retransmission), ideal for VoIP and live streaming.\n\n"
        "3. NETWORK LAYER (PDU: Packets)\n"
        "• Handles logical addressing (IPv4/IPv6) and path determination (Routing).\n"
        "• Hardware: Routers, Layer 3 Switches.\n"
        "• Protocols: IP, ICMP (ping), IGMP, OSPF, BGP, RIP, EIGRP.\n\n"
        "2. DATA LINK LAYER (PDU: Frames)\n"
        "• Handles physical addressing (MAC addresses) and local hop-to-hop framing.\n"
        "• Sublayers: LLC (Logical Link Control - flow control) and MAC (Media Access Control - hardware addressing).\n"
        "• Hardware: Switches, Bridges, Network Interface Cards (NICs), WAPs.\n"
        "• Protocols: Ethernet (802.3), Wi-Fi (802.11), ARP, STP (802.1D).\n\n"
        "1. PHYSICAL LAYER (PDU: Bits)\n"
        "• Transmits raw binary bitstreams over physical transmission media.\n"
        "• Media: Copper cables (Cat6), Fiber optics, Radio frequencies (RF), Hubs, Repeaters, Transceivers.\n\n"
        "----------------------------------------------------------------------\n"
        "*Layer 1 to 7 Mnemonic:* Please Do Not Throw Sausage Pizza Away.\n"
        "*Layer 7 to 1 Mnemonic:* All People Seem To Need Data Processing."
    ),
    "Ch 2: Ports": (
        "CORE & EXTENDED NETWORK PORTS (Doors to the Computer)\n"
        "----------------------------------------------------------------------\n"
        "Port numbers range from 0 to 65,535:\n"
        "• 0 - 1,023: Well-Known Ports (System & Core Services)\n"
        "• 1,024 - 49,151: Registered Ports (Vendor Specific)\n"
        "• 49,152 - 65,535: Dynamic / Private / Ephemeral Ports (Client-side connections)\n\n"
        "CORE EXAM PORTS TO MEMORIZE:\n"
        "• 20/21 (FTP - TCP): File Transfer Protocol (20=Data, 21=Control/Commands).\n"
        "• 22 (SSH / SFTP - TCP): Secure Shell / Secure FTP (Encrypted remote terminal).\n"
        "• 23 (Telnet - TCP): Unencrypted remote command line (Insecure, cleartext).\n"
        "• 25 (SMTP - TCP): Simple Mail Transfer Protocol (Sends email between servers).\n"
        "• 53 (DNS - TCP/UDP): Domain Name System (UDP for queries; TCP for zone transfers).\n"
        "• 67/68 (DHCP - UDP): 67 = DHCP Server, 68 = DHCP Client.\n"
        "• 69 (TFTP - UDP): Trivial File Transfer Protocol (No auth, PXE booting).\n"
        "• 80 (HTTP - TCP): Hypertext Transfer Protocol (Unencrypted web traffic).\n"
        "• 88 (Kerberos - TCP/UDP): Network authentication protocol (Active Directory).\n"
        "• 110 (POP3 - TCP): Post Office Protocol v3 (Downloads and deletes mail from server).\n"
        "• 123 (NTP - UDP): Network Time Protocol (Clock synchronization).\n"
        "• 143 (IMAP - TCP): Internet Message Access Protocol (Syncs mail across clients).\n"
        "• 161/162 (SNMP - UDP): Simple Network Mgmt (161=Queries/Agent, 162=Trap notifications).\n"
        "• 389 (LDAP - TCP/UDP): Lightweight Directory Access Protocol (Directory queries).\n"
        "• 443 (HTTPS - TCP): HTTP Secure (TLS/SSL encrypted web browsing).\n"
        "• 445 (SMB - TCP): Server Message Block (Windows file/folder/printer sharing).\n"
        "• 514 (Syslog - UDP): Centralized system logging from network infrastructure.\n"
        "• 636 (LDAPS - TCP): LDAP over TLS/SSL (Encrypted directory lookup).\n"
        "• 993 (IMAPS - TCP): IMAP over TLS/SSL.\n"
        "• 995 (POP3S - TCP): POP3 over TLS/SSL.\n"
        "• 1433 (MS SQL - TCP): Microsoft SQL Server database engine.\n"
        "• 1521 (Oracle - TCP): Oracle database listener.\n"
        "• 3306 (MySQL - TCP): MySQL database default port.\n"
        "• 3389 (RDP - TCP/UDP): Remote Desktop Protocol (Windows GUI remote control).\n"
        "• 5060/5061 (SIP - TCP/UDP): Session Initiation Protocol (VoIP signaling/setup)."
    ),
    "Ch 3: Hardware": (
        "NETWORK MEDIA, HARDWARE & VLAN ARCHITECTURE\n"
        "----------------------------------------------------------------------\n"
        "COPPER CABLING (Twisted Pair - T568A / T568B Standard):\n"
        "• Cat 5e: 1 Gbps up to 100 meters (100 MHz bandwidth).\n"
        "• Cat 6: 10 Gbps up to 55 meters; 1 Gbps up to 100 meters (250 MHz bandwidth).\n"
        "• Cat 6a: 10 Gbps up to 100 meters (500 MHz bandwidth, improved shielding).\n"
        "• Cat 7: 10 Gbps up to 100 meters (600 MHz, individual pair shielding).\n"
        "• Cat 8: 25 Gbps / 40 Gbps up to 30 meters (2000 MHz, data center runs).\n"
        "• Plenum vs. Non-Plenum (PVC): Plenum cables use special low-smoke, fire-retardant jacket materials for ceiling/air ducts.\n\n"
        "FIBER OPTIC CABLING:\n"
        "• Single-Mode Fiber (SMF): Narrow glass core (8-10 microns). Uses lasers. Reaches tens of kilometers. Yellow outer jacket.\n"
        "• Multi-Mode Fiber (MMF): Wider glass core (50-62.5 microns). Uses LEDs/VCSELs. Shorter distance (up to 550m). Aqua (OM3/OM4) or Orange (OM1/OM2) jacket.\n"
        "• Connectors: LC (Lucent Connector - small form factor), SC (Subscriber Connector - square snap-in), ST (Straight Tip - round bayonet twist), MPO/MTP (Multi-fiber push-on).\n\n"
        "INFRASTRUCTURE HARDWARE:\n"
        "• Hub (Layer 1): Multiport repeater. Broadcasts every bit to all ports. Creates 1 giant collision domain.\n"
        "• Switch (Layer 2): Inspects MAC addresses to selectively forward frames. Breaks up collision domains (each port is its own collision domain). Retains 1 broadcast domain per VLAN.\n"
        "• Router (Layer 3): Routes IP packets between distinct subnets/networks. Breaks up both collision domains and broadcast domains.\n"
        "• Layer 3 Switch: High-speed switch capable of hardware-based (ASIC) IP routing between internal VLANs.\n"
        "• Transceivers: SFP (1 Gbps), SFP+ (10 Gbps), QSFP+ (40 Gbps), QSFP28 (100 Gbps).\n\n"
        "VIRTUAL LOCAL AREA NETWORKS (VLANs) & TRUNKING:\n"
        "• Broadcast Domain Segmentation: VLANs partition a physical switch into distinct logical broadcast domains, improving security, reducing broadcast traffic, and isolating departments.\n"
        "• Access Ports: Assigned to a single VLAN. Forwards untagged Ethernet frames to end-user devices (PCs, printers).\n"
        "• Trunk Ports: Carries traffic for multiple VLANs across a single physical link between switches or between a switch and a router.\n"
        "• IEEE 802.1Q Tagging: The standard trunking protocol that inserts a 4-byte (32-bit) tag into the Ethernet frame header (contains the 12-bit VLAN ID [VID], supporting VLANs 1 to 4094, and 3-bit CoS priority).\n"
        "• Native VLAN: The designated VLAN on an 802.1Q trunk that carries untagged traffic (default is VLAN 1; best practice is to change it to an unused VLAN ID to mitigate VLAN hopping).\n"
        "• Voice VLAN: Allows an access port to support an IP desk phone and a daisy-chained PC simultaneously. The phone uses a tagged Voice VLAN (prioritized via CoS/QoS), while the PC sends untagged data on the native access VLAN.\n"
        "• Inter-VLAN Routing:\n"
        "  - Router-on-a-Stick (ROAS): A single physical router interface connects to a switch trunk port using logical sub-interfaces (e.g., Gig0/0.10, Gig0/0.20), each tagged with 802.1Q encapsulation.\n"
        "  - Layer 3 Switch / SVI: Uses Switch Virtual Interfaces (SVIs) (e.g., 'interface vlan 10') to route packets between VLANs internally at hardware line rate without bottlenecking an external router link.\n"
        "• VLAN Security:\n"
        "  - Switch Spoofing: An attacker negotiates a trunk link using Dynamic Trunking Protocol (DTP). Mitigated by disabling DTP on access ports (`switchport mode access` / `switchport nonegotiate`).\n"
        "  - Double Tagging: An attacker sends frames with two 802.1Q tags to traverse the native VLAN. Mitigated by setting the native VLAN to an unused ID and tagging native traffic."
    ),
    "Ch 4: Subnetting": (
        "SUBNETTING, IPV4 ARCHITECTURE & THE LEADING-BIT RULE\n"
        "----------------------------------------------------------------------\n"
        "IPv4 STRUCTURE: 32 bits total, written as 4 decimal octets separated by dots.\n\n"
        "THE SECRET TO IP CLASSES: THE LEADING-BIT RULE\n"
        "You never have to memorize the class numbers if you look at the first bits of Octet 1:\n"
        "• Class A starts with binary '0'   -> 00000000 to 01111111 (0 - 127)   [50% of all IPv4]\n"
        "• Class B starts with binary '10'  -> 10000000 to 10111111 (128 - 191) [25% of all IPv4]\n"
        "• Class C starts with binary '110' -> 11000000 to 11011111 (192 - 223) [12.5% of all IPv4]\n"
        "• Class D starts with binary '1110'-> 11100000 to 11101111 (224 - 239) [Multicast - 6.25%]\n"
        "• Class E starts with binary '1111'-> 11110000 to 11111111 (240 - 255) [Experimental - 6.25%]\n\n"
        "DEFAULT CLASS MASKS:\n"
        "• Class A: /8  (255.0.0.0)\n"
        "• Class B: /16 (255.255.0.0)\n"
        "• Class C: /24 (255.255.255.0)\n\n"
        "PRIVATE IP RANGES (RFC 1918 - Non-routable on public Internet):\n"
        "• 10.0.0.0 to 10.255.255.255 (10.0.0.0/8)\n"
        "• 172.16.0.0 to 172.31.255.255 (172.16.0.0/12)\n"
        "• 192.168.0.0 to 192.168.255.255 (192.168.0.0/16)\n\n"
        "SPECIAL ADDRESSES:\n"
        "• Loopback: 127.0.0.1 (/8) in IPv4 | ::1 in IPv6\n"
        "• APIPA (Link-Local): 169.254.0.1 to 169.254.255.254 (Assigned when DHCP fails) | fe80::/10 in IPv6\n\n"
        "THE TWO GOLDEN FORMULAS:\n"
        "1. Number of Subnets = 2^n (where n = number of borrowed bits)\n"
        "2. Usable Hosts per Subnet = 2^h - 2 (where h = remaining host bits)\n\n"
        "MAGIC NUMBER (BLOCK SIZE) CALCULATION:\n"
        "1. Identify the 'interesting octet' in the mask (the octet other than 255 or 0).\n"
        "2. Magic Number = 256 - [Mask Value in that Octet].\n"
        "3. Subnets count up by that exact increment starting from 0."
    ),
    "Ch 5: Services": (
        "ESSENTIAL NETWORK SERVICES & ADDRESSING PROTOCOLS\n"
        "----------------------------------------------------------------------\n"
        "DNS (Domain Name System - Port 53):\n"
        "• A Record: Maps hostname to IPv4 address (e.g., host.example.com -> 192.0.2.1).\n"
        "• AAAA Record: Maps hostname to IPv6 address (e.g., host.example.com -> 2001:db8::1).\n"
        "• CNAME (Canonical Name): Alias pointing to another domain name.\n"
        "• MX (Mail Exchanger): Directs incoming email to designated mail servers (includes priority values).\n"
        "• PTR (Pointer): Reverse DNS lookup (Maps IP address back to a hostname).\n"
        "• TXT: Arbitrary text; holds SPF, DKIM, and DMARC records to prevent email spoofing.\n"
        "• SOA (Start of Authority): Contains zone parameters, admin contact, and serial numbers.\n"
        "• NS (Name Server): Specifies the authoritative name servers for the zone.\n\n"
        "DHCP (Dynamic Host Configuration Protocol - Ports 67/68):\n"
        "The D.O.R.A. Lease Sequence:\n"
        "1. Discover (Client broadcast: 'Is there a DHCP server available?')\n"
        "2. Offer (Server unicast/broadcast: 'Here is an IP configuration you can use.')\n"
        "3. Request (Client broadcast: 'I accept your offer for this specific IP.')\n"
        "4. Acknowledge (Server unicast/broadcast: 'Confirmed. The lease is officially yours.')\n"
        "• DHCP Scope: The range of assignable IP addresses in a pool.\n"
        "• DHCP Reservation: Permanently tying a specific IP address to a hardware MAC address.\n"
        "• DHCP Relay / IP Helper: Forwards client DHCP broadcast packets across routers to a centralized DHCP server on another subnet.\n\n"
        "NTP (Network Time Protocol - UDP Port 123):\n"
        "• Synchronizes clocks across infrastructure devices. Critical for Kerberos auth, digital certificates, and chronological log correlation across Syslog."
    ),
    "Ch 6: T-Shoot": (
        "COMPTIA 7-STEP TROUBLESHOOTING METHODOLOGY & TOOLS\n"
        "----------------------------------------------------------------------\n"
        "COMPTIA 7-STEP METHODOLOGY (Strict Exam Order):\n"
        "1. Identify the problem:\n"
        "   - Gather information from users, identify symptoms, duplicate the issue if possible, question users, determine if anything has changed.\n"
        "2. Establish a theory of probable cause:\n"
        "   - Question the obvious (Is cable plugged in? Is port enabled?). Consider multiple approaches (top-to-bottom, bottom-up OSI, divide-and-conquer).\n"
        "3. Test the theory to determine cause:\n"
        "   - Once confirmed, determine next steps. If theory is not confirmed, re-establish a new theory or escalate.\n"
        "4. Establish a plan of action to resolve the problem and identify potential effects:\n"
        "   - Account for downtime, side effects on other systems, and prepare a rollback plan.\n"
        "5. Implement the solution or escalate as necessary.\n"
        "6. Verify full system functionality and, if applicable, implement preventive measures:\n"
        "   - Verify with the end user that the problem is fixed. Configure backups/monitoring so it does not recur.\n"
        "7. Document findings, actions, and outcomes:\n"
        "   - Update ticketing systems, network diagrams, and knowledge base articles for future reference.\n\n"
        "ESSENTIAL COMMAND-LINE TOOLS:\n"
        "• ping: Tests Layer 3 IP connectivity using ICMP Echo Request/Reply.\n"
        "• traceroute / tracert: Traces the Layer 3 hop-by-hop path to a host using TTL expiration.\n"
        "• ipconfig / ifconfig / ip addr: Displays local network interface parameters, IP, mask, gateway.\n"
        "• nslookup / dig: Queries DNS servers for specific resource records.\n"
        "• netstat / ss: Displays active TCP/UDP connections, listening ports, and routing tables.\n"
        "• arp: Shows the local ARP cache mapping IP addresses to MAC addresses.\n"
        "• route: Displays and modifies the local routing table."
    ),
    "Ch 7: Wireless": (
        "WIRELESS NETWORKING STANDARDS & SECURITY ARCHITECTURE\n"
        "----------------------------------------------------------------------\n"
        "802.11 WI-FI STANDARDS SPECTRUM:\n"
        "• 802.11b: 2.4 GHz | Up to 11 Mbps (DSSS modulation).\n"
        "• 802.11a: 5 GHz | Up to 54 Mbps (OFDM modulation).\n"
        "• 802.11g: 2.4 GHz | Up to 54 Mbps (Backwards compatible with 802.11b).\n"
        "• 802.11n (Wi-Fi 4): 2.4 GHz & 5 GHz | Up to 600 Mbps (Introduced MIMO - Multiple Input Multiple Output).\n"
        "• 802.11ac (Wi-Fi 5): 5 GHz only | Up to 6.9 Gbps (Introduced MU-MIMO, beamforming, 80/160 MHz channels).\n"
        "• 802.11ax (Wi-Fi 6 / 6E): 2.4 GHz, 5 GHz, 6 GHz | Up to 9.6 Gbps (Introduced OFDMA for high-density efficiency).\n\n"
        "FREQUENCY BANDS & CHANNELS:\n"
        "• 2.4 GHz Band: Longer range, superior wall penetration, limited to 3 non-overlapping 20 MHz channels (1, 6, 11). Highly susceptible to interference (microwaves, Bluetooth).\n"
        "• 5 GHz Band: Shorter range, reduced wall penetration, higher throughput, 24+ non-overlapping channels.\n\n"
        "WIRELESS SECURITY PROTOCOLS:\n"
        "• WEP: 64/128-bit RC4 cipher. Insecure, easily cracked via IV collisions.\n"
        "• WPA: RC4 with TKIP (Temporal Key Integrity Protocol). Deprecated.\n"
        "• WPA2: AES (Advanced Encryption Standard) with CCMP cipher. WPA2-Personal uses PSK (Pre-Shared Key); WPA2-Enterprise uses 802.1X with a centralized RADIUS server.\n"
        "• WPA3: Uses GCMP-256 cipher and SAE (Simultaneous Authentication of Equals) to prevent offline dictionary brute-force attacks. Mandates Protected Management Frames (PMF)."
    ),
    "Ch 8: Cloud": (
        "CLOUD DEPLOYMENT, SERVICES & VIRTUALIZATION\n"
        "----------------------------------------------------------------------\n"
        "CLOUD SERVICE MODELS (The Pizza / Shared Responsibility Model):\n"
        "• IaaS (Infrastructure as a Service): Cloud provider supplies raw compute, storage, and networking. Customer manages OS, runtime, middleware, data, and apps (e.g., AWS EC2, Azure VMs).\n"
        "• PaaS (Platform as a Service): Cloud provider manages hardware and operating system. Customer only brings application code and data (e.g., AWS Elastic Beanstalk, Heroku).\n"
        "• SaaS (Software as a Service): Fully managed application hosted by vendor. User simply consumes service via browser/API (e.g., Microsoft 365, Google Workspace, Salesforce).\n\n"
        "CLOUD DEPLOYMENT MODELS:\n"
        "• Public Cloud: Multi-tenant environment owned and operated by third-party provider.\n"
        "• Private Cloud: Single-tenant infrastructure provisioned exclusively for one organization.\n"
        "• Hybrid Cloud: Combines on-premises private infrastructure with public cloud workloads.\n"
        "• Community Cloud: Shared infrastructure tailored for organizations with common compliance/security requirements.\n\n"
        "VIRTUALIZATION & NETWORKING:\n"
        "• Type 1 Hypervisor (Bare-Metal): Installs directly on physical server hardware (e.g., VMware ESXi, Microsoft Hyper-V, KVM). Enterprise standard.\n"
        "• Type 2 Hypervisor (Hosted): Runs as an application on top of an existing host OS (e.g., VirtualBox, VMware Workstation).\n"
        "• vSwitch (Virtual Switch): Software-defined switch operating inside hypervisor to route traffic between virtual machines.\n"
        "• SAN (Storage Area Network): Dedicated high-speed network for block-level data storage (iSCSI, Fibre Channel).\n"
        "• NAS (Network Attached Storage): Dedicated appliance providing file-level storage over standard Ethernet (NFS, SMB)."
    ),
    "Ch 9: Security": (
        "NETWORK SECURITY, THREATS & HARDENING DEFENSES\n"
        "----------------------------------------------------------------------\n"
        "COMMON ATTACK VECTORS:\n"
        "• DoS / DDoS (Distributed Denial of Service): Flooding targets with traffic to exhaust bandwidth/resources (SYN floods, NTP/DNS amplification).\n"
        "• On-Path Attack (Man-in-the-Middle): Intercepting and altering traffic between two systems (ARP spoofing, DNS poisoning).\n"
        "• Phishing / Social Engineering: Tricking authorized users into revealing credentials or running malicious payloads.\n"
        "• Rogue Access Point / Evil Twin: Unauthorized WAP broadcasting a legitimate corporate SSID to harvest credentials.\n"
        "• Ransomware: Encrypts organizational files and demands payment for decryption keys.\n\n"
        "DEFENSE IN DEPTH & NETWORK HARDENING:\n"
        "• Firewalls:\n"
        "  - Stateless: Filters packets based solely on source/destination IP, port, and protocol headers.\n"
        "  - Stateful: Tracks active TCP/UDP connection states in a state table.\n"
        "  - NGFW (Next-Gen Firewall): Inspects Layer 7 application payloads, deep packet inspection (DPI), integrated IDS/IPS.\n"
        "• IDS vs. IPS:\n"
        "  - IDS (Intrusion Detection System): Passive monitoring via SPAN/mirror port; generates alerts.\n"
        "  - IPS (Intrusion Prevention System): In-line placement; actively blocks and drops malicious traffic.\n"
        "• DMZ (Demilitarized Zone): Perimeter network hosting public-facing servers (Web, Mail, DNS) isolated from the internal LAN.\n"
        "• NAC (Network Access Control): Evaluates endpoint posture (antivirus, patches) before granting network access via 802.1X.\n"
        "• VPN Technologies: IPsec (Layer 3 tunnel using AH/ESP for site-to-site) vs. SSL/TLS VPN (Layer 4/7 clientless remote access)."
    ),
    "Ch 10: Ops": (
        "NETWORK OPERATIONS, MONITORING & BUSINESS CONTINUITY\n"
        "----------------------------------------------------------------------\n"
        "MONITORING & METRICS:\n"
        "• SNMP (Simple Network Management Protocol - UDP 161/162):\n"
        "  - MIB (Management Information Base): Database containing performance metrics on the managed device.\n"
        "  - SNMPv1/v2c: Insecure, transmits community strings in cleartext.\n"
        "  - SNMPv3: Modern standard providing Authentication (SHA/MD5) and Encryption (AES/DES).\n"
        "• Baseline: Historical snapshot of normal network performance used to identify deviations and capacity trends.\n"
        "• NetFlow / sFlow: Collects IP traffic statistics and session metadata for bandwidth analysis.\n"
        "• Syslog Severity Levels: 0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, 5=Notice, 6=Informational, 7=Debug.\n\n"
        "HIGH AVAILABILITY & DISASTER RECOVERY:\n"
        "• MTBF (Mean Time Between Failures): Expected operational lifetime of a hardware component before failure.\n"
        "• MTTR (Mean Time To Repair): Average time required to diagnose, repair, and restore a failed system.\n"
        "• RTO (Recovery Time Objective): Maximum acceptable downtime duration following an outage.\n"
        "• RPO (Recovery Point Objective): Maximum acceptable data loss duration measured in time (backup age).\n\n"
        "BACKUP STRATEGIES:\n"
        "• Full Backup: Copies all selected data and clears the archive bit. Slowest backup, fastest single-step restore.\n"
        "• Incremental Backup: Backs up only files modified since the last Full OR Incremental backup; clears archive bit. Fast backup, slow restore (requires Full + all Incrementals in sequence).\n"
        "• Differential Backup: Backs up all files modified since the last Full backup; does NOT clear archive bit. Moderate backup, fast restore (requires Full + last Differential)."
    ),
    "Ch 11: Routing & WAN": (
        "ROUTING PROTOCOLS & WAN TECHNOLOGIES\n"
        "----------------------------------------------------------------------\n"
        "ROUTING CONCEPTS & ADMINISTRATIVE DISTANCE (AD):\n"
        "• Administrative Distance: Metric of believability (Lower AD is preferred).\n"
        "  - Connected: 0 | Static Route: 1 | eBGP: 20 | EIGRP (Internal): 90 | OSPF: 110 | RIP: 120 | iBGP: 200.\n\n"
        "INTERIOR ROUTING PROTOCOLS (IGP):\n"
        "• Distance-Vector (RIP): Uses hop count as its metric (max 15 hops; 16 is unreachable). Slow convergence.\n"
        "• Link-State (OSPF - Open Shortest Path First): Uses Dijkstra's SPF algorithm and link cost (bandwidth). Fast convergence, area-based hierarchy (Area 0 Backbone).\n"
        "• Advanced Distance-Vector / Hybrid (EIGRP): Cisco proprietary/open standard. Uses composite metric (Bandwidth + Delay). Extremely fast convergence using DUAL.\n\n"
        "EXTERIOR ROUTING PROTOCOLS (EGP):\n"
        "• BGP (Border Gateway Protocol - TCP 179): The path-vector protocol connecting Autonomous Systems (AS) across the global Internet.\n\n"
        "WAN TECHNOLOGIES:\n"
        "• MPLS (Multiprotocol Label Switching): High-speed Layer 2.5 carrier WAN using labels for forwarding instead of full IP lookups.\n"
        "• SD-WAN (Software-Defined WAN): Dynamically routes traffic across broadband, cellular, and MPLS based on real-time latency/jitter.\n"
        "• Metro Ethernet: Connecting enterprise branches across a metropolitan area using native Ethernet transport.\n"
        "• Satellite (LEO / GEO): Low Earth Orbit (e.g., Starlink) provides low latency (~30ms); Geostationary (GEO) suffers high latency (~600ms)."
    ),
    "Ch 12: Optimization": (
        "NETWORK PERFORMANCE, HIGH AVAILABILITY & QOS\n"
        "----------------------------------------------------------------------\n"
        "TRAFFIC SHAPING & QUALITY OF SERVICE (QoS):\n"
        "• Traffic Shaping / Policing: Delaying or dropping non-critical packets to guarantee bandwidth for critical services (VoIP).\n"
        "• Classification & Marking:\n"
        "  - Layer 2: CoS (Class of Service) inside 802.1Q tag (3 bits, 0-7).\n"
        "  - Layer 3: DiffServ / DSCP (Differentiated Services Code Point - 6 bits inside IP header; e.g., EF = Expedited Forwarding for VoIP).\n\n"
        "HIGH AVAILABILITY & REDUNDANCY:\n"
        "• First Hop Redundancy Protocols (FHRP):\n"
        "  - HSRP (Hot Standby Router Protocol): Cisco proprietary; provides active/standby router gateway redundancy.\n"
        "  - VRRP (Virtual Router Redundancy Protocol): Open standard equivalent to HSRP.\n"
        "  - GLBP (Gateway Load Balancing Protocol): Cisco proprietary; active/active gateway load balancing.\n"
        "• Link Aggregation (LACP - 802.3ad/802.1ax): Bundles multiple physical switch links into a single logical channel for combined throughput and link failover.\n"
        "• Load Balancers: Distributes application traffic across server pools using algorithms (Round Robin, Least Connections, IP Hash, Weighted)."
    ),
    "Ch 13: Hardening": (
        "PHYSICAL SECURITY, DEVICE HARDENING & ORGANIZATIONAL POLICIES\n"
        "----------------------------------------------------------------------\n"
        "LAYER 2 SWITCH HARDENING:\n"
        "• Port Security: Restricts interface traffic to specific MAC addresses (Static or Sticky MAC) and disables the port upon violation (err-disable).\n"
        "• DHCP Snooping: Distinguishes between trusted (DHCP server) and untrusted ports to prevent rogue DHCP server attacks.\n"
        "• Dynamic ARP Inspection (DAI): Validates ARP packets against the DHCP Snooping database to prevent ARP poisoning/spoofing.\n"
        "• BPDU Guard: Disables STP-enabled access ports if a switch (BPDU packet) is plugged in to protect the STP topology.\n\n"
        "PHYSICAL & ENVIRONMENTAL SECURITY:\n"
        "• Environmental Controls: HVAC hot-aisle/cold-aisle containment to optimize cooling.\n"
        "• Fire Suppression: Wet-pipe (water in pipes) vs. Dry-pipe (water held back until heat activates) vs. Clean-Agent Gas (FM-200/Inergen for electrical safety).\n\n"
        "GOVERNANCE & ORGANIZATIONAL POLICIES:\n"
        "• AUP (Acceptable Use Policy): Defines permissible user activities on enterprise hardware and networks.\n"
        "• NDA (Non-Disclosure Agreement): Protects confidential proprietary business data.\n"
        "• SLA (Service Level Agreement): Contractually defines uptime, response times, and penalties from a service provider.\n"
        "• Change Management: Formal process for requesting, evaluating, testing, and approving infrastructure modifications."
    ),
    "Ch 14: Architecture": (
        "NETWORK TOPOLOGIES, ARCHITECTURES & ZERO TRUST\n"
        "----------------------------------------------------------------------\n"
        "PHYSICAL & LOGICAL TOPOLOGIES:\n"
        "• Star Topology: End devices connect to a central switch. Single point of failure at the switch, but easy to scale.\n"
        "• Full Mesh vs. Partial Mesh: Full mesh connects every node directly ($n(n-1)/2$ links). Highly redundant, high cost.\n"
        "• Spine-and-Leaf Architecture: Modern data center fabric replacing 3-tier core/distribution/access. Every Leaf switch connects to every Spine switch, providing predictable low-latency East-West traffic.\n\n"
        "SOFTWARE-DEFINED NETWORKING (SDN):\n"
        "• Decouples the Control Plane (routing intelligence/decisions) from the Data/Forwarding Plane (physical packet switching).\n"
        "• Northbound APIs: Connects the centralized SDN controller to applications/orchestration software.\n"
        "• Southbound APIs (e.g., OpenFlow): Connects the SDN controller to physical network switches.\n\n"
        "ZERO TRUST ARCHITECTURE:\n"
        "• Core Philosophy: 'Never trust, always verify.' Assumes breaches will occur.\n"
        "• Microsegmentation: Isolates workloads and servers into granular secure zones to prevent lateral movement of attackers."
    )
}

# --- Comprehensive Glossary ---
GLOSSARY_TERMS = {
    "AAA (Authentication, Authorization, Accounting)": "Framework for controlling access to network resources, verifying identity, and tracking user activities (e.g., RADIUS, TACACS+).",
    "Access Port": "A switch port configured to carry untagged Ethernet traffic for only one single VLAN (typically connects to end-user PCs or printers).",
    "ACL (Access Control List)": "Sequential set of permit/deny rules applied to IP addresses, ports, or protocols on routers and firewalls.",
    "Administrative Distance (AD)": "A value between 0-255 defining the trustworthiness of a routing source. Lower values are preferred (e.g., Connected=0, Static=1, OSPF=110).",
    "APIPA (Automatic Private IP Addressing)": "Automatic link-local IPv4 address assignment in the 169.254.0.0/16 range when a DHCP server is unreachable.",
    "ARP (Address Resolution Protocol)": "Resolves a known Layer 3 IPv4 address to an unknown Layer 2 physical MAC address on a local segment.",
    "BGP (Border Gateway Protocol)": "The standard exterior gateway routing protocol (EGP) used to route traffic between Autonomous Systems (AS) across the Internet.",
    "CIDR (Classless Inter-Domain Routing)": "Method of IP address allocation and routing that uses prefix masks (e.g., /24) to replace legacy Class A/B/C addressing.",
    "CSMA/CD & CSMA/CA": "Media access mechanisms. CSMA/CD (Collision Detection) is used in legacy half-duplex Ethernet; CSMA/CA (Collision Avoidance) is used in Wi-Fi (802.11).",
    "DAI (Dynamic ARP Inspection)": "Switch security feature that validates ARP packets against the DHCP snooping binding database to block ARP poisoning.",
    "DHCP (Dynamic Host Configuration Protocol)": "Automated protocol that assigns IP addresses, subnet masks, gateways, and DNS parameters using the DORA sequence.",
    "DHCP Snooping": "Switch security mechanism filtering unauthorized (rogue) DHCP server responses on untrusted switch ports.",
    "DKIM / SPF / DMARC": "DNS TXT records configured to validate email sender authenticity and prevent phishing, spoofing, and spam.",
    "DMZ (Demilitarized Zone)": "A physical or logical subnetwork that exposes an organization's external-facing services to an untrusted network while protecting the LAN.",
    "DNS (Domain Name System)": "Distributed naming system resolving human-readable hostnames (e.g., example.com) to machine-routable IP addresses.",
    "DSCP (Differentiated Services Code Point)": "A 6-bit field in the IPv4/IPv6 packet header used to classify and prioritize Layer 3 traffic for Quality of Service (QoS).",
    "FHRP (First Hop Redundancy Protocol)": "Protocols like HSRP, VRRP, and GLBP that provide default gateway redundancy using a shared virtual IP address.",
    "ICMP (Internet Control Message Protocol)": "Network layer protocol used for network diagnostics, error reporting, and utilities like ping and traceroute.",
    "IEEE 802.1Q": "The networking standard supporting VLAN tagging on Ethernet frames across trunk links by inserting a 4-byte identifier into the header.",
    "IPsec (Internet Protocol Security)": "Suite of protocols (AH, ESP, IKE) providing authentication, integrity, and encryption for Layer 3 network traffic and VPNs.",
    "Jumbo Frame": "Ethernet frame with a payload greater than the standard 1,500-byte MTU, typically up to 9,000 bytes, used in SANs to reduce CPU overhead.",
    "LACP (Link Aggregation Control Protocol)": "IEEE 802.3ad/802.1ax standard that bundles multiple physical network links into a single logical channel for redundancy and throughput.",
    "MAC (Media Access Control) Address": "Unique 48-bit (6-byte) physical identifier burned into a NIC, represented as hexadecimal (e.g., 00:1A:2B:3C:4D:5E).",
    "MIMO (Multiple Input Multiple Output)": "Wireless technology using multiple antennas at transmitter and receiver to improve communication performance and data throughput.",
    "MPLS (Multiprotocol Label Switching)": "High-performance telecom routing technique that directs data from one node to the next based on short path labels rather than long IP lookups.",
    "MTU (Maximum Transmission Unit)": "The largest size packet or frame (in bytes) that can be transmitted over a physical network interface without fragmentation (default 1500 bytes for Ethernet).",
    "NAC (Network Access Control)": "Security solution enforcing endpoint compliance and security posture checks prior to granting network access via 802.1X.",
    "NAT (Network Address Translation)": "Translates private (RFC 1918) IP addresses to a public routable IP address for internet access (PAT / NAT Overload).",
    "Native VLAN": "The designated VLAN on an 802.1Q trunk link that transmits frames without an 802.1Q tag (default is VLAN 1).",
    "OSPF (Open Shortest Path First)": "A standard interior gateway link-state routing protocol utilizing Dijkstra's algorithm to calculate the shortest path through a network area.",
    "PDU (Protocol Data Unit)": "Unit of data specified in a given layer of the OSI model: Bits (L1), Frames (L2), Packets (L3), Segments/Datagrams (L4), Data (L5-7).",
    "PoE (Power over Ethernet)": "Standards (802.3af 15.4W, 802.3at PoE+ 30W, 802.3bt 60W-90W) that pass electrical power alongside data on twisted-pair Ethernet cables.",
    "Port Security": "Layer 2 switch feature that restricts port access to specific learned or configured MAC addresses to block unauthorized devices.",
    "QoS (Quality of Service)": "Techniques prioritizing latency-sensitive network traffic (VoIP, video) using tagging mechanisms like DiffServ, CoS, and DSCP.",
    "RADIUS / TACACS+": "Centralized AAA protocols. RADIUS combines authentication/authorization using UDP; TACACS+ separates AAA and encrypts the full payload over TCP port 49.",
    "Router-on-a-Stick (ROAS)": "Inter-VLAN routing configuration where a single physical router interface connects to a switch trunk port using sub-interfaces tagged with 802.1Q.",
    "RSTP (Rapid Spanning Tree Protocol)": "IEEE 802.1w protocol that prevents Layer 2 switching loops while converging topology changes significantly faster than legacy 802.1D STP.",
    "SD-WAN (Software-Defined Wide Area Network)": "An overlay architecture that dynamically and intelligently routes traffic across multiple WAN transport connections based on performance.",
    "SDN (Software-Defined Networking)": "Architecture decoupling the network control plane (decision-making) from the data plane (underlying packet forwarding).",
    "SFP / SFP+ / QSFP+": "Hot-swappable transceiver form factors supporting Gigabit (SFP), 10 Gigabit (SFP+), and 40 Gigabit (QSFP+) optical or direct-attach copper links.",
    "SNMP (Simple Network Management Protocol)": "Application-layer protocol for monitoring and configuring network devices via MIB queries (UDP 161) and event Traps (UDP 162).",
    "Spine-and-Leaf": "Two-tier data center switching architecture where every leaf switch connects to every spine switch, optimizing east-west traffic.",
    "Syslog": "Standard protocol logging event notifications from network infrastructure to a central server over UDP port 514.",
    "Trunk Port": "A switch port configured to carry traffic for multiple VLANs simultaneously across switches using IEEE 802.1Q encapsulation.",
    "VLAN (Virtual Local Area Network)": "Logical partition of a physical Layer 2 switch into multiple distinct broadcast domains (standardized by IEEE 802.1Q tagging).",
    "Voice VLAN": "A specialized VLAN carrying prioritized voice traffic (VoIP) alongside standard untagged PC data on a single access switch port.",
    "VPN (Virtual Private Network)": "Encrypted tunnel extending a private network across a public network to secure communications.",
    "VRRP (Virtual Router Redundancy Protocol)": "Open-standard FHRP providing automatic assignment of available IP routers to participating hosts.",
    "WPA3 (Wi-Fi Protected Access 3)": "Current wireless security standard mandating Protected Management Frames and replacing PSK with SAE to prevent dictionary attacks.",
    "Zero Trust": "Security paradigm requiring strict verification for every user and device attempting to access network resources, regardless of location."
}

# --- Quick Drill Flashcard Decks ---
QUIZ_DATA = {
    "Ch 1: OSI Model": [
        ("What is the Protocol Data Unit (PDU) at Layer 2 of the OSI Model?", "Frame"),
        ("Which layer handles end-to-end flow control, sequencing, and port numbers?", "Layer 4 (Transport Layer)"),
        ("What is the 3-way handshake sequence used by TCP?", "SYN -> SYN-ACK -> ACK"),
        ("At which OSI layer does an IP Router make its forwarding decisions?", "Layer 3 (Network Layer)"),
        ("What layer handles encryption, formatting, and data compression?", "Layer 6 (Presentation Layer)"),
        ("Which layer is responsible for MAC addresses and physical framing?", "Layer 2 (Data Link Layer)")
    ],
    "Ch 2: Ports": [
        ("What port is used for secure remote desktop connections on Windows?", "Port 3389 (RDP)"),
        ("Which port does unencrypted Telnet use, and what secure protocol replaces it?", "Port 23 (Telnet) is replaced by Port 22 (SSH)"),
        ("What port and protocol does DNS use for standard client lookups?", "Port 53 (UDP)"),
        ("What port is used for Windows file and printer sharing via SMB?", "Port 445"),
        ("Which two ports are used by standard unencrypted DHCP?", "Port 67 (Server) and Port 68 (Client)"),
        ("What port is used for secure, encrypted web browsing?", "Port 443 (HTTPS)")
    ],
    "Ch 3: Hardware": [
        ("What is the standard IEEE protocol for tagging Ethernet frames across VLAN trunk links?", "IEEE 802.1Q (inserts a 4-byte tag with a 12-bit VLAN ID)"),
        ("What is the difference between an Access Port and a Trunk Port?", "Access ports carry untagged traffic for 1 VLAN; Trunk ports carry tagged traffic for multiple VLANs."),
        ("What happens to untagged frames passing over an 802.1Q trunk link?", "They are forwarded onto the designated Native VLAN (default VLAN 1)."),
        ("What is Router-on-a-Stick (ROAS)?", "Inter-VLAN routing using a single physical router interface divided into logical 802.1Q sub-interfaces."),
        ("What type of cable jacket is required for installation in drop ceilings and air ducts?", "Plenum-rated jacket (CMP)"),
        ("Which fiber optic type uses lasers for long-distance runs and has a yellow jacket?", "Single-Mode Fiber (SMF)"),
        ("What device breaks up collision domains per-port while maintaining one broadcast domain?", "A Layer 2 Switch")
    ],
    "Ch 4: Subnetting": [
        ("How are the starting decimal numbers for Class A, B, and C determined in binary?", "By leading bits: Class A starts with '0', Class B with '10', Class C with '110'."),
        ("How many usable host IP addresses are available in a /28 subnet?", "14 usable hosts (2^4 - 2 = 14)"),
        ("What is the subnet mask representation for a /26 network?", "255.255.255.192"),
        ("What are the three RFC 1918 private IPv4 address ranges?", "10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16"),
        ("If a workstation has an IP of 169.254.10.5, what occurred?", "APIPA assigned it because the DHCP server was unreachable."),
        ("What is the block size (magic number) for a subnet with a 255.255.255.224 mask?", "32 (256 - 224 = 32)"),
        ("Why do you subtract 2 when calculating usable hosts?", "To exclude the Network ID and the Broadcast address.")
    ],
    "Ch 5: Services": [
        ("What DNS record type maps an IPv6 address to a hostname?", "AAAA Record"),
        ("What are the four steps of the DHCP IP address leasing process?", "D.O.R.A. (Discover, Offer, Request, Acknowledge)"),
        ("What DNS record specifies the mail server responsible for receiving domain emails?", "MX (Mail Exchanger) Record"),
        ("What feature allows routers to forward DHCP broadcast requests to a remote DHCP server?", "DHCP Relay (or IP Helper-Address)"),
        ("Which DNS records are used to prevent email spoofing and phishing?", "SPF, DKIM, and DMARC (stored in TXT records)"),
        ("What protocol uses UDP port 123 to keep system clocks synchronized?", "NTP (Network Time Protocol)")
    ],
    "Ch 6: T-Shoot": [
        ("What is the very first step in the CompTIA 7-step troubleshooting methodology?", "Identify the problem"),
        ("After establishing a theory of probable cause, what is the immediate next step?", "Test the theory to determine the cause"),
        ("What command displays the Layer 3 path and hop-by-hop latency to a remote host?", "traceroute (Linux) / tracert (Windows)"),
        ("What is the final step of the CompTIA troubleshooting methodology?", "Document findings, actions, and outcomes"),
        ("What tool tests Layer 3 reachability using ICMP Echo Requests?", "ping"),
        ("What command displays active network connections, listening ports, and sockets?", "netstat (or ss)")
    ],
    "Ch 7: Wireless": [
        ("Which wireless standard operates exclusively in the 5 GHz band?", "802.11ac (Wi-Fi 5)"),
        ("What are the three non-overlapping channels in the 2.4 GHz spectrum (North America)?", "Channels 1, 6, and 11 (at 20 MHz width)"),
        ("What authentication handshake does WPA3 use to replace vulnerable PSK?", "SAE (Simultaneous Authentication of Equals)"),
        ("What wireless enterprise standard uses 802.1X and a centralized RADIUS server?", "WPA2/WPA3 Enterprise"),
        ("What antenna technology sends targeted wireless signals directly toward connected clients?", "Beamforming"),
        ("Which standard introduced OFDMA to improve high-density multi-device efficiency?", "802.11ax (Wi-Fi 6)")
    ],
    "Ch 8: Cloud": [
        ("What cloud service model gives the customer control over the OS, storage, and networking?", "IaaS (Infrastructure as a Service)"),
        ("What type of hypervisor runs directly on the bare physical server hardware?", "Type 1 Hypervisor (e.g., ESXi, Hyper-V)"),
        ("What cloud model represents fully managed applications like Microsoft 365 or Gmail?", "SaaS (Software as a Service)"),
        ("What technology allows multiple isolated virtual networks to share a physical switch?", "vSwitch (Virtual Switch)"),
        ("What is the difference between SAN and NAS?", "SAN provides block-level storage (iSCSI/FC); NAS provides file-level storage (NFS/SMB)."),
        ("What cloud deployment combines on-premises private servers with public cloud infrastructure?", "Hybrid Cloud")
    ],
    "Ch 9: Security": [
        ("What attack intercepts traffic between two hosts by poisoning local ARP caches?", "On-Path / Man-in-the-Middle Attack (ARP Poisoning)"),
        ("What is the primary difference between an IDS and an IPS?", "An IDS passively detects/alerts; an IPS sits in-line and actively blocks threats."),
        ("What security system checks endpoint compliance (antivirus, patches) before network admission?", "NAC (Network Access Control)"),
        ("What perimeter network segment isolates public-facing web servers from the internal LAN?", "DMZ (Demilitarized Zone)"),
        ("What type of firewall inspects Layer 7 application payloads and deep packet contents?", "NGFW (Next-Generation Firewall)"),
        ("What attack overwhelms a server by sending millions of spoofed requests from a botnet?", "DDoS (Distributed Denial of Service)")
    ],
    "Ch 10: Ops": [
        ("Which SNMP version provides secure cryptographic authentication and AES encryption?", "SNMPv3"),
        ("What metric defines the maximum acceptable downtime an organization can tolerate during an outage?", "RTO (Recovery Time Objective)"),
        ("What type of backup copies only files modified since the last Full or Incremental backup and clears the archive bit?", "Incremental Backup"),
        ("What metric describes the average operational time a device functions before experiencing hardware failure?", "MTBF (Mean Time Between Failures)"),
        ("What protocol collects traffic metadata and flow statistics across switch interfaces?", "NetFlow / sFlow / IPFIX"),
        ("What Syslog severity level corresponds to an 'Emergency' condition?", "Level 0 (Emergency)")
    ],
    "Ch 11: Routing & WAN": [
        ("What is the Administrative Distance of OSPF by default?", "110 (Static is 1, eBGP is 20, EIGRP is 90)"),
        ("What protocol connects Autonomous Systems (AS) across the global Internet?", "BGP (Border Gateway Protocol)"),
        ("What WAN technology forwards packets using short labels instead of complex Layer 3 lookups?", "MPLS (Multiprotocol Label Switching)"),
        ("What is the metric limit for Routing Information Protocol (RIP)?", "15 hops (16 is considered unreachable)"),
        ("What WAN architecture dynamically steers traffic across broadband, cellular, and MPLS?", "SD-WAN (Software-Defined WAN)")
    ],
    "Ch 12: Optimization": [
        ("What field in an IPv4 header is used by DiffServ to provide Layer 3 QoS markings?", "DSCP (Differentiated Services Code Point - 6 bits)"),
        ("What open-standard protocol provides default gateway redundancy across routers?", "VRRP (Virtual Router Redundancy Protocol)"),
        ("What protocol standardizes link aggregation to combine multiple physical links into one?", "LACP (IEEE 802.3ad/802.1ax)"),
        ("What is the difference between traffic shaping and traffic policing?", "Shaping buffers and delays excess traffic; policing drops excess traffic immediately."),
        ("What load balancing algorithm directs traffic to the server with the fewest active sessions?", "Least Connections")
    ],
    "Ch 13: Hardening": [
        ("What switch security feature prevents rogue DHCP servers by designating trusted ports?", "DHCP Snooping"),
        ("What Layer 2 security mechanism inspects and validates ARP packets against the DHCP snooping table?", "Dynamic ARP Inspection (DAI)"),
        ("What port security violation mode drops offending packets and shuts down the port entirely?", "Shutdown (places port in err-disable state)"),
        ("What type of data center fire suppression uses clean chemical gas without damaging electronics?", "Clean-Agent Gas Suppression (e.g., FM-200/Inergen)"),
        ("What agreement defines required uptime, support response times, and failure penalties with a vendor?", "SLA (Service Level Agreement)")
    ],
    "Ch 14: Architecture": [
        ("What modern two-tier data center topology optimizes predictable east-west traffic?", "Spine-and-Leaf Architecture"),
        ("In SDN architecture, what API connects the SDN controller to physical network switches?", "Southbound API (e.g., OpenFlow)"),
        ("What security paradigm operates on the core principle of 'Never trust, always verify'?", "Zero Trust Architecture"),
        ("What formula calculates the total number of links required in a full mesh network of n nodes?", "n(n - 1) / 2"),
        ("What technique divides data center workloads into granular isolated zones to prevent lateral movement?", "Microsegmentation")
    ]
}

# --- Comprehensive Practice Exam Bank (Categorized) ---
PRACTICE_TEST_BANK = [
    # --- PART 1: CHAPTERS 1-6 (Foundations & VLANs) ---
    {"cat": "1-6", "q": "Which networking standard is used to insert a 4-byte VLAN identification tag into an Ethernet frame header on trunk links?", "options": ["IEEE 802.1X", "IEEE 802.1Q", "IEEE 802.3ad", "IEEE 802.11ac"], "answer": "IEEE 802.1Q", "exp": "IEEE 802.1Q is the industry standard for VLAN tagging, inserting a 32-bit (4-byte) field containing a 12-bit VLAN ID."},
    {"cat": "1-6", "q": "A network technician needs to route traffic between multiple VLANs using a single physical router interface. What configuration is required?", "options": ["Router-on-a-Stick with 802.1Q sub-interfaces", "Dynamic ARP Inspection", "LACP link aggregation", "Split Horizon with Poison Reverse"], "answer": "Router-on-a-Stick with 802.1Q sub-interfaces", "exp": "Router-on-a-Stick connects a single router interface to a switch trunk port, splitting the interface into logical 802.1Q-tagged sub-interfaces."},
    {"cat": "1-6", "q": "What happens to untagged traffic traversing an IEEE 802.1Q trunk link?", "options": ["It is dropped automatically", "It is placed onto the Native VLAN", "It is forwarded to the management VLAN", "It is encapsulated into an IPsec tunnel"], "answer": "It is placed onto the Native VLAN", "exp": "802.1Q trunk links place all untagged frames onto the designated Native VLAN (default VLAN 1)."},
    {"cat": "1-6", "q": "According to the binary leading-bit rule for classful addressing, what binary value must the first octet of a Class B IP address start with?", "options": ["0", "10", "110", "1110"], "answer": "10", "exp": "Class B addresses always begin with the leading binary bits '10', establishing the 128 to 191 decimal boundary."},
    {"cat": "1-6", "q": "A network engineer needs to configure an Access Control List (ACL) to block unencrypted web browsing traffic. Which port should be filtered?", "options": ["Port 443", "Port 80", "Port 22", "Port 53"], "answer": "Port 80", "exp": "Port 80 is used by HTTP for cleartext web traffic. Port 443 is HTTPS (encrypted)."},
    {"cat": "1-6", "q": "At which layer of the OSI model does a standard Layer 2 Ethernet switch make its forwarding decisions?", "options": ["Layer 1 (Physical)", "Layer 2 (Data Link)", "Layer 3 (Network)", "Layer 4 (Transport)"], "answer": "Layer 2 (Data Link)", "exp": "Layer 2 switches evaluate Destination MAC addresses inside Ethernet frame headers to make forwarding decisions."},
    {"cat": "1-6", "q": "A user reports they cannot connect to any network resources. According to the CompTIA troubleshooting methodology, what should the technician do FIRST?", "options": ["Establish a theory of probable cause", "Identify the problem", "Test the theory to determine cause", "Establish a plan of action"], "answer": "Identify the problem", "exp": "Step 1 is always Identify the Problem by questioning the user, identifying symptoms, and checking for recent changes."},
    {"cat": "1-6", "q": "Which DNS resource record is responsible for directing incoming domain email to the authoritative mail server?", "options": ["A Record", "CNAME Record", "MX Record", "PTR Record"], "answer": "MX Record", "exp": "MX (Mail Exchanger) records route email to designated mail servers with configurable priority metrics."},
    {"cat": "1-6", "q": "How many usable host IP addresses are available in a network configured with a /28 subnet mask?", "options": ["14", "16", "30", "32"], "answer": "14", "exp": "A /28 mask leaves 4 host bits (32 - 28 = 4). 2^4 - 2 = 16 - 2 = 14 usable host addresses."},
    {"cat": "1-6", "q": "Which fiber optic cabling type uses narrow core diameters and lasers for multi-kilometer backbone transmissions?", "options": ["Multi-Mode Fiber (MMF)", "Single-Mode Fiber (SMF)", "Cat 6a STP", "Coaxial RG-6"], "answer": "Single-Mode Fiber (SMF)", "exp": "SMF has an 8-10 micron core and uses laser optics to transmit over long distances with minimal modal dispersion."},
    {"cat": "1-6", "q": "Which port and protocol does Microsoft Remote Desktop Protocol (RDP) utilize by default?", "options": ["Port 22 TCP", "Port 3389 TCP", "Port 445 TCP", "Port 5060 UDP"], "answer": "Port 3389 TCP", "exp": "RDP uses TCP (and optionally UDP) port 3389 for remote desktop management sessions."},
    {"cat": "1-6", "q": "What is the third message exchanged in the standard DHCP address leasing process?", "options": ["Discover", "Offer", "Request", "Acknowledge"], "answer": "Request", "exp": "The DHCP D.O.R.A. sequence is: 1. Discover, 2. Offer, 3. Request, 4. Acknowledge."},
    {"cat": "1-6", "q": "Which Protocol Data Unit (PDU) is encapsulated and processed at Layer 3 of the OSI model?", "options": ["Bit", "Frame", "Packet", "Segment"], "answer": "Packet", "exp": "PDUs: Layer 1 = Bits, Layer 2 = Frames, Layer 3 = Packets, Layer 4 = Segments (TCP) / Datagrams (UDP)."},
    {"cat": "1-6", "q": "What is the maximum certified cable length for 10GBASE-T Ethernet transmission over Category 6 UTP cabling?", "options": ["100 meters", "55 meters", "30 meters", "10 meters"], "answer": "55 meters", "exp": "Cat 6 supports 10 Gbps up to 55 meters. Cat 6a is required for 10 Gbps up to the full 100-meter standard."},
    {"cat": "1-6", "q": "Which layer of the OSI model manages dialogue control, session synchronization, and token management between applications?", "options": ["Layer 4 (Transport)", "Layer 5 (Session)", "Layer 6 (Presentation)", "Layer 7 (Application)"], "answer": "Layer 5 (Session)", "exp": "The Session layer establishes, maintains, and terminates communication sessions between software processes."},
    {"cat": "1-6", "q": "Which protocol and port does DNS utilize for standard client-to-server hostname resolution queries?", "options": ["Port 53 UDP", "Port 53 TCP", "Port 67 UDP", "Port 123 UDP"], "answer": "Port 53 UDP", "exp": "DNS uses UDP port 53 for standard name resolution queries and TCP port 53 for large zone transfers."},
    {"cat": "1-6", "q": "What network hardware device forwards packets between distinct IP subnets based on Layer 3 routing tables?", "options": ["Layer 2 Switch", "Hub", "Router", "Bridge"], "answer": "Router", "exp": "Routers operate at Layer 3 to route packets across logical network boundaries and isolate broadcast domains."},
    {"cat": "1-6", "q": "What is the decimal dotted-quad subnet mask for a network prefix of /26?", "options": ["255.255.255.0", "255.255.255.128", "255.255.255.192", "255.255.255.224"], "answer": "255.255.255.192", "exp": "A /26 has 26 network bits: 11111111.11111111.11111111.11000000 = 255.255.255.192."},
    {"cat": "1-6", "q": "A client laptop fails to reach a DHCP server and self-assigns the IP address 169.254.42.10. What mechanism assigned this address?", "options": ["DNS", "APIPA", "Static ARP", "NAT"], "answer": "APIPA", "exp": "APIPA automatically assigns an address in the 169.254.0.0/16 range when DHCP discovery fails."},
    {"cat": "1-6", "q": "After confirming a theory of probable cause during troubleshooting, what is the immediate NEXT step in the CompTIA methodology?", "options": ["Document findings", "Verify full system functionality", "Establish a plan of action and identify potential effects", "Implement the solution"], "answer": "Establish a plan of action and identify potential effects", "exp": "Step 4 is establishing a plan of action and considering collateral impacts before making any production changes."},
    {"cat": "1-6", "q": "Which cable standard is mandatory when routing Ethernet cabling through building plenum air-handling spaces?", "options": ["PVC / CM", "Plenum / CMP", "LSZH", "Direct Burial"], "answer": "Plenum / CMP", "exp": "CMP (Plenum-rated) cabling uses low-smoke, fire-retardant materials to prevent toxic fumes in HVAC ducts."},
    {"cat": "1-6", "q": "Which port provides secure, encrypted interactive command-line access to replace legacy Telnet?", "options": ["Port 21", "Port 22", "Port 23", "Port 25"], "answer": "Port 22", "exp": "SSH (Secure Shell) operates on TCP port 22, encrypting terminal sessions to replace unencrypted Telnet (port 23)."},
    {"cat": "1-6", "q": "Which DNS record type acts as an alias, pointing one hostname to another canonical hostname?", "options": ["A Record", "AAAA Record", "CNAME Record", "PTR Record"], "answer": "CNAME Record", "exp": "A CNAME (Canonical Name) record aliases an alternative name to an existing canonical domain name."},

    # --- PART 2: CHAPTERS 7-10 (Wireless, Cloud & Security) ---
    {"cat": "7-10", "q": "Which wireless standard operates exclusively in the 5 GHz radio spectrum?", "options": ["802.11b", "802.11g", "802.11n", "802.11ac"], "answer": "802.11ac", "exp": "802.11ac (Wi-Fi 5) operates exclusively on the 5 GHz band. 802.11n and 802.11ax operate on both bands."},
    {"cat": "7-10", "q": "What type of hypervisor installs directly on bare physical server hardware without a host OS?", "options": ["Type 1 (Bare-Metal)", "Type 2 (Hosted)", "Container Engine", "Virtual Appliance"], "answer": "Type 1 (Bare-Metal)", "exp": "Type 1 hypervisors (e.g., VMware ESXi, Hyper-V) run directly on server hardware for maximum performance."},
    {"cat": "7-10", "q": "A company subscribes to Microsoft 365 for cloud email and office productivity. What cloud model is this?", "options": ["IaaS", "PaaS", "SaaS", "DaaS"], "answer": "SaaS", "exp": "Software as a Service (SaaS) delivers fully managed vendor-hosted applications accessible via browser/client."},
    {"cat": "7-10", "q": "Which attack intercepts and alters communication between two network hosts by poisoning ARP caches?", "options": ["DDoS", "On-Path (Man-in-the-Middle)", "Phishing", "Ransomware"], "answer": "On-Path (Man-in-the-Middle)", "exp": "On-path attacks intercept, monitor, or alter transit traffic between endpoints (e.g., via ARP poisoning)."},
    {"cat": "7-10", "q": "Which protocol monitors device telemetry and query metrics on routers and switches using UDP port 161?", "options": ["SNMP", "SMTP", "SMB", "SIP"], "answer": "SNMP", "exp": "SNMP (Simple Network Management Protocol) polls device health and metrics over UDP port 161."},
    {"cat": "7-10", "q": "What metric represents the average time required to repair and restore a failed system component?", "options": ["MTBF", "MTTR", "RTO", "RPO"], "answer": "MTTR", "exp": "Mean Time To Repair (MTTR) measures the average elapsed time to resolve a failure and restore functionality."},
    {"cat": "7-10", "q": "Which Wi-Fi security protocol introduced Simultaneous Authentication of Equals (SAE) to block dictionary attacks?", "options": ["WEP", "WPA", "WPA2", "WPA3"], "answer": "WPA3", "exp": "WPA3 replaces Pre-Shared Key exchange with SAE to eliminate vulnerability to offline dictionary attacks."},
    {"cat": "7-10", "q": "A backup job archives all files modified since the last FULL backup without clearing the archive bit. What backup type is this?", "options": ["Full", "Incremental", "Differential", "Snapshot"], "answer": "Differential", "exp": "Differential backups copy all files changed since the last full backup and leave archive bits intact."},
    {"cat": "7-10", "q": "Which layer of the OSI model handles data formatting, character encoding, and TLS/SSL encryption?", "options": ["Layer 7", "Layer 6", "Layer 5", "Layer 4"], "answer": "Layer 6", "exp": "Layer 6 (Presentation) formats, compresses, and encrypts/decrypts data payloads for application delivery."},
    {"cat": "7-10", "q": "A network administrator needs to transfer files securely over an encrypted SSH channel. Which protocol should be used?", "options": ["FTP", "TFTP", "SFTP", "FTPS"], "answer": "SFTP", "exp": "SFTP (SSH File Transfer Protocol) runs inside an encrypted SSH tunnel over TCP port 22."},
    {"cat": "7-10", "q": "Which physical device can be deployed to filter incoming network traffic based on IP addresses and port numbers?", "options": ["Layer 2 Switch", "Hub", "Firewall", "Access Point"], "answer": "Firewall", "exp": "Firewalls evaluate Access Control Lists (ACLs) and state tables to filter traffic by IP, port, and protocol."},
    {"cat": "7-10", "q": "What centralized protocol collects event notifications and system logs from routers and switches over UDP port 514?", "options": ["Syslog", "SNMP", "RADIUS", "NTP"], "answer": "Syslog", "exp": "Syslog standardizes system event logging, aggregating messages to centralized collectors on UDP 514."},
    {"cat": "7-10", "q": "What is the primary operational objective of establishing a formal network performance baseline?", "options": ["Upgrade firmware", "Compare normal traffic patterns against anomalies", "Block MAC addresses", "Configure IPsec tunnels"], "answer": "Compare normal traffic patterns against anomalies", "exp": "Baselines document normal operational metrics, allowing engineers to spot anomalies and plan capacity."},
    {"cat": "7-10", "q": "Which wireless frequency band provides superior range and wall penetration at the cost of lower throughput?", "options": ["5 GHz", "2.4 GHz", "6 GHz", "60 GHz"], "answer": "2.4 GHz", "exp": "Lower frequency radio waves (2.4 GHz) travel farther and penetrate walls better than higher frequency 5 GHz waves."},
    {"cat": "7-10", "q": "A network engineer needs to subnet 192.168.10.0/24 to support exactly 30 usable hosts per subnet. What CIDR notation is required?", "options": ["/26", "/27", "/28", "/29"], "answer": "/27", "exp": "A /27 mask leaves 5 host bits: 2^5 - 2 = 32 - 2 = 30 usable host addresses per subnet."},
    {"cat": "7-10", "q": "Which email protocol downloads messages to a local client and typically deletes them from the central mail server?", "options": ["POP3", "IMAP", "SMTP", "SNMP"], "answer": "POP3", "exp": "POP3 (port 110) downloads email locally and deletes server copies, unlike IMAP (port 143) which syncs."},
    {"cat": "7-10", "q": "Which attack floods a target with spoofed traffic from thousands of compromised distributed botnet devices?", "options": ["Phishing", "DDoS", "Ransomware", "SQL Injection"], "answer": "DDoS", "exp": "Distributed Denial of Service (DDoS) leverages distributed botnets to overwhelm bandwidth or compute capacity."},
    {"cat": "7-10", "q": "Immediately after implementing a solution to fix a network fault, what is the next step in the CompTIA methodology?", "options": ["Document findings", "Verify full system functionality and implement preventive measures", "Test the theory", "Identify the problem"], "answer": "Verify full system functionality and implement preventive measures", "exp": "Step 6 requires verifying that the system is fully functional with the user and applying preventive controls."},
    {"cat": "7-10", "q": "What spanning-tree protocol standard (IEEE 802.1w) provides fast convergence to prevent Layer 2 switching loops?", "options": ["STP (802.1D)", "RSTP (802.1w)", "LACP (802.3ad)", "VLAN (802.1Q)"], "answer": "RSTP (802.1w)", "exp": "Rapid Spanning Tree Protocol (RSTP / 802.1w) provides sub-second convergence to eliminate switching loops."},
    {"cat": "7-10", "q": "Which IPv6 address represents the equivalent of the IPv4 loopback address 127.0.0.1?", "options": ["::1", "fe80::1", "2001::1", "ff02::1"], "answer": "::1", "exp": "The IPv6 loopback address is written as ::1 (0000:0000:0000:0000:0000:0000:0000:0001)."},

    # --- PART 3: CHAPTERS 11-14 (Routing, Hardening & Architecture) ---
    {"cat": "11-end", "q": "What is the default Administrative Distance (AD) of the Open Shortest Path First (OSPF) routing protocol?", "options": ["90", "110", "120", "20"], "answer": "110", "exp": "OSPF has an AD of 110. EIGRP is 90, RIP is 120, and eBGP is 20."},
    {"cat": "11-end", "q": "Which Layer 2 switch security feature mitigates ARP cache poisoning by checking ARP packets against trusted bindings?", "options": ["BPDU Guard", "DHCP Snooping", "Dynamic ARP Inspection (DAI)", "Port Fast"], "answer": "Dynamic ARP Inspection (DAI)", "exp": "DAI intercepts, inspects, and validates ARP packets against the DHCP Snooping database to block invalid mappings."},
    {"cat": "11-end", "q": "What data center switching topology connects every leaf switch to every spine switch for optimized East-West traffic?", "options": ["Spine-and-Leaf", "Ring Topology", "Star Topology", "Bus Topology"], "answer": "Spine-and-Leaf", "exp": "Spine-and-Leaf provides high-bandwidth, deterministic single-hop latency between all servers across data centers."},
    {"cat": "11-end", "q": "Which exterior gateway routing protocol utilizes TCP port 179 to connect global Autonomous Systems?", "options": ["OSPF", "IS-IS", "BGP", "EIGRP"], "answer": "BGP", "exp": "Border Gateway Protocol (BGP) forms reliable neighbor adjacencies over TCP port 179."},
    {"cat": "11-end", "q": "What 6-bit field in the IPv4 packet header is used by DiffServ architecture to provide Layer 3 QoS prioritization?", "options": ["TTL", "DSCP", "CoS", "Total Length"], "answer": "DSCP", "exp": "Differentiated Services Code Point (DSCP) uses 6 bits in the IP header to specify per-hop traffic prioritization."},
    {"cat": "11-end", "q": "Which First Hop Redundancy Protocol (FHRP) is an open IETF standard for default gateway redundancy?", "options": ["HSRP", "GLBP", "VRRP", "CARP"], "answer": "VRRP", "exp": "Virtual Router Redundancy Protocol (VRRP) is the open industry standard; HSRP and GLBP are Cisco proprietary."},
    {"cat": "11-end", "q": "In Software-Defined Networking (SDN), which API type links the central controller to the underlying physical data plane switches?", "options": ["Northbound API", "Southbound API", "Eastbound API", "RESTful Webhook"], "answer": "Southbound API", "exp": "Southbound APIs (e.g., OpenFlow) communicate downward from the controller to control data plane hardware."},
    {"cat": "11-end", "q": "What switch feature prevents unauthorized DHCP servers by blocking DHCP server offer packets on untrusted ports?", "options": ["DHCP Snooping", "Port Security", "802.1X", "IP Source Guard"], "answer": "DHCP Snooping", "exp": "DHCP Snooping designates switch ports as trusted or untrusted, dropping rogue DHCP server broadcasts."},
    {"cat": "11-end", "q": "What WAN technology uses short path labels rather than complex routing table lookups to forward Layer 2.5 traffic?", "options": ["MPLS", "Frame Relay", "ATM", "Dial-up"], "answer": "MPLS", "exp": "Multiprotocol Label Switching (MPLS) assigns short labels to packets for fast forwarding across telecom backbones."},
    {"cat": "11-end", "q": "What formal agreement defines mandatory service uptime percentages, mean-time-to-respond, and penalties from an ISP?", "options": ["AUP", "SLA", "NDA", "MOU"], "answer": "SLA", "exp": "A Service Level Agreement (SLA) is a legally binding contract defining measurable service metrics and remedies."},
    {"cat": "11-end", "q": "Which security philosophy assumes network breaches are inevitable and mandates continuous verification of all entities?", "options": ["Defense in Depth", "Zero Trust", "Air-gapping", "Least Privilege"], "answer": "Zero Trust", "exp": "Zero Trust enforces 'Never trust, always verify', requiring continuous authentication and microsegmentation."},
    {"cat": "11-end", "q": "What fire suppression system type utilizes clean chemical gas agents to protect electrical server hardware from water damage?", "options": ["Wet-pipe sprinkler", "Dry-pipe sprinkler", "Clean-Agent Gas (FM-200/Inergen)", "Deluge system"], "answer": "Clean-Agent Gas (FM-200/Inergen)", "exp": "Clean-agent gas systems extinguish electrical fires by heat absorption without leaving conductive water residue."},
    {"cat": "11-end", "q": "How many total physical cable links are required to build a fully redundant full mesh network with 6 nodes?", "options": ["6", "12", "15", "30"], "answer": "15", "exp": "Full mesh formula: n(n - 1) / 2 -> 6(5) / 2 = 30 / 2 = 15 total links."},
    {"cat": "11-end", "q": "What port security mode drops violating packets and transitions the switch port into an err-disabled shutdown state?", "options": ["Protect", "Restrict", "Shutdown", "Monitor"], "answer": "Shutdown", "exp": "The 'Shutdown' violation mode disables the interface completely, requiring admin intervention or auto-recovery."},
    {"cat": "11-end", "q": "Which technology aggregates multiple physical network connections into a single logical channel using the IEEE 802.3ad standard?", "options": ["LACP", "STP", "LLDP", "CDP"], "answer": "LACP", "exp": "Link Aggregation Control Protocol (LACP - 802.3ad) provides combined link bandwidth and automatic link failover."}
]

class StudyTab(ttk.Frame):
    def __init__(self, parent, chapter_name):
        super().__init__(parent)
        self.chapter_name = chapter_name
        self.questions = QUIZ_DATA.get(chapter_name, [])
        self.current_q_index = 0
        
        # Bottom flashcard container
        quiz_frame = ttk.LabelFrame(self, text="Practice Flashcards")
        quiz_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False, padx=10, pady=(5, 10))
        
        text_frame = ttk.Frame(quiz_frame)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 10), pady=15)
        
        btn_frame = ttk.Frame(quiz_frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 20), pady=15)
        
        self.lbl_progress = tk.Label(text_frame, text="", font=("Helvetica", 9, "bold"), fg="#7f8c8d", justify="left")
        self.lbl_progress.pack(anchor="w", pady=(0, 2))

        self.lbl_question = tk.Label(text_frame, text="", font=("Helvetica", 11, "bold"), wraplength=480, justify="left", height=2)
        self.lbl_question.pack(anchor="w", pady=(2, 5))
        
        self.lbl_answer = tk.Label(text_frame, text="", font=("Helvetica", 11, "italic"), fg="#27ae60", wraplength=480, justify="left", height=2)
        self.lbl_answer.pack(anchor="w", pady=(0, 5))
        
        self.btn_show = ttk.Button(btn_frame, text="Show Answer", command=self.show_answer)
        self.btn_show.pack(fill=tk.X, pady=(5, 5))
        
        self.btn_next = ttk.Button(btn_frame, text="Next Question", command=self.next_question)
        self.btn_next.pack(fill=tk.X, pady=(5, 5))

        # Top summary container
        notes_frame = ttk.LabelFrame(self, text="Chapter Summary")
        notes_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        
        self.notes_text = tk.Text(
            notes_frame, 
            wrap=tk.WORD, 
            font=("Helvetica", 10), 
            padx=18, 
            pady=18, 
            spacing1=4,
            spacing2=3,
            spacing3=4,
            relief=tk.FLAT
        )
        self.notes_text.insert(tk.END, CHAPTER_CONTENT.get(chapter_name, "No content available."))
        self.notes_text.config(state=tk.DISABLED)
        self.notes_text.pack(fill=tk.BOTH, expand=True)
        
        random.shuffle(self.questions)
        self.load_question()

    def update_theme(self, bg_text, fg_main, fg_accent):
        self.notes_text.config(bg=bg_text, fg=fg_main)
        self.lbl_answer.config(fg=fg_accent)

    def load_question(self, reset_color=False):
        if reset_color:
            self.lbl_progress.config(fg="#7f8c8d")
            self.btn_show.config(state=tk.NORMAL)
            self.btn_next.config(state=tk.NORMAL)

        if self.questions:
            q, _ = self.questions[self.current_q_index]
            total = len(self.questions)
            current = self.current_q_index + 1
            
            if self.lbl_progress.cget("text") != "Deck Completed! Reshuffling...":
                self.lbl_progress.config(text=f"Card {current} of {total}")
            
            self.lbl_question.config(text=f"Q: {q}")
            self.lbl_answer.config(text="?")
            self.btn_show.config(state=tk.NORMAL)
        else:
            self.lbl_progress.config(text="No cards available.")
            self.lbl_question.config(text="No questions available.")

    def show_answer(self):
        if self.questions:
            _, a = self.questions[self.current_q_index]
            self.lbl_answer.config(text=f"A: {a}")
            self.btn_show.config(state=tk.DISABLED)

    def next_question(self):
        if self.questions:
            next_index = self.current_q_index + 1
            
            if next_index >= len(self.questions):
                self.current_q_index = 0
                random.shuffle(self.questions)
                
                self.lbl_progress.config(text="Deck Completed! Reshuffling...", fg="#27ae60")
                self.lbl_question.config(text="")
                self.lbl_answer.config(text="")
                self.btn_show.config(state=tk.DISABLED)
                self.btn_next.config(state=tk.DISABLED)
                
                self.after(1200, lambda: self.load_question(reset_color=True))
            else:
                self.current_q_index = next_index
                self.load_question()

class GlossaryTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        tk.Label(search_frame, text="Search Term:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_list)
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, font=("Helvetica", 11))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        list_frame = ttk.Frame(paned)
        paned.add(list_frame, weight=1)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(list_frame, font=("Helvetica", 10), yscrollcommand=scrollbar.set, selectbackground="#3498db")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        self.listbox.bind("<<ListboxSelect>>", self.show_definition)
        
        def_frame = ttk.LabelFrame(paned, text="Definition & Exam Context")
        paned.add(def_frame, weight=2)
        
        self.def_text = tk.Text(
            def_frame, 
            wrap=tk.WORD, 
            font=("Helvetica", 11), 
            padx=18, 
            pady=18, 
            spacing1=6,
            spacing2=4,
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.def_text.pack(fill=tk.BOTH, expand=True)

        self.all_terms = sorted(GLOSSARY_TERMS.keys())
        self.update_listbox(self.all_terms)

    def update_theme(self, bg_text, fg_main, bg_alt):
        self.listbox.config(bg=bg_text, fg=fg_main)
        self.def_text.config(bg=bg_text, fg=fg_main)

    def filter_list(self, *args):
        query = self.search_var.get().lower()
        if not query:
            self.update_listbox(self.all_terms)
        else:
            filtered = [term for term in self.all_terms if query in term.lower()]
            self.update_listbox(filtered)

    def update_listbox(self, items):
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)

    def show_definition(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
            
        term = self.listbox.get(selection[0])
        definition = GLOSSARY_TERMS.get(term, "Definition not found.")
        
        self.def_text.config(state=tk.NORMAL)
        self.def_text.delete(1.0, tk.END)
        self.def_text.insert(tk.END, f"{term}\n\n", "bold")
        self.def_text.insert(tk.END, definition)
        self.def_text.tag_configure("bold", font=("Helvetica", 12, "bold"))
        self.def_text.config(state=tk.DISABLED)

class PracticeTestTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_test = []
        self.current_q_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()
        self.exam_mode = tk.StringVar(value="full")
        
        self.header_lbl = tk.Label(self, text="CompTIA Practice Simulator", font=("Helvetica", 14, "bold"))
        self.header_lbl.pack(pady=(15, 2))
        
        self.progress_lbl = tk.Label(self, text="", font=("Helvetica", 10), fg="#7f8c8d")
        self.progress_lbl.pack(pady=(0, 15))
        
        self.q_frame = ttk.Frame(self)
        self.q_frame.pack(fill=tk.BOTH, expand=True, padx=30)
        
        self.start_frame = ttk.Frame(self.q_frame)
        self.start_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        tk.Label(self.start_frame, text="Select Exam Study Domain:", font=("Helvetica", 12, "bold")).pack(pady=(0, 15))
        
        cnt_1_6 = len([q for q in PRACTICE_TEST_BANK if q["cat"] == "1-6"])
        cnt_7_10 = len([q for q in PRACTICE_TEST_BANK if q["cat"] == "7-10"])
        cnt_11_end = len([q for q in PRACTICE_TEST_BANK if q["cat"] == "11-end"])
        cnt_full = len(PRACTICE_TEST_BANK)

        ttk.Radiobutton(self.start_frame, text=f"Part 1: Foundations & VLANs (Ch 1–6) — {cnt_1_6} Questions", variable=self.exam_mode, value="1-6").pack(anchor="w", padx=120, pady=5)
        ttk.Radiobutton(self.start_frame, text=f"Part 2: Wireless, Cloud & Security (Ch 7–10) — {cnt_7_10} Questions", variable=self.exam_mode, value="7-10").pack(anchor="w", padx=120, pady=5)
        ttk.Radiobutton(self.start_frame, text=f"Part 3: Routing, Hardening & Arch (Ch 11–14) — {cnt_11_end} Questions", variable=self.exam_mode, value="11-end").pack(anchor="w", padx=120, pady=5)
        ttk.Radiobutton(self.start_frame, text=f"Full Practice Exam (All Chapters Combined) — {cnt_full} Questions", variable=self.exam_mode, value="full").pack(anchor="w", padx=120, pady=5)
        
        ttk.Button(self.start_frame, text="Begin Selected Exam", command=self.start_new_test).pack(pady=25)
        
        self.lbl_question = tk.Label(self.q_frame, text="", font=("Helvetica", 11, "bold"), wraplength=600, justify="left")
        self.radio_btns = []
        for _ in range(4):
            rb = ttk.Radiobutton(self.q_frame, text="", variable=self.selected_answer, value="")
            self.radio_btns.append(rb)
            
        self.feedback_lbl = tk.Label(self.q_frame, text="", font=("Helvetica", 11, "bold"), wraplength=600, justify="left")
        self.exp_lbl = tk.Label(self.q_frame, text="", font=("Helvetica", 10, "italic"), wraplength=600, justify="left")
        
        self.controls_frame = ttk.Frame(self)
        
        self.btn_submit = ttk.Button(self.controls_frame, text="Submit Answer", command=self.submit_answer)
        self.btn_next = ttk.Button(self.controls_frame, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.btn_restart = ttk.Button(self.controls_frame, text="Return to Menu", command=self.show_menu)

    def update_theme(self, fg_main, bg_main):
        self.header_lbl.config(fg=fg_main, bg=bg_main)
        self.lbl_question.config(fg=fg_main, bg=bg_main)
        self.progress_lbl.config(bg=bg_main)
        self.feedback_lbl.config(bg=bg_main)
        self.exp_lbl.config(fg=fg_main, bg=bg_main)

    def show_menu(self):
        self.controls_frame.pack_forget()
        self.lbl_question.pack_forget()
        self.feedback_lbl.pack_forget()
        self.exp_lbl.pack_forget()
        for rb in self.radio_btns:
            rb.pack_forget()
            
        self.progress_lbl.config(text="")
        self.start_frame.pack(fill=tk.BOTH, expand=True, pady=20)

    def start_new_test(self):
        self.start_frame.pack_forget()
        
        self.lbl_question.pack(anchor="w", pady=(0, 15))
        self.feedback_lbl.pack(anchor="w", pady=(15, 5))
        self.exp_lbl.pack(anchor="w", pady=(0, 15))
        self.controls_frame.pack(fill=tk.X, padx=30, pady=15)
        
        self.btn_restart.pack_forget()
        self.btn_submit.pack(side=tk.LEFT, padx=(0, 10))
        self.btn_next.pack(side=tk.LEFT)

        mode = self.exam_mode.get()
        if mode == "full":
            pool = PRACTICE_TEST_BANK
        else:
            pool = [q for q in PRACTICE_TEST_BANK if q["cat"] == mode]

        self.current_test = random.sample(pool, len(pool))
        self.current_q_index = 0
        self.score = 0
        
        self.load_question()
        
    def load_question(self):
        self.selected_answer.set("") 
        self.feedback_lbl.config(text="")
        self.exp_lbl.config(text="")
        self.btn_submit.config(state=tk.NORMAL)
        self.btn_next.config(state=tk.DISABLED)
        self.btn_next.config(text="Next Question")
        
        for rb in self.radio_btns:
            rb.config(state=tk.NORMAL)
        
        q_data = self.current_test[self.current_q_index]
        self.progress_lbl.config(text=f"Question {self.current_q_index + 1} of {len(self.current_test)} | Current Score: {self.score}")
        self.lbl_question.config(text=q_data["q"])
        
        options = q_data["options"].copy()
        random.shuffle(options)
        
        for i, rb in enumerate(self.radio_btns):
            if i < len(options):
                rb.config(text=options[i], value=options[i])
                rb.pack(anchor="w", pady=4, before=self.feedback_lbl)
            else:
                rb.pack_forget() 

    def submit_answer(self):
        selected = self.selected_answer.get()
        if not selected:
            self.feedback_lbl.config(text="Please select an option before submitting!", fg="#e74c3c")
            return
            
        q_data = self.current_test[self.current_q_index]
        self.btn_submit.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL)
        
        for rb in self.radio_btns:
            rb.config(state=tk.DISABLED)
            
        if selected == q_data["answer"]:
            self.score += 1
            self.feedback_lbl.config(text="✅ Correct!", fg="#27ae60")
        else:
            self.feedback_lbl.config(text=f"❌ Incorrect. Correct answer: {q_data['answer']}", fg="#c0392b")
            
        self.exp_lbl.config(text=f"Explanation: {q_data['exp']}")
        self.progress_lbl.config(text=f"Question {self.current_q_index + 1} of {len(self.current_test)} | Current Score: {self.score}")
        
        if self.current_q_index >= len(self.current_test) - 1:
            self.btn_next.config(text="Finish Exam")

    def next_question(self):
        self.current_q_index += 1
        if self.current_q_index < len(self.current_test):
            self.load_question()
        else:
            self.show_results()
            
    def show_results(self):
        self.lbl_question.config(text=f"Exam Simulation Complete!\n\nFinal Score: {self.score} out of {len(self.current_test)}")
        percent = (self.score / len(self.current_test)) * 100
        
        if percent >= 85:
            msg = f"Score: {percent:.1f}% - Excellent! Fully prepared for Network+."
            color = "#27ae60"
        elif percent >= 75:
            msg = f"Score: {percent:.1f}% - Passing! Review missed concepts in flashcards."
            color = "#2980b9"
        else:
            msg = f"Score: {percent:.1f}% - Needs review. Re-visit Chapter Summaries & Glossary."
            color = "#f39c12"
            
        self.feedback_lbl.config(text=msg, fg=color)
        self.exp_lbl.config(text="")
        self.progress_lbl.config(text="")
        
        for rb in self.radio_btns:
            rb.pack_forget()
            
        self.btn_submit.pack_forget()
        self.btn_next.pack_forget()
        self.btn_restart.pack(side=tk.LEFT)

class GlobalSearchTab(ttk.Frame):
    def __init__(self, parent, notebook_ref, chapter_map):
        super().__init__(parent)
        self.notebook = notebook_ref
        self.chapter_map = chapter_map
        
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        tk.Label(search_frame, text="Search All Content:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.perform_search)
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, font=("Helvetica", 11))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.lbl_count = tk.Label(search_frame, text="Type to search...", font=("Helvetica", 9, "italic"), fg="#7f8c8d")
        self.lbl_count.pack(side=tk.RIGHT, padx=(10, 0))

        paned = ttk.PanedWindow(self, orient=tk.VERTICAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        # Results Table
        tree_frame = ttk.Frame(paned)
        paned.add(tree_frame, weight=2)
        
        columns = ("Type", "Location", "Match")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8)
        self.tree.heading("Type", text="Type")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Match", text="Matched Snippet")
        
        self.tree.column("Type", width=110, anchor="center")
        self.tree.column("Location", width=140)
        self.tree.column("Match", width=580)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<<TreeviewSelect>>", self.on_result_select)
        self.tree.bind("<Double-1>", self.jump_to_source)
        
        # Preview Pane
        preview_frame = ttk.LabelFrame(paned, text="Matched Context / Details (Double-click item to Jump)")
        paned.add(preview_frame, weight=3)
        
        self.txt_preview = tk.Text(
            preview_frame,
            wrap=tk.WORD,
            font=("Helvetica", 10),
            padx=15,
            pady=15,
            spacing1=4,
            spacing2=2,
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.txt_preview.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        btn_bar = ttk.Frame(preview_frame)
        btn_bar.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        
        self.btn_jump = ttk.Button(btn_bar, text="Jump to Tab", command=self.jump_to_source, state=tk.DISABLED)
        self.btn_jump.pack(anchor="n")
        
        self.stored_results = []

    def update_theme(self, bg_text, fg_main, bg_alt):
        self.txt_preview.config(bg=bg_text, fg=fg_main)

    def perform_search(self, *args):
        query = self.search_var.get().strip().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.stored_results.clear()
        self.txt_preview.config(state=tk.NORMAL)
        self.txt_preview.delete(1.0, tk.END)
        self.txt_preview.config(state=tk.DISABLED)
        self.btn_jump.config(state=tk.DISABLED)
        
        if not query or len(query) < 2:
            self.lbl_count.config(text="Type at least 2 characters...")
            return

        matches = []
        
        # 1. Search Chapter Summaries
        for ch, text in CHAPTER_CONTENT.items():
            if query in text.lower() or query in ch.lower():
                snippet = self.extract_snippet(text, query)
                matches.append({
                    "type": "Chapter",
                    "loc": ch.split(":")[0],
                    "match": snippet,
                    "full": f"--- {ch} ---\n\n{text}",
                    "tab_target": ch.split(":")[0]
                })

        # 2. Search Flashcards
        for ch, cards in QUIZ_DATA.items():
            for q, a in cards:
                if query in q.lower() or query in a.lower():
                    matches.append({
                        "type": "Flashcard",
                        "loc": ch.split(":")[0],
                        "match": f"Q: {q}",
                        "full": f"--- Flashcard ({ch}) ---\n\nQ: {q}\n\nA: {a}",
                        "tab_target": ch.split(":")[0]
                    })

        # 3. Search Glossary
        for term, defn in GLOSSARY_TERMS.items():
            if query in term.lower() or query in defn.lower():
                matches.append({
                    "type": "Glossary",
                    "loc": "Glossary",
                    "match": term,
                    "full": f"--- Glossary Term ---\n\n{term}\n\n{defn}",
                    "tab_target": "📖 Glossary"
                })

        # 4. Search Exam Bank
        for idx, q in enumerate(PRACTICE_TEST_BANK):
            q_text = q["q"]
            exp = q["exp"]
            ans = q["answer"]
            opts = " | ".join(q["options"])
            if query in q_text.lower() or query in exp.lower() or query in ans.lower():
                matches.append({
                    "type": "Exam Q",
                    "loc": f"Domain {q['cat']}",
                    "match": q_text[:80] + "...",
                    "full": f"--- Practice Exam Question (Domain {q['cat']}) ---\n\nQ: {q_text}\n\nOptions: {opts}\n\nAnswer: {ans}\n\nExplanation: {exp}",
                    "tab_target": "🎓 Exam Simulator"
                })

        self.stored_results = matches
        self.lbl_count.config(text=f"{len(matches)} match{'es' if len(matches) != 1 else ''} found")

        for idx, m in enumerate(matches):
            self.tree.insert("", "end", iid=str(idx), values=(f"[{m['type']}]", m['loc'], m['match']))

    def extract_snippet(self, text, query):
        idx = text.lower().find(query)
        if idx == -1:
            return text[:90].replace("\n", " ") + "..."
        start = max(0, idx - 30)
        end = min(len(text), idx + len(query) + 50)
        snippet = text[start:end].replace("\n", " ").strip()
        return ("..." if start > 0 else "") + snippet + ("..." if end < len(text) else "")

    def on_result_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        idx = int(selected[0])
        data = self.stored_results[idx]
        
        self.txt_preview.config(state=tk.NORMAL)
        self.txt_preview.delete(1.0, tk.END)
        self.txt_preview.insert(tk.END, data["full"])
        self.txt_preview.config(state=tk.DISABLED)
        self.btn_jump.config(state=tk.NORMAL)

    def jump_to_source(self, event=None):
        selected = self.tree.selection()
        if not selected:
            return
        idx = int(selected[0])
        data = self.stored_results[idx]
        target_tab = data["tab_target"]
        
        # Locate tab index by text
        for tab_id in self.notebook.tabs():
            if self.notebook.tab(tab_id, "text") == target_tab:
                self.notebook.select(tab_id)
                break

class NetworkStudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Network+ Comprehensive Study System - Build {APP_VERSION}")
        self.root.geometry("960x860")
        
        self.is_dark_mode = False
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # 1. Header
        self.header_frame = tk.Frame(root, pady=12)
        self.header_frame.pack(fill=tk.X, side=tk.TOP)
        
        self.header_title = tk.Label(self.header_frame, text="CompTIA Network+ Study Suite", font=("Helvetica", 15, "bold"))
        self.header_title.pack(side=tk.LEFT, padx=20)
        
        self.btn_theme = ttk.Button(self.header_frame, text="🌙 Dark Mode", command=self.toggle_theme)
        self.btn_theme.pack(side=tk.RIGHT, padx=20)
        
        # 2. Footer
        self.footer_frame = tk.Frame(root, pady=5)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_text = f"Built by {AUTHOR} | {BUILD_DATE} | Build {APP_VERSION}"
        self.footer_label = tk.Label(self.footer_frame, text=footer_text, font=("Helvetica", 8, "bold"))
        self.footer_label.pack()

        # 3. Notebook Tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Global Search Tab (First Tab)
        self.search_tab = GlobalSearchTab(self.notebook, self.notebook, CHAPTER_CONTENT)
        self.notebook.add(self.search_tab, text="🔍 Search All")

        self.chapter_tabs = []
        for chapter in CHAPTER_CONTENT.keys():
            tab = StudyTab(self.notebook, chapter)
            short_name = chapter.split(":")[0] 
            self.notebook.add(tab, text=short_name)
            self.chapter_tabs.append(tab)
            
        self.glossary_tab = GlossaryTab(self.notebook)
        self.notebook.add(self.glossary_tab, text="📖 Glossary")
            
        self.test_tab = PracticeTestTab(self.notebook)
        self.notebook.add(self.test_tab, text="🎓 Exam Simulator")
        
        self.apply_theme()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            bg_main = "#23272a"
            fg_main = "#e0e0e0"
            bg_alt = "#2c2f33"
            bg_text = "#18191c"
            head_bg = "#1e2124"
            head_fg = "#ffffff"
            accent_fg = "#2ecc71"
            btn_text = "☀️ Light Mode"
        else:
            bg_main = "#f4f6f9"
            fg_main = "#2c3e50"
            bg_alt = "#e2e6ea"
            bg_text = "#ffffff"
            head_bg = "#34495e"
            head_fg = "#ffffff"
            accent_fg = "#27ae60"
            btn_text = "🌙 Dark Mode"
            
        self.btn_theme.config(text=btn_text)
        self.root.config(bg=bg_main)
        self.header_frame.config(bg=head_bg)
        self.header_title.config(bg=head_bg, fg=head_fg)
        self.footer_frame.config(bg=head_bg)
        self.footer_label.config(bg=head_bg, fg="#95a5a6")
        
        self.style.configure('TFrame', background=bg_main)
        self.style.configure('TLabel', background=bg_main, foreground=fg_main)
        self.style.configure('TButton', background=bg_alt, foreground=fg_main)
        self.style.configure('TNotebook', background=bg_main)
        self.style.configure('TNotebook.Tab', background=bg_alt, foreground=fg_main, padding=[5, 2])
        self.style.map('TNotebook.Tab', background=[('selected', bg_main)])
        
        self.style.configure("Treeview", background=bg_text, foreground=fg_main, fieldbackground=bg_text)
        self.style.configure("Treeview.Heading", background=bg_alt, foreground=fg_main)

        self.search_tab.update_theme(bg_text, fg_main, bg_alt)
        for tab in self.chapter_tabs:
            tab.update_theme(bg_text, fg_main, accent_fg)
            
        self.glossary_tab.update_theme(bg_text, fg_main, bg_alt)
        self.test_tab.update_theme(fg_main, bg_main)

def main():
    root = tk.Tk()
    app = NetworkStudyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
