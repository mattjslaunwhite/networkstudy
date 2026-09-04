import tkinter as tk
from tkinter import ttk, messagebox

class NetworkWonderlandApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alice's Network Troubleshooting Lab - Day 15")
        self.geometry("860x660")
        self.resizable(False, False)

        # Style configuration
        style = ttk.Style(self)
        style.theme_use("clam")
        
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Tabs
        self.tab_ping = ttk.Frame(notebook)
        self.tab_cables = ttk.Frame(notebook)
        self.tab_tools = ttk.Frame(notebook)
        self.tab_method = ttk.Frame(notebook)
        self.tab_study = ttk.Frame(notebook)

        notebook.add(self.tab_ping, text="1. The Ping Ladder")
        notebook.add(self.tab_cables, text="2. Cable & Link Tester")
        notebook.add(self.tab_tools, text="3. Tool Matcher")
        notebook.add(self.tab_method, text="4. 7-Step Method")
        notebook.add(self.tab_study, text="5. Study Notes & Facts")

        self.build_ping_tab()
        self.build_cables_tab()
        self.build_tools_tab()
        self.build_method_tab()
        self.build_study_tab()

    # -------------------------------------------------------------
    # TAB 1: Ping Ladder Simulator
    # -------------------------------------------------------------
    def build_ping_tab(self):
        frame = ttk.LabelFrame(self.tab_ping, text="Simulate the Step-by-Step Diagnostic Ladder", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        desc = (
            "Select an injected fault to see how the 'Ping Ladder' isolates the exact failure point:\n"
            "• Step 1: Default Gateway (Tests local router & link)\n"
            "• Step 2: 8.8.8.8 (Tests routing beyond gateway to public Internet)\n"
            "• Step 3: google.ca (Tests DNS name resolution)"
        )
        ttk.Label(frame, text=desc, justify="left", wraplength=800).pack(anchor="w", pady=(0, 10))

        scenario_frame = ttk.Frame(frame)
        scenario_frame.pack(fill="x", pady=5)
        ttk.Label(scenario_frame, text="Inject Network Fault: ").pack(side="left")

        self.fault_var = tk.StringVar(value="None (Healthy Network)")
        faults = [
            "None (Healthy Network)",
            "Unplugged Cable / Bad Local Switch",
            "ISP / Default Gateway Outage",
            "Broken DNS Server Configuration"
        ]
        fault_menu = ttk.Combobox(scenario_frame, textvariable=self.fault_var, values=faults, state="readonly", width=35)
        fault_menu.pack(side="left", padx=5)

        run_btn = ttk.Button(scenario_frame, text="Run Diagnostic Ladder", command=self.run_ping_ladder)
        run_btn.pack(side="left", padx=10)

        self.ping_terminal = tk.Text(frame, height=16, bg="#1e1e1e", fg="#4af626", font=("Consolas", 10), insertbackground="white")
        self.ping_terminal.pack(fill="both", expand=True, pady=10)

    def run_ping_ladder(self):
        fault = self.fault_var.get()
        self.ping_terminal.delete("1.0", tk.END)
        self.ping_terminal.insert(tk.END, f"[*] Diagnostic initiated with state: {fault}\n")
        self.ping_terminal.insert(tk.END, "------------------------------------------------------------\n")

        self.ping_terminal.insert(tk.END, "[Step 1] ping 192.168.1.1 (Default Gateway)... ")
        if fault == "Unplugged Cable / Bad Local Switch":
            self.ping_terminal.insert(tk.END, "FAILED! Destination Host Unreachable.\n")
            self.ping_terminal.insert(tk.END, "\n[-] DIAGNOSIS: Physical layer / LAN issue! Link light is off or switch is down.\n")
            return
        self.ping_terminal.insert(tk.END, "SUCCESS (2ms, TTL=64)\n")

        self.ping_terminal.insert(tk.END, "[Step 2] ping 8.8.8.8 (Public Internet IP)... ")
        if fault == "ISP / Default Gateway Outage":
            self.ping_terminal.insert(tk.END, "FAILED! Request timed out.\n")
            self.ping_terminal.insert(tk.END, "\n[-] DIAGNOSIS: Local LAN works, but no path out! Check router NAT/ISP link.\n")
            return
        self.ping_terminal.insert(tk.END, "SUCCESS (18ms, TTL=118)\n")

        self.ping_terminal.insert(tk.END, "[Step 3] ping google.ca (DNS Name Resolution)... ")
        if fault == "Broken DNS Server Configuration":
            self.ping_terminal.insert(tk.END, "FAILED! Ping request could not find host google.ca.\n")
            self.ping_terminal.insert(tk.END, "\n[-] DIAGNOSIS: IP routing works, but DNS cannot translate names! Run nslookup/dig.\n")
            return
        self.ping_terminal.insert(tk.END, "SUCCESS (19ms, TTL=118)\n")

        self.ping_terminal.insert(tk.END, "\n[+] ALL CLEAR: Physical, LAN, Gateway, WAN, and DNS resolution fully operational!\n")

    # -------------------------------------------------------------
    # TAB 2: Cable Distance & Speed Evaluator
    # -------------------------------------------------------------
    def build_cables_tab(self):
        frame = ttk.LabelFrame(self.tab_cables, text="Ethernet Cable & Hardware Bottleneck Calculator", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        grid = ttk.Frame(frame)
        grid.pack(anchor="w", pady=5)

        ttk.Label(grid, text="Cable Standard:").grid(row=0, column=0, sticky="w", pady=5)
        self.cable_std = tk.StringVar(value="Cat6")
        ttk.Combobox(grid, textvariable=self.cable_std, values=["Cat6", "Cat6a"], state="readonly", width=15).grid(row=0, column=1, padx=10)

        ttk.Label(grid, text="Cable Run Length (Meters):").grid(row=1, column=0, sticky="w", pady=5)
        self.cable_dist = tk.IntVar(value=60)
        ttk.Spinbox(grid, from_=1, to=150, textvariable=self.cable_dist, width=15).grid(row=1, column=1, padx=10)

        ttk.Label(grid, text="Computer NIC Speed:").grid(row=2, column=0, sticky="w", pady=5)
        self.nic_speed = tk.StringVar(value="1 Gbps")
        ttk.Combobox(grid, textvariable=self.nic_speed, values=["1 Gbps", "10 Gbps"], state="readonly", width=15).grid(row=2, column=1, padx=10)

        ttk.Button(frame, text="Evaluate Link Negotiation", command=self.eval_cable).pack(anchor="w", pady=10)

        self.cable_result = ttk.Label(frame, text="", font=("Segoe UI", 10, "bold"), justify="left")
        self.cable_result.pack(anchor="w", pady=5)

    def eval_cable(self):
        std = self.cable_std.get()
        dist = self.cable_dist.get()
        nic = self.nic_speed.get()

        if dist > 100:
            self.cable_result.config(text=f"❌ FAILED: Maximum Ethernet distance is 100m! {dist}m exceeds specification (signal attenuation).", foreground="#d9534f")
            return

        if std == "Cat6":
            cable_cap = 10 if dist <= 55 else 1
            cap_text = "10 Gbps (<=55m)" if dist <= 55 else "1 Gbps (exceeds 55m limit for 10G)"
        else:
            cable_cap = 10
            cap_text = "10 Gbps (rated up to 100m)"

        nic_cap = 10 if "10" in nic else 1
        negotiated = min(cable_cap, nic_cap)

        notes = []
        if nic_cap < cable_cap:
            notes.append(f"Bottleneck: The NIC is only {nic}, limiting link speed despite {std} capability.")
        elif cable_cap < nic_cap:
            notes.append(f"Bottleneck: {std} cannot sustain 10 Gbps beyond 55m (dropped to 1 Gbps).")
        else:
            notes.append("Hardware and cabling run at optimal capability!")

        msg = (
            f"• Cable Limit: {cap_text}\n"
            f"• Transceiver/NIC Limit: {nic}\n"
            f"✔ Negotiated Link Speed: {negotiated} Gbps\n\n"
            + notes[0]
        )
        self.cable_result.config(text=msg, foreground="#0275d8")

    # -------------------------------------------------------------
    # TAB 3: Tool Matcher
    # -------------------------------------------------------------
    def build_tools_tab(self):
        frame = ttk.LabelFrame(self.tab_tools, text="Match the Proper Hardware & Software Tool", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.scenario_idx = 0
        self.scenarios = [
            ("A fiber strand appears snapped inside a wall riser. What tool pinpoints the break location?", "OTDR"),
            ("A technician needs to identify which specific unmarked cable in a patch closet leads to Office 4.", "Tone Generator (Fox & Hound)"),
            ("You suspect an office microwave is corrupting Wi-Fi transmissions through raw RF interference.", "Spectrum Analyzer"),
            ("You need to verify whether a server NIC's RJ45 transceiver port is physically transmitting and receiving.", "Loopback Adapter"),
            ("You must connect raw unterminated twisted pairs onto the back of a punchdown patch panel.", "Punchdown Tool"),
            ("You need to see if port 443 and port 22 are listening on an internal server.", "nmap (Port Scanner)")
        ]

        self.tool_prompt = ttk.Label(frame, text="", wraplength=800, font=("Segoe UI", 10, "italic"))
        self.tool_prompt.pack(anchor="w", pady=(0, 10))

        self.user_tool_choice = tk.StringVar()
        tool_options = [
            "OTDR",
            "Tone Generator (Fox & Hound)",
            "Spectrum Analyzer",
            "Loopback Adapter",
            "Punchdown Tool",
            "nmap (Port Scanner)",
            "Crimper"
        ]
        self.tool_combo = ttk.Combobox(frame, textvariable=self.user_tool_choice, values=tool_options, state="readonly", width=30)
        self.tool_combo.pack(anchor="w", pady=5)

        btn_box = ttk.Frame(frame)
        btn_box.pack(anchor="w", pady=5)
        ttk.Button(btn_box, text="Check Answer", command=self.check_tool_answer).pack(side="left", padx=(0, 5))
        ttk.Button(btn_box, text="Next Scenario", command=self.load_tool_scenario).pack(side="left")

        self.tool_feedback = ttk.Label(frame, text="", font=("Segoe UI", 10, "bold"))
        self.tool_feedback.pack(anchor="w", pady=10)

        self.load_tool_scenario()

    def load_tool_scenario(self):
        prompt, _ = self.scenarios[self.scenario_idx % len(self.scenarios)]
        self.tool_prompt.config(text=f"Scenario {self.scenario_idx + 1}: {prompt}")
        self.tool_feedback.config(text="")
        self.tool_combo.set("")

    def check_tool_answer(self):
        _, correct = self.scenarios[self.scenario_idx % len(self.scenarios)]
        chosen = self.user_tool_choice.get()
        if chosen == correct:
            self.tool_feedback.config(text="✔ Spot on! That is precisely the right instrument.", foreground="#5cb85c")
            self.scenario_idx += 1
        else:
            self.tool_feedback.config(text=f"✘ Not quite. (Expected: {correct})", foreground="#d9534f")

    # -------------------------------------------------------------
    # TAB 4: 7-Step Methodology Order Quiz
    # -------------------------------------------------------------
    def build_method_tab(self):
        frame = ttk.LabelFrame(self.tab_method, text="CompTIA 7-Step Troubleshooting Sequence", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(frame, text="Reorder these steps into the proper order (1 to 7):").pack(anchor="w", pady=(0, 10))

        self.steps_scrambled = [
            "Plan a solution to resolve the problem",
            "Verify full system functionality",
            "Establish a theory of probable cause",
            "Document findings, actions, and outcomes",
            "Identify the problem",
            "Implement the solution",
            "Test the theory to determine cause"
        ]

        self.step_entries = []
        for i, step in enumerate(self.steps_scrambled):
            row = ttk.Frame(frame)
            row.pack(fill="x", pady=2)
            spin = ttk.Spinbox(row, from_=1, to=7, width=4)
            spin.set(1)
            spin.pack(side="left", padx=(0, 10))
            ttk.Label(row, text=step).pack(side="left")
            self.step_entries.append((spin, step))

        ttk.Button(frame, text="Validate Methodology", command=self.check_methodology).pack(anchor="w", pady=15)
        self.method_result = ttk.Label(frame, text="", font=("Segoe UI", 10, "bold"))
        self.method_result.pack(anchor="w")

    def check_methodology(self):
        correct_order = {
            "Identify the problem": 1,
            "Establish a theory of probable cause": 2,
            "Test the theory to determine cause": 3,
            "Plan a solution to resolve the problem": 4,
            "Implement the solution": 5,
            "Verify full system functionality": 6,
            "Document findings, actions, and outcomes": 7
        }

        user_order = {}
        for spin, text in self.step_entries:
            try:
                val = int(spin.get())
                user_order[text] = val
            except ValueError:
                self.method_result.config(text="Please assign integers 1 through 7 to each step.", foreground="#d9534f")
                return

        mistakes = 0
        for step_name, correct_pos in correct_order.items():
            if user_order.get(step_name) != correct_pos:
                mistakes += 1

        if mistakes == 0:
            self.method_result.config(text="✔ Splendid! Every single step stands in its rightful order.", foreground="#5cb85c")
        else:
            self.method_result.config(text=f"✘ {mistakes} step(s) are misplaced. Remember: Identify -> Theory -> Test -> Plan -> Implement -> Verify -> Document.", foreground="#d9534f")

    # -------------------------------------------------------------
    # TAB 5: Study Notes & Lines from the Book
    # -------------------------------------------------------------
    def build_study_tab(self):
        frame = ttk.LabelFrame(self.tab_study, text="Direct Study Lines & Reference Rules", padding=15)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        filter_frame = ttk.Frame(frame)
        filter_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(filter_frame, text="Filter by Topic: ").pack(side="left")
        self.topic_var = tk.StringVar(value="All Topics")
        topics = [
            "All Topics",
            "Datacenter & Cloud Review",
            "Network Monitoring & Errors",
            "Cables & Distance Specs",
            "Hardware & Software Tools",
            "Troubleshooting Rules & Methodology",
            "Wi-Fi & Common Network Faults",
            "Essential Commands"
        ]
        topic_menu = ttk.Combobox(filter_frame, textvariable=self.topic_var, values=topics, state="readonly", width=30)
        topic_menu.pack(side="left", padx=5)
        topic_menu.bind("<<ComboboxSelected>>", self.refresh_study_notes)

        # Text display with scrollbar
        text_container = ttk.Frame(frame)
        text_container.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_container)
        scrollbar.pack(side="right", fill="y")

        self.study_text = tk.Text(text_container, wrap="word", yscrollcommand=scrollbar.set, bg="#fafafa", fg="#222222", font=("Segoe UI", 10))
        self.study_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.study_text.yview)

        # Tag configurations for clean formatting
        self.study_text.tag_config("heading", font=("Segoe UI", 11, "bold"), foreground="#003366")
        self.study_text.tag_config("bullet", lmargin1=15, lmargin2=30)
        self.study_text.tag_config("code", font=("Consolas", 10, "bold"), foreground="#9c27b0")

        self.study_data = {
            "Datacenter & Cloud Review": [
                "Leaf/Spine: Switches at top of rack connecting servers directly = access/edge/leaf layer; switches connecting leaf switches = distribution/aggregation/spine layer.",
                "SAN vs. NAS: SAN is block-level external storage shared over iSCSI or FCoE (like a shared USB hard drive for servers); NAS is an OS file server sharing folders via SMB/NFS/FTP/HTTP.",
                "SAN Connections: FCoE connects via FC HBA (proprietary NIC); iSCSI connects via iSCSI Initiator client built into OS.",
                "Cloud Models: SaaS (provider hosts app), PaaS (provider hosts container/environment), IaaS (provider hosts raw VM).",
                "Cloud Terms: IaC (Infrastructure as Code - Ansible/Kubernetes), Tenancy (rented tenant space), Elasticity (rapidly increasing or reducing tenancy)."
            ],
            "Network Monitoring & Errors": [
                "Baselines: Establishing what 'normal' looks like across temperature, CPU, memory, network latency, and jitter.",
                "CRC Errors: Cyclic Redundancy Check failures indicate damaged frames requiring re-transmissions.",
                "Runts & Giants: Runts are packets smaller than 64 bytes; Giants are packets larger than 1518 bytes.",
                "Encapsulation Errors: Typically caused by overloaded routers or MTU/protocol mismatches.",
                "SNMP Architecture: Managed devices have an OID (Object Identifier) and push traps/alerts to the MIB (Management Information Base).",
                "Syslog: Centrally forwards event/audit logs separate from traffic flows; alerts filtered by minimum severity level."
            ],
            "Cables & Distance Specs": [
                "Link Light Rule: Look for a glowing link light on NIC or switch first; link light = confirmed physical connection.",
                "Cat6 Spec: 10 Gbps up to 55 meters (165 feet); 1 Gbps up to 100 meters (328 feet).",
                "Cat6a Spec: Full 10 Gbps up to 100 meters (328 feet).",
                "Cable Bottlenecks: A 1 Gbps NIC transceiver plugged into Cat6a will negotiate at 1 Gbps maximum.",
                "Plenum Cable: Fire-rated cable with Teflon jacket; non-plenum installed in drop-ceilings violates fire code and degrades signals."
            ],
            "Hardware & Software Tools": [
                "Tone Generator (Fox & Hound): Traces copper/coax wire by injecting an audio tone to find unmarked terminations in closets.",
                "OTDR (Optical Time Domain Reflectometer): Sends light pulses down fiber to locate micro-bends, breaks, and dirty terminations.",
                "Spectrum Analyzer: Wi-Fi only tool that detects non-802.11 RF noise (microwaves, baby monitors, raw interference).",
                "Loopback Adapter: Plugs back into NIC port to test transmit/receive pins and diagnose fried transceiver chipsets.",
                "Punchdown Tool: Connects twisted pairs onto punch blocks and patch panels; Crimper fixes modular RJ45 heads onto ends.",
                "Software Tools: Wireshark/tcpdump (packet sniffers), nmap (port/IP scanner), iperf (bandwidth speed tester)."
            ],
            "Troubleshooting Rules & Methodology": [
                "The 7-Step Flow: (1) Identify problem -> (2) Establish theory -> (3) Test theory -> (4) Plan solution -> (5) Implement fix -> (6) Verify full system functionality -> (7) Document findings.",
                "Golden Question: Always ask: 'Has anything changed recently?'",
                "Scope Rule: Does it break for one user (local host/cable/port) or many users (switch/router/DHCP server)?",
                "The Ping Diagnostic Order: Ping Gateway (tests switch/LAN) -> Ping 8.8.8.8 (tests router/WAN) -> Ping google.ca (tests DNS)."
            ],
            "Wi-Fi & Common Network Faults": [
                "Wi-Fi Connection Failures: Wrong PSK/SSID, low RSSI signal, polarization (antenna angle), or 802.11n NIC joining an 802.11ax-only WAP.",
                "Disassociation Attacks: Malicious deauth frames forged by attackers causing repeated dropped client connections.",
                "Rogue DHCP: A second unauthorized DHCP server handing out incorrect IP leases or malicious gateways.",
                "Switch Collisions & Storms: Collisions indicate flakey switch hardware or duplex mismatch; broadcast storms require loop prevention (STP)."
            ],
            "Essential Commands": [
                "IP Configuration: ipconfig (Windows) vs. ip addr show / ifconfig (Linux).",
                "Path Discovery: tracert (Windows) vs. traceroute / mtr (Linux).",
                "DNS Lookup: nslookup (Windows) vs. dig (Linux).",
                "Active Sockets: netstat (shows listening ports and established connections on both OSes).",
                "Layer 2 Resolution: arp (displays current IP-to-MAC hardware translation cache)."
            ]
        }

        self.refresh_study_notes()

    def refresh_study_notes(self, event=None):
        topic = self.topic_var.get()
        self.study_text.config(state="normal")
        self.study_text.delete("1.0", tk.END)

        for heading, lines in self.study_data.items():
            if topic != "All Topics" and topic != heading:
                continue

            self.study_text.insert(tk.END, f"\n{heading}\n", "heading")
            self.study_text.insert(tk.END, ("-" * len(heading)) + "\n")
            for line in lines:
                self.study_text.insert(tk.END, f"• {line}\n\n", "bullet")

        self.study_text.config(state="disabled")

if __name__ == "__main__":
    app = NetworkWonderlandApp()
    app.mainloop()