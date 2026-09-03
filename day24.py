#!/usr/bin/env python3
"""
IT Professional Program: Introduction to Network Administration
Day 14 - Chapter 17: Data Center and Cloud Concepts
Study, Testing, and Interactive Lab Training Application
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

# --- METADATA ---
COURSE_NAME = "Day 14: Data Center & Cloud Concepts"
BUILD_VERSION = "Build 1.0.0"

# --- COMPREHENSIVE STUDY CURRICULUM ---
STUDY_TOPICS = {
    "1. Switch & Route Redundancy": (
        "HIGH AVAILABILITY & INFRASTRUCTURE REDUNDANCY\n"
        "----------------------------------------------------------------------\n"
        "• NIC Teaming (Bonding / Link Aggregation):\n"
        "  - Combines 2 or more physical server NICs into a single logical link to the switch.\n"
        "  - Provides link fault tolerance and combined bandwidth.\n\n"
        "• MPIO (Multi-Path I/O):\n"
        "  - Used when an organization has multiple redundant Storage Area Networks (SANs).\n"
        "  - Provides fault-tolerant, redundant physical paths and load balancing from the server to storage.\n\n"
        "• Hardware Spare Strategies:\n"
        "  - Switch / Router / Next-Gen Firewall (NGFW): Maintain 1 spare unit on-site for fast swap.\n"
        "  - Demarc / Last Mile: Redundant 2nd Internet/WAN connection (active or passive failover).\n"
        "  - First Hop Redundancy: Protocol running from NGFW/Routers to dual demarcs (e.g., FHRP, HSRP, VRRP).\n\n"
        "• Offsite Server & Data Recovery:\n"
        "  - 90%+ of modern on-premises servers run as Virtual Machines (VMs) contained in single virtual disks (e.g., .vhdx).\n"
        "  - Offsite strategy: Synchronize VM files directly to a cloud data center, or replicate SAN block storage to a remote cloud SAN."
    ),
    "2. Data Center Topologies": (
        "DATA CENTER NETWORK ARCHITECTURES\n"
        "----------------------------------------------------------------------\n"
        "• Traditional 3-Tier Model:\n"
        "  1. Access Layer: Connects directly to servers at the top of each server rack.\n"
        "  2. Aggregation / Distribution Layer: Aggregates connections from multiple access switches.\n"
        "  3. Core Layer: High-speed backbone routing traffic across the entire enterprise data center.\n\n"
        "• Modern 2-Tier Leaf-Spine Architecture:\n"
        "  - Designed specifically for modern virtualized and containerized environments.\n"
        "  - Leaf Switches (Access / Edge / Top-of-Rack): Every server rack connects directly to a leaf switch.\n"
        "  - Spine Switches (Aggregation / Backbone): Interconnects all leaf switches in a non-blocking mesh fabric.\n"
        "  - Every leaf switch connects to every spine switch—no leaf-to-leaf or spine-to-spine connections.\n\n"
        "• Traffic Direction Terminology:\n"
        "  - North-South Traffic: Data moving in and out of the data center (between client/internet and the servers).\n"
        "  - East-West Traffic: Data moving laterally between servers inside the data center (e.g., app server to database, VM migration, SAN replication)."
    ),
    "3. Storage: SAN vs. NAS & iSCSI": (
        "DATA CENTER STORAGE ARCHITECTURES\n"
        "----------------------------------------------------------------------\n"
        "• NAS (Network Attached Storage):\n"
        "  - Dedicated file server appliance running a storage OS.\n"
        "  - Provides FILE-LEVEL storage access over existing LAN connections.\n"
        "  - Accessible via network shares using SMB (Windows: \\\\server\\share) or NFS (Linux).\n\n"
        "• SAN (Storage Area Network):\n"
        "  - High-performance, dedicated network for BLOCK-LEVEL storage only (behaves like a local physical hard drive).\n"
        "  - Connects servers to redundant storage arrays using two main methods:\n"
        "    1. iSCSI: Encapsulates SCSI commands inside standard TCP/IP Ethernet packets over 10GbE+ copper (UTP/STP).\n"
        "    2. FCoE (Fibre Channel over Ethernet): Uses specialized fiber optic Host Bus Adapters (HBAs).\n\n"
        "• iSCSI Components:\n"
        "  - iSCSI Target: The SAN storage device providing the shared disk volumes. Identifies permitted servers by IQN (iSCSI Qualified Name).\n"
        "  - iSCSI Initiator: The client software or hardware on the server connecting to the target."
    ),
    "4. Cloud Models & Pizza Analogy": (
        "CLOUD SERVICE MODELS & RESPONSIBILITY\n"
        "----------------------------------------------------------------------\n"
        "• Cloud Hosting Types:\n"
        "  - On-Premises: Private data center located in company headquarters or branch offices (server room / DMZ).\n"
        "  - Colocation (Colo): Company rents rack space, power, and cooling at a 3rd-party facility but owns and manages the physical servers.\n"
        "  - Public Cloud (AWS, Azure, GCP): Multi-tenant environment; provider owns and maintains all physical hardware.\n"
        "  - Hybrid Cloud: Synchronizing workloads and data between a private on-prem data center and public cloud via VPN or direct connection.\n\n"
        "• The 'Pizza as a Service' Analogy:\n"
        "  - Traditional On-Prem (Homemade): You provide everything—gas/electricity, oven, fire, dough/pizza, drinks, and dining table.\n"
        "  - IaaS (Take & Bake): Vendor provides the raw infrastructure (electricity, oven, fire). You manage the OS, runtime, and data (pizza, drinks, table).\n"
        "  - PaaS (Delivery): Vendor provides the environment and execution platform (oven, ingredients, baked pizza). You only provide the dining table and drinks (your application code and data).\n"
        "  - SaaS (Dining Out at Restaurant): Vendor manages 100% of the stack. You simply sit down and eat (use the app, like Microsoft 365 or Salesforce).\n\n"
        "• Advanced Concepts:\n"
        "  - Infrastructure as Code (IaC): Automating infrastructure deployment using scripts (e.g., Ansible, Terraform) or orchestrating containers (e.g., Kubernetes).\n"
        "  - Elasticity vs. Scalability: Dynamically allocating more compute resources (RAM, CPU) on-demand."
    )
}

# --- FLASHCARD DRILL DATA ---
FLASHCARDS = [
    ("What technology combines 2+ server NICs to provide fault tolerance to a switch?", "NIC Teaming (Bonding / Aggregation)"),
    ("What technology provides redundant physical paths from a server to multiple SANs?", "MPIO (Multi-Path Input/Output)"),
    ("What are the two common switch tiers in a modern data center fabric?", "Leaf (Top-of-Rack / Access) and Spine (Aggregation / Distribution)"),
    ("What is the difference between North-South and East-West traffic?", "North-South is client-to-datacenter traffic; East-West is server-to-server lateral traffic inside the datacenter."),
    ("Does a NAS provide file-level or block-level storage?", "File-level storage (shared via SMB or NFS). SAN provides block-level storage."),
    ("In iSCSI storage, what is the server client called, and what is the SAN storage called?", "The server is the iSCSI Initiator; the SAN storage is the iSCSI Target."),
    ("In the 'Pizza as a Service' analogy, which cloud model corresponds to 'Take & Bake'?", "IaaS (Infrastructure as a Service). PaaS is 'Delivery' and SaaS is 'Dining Out'."),
    ("What is the difference between Colocation (Colo) and Public Cloud?", "In a Colo you rent rack space and own your physical servers; in Public Cloud you rent virtual instances and the provider owns the hardware.")
]

# --- EXAM TEST BANK ---
EXAM_QUESTIONS = [
    {
        "q": "An administrator wants to configure fault tolerance on a critical database server connected to an access switch. Which technology should be implemented on the server's network adapters?",
        "options": ["MPIO", "NIC Teaming (Bonding)", "FHRP", "iSCSI Initiator"],
        "answer": "NIC Teaming (Bonding)",
        "exp": "NIC Teaming (also known as bonding or aggregation) links two or more physical network adapters into a logical pair for redundancy and throughput."
    },
    {
        "q": "Your enterprise has redundant SAN arrays replicating data. Which protocol/driver must be configured on the servers to provide redundant paths and load balancing to those SANs?",
        "options": ["LACP", "MPIO", "STP", "VLAN Trunking"],
        "answer": "MPIO",
        "exp": "MPIO (Multi-Path I/O) creates redundant logical pathways between servers and SAN storage controllers."
    },
    {
        "q": "In a modern data center Leaf-Spine switching architecture, which switch tier connects directly to the servers at the top of each rack?",
        "options": ["Spine Switches", "Core Switches", "Leaf (Access / Edge) Switches", "Border Gateway Routers"],
        "answer": "Leaf (Access / Edge) Switches",
        "exp": "Leaf switches (also called Top-of-Rack or Access switches) connect directly to servers in that rack and uplink to all spine switches."
    },
    {
        "q": "Traffic traveling laterally between an application server and a database server inside the same data center is classified as what type of traffic?",
        "options": ["North-South Traffic", "East-West Traffic", "Ingress Demarc Traffic", "Loopback Traffic"],
        "answer": "East-West Traffic",
        "exp": "East-West traffic represents lateral communication moving between internal servers, SANs, and hypervisors inside the data center."
    },
    {
        "q": "Which storage solution operates as a dedicated file server, running an OS and sharing folders across the network using SMB and NFS?",
        "options": ["Storage Area Network (SAN)", "Network Attached Storage (NAS)", "iSCSI Target", "Host Bus Adapter (HBA)"],
        "answer": "Network Attached Storage (NAS)",
        "exp": "NAS is a file-level storage appliance accessed via standard protocols like SMB (Windows) or NFS (Linux)."
    },
    {
        "q": "When setting up block-level network storage over standard twisted-pair Ethernet cabling, which protocol is utilized?",
        "options": ["Fibre Channel (FC)", "iSCSI", "NFS", "FTP"],
        "answer": "iSCSI",
        "exp": "iSCSI encapsulates SCSI storage commands inside standard IP/Ethernet packets, allowing standard copper or fiber NICs to connect to SAN storage."
    },
    {
        "q": "A server connecting to a centralized SAN storage array runs client software known as the:",
        "options": ["iSCSI Target", "iSCSI Initiator", "SMB Broker", "MPIO Resolver"],
        "answer": "iSCSI Initiator",
        "exp": "The client server uses an iSCSI Initiator to discover and attach to the remote iSCSI Target hosted on the SAN."
    },
    {
        "q": "According to the 'Pizza as a Service' cloud analogy, which cloud model corresponds to 'Delivery' where the vendor manages the infrastructure and runtime, but you bring your own dining table and drinks (data and apps)?",
        "options": ["On-Premises", "Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Software as a Service (SaaS)"],
        "answer": "Platform as a Service (PaaS)",
        "exp": "PaaS provides the underlying hardware, OS, and application container engine; the customer only supplies application code and data."
    },
    {
        "q": "A company wants to rent rack space, clean electrical power, and cooling at a commercial data center facility while retaining full ownership and management of their physical server hardware. What is this called?",
        "options": ["Public Cloud", "Colocation (Colo)", "Software as a Service", "Hybrid Multi-tenant"],
        "answer": "Colocation (Colo)",
        "exp": "Colocation facilities allow organizations to house their own physical servers inside a secure, monitored facility with redundant power and uplinks."
    },
    {
        "q": "Which technology allows network administrators to manage data center server configurations and deployment pipelines through automated scripting tools like Ansible or Kubernetes?",
        "options": ["Infrastructure as Code (IaC)", "MPIO Multipathing", "Dynamic Routing", "FHRP Virtual Routing"],
        "answer": "Infrastructure as Code (IaC)",
        "exp": "IaC defines and provisions computing, storage, and networking resources automatically through machine-readable definition files."
    }
]


# =====================================================================
# SECTION 1: STUDY MODULE (Notes + Flashcard Engine)
# =====================================================================
class StudyModule(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Split into Left (Topic Selector & Notes) and Right (Flashcard Drawer)
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left Side: Topic Viewer
        left_frame = ttk.Frame(paned)
        paned.add(left_frame, weight=3)
        
        top_ctrl = ttk.Frame(left_frame)
        top_ctrl.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(top_ctrl, text="Select Topic Module:", font=("Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        self.topic_cb = ttk.Combobox(top_ctrl, values=list(STUDY_TOPICS.keys()), state="readonly", width=35)
        self.topic_cb.current(0)
        self.topic_cb.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.topic_cb.bind("<<ComboboxSelected>>", self.display_topic)
        
        self.txt_notes = tk.Text(
            left_frame,
            wrap=tk.WORD,
            font=("Helvetica", 11),
            bg="#ffffff",
            fg="#2c3e50",
            padx=15,
            pady=15,
            spacing1=4,
            spacing2=3,
            relief=tk.FLAT
        )
        self.txt_notes.pack(fill=tk.BOTH, expand=True)
        
        # Right Side: Interactive Flashcard Box
        right_frame = ttk.LabelFrame(paned, text="⚡ Quick Review Flashcards")
        paned.add(right_frame, weight=2)
        
        self.cards = FLASHCARDS.copy()
        random.shuffle(self.cards)
        self.card_idx = 0
        
        self.lbl_card_prog = tk.Label(right_frame, text="", font=("Helvetica", 9, "bold"), fg="#7f8c8d")
        self.lbl_card_prog.pack(anchor="w", padx=15, pady=(15, 5))
        
        self.lbl_card_q = tk.Label(right_frame, text="", font=("Helvetica", 11, "bold"), wraplength=300, justify="left")
        self.lbl_card_q.pack(anchor="w", padx=15, pady=5)
        
        self.lbl_card_a = tk.Label(right_frame, text="", font=("Helvetica", 11, "italic"), fg="#27ae60", wraplength=300, justify="left")
        self.lbl_card_a.pack(anchor="w", padx=15, pady=5)
        
        btn_box = ttk.Frame(right_frame)
        btn_box.pack(fill=tk.X, padx=15, pady=15)
        
        self.btn_show_ans = ttk.Button(btn_box, text="Show Answer", command=self.show_flashcard_answer)
        self.btn_show_ans.pack(fill=tk.X, pady=3)
        
        self.btn_next_card = ttk.Button(btn_box, text="Next Flashcard", command=self.next_flashcard)
        self.btn_next_card.pack(fill=tk.X, pady=3)
        
        self.display_topic()
        self.load_flashcard()

    def display_topic(self, event=None):
        selected = self.topic_cb.get()
        text_content = STUDY_TOPICS.get(selected, "")
        self.txt_notes.config(state=tk.NORMAL)
        self.txt_notes.delete(1.0, tk.END)
        self.txt_notes.insert(tk.END, text_content)
        self.txt_notes.config(state=tk.DISABLED)

    def load_flashcard(self):
        q, _ = self.cards[self.card_idx]
        self.lbl_card_prog.config(text=f"Card {self.card_idx + 1} of {len(self.cards)}")
        self.lbl_card_q.config(text=f"Q: {q}")
        self.lbl_card_a.config(text="?")
        self.btn_show_ans.config(state=tk.NORMAL)

    def show_flashcard_answer(self):
        _, a = self.cards[self.card_idx]
        self.lbl_card_a.config(text=f"A: {a}")
        self.btn_show_ans.config(state=tk.DISABLED)

    def next_flashcard(self):
        self.card_idx = (self.card_idx + 1) % len(self.cards)
        self.load_flashcard()


# =====================================================================
# SECTION 2: TESTING MODULE (Exam Simulator)
# =====================================================================
class TestingModule(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.test_pool = EXAM_QUESTIONS.copy()
        self.current_idx = 0
        self.score = 0
        self.selected_opt = tk.StringVar()
        
        # Header
        head_box = ttk.Frame(self)
        head_box.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        self.lbl_title = tk.Label(head_box, text="Day 14 Practice Exam: Data Center & Cloud", font=("Helvetica", 14, "bold"), fg="#2c3e50")
        self.lbl_title.pack(side=tk.LEFT)
        
        self.lbl_stats = tk.Label(head_box, text="", font=("Helvetica", 10, "bold"), fg="#7f8c8d")
        self.lbl_stats.pack(side=tk.RIGHT)
        
        # Question Display
        q_frame = ttk.LabelFrame(self, text="Question")
        q_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.lbl_q_text = tk.Label(q_frame, text="", font=("Helvetica", 12, "bold"), wraplength=750, justify="left")
        self.lbl_q_text.pack(anchor="w", padx=20, pady=(15, 15))
        
        self.radio_buttons = []
        for _ in range(4):
            rb = ttk.Radiobutton(q_frame, text="", variable=self.selected_opt, value="")
            rb.pack(anchor="w", padx=30, pady=5)
            self.radio_buttons.append(rb)
            
        self.lbl_feedback = tk.Label(q_frame, text="", font=("Helvetica", 11, "bold"), wraplength=750, justify="left")
        self.lbl_feedback.pack(anchor="w", padx=20, pady=(15, 2))
        
        self.lbl_explanation = tk.Label(q_frame, text="", font=("Helvetica", 10, "italic"), fg="#34495e", wraplength=750, justify="left")
        self.lbl_explanation.pack(anchor="w", padx=20, pady=(0, 15))
        
        # Buttons
        ctrl_frame = ttk.Frame(self)
        ctrl_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self.btn_submit = ttk.Button(ctrl_frame, text="Submit Answer", command=self.submit_answer)
        self.btn_submit.pack(side=tk.LEFT, padx=(0, 10))
        
        self.btn_next = ttk.Button(ctrl_frame, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.btn_next.pack(side=tk.LEFT)
        
        self.btn_reset = ttk.Button(ctrl_frame, text="Restart Exam", command=self.start_new_test)
        self.btn_reset.pack(side=tk.RIGHT)
        
        self.start_new_test()

    def start_new_test(self):
        random.shuffle(self.test_pool)
        self.current_idx = 0
        self.score = 0
        self.load_question()

    def load_question(self):
        self.selected_opt.set("")
        self.lbl_feedback.config(text="")
        self.lbl_explanation.config(text="")
        self.btn_submit.config(state=tk.NORMAL)
        self.btn_next.config(state=tk.DISABLED)
        
        for rb in self.radio_buttons:
            rb.config(state=tk.NORMAL)
            
        q_item = self.test_pool[self.current_idx]
        self.lbl_stats.config(text=f"Question {self.current_idx + 1} of {len(self.test_pool)} | Current Score: {self.score}")
        self.lbl_q_text.config(text=q_item["q"])
        
        options = q_item["options"].copy()
        random.shuffle(options)
        
        for idx, rb in enumerate(self.radio_buttons):
            rb.config(text=options[idx], value=options[idx])

    def submit_answer(self):
        chosen = self.selected_opt.get()
        if not chosen:
            messagebox.showwarning("Select Answer", "Please select an answer choice before submitting.")
            return
            
        q_item = self.test_pool[self.current_idx]
        self.btn_submit.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL)
        
        for rb in self.radio_buttons:
            rb.config(state=tk.DISABLED)
            
        if chosen == q_item["answer"]:
            self.score += 1
            self.lbl_feedback.config(text="✅ Correct!", fg="#27ae60")
        else:
            self.lbl_feedback.config(text=f"❌ Incorrect. Correct Answer: {q_item['answer']}", fg="#c0392b")
            
        self.lbl_explanation.config(text=f"Explanation: {q_item['exp']}")
        self.lbl_stats.config(text=f"Question {self.current_idx + 1} of {len(self.test_pool)} | Current Score: {self.score}")
        
        if self.current_idx == len(self.test_pool) - 1:
            self.btn_next.config(text="Finish Exam")
        else:
            self.btn_next.config(text="Next Question")

    def next_question(self):
        self.current_idx += 1
        if self.current_idx < len(self.test_pool):
            self.load_question()
        else:
            pct = (self.score / len(self.test_pool)) * 100
            msg = f"Exam Completed!\n\nScore: {self.score}/{len(self.test_pool)} ({pct:.1f}%)\n"
            if pct >= 80:
                msg += "Great job! You have mastered Day 14 concepts."
            else:
                msg += "Review the study notes and iSCSI lab before attempting again."
            messagebox.showinfo("Results", msg)
            self.start_new_test()


# =====================================================================
# SECTION 3: INTERACTIVE LAB & PRACTICAL TEACHING GAMES
# =====================================================================
class LabSection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        lab_notebook = ttk.Notebook(self)
        lab_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Sub-Lab 1: iSCSI Target & Initiator Provisioner
        self.tab_iscsi = ISCSILabTab(lab_notebook)
        lab_notebook.add(self.tab_iscsi, text="🛠️ Lab 1: iSCSI SAN Storage Setup")
        
        # Sub-Lab 2: Data Center Topology Traffic Simulator
        self.tab_traffic = TrafficLabTab(lab_notebook)
        lab_notebook.add(self.tab_traffic, text="🧭 Lab 2: Leaf-Spine & Traffic Simulator")
        
        # Sub-Lab 3: Pizza-as-a-Service Game
        self.tab_pizza = PizzaGameTab(lab_notebook)
        lab_notebook.add(self.tab_pizza, text="🍕 Lab 3: Pizza-as-a-Service Cloud Matcher")


# --- LAB 1: iSCSI TARGET & INITIATOR LAB ---
class ISCSILabTab(ttk.Frame):
    """
    Directly models the Day 14 Lab Task:
    'Install iSCSI Target Server on SERVER1, configure storage,
    and connect to it using iSCSI Initiator on SERVER2'
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.current_step = 1
        
        # Instructions Box
        instr_frame = ttk.LabelFrame(self, text="Assignment Objective: Configure SAN Block Storage")
        instr_frame.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Label(
            instr_frame,
            text="Simulate the Day 14 task: Provision an iSCSI Virtual Disk Target on SERVER1, assign authorized IQN,\n"
                 "and initiate the block connection from SERVER2 using the Microsoft iSCSI Initiator client.",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=8)
        
        # Split View (SERVER1 Target vs SERVER2 Initiator)
        work_paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        work_paned.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        # SERVER1 Panel (Storage Target)
        self.srv1_frame = ttk.LabelFrame(work_paned, text="SERVER1 (iSCSI Storage Target)")
        work_paned.add(self.srv1_frame, weight=1)
        
        self.lbl_s1_status = tk.Label(self.srv1_frame, text="Role: Not Installed", fg="#c0392b", font=("Helvetica", 10, "bold"))
        self.lbl_s1_status.pack(anchor="w", padx=10, pady=5)
        
        self.btn_install_target = ttk.Button(self.srv1_frame, text="1. Install iSCSI Target Server Role", command=self.step1_install)
        self.btn_install_target.pack(fill=tk.X, padx=10, pady=4)
        
        ttk.Label(self.srv1_frame, text="Virtual Disk Name:").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_vdisk = ttk.Entry(self.srv1_frame)
        self.entry_vdisk.insert(0, "DataLUN_01.vhdx")
        self.entry_vdisk.pack(fill=tk.X, padx=10, pady=2)
        
        ttk.Label(self.srv1_frame, text="Target Name:").pack(anchor="w", padx=10, pady=(5, 0))
        self.entry_target_name = ttk.Entry(self.srv1_frame)
        self.entry_target_name.insert(0, "Target-Server1")
        self.entry_target_name.pack(fill=tk.X, padx=10, pady=2)
        
        self.btn_create_lun = ttk.Button(self.srv1_frame, text="2. Create iSCSI Target & Virtual Disk", command=self.step2_create_lun, state=tk.DISABLED)
        self.btn_create_lun.pack(fill=tk.X, padx=10, pady=8)
        
        # SERVER2 Panel (Client Initiator)
        self.srv2_frame = ttk.LabelFrame(work_paned, text="SERVER2 (iSCSI Initiator Client)")
        work_paned.add(self.srv2_frame, weight=1)
        
        self.lbl_s2_iqn = tk.Label(self.srv2_frame, text="Client IQN: iqn.1991-05.com.microsoft:server2", font=("Monospace", 8), fg="#7f8c8d")
        self.lbl_s2_iqn.pack(anchor="w", padx=10, pady=5)
        
        ttk.Label(self.srv2_frame, text="Connect to Target IP:").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_target_ip = ttk.Entry(self.srv2_frame)
        self.entry_target_ip.insert(0, "192.168.10.1")
        self.entry_target_ip.pack(fill=tk.X, padx=10, pady=2)
        
        self.btn_connect = ttk.Button(self.srv2_frame, text="3. Discover & Connect iSCSI Target", command=self.step3_connect, state=tk.DISABLED)
        self.btn_connect.pack(fill=tk.X, padx=10, pady=8)
        
        self.lbl_disk_mgr = tk.Label(self.srv2_frame, text="Disk Management:\nNo Remote SAN Disk Attached", bg="#2c3e50", fg="white", font=("Monospace", 9), justify="left", height=5)
        self.lbl_disk_mgr.pack(fill=tk.X, padx=10, pady=10)
        
        self.btn_mount = ttk.Button(self.srv2_frame, text="4. Initialize & Mount as Drive X:", command=self.step4_mount, state=tk.DISABLED)
        self.btn_mount.pack(fill=tk.X, padx=10, pady=4)

    def step1_install(self):
        self.lbl_s1_status.config(text="Role: iSCSI Target Server (ACTIVE)", fg="#27ae60")
        self.btn_install_target.config(state=tk.DISABLED)
        self.btn_create_lun.config(state=tk.NORMAL)
        messagebox.showinfo("SERVER1", "iSCSI Target Server Role installed successfully.")

    def step2_create_lun(self):
        target = self.entry_target_name.get().strip()
        vdisk = self.entry_vdisk.get().strip()
        if not target or not vdisk:
            messagebox.showwarning("Incomplete", "Provide both Virtual Disk name and Target Name.")
            return
        self.btn_create_lun.config(state=tk.DISABLED)
        self.btn_connect.config(state=tk.NORMAL)
        messagebox.showinfo("SERVER1", f"Target '{target}' hosting '{vdisk}' created.\nAuthorized IQN set to: iqn.1991-05.com.microsoft:server2")

    def step3_connect(self):
        ip = self.entry_target_ip.get().strip()
        if ip != "192.168.10.1":
            messagebox.showerror("Connection Failed", "Cannot reach storage target. Use SERVER1 IP: 192.168.10.1")
            return
        self.lbl_disk_mgr.config(text="Disk Management:\nDisk 1 (Raw Block Device - 500GB)\nStatus: Offline (Uninitialized)")
        self.btn_connect.config(state=tk.DISABLED)
        self.btn_mount.config(state=tk.NORMAL)
        messagebox.showinfo("SERVER2", "Connected to iSCSI Target!\nNew raw storage block detected in Disk Management.")

    def step4_mount(self):
        self.lbl_disk_mgr.config(text="Disk Management:\nDisk 1: [ Drive X: (NTFS) - 500GB Online ]\nConnection: iSCSI (Ethernet SAN)")
        self.btn_mount.config(state=tk.DISABLED)
        messagebox.showinfo("Lab Complete!", "🎉 SUCCESS!\nSERVER2 has mounted block storage from SERVER1 over iSCSI.\nDrive X: is ready for production!")


# --- LAB 2: DATA CENTER TOPOLOGY TRAFFIC GAME ---
class TrafficLabTab(ttk.Frame):
    """
    Teaches the Leaf-Spine Architecture and differentiates
    North-South vs. East-West traffic flows interactively.
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        info_frame = ttk.LabelFrame(self, text="Traffic Pattern Simulator")
        info_frame.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Label(
            info_frame,
            text="Interactive Leaf-Spine Fabric: Click a scenario to test your traffic routing knowledge.\n"
                 "Determine whether the communication flow is North-South or East-West, and trace the path.",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=5)
        
        # Interactive Canvas
        self.canvas = tk.Canvas(self, bg="#1e272e", height=320)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        # Control Buttons
        btn_box = ttk.Frame(self)
        btn_box.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Button(btn_box, text="Scenario A: Web Client Browsing Web App", command=self.sim_north_south).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_box, text="Scenario B: Server 1 Replicating DB to Server 3", command=self.sim_east_west).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_box, text="Reset Fabric", command=self.draw_topology).pack(side=tk.RIGHT, padx=5)
        
        self.lbl_expl = tk.Label(self, text="Select a scenario to trace traffic path.", font=("Helvetica", 11, "bold"), fg="#2c3e50")
        self.lbl_expl.pack(pady=5)
        
        self.draw_topology()

    def draw_topology(self):
        self.canvas.delete("all")
        self.lbl_expl.config(text="Select a scenario to trace traffic path.", fg="#2c3e50")
        
        # Internet Cloud / Client (North)
        self.canvas.create_oval(340, 20, 460, 70, fill="#3498db", outline="white", width=2)
        self.canvas.create_text(400, 45, text="Internet / Client\n(North)", fill="white", font=("Helvetica", 9, "bold"), justify="center")
        
        # Spine Switches (Aggregation)
        self.canvas.create_rectangle(220, 110, 320, 150, fill="#e67e22", outline="white", width=2)
        self.canvas.create_text(270, 130, text="Spine Switch 1", fill="white", font=("Helvetica", 9, "bold"))
        
        self.canvas.create_rectangle(480, 110, 580, 150, fill="#e67e22", outline="white", width=2)
        self.canvas.create_text(530, 130, text="Spine Switch 2", fill="white", font=("Helvetica", 9, "bold"))
        
        # Leaf Switches (Top of Rack)
        self.canvas.create_rectangle(140, 190, 240, 230, fill="#27ae60", outline="white", width=2)
        self.canvas.create_text(190, 210, text="Leaf 1 (Rack 1)", fill="white", font=("Helvetica", 9, "bold"))
        
        self.canvas.create_rectangle(350, 190, 450, 230, fill="#27ae60", outline="white", width=2)
        self.canvas.create_text(400, 210, text="Leaf 2 (Rack 2)", fill="white", font=("Helvetica", 9, "bold"))
        
        self.canvas.create_rectangle(560, 190, 660, 230, fill="#27ae60", outline="white", width=2)
        self.canvas.create_text(610, 210, text="Leaf 3 (Rack 3)", fill="white", font=("Helvetica", 9, "bold"))
        
        # Fabric Mesh Lines (Spine to Leaf)
        for spine_x in [270, 530]:
            for leaf_x in [190, 400, 610]:
                self.canvas.create_line(spine_x, 150, leaf_x, 190, fill="#7f8c8d", width=1, dash=(3, 3))
                
        # Servers
        self.canvas.create_rectangle(160, 260, 220, 300, fill="#8e44ad", outline="white")
        self.canvas.create_text(190, 280, text="Server 1", fill="white", font=("Helvetica", 8, "bold"))
        self.canvas.create_line(190, 230, 190, 260, fill="#ecf0f1", width=2)
        
        self.canvas.create_rectangle(370, 260, 430, 300, fill="#8e44ad", outline="white")
        self.canvas.create_text(400, 280, text="Server 2", fill="white", font=("Helvetica", 8, "bold"))
        self.canvas.create_line(400, 230, 400, 260, fill="#ecf0f1", width=2)
        
        self.canvas.create_rectangle(580, 260, 640, 300, fill="#8e44ad", outline="white")
        self.canvas.create_text(610, 280, text="Server 3", fill="white", font=("Helvetica", 8, "bold"))
        self.canvas.create_line(610, 230, 610, 260, fill="#ecf0f1", width=2)

    def sim_north_south(self):
        self.draw_topology()
        # Draw highlighted path down to Server 2
        self.canvas.create_line(400, 70, 530, 110, fill="#f1c40f", width=4)
        self.canvas.create_line(530, 150, 400, 190, fill="#f1c40f", width=4)
        self.canvas.create_line(400, 230, 400, 260, fill="#f1c40f", width=4)
        self.lbl_expl.config(
            text="NORTH-SOUTH TRAFFIC: Data enters from external client -> Spine Switch -> Leaf 2 -> Server 2.",
            fg="#2980b9"
        )

    def sim_east_west(self):
        self.draw_topology()
        # Draw path from Server 1 up to Spine 1 across to Leaf 3 down to Server 3
        self.canvas.create_line(190, 260, 190, 230, fill="#2ecc71", width=4)
        self.canvas.create_line(190, 190, 270, 150, fill="#2ecc71", width=4)
        self.canvas.create_line(270, 150, 610, 190, fill="#2ecc71", width=4)
        self.canvas.create_line(610, 230, 610, 260, fill="#2ecc71", width=4)
        self.lbl_expl.config(
            text="EAST-WEST TRAFFIC: Server 1 talks laterally across data center fabric to Server 3 via Spine 1.",
            fg="#27ae60"
        )


# --- LAB 3: PIZZA-AS-A-SERVICE SORTING GAME ---
class PizzaGameTab(ttk.Frame):
    """
    Interactive teaching game based on the slide:
    'Pizza as a Service' (Traditional On-Prem, IaaS, PaaS, SaaS)
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        info = ttk.LabelFrame(self, text="Cloud Service Model Matcher (Pizza-as-a-Service)")
        info.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Label(
            info,
            text="Drag or assign the real-world cloud components to their corresponding Pizza Analogy.\n"
                 "Test your grasp of who manages what: You (Customer) vs. Cloud Vendor.",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=5)
        
        self.game_questions = [
            ("Dining Table & Drinks", "Customer provides location & drinks; vendor makes & delivers pizza.", "PaaS (Platform as a Service)"),
            ("Oven, Gas/Electric & Fire", "Vendor provides physical power and hardware; you bake the pizza and bring the rest.", "IaaS (Infrastructure as a Service)"),
            ("Everything Made at Home", "You provide all electricity, oven, ingredients, dough, and seating yourself.", "Traditional On-Premises"),
            ("Eating at a Restaurant", "Vendor handles 100% of food, cooking, cleaning, and table; you just consume.", "SaaS (Software as a Service)"),
            ("AWS EC2 / Azure Virtual Machines", "Renting virtual raw compute and storage; you configure the OS and middleware.", "IaaS (Infrastructure as a Service)"),
            ("Google App Engine / Heroku", "Uploading application code directly; vendor handles operating system updates and runtimes.", "PaaS (Platform as a Service)"),
            ("Microsoft 365 / Salesforce / Gmail", "Turnkey software fully hosted and managed by vendor; accessed via browser.", "SaaS (Software as a Service)")
        ]
        
        random.shuffle(self.game_questions)
        self.g_idx = 0
        self.g_score = 0
        
        self.card_box = ttk.LabelFrame(self, text="Current Challenge Card")
        self.card_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.lbl_component = tk.Label(self.card_box, text="", font=("Helvetica", 14, "bold"), fg="#2c3e50")
        self.lbl_component.pack(pady=(20, 5))
        
        self.lbl_desc = tk.Label(self.card_box, text="", font=("Helvetica", 11, "italic"), wraplength=650)
        self.lbl_desc.pack(pady=(0, 20))
        
        btn_grid = ttk.Frame(self.card_box)
        btn_grid.pack(pady=10)
        
        self.models = [
            "Traditional On-Premises",
            "IaaS (Infrastructure as a Service)",
            "PaaS (Platform as a Service)",
            "SaaS (Software as a Service)"
        ]
        
        for m in self.models:
            ttk.Button(btn_grid, text=m, width=32, command=lambda chosen=m: self.check_choice(chosen)).pack(pady=4)
            
        self.lbl_game_stats = tk.Label(self, text="", font=("Helvetica", 10, "bold"), fg="#7f8c8d")
        self.lbl_game_stats.pack(pady=10)
        
        self.load_game_card()

    def load_game_card(self):
        if self.g_idx < len(self.game_questions):
            comp, desc, _ = self.game_questions[self.g_idx]
            self.lbl_component.config(text=comp)
            self.lbl_desc.config(text=desc)
            self.lbl_game_stats.config(text=f"Card {self.g_idx + 1} of {len(self.game_questions)} | Score: {self.g_score}")
        else:
            messagebox.showinfo("Game Over!", f"Challenge Complete!\nFinal Score: {self.g_score}/{len(self.game_questions)}")
            self.g_idx = 0
            self.g_score = 0
            random.shuffle(self.game_questions)
            self.load_game_card()

    def check_choice(self, chosen):
        _, _, correct = self.game_questions[self.g_idx]
        if chosen == correct:
            self.g_score += 1
            messagebox.showinfo("Correct!", f"✅ Right! '{chosen}' matches this model perfectly.")
        else:
            messagebox.showerror("Incorrect", f"❌ Not quite.\nCorrect model is: {correct}")
        self.g_idx += 1
        self.load_game_card()


# =====================================================================
# MAIN APPLICATION CONTROLLER
# =====================================================================
class DataCenterLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Introduction to Network Administration - {COURSE_NAME}")
        self.root.geometry("980x720")
        
        # Configure theme
        style = ttk.Style()
        style.theme_use('clam')
        
        # Top Header Banner
        header = tk.Frame(root, bg="#1b2a4a", pady=12)
        header.pack(fill=tk.X, side=tk.TOP)
        
        tk.Label(
            header,
            text="triOS / Eastern College - IT Professional Program",
            font=("Helvetica", 11),
            fg="#bdc3c7",
            bg="#1b2a4a"
        ).pack()
        
        tk.Label(
            header,
            text="Day 14: Data Center, Cloud Concepts & SAN Administration",
            font=("Helvetica", 15, "bold"),
            fg="white",
            bg="#1b2a4a"
        ).pack()
        
        # Footer
        footer = tk.Frame(root, bg="#ecf0f1", pady=5)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        
        tk.Label(
            footer,
            text=f"Course Module: Chapter 17 | {BUILD_VERSION}",
            font=("Helvetica", 8, "bold"),
            fg="#7f8c8d",
            bg="#ecf0f1"
        ).pack()
        
        # Main Navigation Tabs
        main_notebook = ttk.Notebook(root)
        main_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Tab 1: Study Module
        self.tab_study = StudyModule(main_notebook)
        main_notebook.add(self.tab_study, text="📖 Study & Lecture Notes")
        
        # Tab 2: Lab & Games Module
        self.tab_labs = LabSection(main_notebook)
        main_notebook.add(self.tab_labs, text="🎮 Interactive Labs & Games")
        
        # Tab 3: Practice Exam
        self.tab_testing = TestingModule(main_notebook)
        main_notebook.add(self.tab_testing, text="🎓 Practice Exam")


def main():
    root = tk.Tk()
    app = DataCenterLearningApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()