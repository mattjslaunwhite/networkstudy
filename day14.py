#!/usr/bin/env python3
"""
IT Professional Program: Introduction to Network Administration
Day 14 - Chapter 17: Data Center and Cloud Concepts
Study, Testing, Interactive Labs, and Hyper-V Management Hooks
"""

import sys
import os
import ctypes
import subprocess
import platform
import shutil
import random
import csv
import tkinter as tk
from tkinter import ttk, messagebox

# --- METADATA ---
COURSE_NAME = "Day 14: Data Center & Cloud Concepts"
BUILD_VERSION = "Build 1.2.0 (Admin Elevation & Theme Edition)"

# --- PRIVILEGE ELEVATION UTILITIES ---
def is_admin():
    """Check if the current script is running with elevated administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        # Non-Windows systems check uid 0
        return os.getuid() == 0 if hasattr(os, "getuid") else False

def run_as_admin():
    """Relaunch the current python script with elevated administrator privileges via UAC."""
    if platform.system() != "Windows":
        messagebox.showinfo("Elevation", "Elevation prompt is only applicable on Windows hosts.")
        return
        
    try:
        params = f'"{os.path.abspath(sys.argv[0])}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit(0)
    except Exception as ex:
        messagebox.showerror("Elevation Failed", f"Could not elevate permissions:\n{ex}")

# --- COMPREHENSIVE STUDY CURRICULUM ---
STUDY_TOPICS = {
    "1. Switch & Route Redundancy": (
        "HIGH AVAILABILITY & INFRASTRUCTURE REDUNDANCY\n"
        "----------------------------------------------------------------------\n"
        "• NIC Teaming (Bonding / Link Aggregation):\n"
        "  - Combines 2 or more physical server NICs into a single logical link to the switch[cite: 1].\n"
        "  - Provides link fault tolerance and combined bandwidth.\n\n"
        "• MPIO (Multi-Path I/O):\n"
        "  - Used when an organization has multiple redundant Storage Area Networks (SANs)[cite: 1].\n"
        "  - Provides fault-tolerant, redundant physical paths and load balancing from the server to storage[cite: 1].\n\n"
        "• Hardware Spare Strategies:\n"
        "  - Switch / Router / Next-Gen Firewall (NGFW): Maintain 1 spare unit on-site for fast swap[cite: 1].\n"
        "  - Demarc / Last Mile: Redundant 2nd Internet/WAN connection (active or passive failover)[cite: 1].\n"
        "  - First Hop Redundancy: Protocol running from NGFW/Routers to dual demarcs (e.g., FHRP, HSRP, VRRP)[cite: 1].\n\n"
        "• Offsite Server & Data Recovery:\n"
        "  - 90%+ of modern on-premises servers run as Virtual Machines (VMs) contained in single virtual disks (e.g., .vhdx)[cite: 1].\n"
        "  - Offsite strategy: Synchronize VM files directly to a cloud data center, or replicate SAN block storage to a remote cloud SAN[cite: 1]."
    ),
    "2. Data Center Topologies": (
        "DATA CENTER NETWORK ARCHITECTURES\n"
        "----------------------------------------------------------------------\n"
        "• Traditional 3-Tier Model:\n"
        "  1. Access Layer: Connects directly to servers at the top of each server rack[cite: 1].\n"
        "  2. Aggregation / Distribution Layer: Aggregates connections from multiple access switches[cite: 1].\n"
        "  3. Core Layer: High-speed backbone routing traffic across the entire enterprise data center[cite: 1].\n\n"
        "• Modern 2-Tier Leaf-Spine Architecture:\n"
        "  - Designed specifically for modern virtualized and containerized environments[cite: 1].\n"
        "  - Leaf Switches (Access / Edge / Top-of-Rack): Every server rack connects directly to a leaf switch[cite: 1].\n"
        "  - Spine Switches (Aggregation / Backbone): Interconnects all leaf switches in a non-blocking mesh fabric[cite: 1].\n"
        "  - Every leaf switch connects to every spine switch—no leaf-to-leaf or spine-to-spine connections.\n\n"
        "• Traffic Direction Terminology:\n"
        "  - North-South Traffic: Data moving in and out of the data center (between client/internet and the servers)[cite: 1].\n"
        "  - East-West Traffic: Data moving laterally between servers inside the data center (e.g., app server to database, VM migration, SAN replication)[cite: 1]."
    ),
    "3. Storage: SAN vs. NAS & iSCSI": (
        "DATA CENTER STORAGE ARCHITECTURES\n"
        "----------------------------------------------------------------------\n"
        "• NAS (Network Attached Storage):\n"
        "  - Dedicated file server appliance running a storage OS[cite: 1].\n"
        "  - Provides FILE-LEVEL storage access over existing LAN connections[cite: 1].\n"
        "  - Accessible via network shares using SMB (Windows: \\\\server\\share) or NFS (Linux)[cite: 1].\n\n"
        "• SAN (Storage Area Network):\n"
        "  - High-performance, dedicated network for BLOCK-LEVEL storage only (behaves like a local physical hard drive)[cite: 1].\n"
        "  - Connects servers to redundant storage arrays using two main methods[cite: 1]:\n"
        "    1. iSCSI: Encapsulates SCSI commands inside standard TCP/IP Ethernet packets over 10GbE+ copper (UTP/STP)[cite: 1].\n"
        "    2. FCoE (Fibre Channel over Ethernet): Uses specialized fiber optic Host Bus Adapters (HBAs)[cite: 1].\n\n"
        "• iSCSI Components:\n"
        "  - iSCSI Target: The SAN storage device providing the shared disk volumes. Identifies permitted servers by IQN (iSCSI Qualified Name)[cite: 1].\n"
        "  - iSCSI Initiator: The client software or hardware on the server connecting to the target[cite: 1]."
    ),
    "4. Cloud Models & Pizza Analogy": (
        "CLOUD SERVICE MODELS & RESPONSIBILITY\n"
        "----------------------------------------------------------------------\n"
        "• Cloud Hosting Types:\n"
        "  - On-Premises: Private data center located in company headquarters or branch offices (server room / DMZ)[cite: 1].\n"
        "  - Colocation (Colo): Company rents rack space, power, and cooling at a 3rd-party facility but owns and manages the physical servers[cite: 1].\n"
        "  - Public Cloud (AWS, Azure, GCP): Multi-tenant environment; provider owns and maintains all physical hardware[cite: 1].\n"
        "  - Hybrid Cloud: Synchronizing workloads and data between a private on-prem data center and public cloud via VPN or direct connection[cite: 1].\n\n"
        "• The 'Pizza as a Service' Analogy[cite: 1]:\n"
        "  - Traditional On-Prem (Homemade): You provide everything—gas/electricity, oven, fire, dough/pizza, drinks, and dining table[cite: 1].\n"
        "  - IaaS (Take & Bake): Vendor provides the raw infrastructure (electricity, oven, fire)[cite: 1]. You manage the OS, runtime, and data (pizza, drinks, table)[cite: 1].\n"
        "  - PaaS (Delivery): Vendor provides the environment and execution platform (oven, ingredients, baked pizza)[cite: 1]. You only provide the dining table and drinks (your application code and data)[cite: 1].\n"
        "  - SaaS (Dining Out at Restaurant): Vendor manages 100% of the stack[cite: 1]. You simply sit down and eat (use the app, like Microsoft 365 or Salesforce)[cite: 1].\n\n"
        "• Advanced Concepts:\n"
        "  - Infrastructure as Code (IaC): Automating infrastructure deployment using scripts (e.g., Ansible, Terraform) or orchestrating containers (e.g., Kubernetes)[cite: 1].\n"
        "  - Elasticity vs. Scalability: Dynamically allocating more compute resources (RAM, CPU) on-demand[cite: 1]."
    )
}

FLASHCARDS = [
    ("What technology combines 2+ server NICs to provide fault tolerance to a switch?", "NIC Teaming (Bonding / Aggregation)[cite: 1]"),
    ("What technology provides redundant physical paths from a server to multiple SANs?", "MPIO (Multi-Path Input/Output)[cite: 1]"),
    ("What are the two common switch tiers in a modern data center fabric?", "Leaf (Top-of-Rack / Access) and Spine (Aggregation / Distribution)[cite: 1]"),
    ("What is the difference between North-South and East-West traffic?", "North-South is client-to-datacenter traffic; East-West is server-to-server lateral traffic inside the datacenter[cite: 1]."),
    ("Does a NAS provide file-level or block-level storage?", "File-level storage (shared via SMB or NFS). SAN provides block-level storage[cite: 1]."),
    ("In iSCSI storage, what is the server client called, and what is the SAN storage called?", "The server is the iSCSI Initiator; the SAN storage is the iSCSI Target[cite: 1]."),
    ("In the 'Pizza as a Service' analogy, which cloud model corresponds to 'Take & Bake'?", "IaaS (Infrastructure as a Service)[cite: 1]. PaaS is 'Delivery' and SaaS is 'Dining Out'[cite: 1]."),
    ("What is the difference between Colocation (Colo) and Public Cloud?", "In a Colo you rent rack space and own your physical servers; in Public Cloud you rent virtual instances and the provider owns the hardware[cite: 1].")
]

EXAM_QUESTIONS = [
    {
        "q": "An administrator wants to configure fault tolerance on a critical database server connected to an access switch. Which technology should be implemented on the server's network adapters?",
        "options": ["MPIO", "NIC Teaming (Bonding)", "FHRP", "iSCSI Initiator"],
        "answer": "NIC Teaming (Bonding)",
        "exp": "NIC Teaming (also known as bonding or aggregation) links two or more physical network adapters into a logical pair for redundancy and throughput[cite: 1]."
    },
    {
        "q": "Your enterprise has redundant SAN arrays replicating data. Which protocol/driver must be configured on the servers to provide redundant paths and load balancing to those SANs?",
        "options": ["LACP", "MPIO", "STP", "VLAN Trunking"],
        "answer": "MPIO",
        "exp": "MPIO (Multi-Path I/O) creates redundant logical pathways between servers and SAN storage controllers[cite: 1]."
    },
    {
        "q": "In a modern data center Leaf-Spine switching architecture, which switch tier connects directly to the servers at the top of each rack?",
        "options": ["Spine Switches", "Core Switches", "Leaf (Access / Edge) Switches", "Border Gateway Routers"],
        "answer": "Leaf (Access / Edge) Switches",
        "exp": "Leaf switches (also called Top-of-Rack or Access switches) connect directly to servers in that rack and uplink to all spine switches[cite: 1]."
    },
    {
        "q": "Traffic traveling laterally between an application server and a database server inside the same data center is classified as what type of traffic?",
        "options": ["North-South Traffic", "East-West Traffic", "Ingress Demarc Traffic", "Loopback Traffic"],
        "answer": "East-West Traffic",
        "exp": "East-West traffic represents lateral communication moving between internal servers, SANs, and hypervisors inside the data center[cite: 1]."
    },
    {
        "q": "Which storage solution operates as a dedicated file server, running an OS and sharing folders across the network using SMB and NFS?",
        "options": ["Storage Area Network (SAN)", "Network Attached Storage (NAS)", "iSCSI Target", "Host Bus Adapter (HBA)"],
        "answer": "Network Attached Storage (NAS)",
        "exp": "NAS is a file-level storage appliance accessed via standard protocols like SMB (Windows) or NFS (Linux)[cite: 1]."
    },
    {
        "q": "When setting up block-level network storage over standard twisted-pair Ethernet cabling, which protocol is utilized?",
        "options": ["Fibre Channel (FC)", "iSCSI", "NFS", "FTP"],
        "answer": "iSCSI",
        "exp": "iSCSI encapsulates SCSI storage commands inside standard IP/Ethernet packets, allowing standard copper or fiber NICs to connect to SAN storage[cite: 1]."
    },
    {
        "q": "A server connecting to a centralized SAN storage array runs client software known as the:",
        "options": ["iSCSI Target", "iSCSI Initiator", "SMB Broker", "MPIO Resolver"],
        "answer": "iSCSI Initiator",
        "exp": "The client server uses an iSCSI Initiator to discover and attach to the remote iSCSI Target hosted on the SAN[cite: 1]."
    },
    {
        "q": "According to the 'Pizza as a Service' cloud analogy, which cloud model corresponds to 'Delivery' where the vendor manages the infrastructure and runtime, but you bring your own dining table and drinks (data and apps)?",
        "options": ["On-Premises", "Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Software as a Service (SaaS)"],
        "answer": "Platform as a Service (PaaS)",
        "exp": "PaaS provides the underlying hardware, OS, and application container engine; the customer only supplies application code and data[cite: 1]."
    },
    {
        "q": "A company wants to rent rack space, clean electrical power, and cooling at a commercial data center facility while retaining full ownership and management of their physical server hardware. What is this called?",
        "options": ["Public Cloud", "Colocation (Colo)", "Software as a Service", "Hybrid Multi-tenant"],
        "answer": "Colocation (Colo)",
        "exp": "Colocation facilities allow organizations to house their own physical servers inside a secure, monitored facility with redundant power and uplinks[cite: 1]."
    },
    {
        "q": "Which technology allows network administrators to manage data center server configurations and deployment pipelines through automated scripting tools like Ansible or Kubernetes?",
        "options": ["Infrastructure as Code (IaC)", "MPIO Multipathing", "Dynamic Routing", "FHRP Virtual Routing"],
        "answer": "Infrastructure as Code (IaC)",
        "exp": "IaC defines and provisions computing, storage, and networking resources automatically through machine-readable definition files[cite: 1]."
    }
]

# =====================================================================
# SECTION 1: STUDY MODULE
# =====================================================================
class StudyModule(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
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
            padx=15,
            pady=15,
            spacing1=4,
            spacing2=3,
            relief=tk.FLAT
        )
        self.txt_notes.pack(fill=tk.BOTH, expand=True)
        
        self.right_frame = ttk.LabelFrame(paned, text="⚡ Quick Review Flashcards")
        paned.add(self.right_frame, weight=2)
        
        self.cards = FLASHCARDS.copy()
        random.shuffle(self.cards)
        self.card_idx = 0
        
        self.lbl_card_prog = tk.Label(self.right_frame, text="", font=("Helvetica", 9, "bold"))
        self.lbl_card_prog.pack(anchor="w", padx=15, pady=(15, 5))
        
        self.lbl_card_q = tk.Label(self.right_frame, text="", font=("Helvetica", 11, "bold"), wraplength=300, justify="left")
        self.lbl_card_q.pack(anchor="w", padx=15, pady=5)
        
        self.lbl_card_a = tk.Label(self.right_frame, text="", font=("Helvetica", 11, "italic"), wraplength=300, justify="left")
        self.lbl_card_a.pack(anchor="w", padx=15, pady=5)
        
        btn_box = ttk.Frame(self.right_frame)
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

    def apply_theme(self, theme):
        self.txt_notes.config(bg=theme["text_bg"], fg=theme["fg"], insertbackground=theme["fg"])
        self.lbl_card_prog.config(bg=theme["frame_bg"], fg=theme["muted"])
        self.lbl_card_q.config(bg=theme["frame_bg"], fg=theme["fg"])
        self.lbl_card_a.config(bg=theme["frame_bg"], fg=theme["accent_green"])

# =====================================================================
# SECTION 2: TESTING MODULE
# =====================================================================
class TestingModule(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.test_pool = EXAM_QUESTIONS.copy()
        self.current_idx = 0
        self.score = 0
        self.selected_opt = tk.StringVar()
        
        head_box = ttk.Frame(self)
        head_box.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        self.lbl_title = tk.Label(head_box, text="Day 14 Practice Exam: Data Center & Cloud", font=("Helvetica", 14, "bold"))
        self.lbl_title.pack(side=tk.LEFT)
        
        self.lbl_stats = tk.Label(head_box, text="", font=("Helvetica", 10, "bold"))
        self.lbl_stats.pack(side=tk.RIGHT)
        
        self.q_frame = ttk.LabelFrame(self, text="Question")
        self.q_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.lbl_q_text = tk.Label(self.q_frame, text="", font=("Helvetica", 12, "bold"), wraplength=750, justify="left")
        self.lbl_q_text.pack(anchor="w", padx=20, pady=(15, 15))
        
        self.radio_buttons = []
        for _ in range(4):
            rb = ttk.Radiobutton(self.q_frame, text="", variable=self.selected_opt, value="")
            rb.pack(anchor="w", padx=30, pady=5)
            self.radio_buttons.append(rb)
            
        self.lbl_feedback = tk.Label(self.q_frame, text="", font=("Helvetica", 11, "bold"), wraplength=750, justify="left")
        self.lbl_feedback.pack(anchor="w", padx=20, pady=(15, 2))
        
        self.lbl_explanation = tk.Label(self.q_frame, text="", font=("Helvetica", 10, "italic"), wraplength=750, justify="left")
        self.lbl_explanation.pack(anchor="w", padx=20, pady=(0, 15))
        
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
                msg += "Splendid! You have mastered Day 14 concepts."
            else:
                msg += "Review the study notes and iSCSI lab before attempting again."
            messagebox.showinfo("Results", msg)
            self.start_new_test()

    def apply_theme(self, theme):
        self.lbl_title.config(bg=theme["bg"], fg=theme["fg"])
        self.lbl_stats.config(bg=theme["bg"], fg=theme["muted"])
        self.lbl_q_text.config(bg=theme["frame_bg"], fg=theme["fg"])
        self.lbl_feedback.config(bg=theme["frame_bg"])
        self.lbl_explanation.config(bg=theme["frame_bg"], fg=theme["muted"])

# =====================================================================
# SECTION 3: LABS, GAMES & HYPER-V INTEGRATION HOOKS
# =====================================================================
class LabSection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.lab_notebook = ttk.Notebook(self)
        self.lab_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.tab_iscsi = ISCSILabTab(self.lab_notebook)
        self.lab_notebook.add(self.tab_iscsi, text="🛠️ Lab 1: iSCSI SAN Storage Setup")
        
        self.tab_traffic = TrafficLabTab(self.lab_notebook)
        self.lab_notebook.add(self.tab_traffic, text="🧭 Lab 2: Leaf-Spine & Traffic Simulator")
        
        self.tab_pizza = PizzaGameTab(self.lab_notebook)
        self.lab_notebook.add(self.tab_pizza, text="🍕 Lab 3: Pizza-as-a-Service Cloud Matcher")

        self.tab_hyperv = HyperVHookTab(self.lab_notebook)
        self.lab_notebook.add(self.tab_hyperv, text="🎛️ Hyper-V Integration")

    def apply_theme(self, theme):
        self.tab_iscsi.apply_theme(theme)
        self.tab_traffic.apply_theme(theme)
        self.tab_pizza.apply_theme(theme)
        self.tab_hyperv.apply_theme(theme)

# --- LAB 1: iSCSI TARGET & INITIATOR LAB ---
class ISCSILabTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        instr_frame = ttk.LabelFrame(self, text="Assignment Objective: Configure SAN Block Storage[cite: 1]")
        instr_frame.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Label(
            instr_frame,
            text="Simulate the Day 14 task: Provision an iSCSI Virtual Disk Target on SERVER1, assign authorized IQN,\n"
                 "and initiate the block connection from SERVER2 using the Microsoft iSCSI Initiator client[cite: 1].",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=8)
        
        work_paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        work_paned.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        # SERVER1 Panel
        self.srv1_frame = ttk.LabelFrame(work_paned, text="SERVER1 (iSCSI Storage Target)[cite: 1]")
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
        
        # SERVER2 Panel
        self.srv2_frame = ttk.LabelFrame(work_paned, text="SERVER2 (iSCSI Initiator Client)[cite: 1]")
        work_paned.add(self.srv2_frame, weight=1)
        
        self.lbl_s2_iqn = tk.Label(self.srv2_frame, text="Client IQN: iqn.1991-05.com.microsoft:server2", font=("Monospace", 8))
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
        messagebox.showinfo("SERVER1", "iSCSI Target Server Role installed successfully[cite: 1].")

    def step2_create_lun(self):
        target = self.entry_target_name.get().strip()
        vdisk = self.entry_vdisk.get().strip()
        if not target or not vdisk:
            messagebox.showwarning("Incomplete", "Provide both Virtual Disk name and Target Name.")
            return
        self.btn_create_lun.config(state=tk.DISABLED)
        self.btn_connect.config(state=tk.NORMAL)
        messagebox.showinfo("SERVER1", f"Target '{target}' hosting '{vdisk}' created.\nAuthorized IQN set to: iqn.1991-05.com.microsoft:server2[cite: 1]")

    def step3_connect(self):
        ip = self.entry_target_ip.get().strip()
        if ip != "192.168.10.1":
            messagebox.showerror("Connection Failed", "Cannot reach storage target. Use SERVER1 IP: 192.168.10.1")
            return
        self.lbl_disk_mgr.config(text="Disk Management:\nDisk 1 (Raw Block Device - 500GB)\nStatus: Offline (Uninitialized)")
        self.btn_connect.config(state=tk.DISABLED)
        self.btn_mount.config(state=tk.NORMAL)
        messagebox.showinfo("SERVER2", "Connected to iSCSI Target!\nNew raw storage block detected in Disk Management[cite: 1].")

    def step4_mount(self):
        self.lbl_disk_mgr.config(text="Disk Management:\nDisk 1: [ Drive X: (NTFS) - 500GB Online ]\nConnection: iSCSI (Ethernet SAN)")
        self.btn_mount.config(state=tk.DISABLED)
        messagebox.showinfo("Lab Complete!", "🎉 SUCCESS!\nSERVER2 has mounted block storage from SERVER1 over iSCSI.\nDrive X: is ready for production[cite: 1]!")

    def apply_theme(self, theme):
        self.lbl_s1_status.config(bg=theme["frame_bg"])
        self.lbl_s2_iqn.config(bg=theme["frame_bg"], fg=theme["muted"])

# --- LAB 2: DATA CENTER TOPOLOGY TRAFFIC GAME ---
class TrafficLabTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        info_frame = ttk.LabelFrame(self, text="Traffic Pattern Simulator[cite: 1]")
        info_frame.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Label(
            info_frame,
            text="Interactive Leaf-Spine Fabric: Click a scenario to test your traffic routing knowledge[cite: 1].\n"
                 "Determine whether the communication flow is North-South or East-West, and trace the path[cite: 1].",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=5)
        
        self.canvas = tk.Canvas(self, bg="#1e272e", height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        btn_box = ttk.Frame(self)
        btn_box.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Button(btn_box, text="Scenario A: Web Client Browsing Web App", command=self.sim_north_south).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_box, text="Scenario B: Server 1 Replicating DB to Server 3", command=self.sim_east_west).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_box, text="Reset Fabric", command=self.draw_topology).pack(side=tk.RIGHT, padx=5)
        
        self.lbl_expl = tk.Label(self, text="Select a scenario to trace traffic path.", font=("Helvetica", 11, "bold"))
        self.lbl_expl.pack(pady=5)
        
        self.draw_topology()

    def draw_topology(self):
        self.canvas.delete("all")
        self.lbl_expl.config(text="Select a scenario to trace traffic path.", fg="#7f8c8d")
        
        # Internet Cloud / Client (North)
        self.canvas.create_oval(340, 20, 460, 70, fill="#3498db", outline="white", width=2)
        self.canvas.create_text(400, 45, text="Internet / Client\n(North)", fill="white", font=("Helvetica", 9, "bold"), justify="center")
        
        # Spine Switches
        self.canvas.create_rectangle(220, 110, 320, 150, fill="#e67e22", outline="white", width=2)
        self.canvas.create_text(270, 130, text="Spine Switch 1", fill="white", font=("Helvetica", 9, "bold"))
        
        self.canvas.create_rectangle(480, 110, 580, 150, fill="#e67e22", outline="white", width=2)
        self.canvas.create_text(530, 130, text="Spine Switch 2", fill="white", font=("Helvetica", 9, "bold"))
        
        # Leaf Switches
        self.canvas.create_rectangle(140, 190, 240, 230, fill="#27ae60", outline="white", width=2)
        self.canvas.create_text(190, 210, text="Leaf 1 (Rack 1)", fill="white", font=("Helvetica", 9, "bold"))
        
        self.canvas.create_rectangle(350, 190, 450, 230, fill="#27ae60", outline="white", width=2)
        self.canvas.create_text(400, 210, text="Leaf 2 (Rack 2)", fill="white", font=("Helvetica", 9, "bold"))
        
        self.canvas.create_rectangle(560, 190, 660, 230, fill="#27ae60", outline="white", width=2)
        self.canvas.create_text(610, 210, text="Leaf 3 (Rack 3)", fill="white", font=("Helvetica", 9, "bold"))
        
        # Fabric Mesh Lines
        for spine_x in [270, 530]:
            for leaf_x in [190, 400, 610]:
                self.canvas.create_line(spine_x, 150, leaf_x, 190, fill="#7f8c8d", width=1, dash=(3, 3))
                
        # Servers
        for idx, (lx, name) in enumerate([(190, "Server 1"), (400, "Server 2"), (610, "Server 3")]):
            self.canvas.create_rectangle(lx - 30, 260, lx + 30, 295, fill="#8e44ad", outline="white")
            self.canvas.create_text(lx, 277, text=name, fill="white", font=("Helvetica", 8, "bold"))
            self.canvas.create_line(lx, 230, lx, 260, fill="#ecf0f1", width=2)

    def sim_north_south(self):
        self.draw_topology()
        self.canvas.create_line(400, 70, 530, 110, fill="#f1c40f", width=4)
        self.canvas.create_line(530, 150, 400, 190, fill="#f1c40f", width=4)
        self.canvas.create_line(400, 230, 400, 260, fill="#f1c40f", width=4)
        self.lbl_expl.config(
            text="NORTH-SOUTH TRAFFIC: Data enters from external client -> Spine Switch -> Leaf 2 -> Server 2[cite: 1].",
            fg="#3498db"
        )

    def sim_east_west(self):
        self.draw_topology()
        self.canvas.create_line(190, 260, 190, 230, fill="#2ecc71", width=4)
        self.canvas.create_line(190, 190, 270, 150, fill="#2ecc71", width=4)
        self.canvas.create_line(270, 150, 610, 190, fill="#2ecc71", width=4)
        self.canvas.create_line(610, 230, 610, 260, fill="#2ecc71", width=4)
        self.lbl_expl.config(
            text="EAST-WEST TRAFFIC: Server 1 communicates laterally across fabric to Server 3 via Spine 1[cite: 1].",
            fg="#27ae60"
        )

    def apply_theme(self, theme):
        self.lbl_expl.config(bg=theme["bg"])

# --- LAB 3: PIZZA-AS-A-SERVICE SORTING GAME ---
class PizzaGameTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        info = ttk.LabelFrame(self, text="Cloud Service Model Matcher (Pizza-as-a-Service)[cite: 1]")
        info.pack(fill=tk.X, padx=15, pady=10)
        
        ttk.Label(
            info,
            text="Drag or assign the real-world cloud components to their corresponding Pizza Analogy[cite: 1].\n"
                 "Test your grasp of who manages what: You (Customer) vs. Cloud Vendor[cite: 1].",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=5)
        
        self.game_questions = [
            ("Dining Table & Drinks", "Customer provides location & drinks; vendor makes & delivers pizza[cite: 1].", "PaaS (Platform as a Service)"),
            ("Oven, Gas/Electric & Fire", "Vendor provides physical power and hardware; you bake the pizza and bring the rest[cite: 1].", "IaaS (Infrastructure as a Service)"),
            ("Everything Made at Home", "You provide all electricity, oven, ingredients, dough, and seating yourself[cite: 1].", "Traditional On-Premises"),
            ("Eating at a Restaurant", "Vendor handles 100% of food, cooking, cleaning, and table; you just consume[cite: 1].", "SaaS (Software as a Service)"),
            ("AWS EC2 / Azure Virtual Machines", "Renting virtual raw compute and storage; you configure the OS and middleware[cite: 1].", "IaaS (Infrastructure as a Service)"),
            ("Google App Engine / Heroku", "Uploading application code directly; vendor handles operating system updates and runtimes.", "PaaS (Platform as a Service)"),
            ("Microsoft 365 / Salesforce / Gmail", "Turnkey software fully hosted and managed by vendor; accessed via browser.", "SaaS (Software as a Service)")
        ]
        
        random.shuffle(self.game_questions)
        self.g_idx = 0
        self.g_score = 0
        
        self.card_box = ttk.LabelFrame(self, text="Current Challenge Card")
        self.card_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.lbl_component = tk.Label(self.card_box, text="", font=("Helvetica", 14, "bold"))
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
            
        self.lbl_game_stats = tk.Label(self, text="", font=("Helvetica", 10, "bold"))
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

    def apply_theme(self, theme):
        self.lbl_component.config(bg=theme["frame_bg"], fg=theme["fg"])
        self.lbl_desc.config(bg=theme["frame_bg"], fg=theme["muted"])
        self.lbl_game_stats.config(bg=theme["bg"], fg=theme["muted"])

# --- LAB 4: HYPER-V HOOK & LIVE DISCOVERY ---
class HyperVHookTab(ttk.Frame):
    """
    Direct PowerShell & Hyper-V Management hooks for SERVER1 and SERVER2
    with an elevation hook to request UAC Administrator access.
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        self.admin_status = is_admin()
        
        top_box = ttk.LabelFrame(self, text="Hyper-V Host Connection & Administrator Controls")
        top_box.pack(fill=tk.X, padx=15, pady=10)
        
        status_frame = ttk.Frame(top_box)
        status_frame.pack(fill=tk.X, padx=10, pady=(6, 2))
        
        ttk.Label(
            status_frame,
            text="Privilege Status:",
            font=("Helvetica", 9, "bold")
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        if self.admin_status:
            self.lbl_perm = tk.Label(
                status_frame, 
                text="● Administrator Privileges Active", 
                fg="#27ae60", 
                font=("Helvetica", 9, "bold")
            )
        else:
            self.lbl_perm = tk.Label(
                status_frame, 
                text="⚠️ Standard User (Read/Write to Hyper-V may be restricted)", 
                fg="#e67e22", 
                font=("Helvetica", 9, "bold")
            )
        self.lbl_perm.pack(side=tk.LEFT)
        
        if not self.admin_status:
            self.btn_elevate = ttk.Button(
                status_frame, 
                text="🛡️ Elevate to Admin (Relaunch)", 
                command=self.request_elevation
            )
            self.btn_elevate.pack(side=tk.RIGHT, padx=5)

        ttk.Label(
            top_box,
            text="Control and query virtual machine states (SERVER1, SERVER2) directly from this workbench.\n"
                 "Interacts with Hyper-V module cmdlets: Get-VM, Start-VM, Stop-VM, and vmconnect.exe.",
            font=("Helvetica", 10)
        ).pack(anchor="w", padx=10, pady=6)
        
        btn_bar = ttk.Frame(top_box)
        btn_bar.pack(fill=tk.X, padx=10, pady=6)
        
        ttk.Button(btn_bar, text="🔄 Query Local Hyper-V VMs", command=self.refresh_vms).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_bar, text="▶️ Start Selected VM", command=self.start_vm).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_bar, text="⏹️ Stop Selected VM", command=self.stop_vm).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_bar, text="🖥️ Launch Virtual Console (vmconnect)", command=self.launch_vmconnect).pack(side=tk.LEFT, padx=3)
        
        paned = ttk.PanedWindow(self, orient=tk.VERTICAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        tree_frame = ttk.Frame(paned)
        paned.add(tree_frame, weight=1)
        
        columns = ("Name", "State", "CPUUsage", "MemoryAssigned", "Uptime")
        self.vm_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=6)
        self.vm_tree.heading("Name", text="VM Name")
        self.vm_tree.heading("State", text="State")
        self.vm_tree.heading("CPUUsage", text="CPU (%)")
        self.vm_tree.heading("MemoryAssigned", text="RAM (MB)")
        self.vm_tree.heading("Uptime", text="Uptime")
        
        self.vm_tree.column("Name", width=160)
        self.vm_tree.column("State", width=100)
        self.vm_tree.column("CPUUsage", width=80, anchor="center")
        self.vm_tree.column("MemoryAssigned", width=120, anchor="center")
        self.vm_tree.column("Uptime", width=160)
        
        scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.vm_tree.yview)
        self.vm_tree.configure(yscroll=scroll.set)
        self.vm_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        log_frame = ttk.LabelFrame(paned, text="Hyper-V Diagnostic Terminal")
        paned.add(log_frame, weight=1)
        
        self.txt_log = tk.Text(log_frame, font=("Monospace", 9), relief=tk.FLAT, padx=10, pady=10)
        self.txt_log.pack(fill=tk.BOTH, expand=True)
        
        self.log(f"Hyper-V Management Hook initialized (Administrator: {self.admin_status}).")
        if not self.admin_status and platform.system() == "Windows":
            self.log("Warning: Without elevated rights, Get-VM or Start-VM commands may return Access Denied errors.")
            
        if platform.system() != "Windows":
            self.log("Notice: Operating system is not Windows. Hyper-V cmdlets will simulate mock targets (SERVER1, SERVER2).")
            self.load_mock_vms()
        else:
            self.refresh_vms()

    def request_elevation(self):
        if messagebox.askyesno("Admin Elevation", "Relaunch this study application with Administrator privileges to permit Hyper-V management?"):
            run_as_admin()

    def log(self, msg):
        self.txt_log.insert(tk.END, f">> {msg}\n")
        self.txt_log.see(tk.END)

    def run_powershell(self, command):
        if platform.system() != "Windows":
            raise EnvironmentError("PowerShell Hyper-V module requires Windows Host.")
        cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=12)
        if result.returncode != 0:
            err = result.stderr.strip()
            if "permission" in err.lower() or "access is denied" in err.lower():
                raise PermissionError("Access is denied. Administrator privileges are required to manage Hyper-V.")
            raise RuntimeError(err)
        return result.stdout.strip()

    def refresh_vms(self):
        for item in self.vm_tree.get_children():
            self.vm_tree.delete(item)
            
        if platform.system() != "Windows":
            self.load_mock_vms()
            return
            
        ps_script = (
            "Get-VM | Select-Object Name, State, CPUUsage, "
            "@{N='MemoryMB';E={[math]::Round($_.MemoryAssigned/1MB)}}, "
            "@{N='UptimeStr';E={$_.Uptime.ToString()}} | ConvertTo-Csv -NoTypeInformation"
        )
        try:
            raw = self.run_powershell(ps_script)
            lines = raw.splitlines()
            if len(lines) > 1:
                reader = csv.DictReader(lines)
                for row in reader:
                    self.vm_tree.insert("", "end", values=(
                        row.get("Name"),
                        row.get("State"),
                        row.get("CPUUsage"),
                        row.get("MemoryMB"),
                        row.get("UptimeStr")
                    ))
                self.log("Successfully polled virtual machines from local Hyper-V host.")
            else:
                self.log("No VMs returned by Hyper-V. Loading default lab instances.")
                self.load_mock_vms()
        except PermissionError as p_err:
            self.log(f"PERMISSION ERROR: {p_err}")
            self.log("Click '🛡️ Elevate to Admin' above to grant the required UAC rights.")
            self.load_mock_vms()
        except Exception as ex:
            self.log(f"Hyper-V query error: {ex}")
            self.log("Switching to offline lab simulation view.")
            self.load_mock_vms()

    def load_mock_vms(self):
        mocks = [
            ("SERVER1", "Running", "2", "2048", "02:15:40"),
            ("SERVER2", "Running", "1", "2048", "02:15:38"),
            ("ROUTER-VM", "Running", "0", "1024", "05:42:10"),
            ("WIN10-CLIENT", "Off", "0", "0", "00:00:00")
        ]
        for row in mocks:
            self.vm_tree.insert("", "end", values=row)
        self.log("Lab targets populated: SERVER1 (Target), SERVER2 (Initiator).")

    def get_selected_vm_name(self):
        sel = self.vm_tree.selection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a virtual machine from the table.")
            return None
        return self.vm_tree.item(sel[0])["values"][0]

    def start_vm(self):
        vm = self.get_selected_vm_name()
        if not vm:
            return
        self.log(f"Attempting Start-VM -Name '{vm}'...")
        try:
            if platform.system() == "Windows":
                self.run_powershell(f"Start-VM -Name '{vm}'")
                self.log(f"VM '{vm}' successfully started.")
                self.refresh_vms()
            else:
                self.log(f"[Simulated] VM '{vm}' transitioned to 'Running'.")
        except PermissionError:
            self.log(f"Permission denied starting '{vm}'. Please elevate to Administrator.")
            messagebox.showerror("Permission Denied", f"Cannot start '{vm}'. Administrator privileges are required.")
        except Exception as ex:
            self.log(f"Failed to start VM '{vm}': {ex}")

    def stop_vm(self):
        vm = self.get_selected_vm_name()
        if not vm:
            return
        self.log(f"Attempting Stop-VM -Name '{vm}' -SaveState...")
        try:
            if platform.system() == "Windows":
                self.run_powershell(f"Stop-VM -Name '{vm}' -SaveState")
                self.log(f"VM '{vm}' saved.")
                self.refresh_vms()
            else:
                self.log(f"[Simulated] VM '{vm}' saved and turned off.")
        except PermissionError:
            self.log(f"Permission denied stopping '{vm}'. Please elevate to Administrator.")
            messagebox.showerror("Permission Denied", f"Cannot stop '{vm}'. Administrator privileges are required.")
        except Exception as ex:
            self.log(f"Failed to stop VM '{vm}': {ex}")

    def launch_vmconnect(self):
        vm = self.get_selected_vm_name()
        if not vm:
            return
        if platform.system() != "Windows":
            messagebox.showinfo("Virtual Machine Connection", f"[Simulation] Spawning vmconnect.exe localhost '{vm}'")
            self.log(f"vmconnect.exe invoked for {vm}.")
            return
            
        vmconnect_path = shutil.which("vmconnect.exe")
        if not vmconnect_path:
            vmconnect_path = r"C:\Windows\System32\vmconnect.exe"
            
        self.log(f"Spawning vmconnect.exe localhost '{vm}'...")
        try:
            subprocess.Popen([vmconnect_path, "localhost", str(vm)])
            self.log(f"Remote console for '{vm}' opened.")
        except Exception as ex:
            self.log(f"Could not open vmconnect: {ex}. Ensure Hyper-V GUI management tools are installed.")

    def apply_theme(self, theme):
        self.txt_log.config(bg=theme["text_bg"], fg=theme["fg"], insertbackground=theme["fg"])
        self.lbl_perm.config(bg=theme["frame_bg"])

# =====================================================================
# MAIN APPLICATION CONTROLLER
# =====================================================================
class DataCenterLearningApp:
    THEMES = {
        "dark": {
            "name": "dark",
            "bg": "#23272a",
            "frame_bg": "#2c2f33",
            "text_bg": "#18191c",
            "fg": "#e0e0e0",
            "muted": "#99aab5",
            "header_bg": "#1e2124",
            "header_fg": "#ffffff",
            "footer_bg": "#1e2124",
            "footer_fg": "#7289da",
            "accent_green": "#2ecc71",
            "btn_bg": "#3c3f41",
            "tree_bg": "#18191c",
            "tree_fg": "#e0e0e0",
            "btn_text": "☀️ Light Mode"
        },
        "light": {
            "name": "light",
            "bg": "#f4f6f9",
            "frame_bg": "#ffffff",
            "text_bg": "#ffffff",
            "fg": "#2c3e50",
            "muted": "#7f8c8d",
            "header_bg": "#1b2a4a",
            "header_fg": "#ffffff",
            "footer_bg": "#ecf0f1",
            "footer_fg": "#7f8c8d",
            "accent_green": "#27ae60",
            "btn_bg": "#e2e6ea",
            "tree_bg": "#ffffff",
            "tree_fg": "#2c3e50",
            "btn_text": "🌙 Dark Mode"
        }
    }

    def __init__(self, root):
        self.root = root
        self.root.title(f"Introduction to Network Administration - {COURSE_NAME}")
        self.root.geometry("1020x760")
        
        self.current_theme = "light"
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Header Banner
        self.header = tk.Frame(root, pady=10)
        self.header.pack(fill=tk.X, side=tk.TOP)
        
        title_box = tk.Frame(self.header)
        title_box.pack(side=tk.LEFT, padx=20)
        
        self.lbl_subhead = tk.Label(title_box, text="triOS / Eastern College - IT Professional Program", font=("Helvetica", 10))
        self.lbl_subhead.pack(anchor="w")
        
        self.lbl_head = tk.Label(title_box, text="Day 14: Data Center, Cloud Concepts & SAN Administration", font=("Helvetica", 14, "bold"))
        self.lbl_head.pack(anchor="w")
        
        self.btn_theme = ttk.Button(self.header, text="🌙 Dark Mode", command=self.toggle_theme)
        self.btn_theme.pack(side=tk.RIGHT, padx=20)
        
        # Footer Banner
        self.footer = tk.Frame(root, pady=4)
        self.footer.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.lbl_foot = tk.Label(self.footer, text=f"Course Module: Chapter 17 | {BUILD_VERSION}", font=("Helvetica", 8, "bold"))
        self.lbl_foot.pack()
        
        # Main Tabs
        self.main_notebook = ttk.Notebook(root)
        self.main_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.tab_study = StudyModule(self.main_notebook)
        self.main_notebook.add(self.tab_study, text="📖 Study & Lecture Notes")
        
        self.tab_labs = LabSection(self.main_notebook)
        self.main_notebook.add(self.tab_labs, text="🎮 Interactive Labs, Games & Hyper-V")
        
        self.tab_testing = TestingModule(self.main_notebook)
        self.main_notebook.add(self.tab_testing, text="🎓 Practice Exam")

        self.apply_theme()

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme()

    def apply_theme(self):
        th = self.THEMES[self.current_theme]
        
        self.root.config(bg=th["bg"])
        self.header.config(bg=th["header_bg"])
        self.header.winfo_children()[0].config(bg=th["header_bg"])
        self.lbl_subhead.config(bg=th["header_bg"], fg="#bdc3c7")
        self.lbl_head.config(bg=th["header_bg"], fg=th["header_fg"])
        
        self.footer.config(bg=th["footer_bg"])
        self.lbl_foot.config(bg=th["footer_bg"], fg=th["footer_fg"])
        self.btn_theme.config(text=th["btn_text"])
        
        self.style.configure('TFrame', background=th["bg"])
        self.style.configure('TLabel', background=th["bg"], foreground=th["fg"])
        self.style.configure('TLabelframe', background=th["bg"], foreground=th["fg"])
        self.style.configure('TLabelframe.Label', background=th["bg"], foreground=th["fg"], font=("Helvetica", 10, "bold"))
        self.style.configure('TButton', background=th["btn_bg"], foreground=th["fg"])
        self.style.configure('TNotebook', background=th["bg"])
        self.style.configure('TNotebook.Tab', background=th["btn_bg"], foreground=th["fg"], padding=[8, 3])
        self.style.map('TNotebook.Tab', background=[('selected', th["bg"])])
        self.style.configure("Treeview", background=th["tree_bg"], foreground=th["tree_fg"], fieldbackground=th["tree_bg"])
        self.style.configure("Treeview.Heading", background=th["btn_bg"], foreground=th["fg"])
        
        self.tab_study.apply_theme(th)
        self.tab_labs.apply_theme(th)
        self.tab_testing.apply_theme(th)

def main():
    root = tk.Tk()
    app = DataCenterLearningApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
