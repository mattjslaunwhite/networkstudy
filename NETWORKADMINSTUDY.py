#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import random

# --- App Metadata ---
APP_VERSION = "1.0.10"
BUILD_DATE = "August 21, 2026"
AUTHOR = "Matt-Réal Slaunwhite"

# --- Data Structure for the App ---
CHAPTER_CONTENT = {
    "Ch 1: OSI Model": (
        "THE OSI MODEL (How Data Travels)\n"
        "--------------------------------------------------\n"
        "Think of the OSI model like a post office processing a package. "
        "As data goes down the layers, it gets boxed up. As it goes up, it gets unboxed.\n"
        "7. APPLICATION\n"
        "• The user interacting with the app (e.g., typing a web address).\n"
        "6. PRESENTATION\n"
        "• Translating and encrypting the data (making sure it's readable/secure).\n"
        "5. SESSION\n"
        "• Opening and closing the connection between two computers.\n"
        "4. TRANSPORT\n"
        "• Sorting the data to the right service (TCP is reliable/tracks delivery, UDP is fast but drops packages).\n"
        "3. NETWORK\n"
        "• The 'GPS' layer. Uses IP addresses to route packets across the internet.\n"
        "2. DATA LINK\n"
        "• Local delivery within the same network. Uses MAC addresses (burned into hardware) to deliver Frames.\n"
        "1. PHYSICAL\n"
        "• The actual cables, radio waves (Wi-Fi), and electrical signals (Bits).\n"
        "--------------------------------------------------\n"
        "*Mnemonic:* Please Do Not Throw Sausage Pizza Away."
    ),
    "Ch 2: Ports": (
        "COMMON PORTS (Doors to the Computer)\n"
        "--------------------------------------------------\n"
        "If an IP address is a building's street address, a Port is the specific apartment door inside that building.\n"
        "• 20/21 (FTP): Used for transferring files.\n"
        "• 22 (SSH): Secure, encrypted command-line access.\n"
        "• 23 (Telnet): Unencrypted command-line access (Avoid using!).\n"
        "• 25 (SMTP): Sending emails out.\n"
        "• 53 (DNS): The internet's phonebook.\n"
        "• 67/68 (DHCP): Automatically handing out IP addresses.\n"
        "• 80 (HTTP): Unencrypted web browsing.\n"
        "• 110 (POP3) & 143 (IMAP): Receiving emails in.\n"
        "• 443 (HTTPS): Secure, encrypted web browsing.\n"
        "• 3389 (RDP): Windows Remote Desktop connection."
    ),
    "Ch 3: Hardware": (
        "NETWORK HARDWARE & CABLES\n"
        "--------------------------------------------------\n"
        "Cables (The Roads):\n"
        "• Cat 5e / Cat 6: Standard copper ethernet cables. Cat 6 is faster but maxes out at 55 meters for its top speed.\n"
        "• Fiber Optic: Uses light instead of electricity.\n"
        "  - Single-mode uses lasers for long distances (miles).\n"
        "  - Multi-mode uses LEDs for shorter distances (data centers).\n"
        "Devices (The Traffic Cops):\n"
        "• Switch (Layer 2): Connects devices in the SAME building/network. It learns MAC addresses to send data only to the right computer.\n"
        "• Router (Layer 3): Connects DIFFERENT networks together (like your home to the Internet). It uses IP addresses to figure out where data needs to go globally."
    ),
    "Ch 4: Subnetting": (
        "SUBNETTING (Slicing the Pie)\n"
        "--------------------------------------------------\n"
        "Subnetting is simply taking a massive block of IP addresses and slicing them up into smaller, manageable networks.\n"
        "The Magic Rule (2^n):\n"
        "When figuring out how many subnets you can make, you borrow 'bits'. If you borrow 3 bits, you calculate 2 to the power of 3 (2 x 2 x 2 = 8 subnets).\n"
        "Common Subnet Masks to recognize:\n"
        "• /24 = 255.255.255.0 (Fits about 254 computers)\n"
        "• /25 = 255.255.255.128 (Fits about 126 computers)\n"
        "• /26 = 255.255.255.192 (Fits about 62 computers)\n"
        "--------------------------------------------------\n"
        "*Exam Tip:* You always lose 2 IP addresses in every subnet—one for the Network ID, and one for the Broadcast address."
    ),
    "Ch 5: Services": (
        "CORE NETWORK SERVICES\n"
        "--------------------------------------------------\n"
        "DNS (Domain Name System): The Internet Phonebook\n"
        "Computers only understand numbers (IP addresses), but humans prefer names (google.com). DNS translates names into numbers.\n"
        "• A Record: Points a name to an IPv4 address.\n"
        "• MX Record: Directs emails to the right mail server.\n"
        "DHCP (Dynamic Host Config Protocol): The Valet Parking\n"
        "Instead of manually typing an IP address into every phone and laptop, DHCP hands them out automatically using the D.O.R.A process:\n"
        "1. Discover: Computer shouts 'I need an IP!'\n"
        "2. Offer: Server says 'Here is one you can use.'\n"
        "3. Request: Computer says 'I will take it!'\n"
        "4. Acknowledge: Server says 'It is yours for the next 24 hours.'"
    ),
    "Ch 6: T-Shoot": (
        "TROUBLESHOOTING METHODOLOGY\n"
        "--------------------------------------------------\n"
        "CompTIA wants you to fix problems in a very specific order. You must memorize these 7 steps:\n"
        "1. Identify the problem: Talk to the user. Ask 'What changed?'\n"
        "2. Establish a theory: Guess what is wrong, starting with the easiest stuff (Is it plugged in?).\n"
        "3. Test the theory: Try your guess. If you are wrong, make a new theory.\n"
        "4. Plan of action: Figure out how to fix it without breaking other things.\n"
        "5. Implement the solution: Actually fix it (or escalate to your boss).\n"
        "6. Verify functionality: Make sure it works, and put steps in place so it doesn't happen again.\n"
        "7. Document findings: Write down what you did so the next IT person knows."
    )
}

QUIZ_DATA = {
    "Ch 1: OSI Model": [
        ("Which layer acts like the 'GPS' by using IP addresses to route traffic?", "Layer 3 (Network Layer)"),
        ("What layer handles physical cables and Wi-Fi radio waves?", "Layer 1 (Physical Layer)"),
        ("Which layer uses MAC addresses to deliver frames locally?", "Layer 2 (Data Link Layer)")
    ],
    "Ch 2: Ports": [
        ("What port number is used for secure web browsing (HTTPS)?", "443"),
        ("If you want to remotely control a Windows computer, what port does RDP use?", "3389"),
        ("What port does DNS use to look up websites?", "53")
    ],
    "Ch 3: Hardware": [
        ("Which type of fiber optic cable uses lasers for long-distance runs?", "Single-mode Fiber"),
        ("What device connects different networks together using IP addresses?", "A Router"),
        ("What device connects computers in the same building using MAC addresses?", "A Switch")
    ],
    "Ch 4: Subnetting": [
        ("Why do we subtract 2 from the total number of IP addresses in a subnet?", "To account for the Network ID and Broadcast Address"),
        ("If you borrow 4 bits for subnetting, how many subnets do you get?", "16 subnets (2^4)"),
        ("How many usable hosts are available in a standard /24 network?", "254 usable hosts")
    ],
    "Ch 5: Services": [
        ("What DNS record type maps a website name to an IPv4 address?", "An 'A' Record"),
        ("What does the 'A' in the DHCP DORA process stand for?", "Acknowledge"),
        ("What service acts like the internet's phonebook?", "DNS (Domain Name System)")
    ],
    "Ch 6: T-Shoot": [
        ("According to CompTIA, what is the very first step of troubleshooting?", "Identify the problem"),
        ("What should you do after you implement a solution?", "Verify full system functionality"),
        ("What is the final step you should always take when a ticket is resolved?", "Document findings, actions, and outcomes")
    ]
}

# --- Multiple Choice Test Bank (20 Questions) ---
PRACTICE_TEST_BANK = [
    {
        "q": "A network technician is configuring a firewall and needs to block unencrypted web traffic. Which port should be blocked?",
        "options": ["Port 443", "Port 80", "Port 22", "Port 53"],
        "answer": "Port 80",
        "exp": "Port 80 is used for HTTP (unencrypted web traffic). Port 443 is HTTPS (encrypted)."
    },
    {
        "q": "At which OSI layer does a standard network switch operate?",
        "options": ["Layer 1 (Physical)", "Layer 2 (Data Link)", "Layer 3 (Network)", "Layer 4 (Transport)"],
        "answer": "Layer 2 (Data Link)",
        "exp": "Switches operate at Layer 2, making forwarding decisions based on MAC addresses."
    },
    {
        "q": "A user states they cannot access the internet. According to the CompTIA troubleshooting methodology, what should the technician do FIRST?",
        "options": ["Establish a theory of probable cause", "Identify the problem", "Test the theory", "Establish a plan of action"],
        "answer": "Identify the problem",
        "exp": "Step 1 is always to identify the problem (e.g., questioning the user, duplicating the issue)."
    },
    {
        "q": "Which DNS record type is responsible for routing email to the correct server?",
        "options": ["A Record", "CNAME Record", "MX Record", "TXT Record"],
        "answer": "MX Record",
        "exp": "MX (Mail Exchanger) records direct email to a mail server."
    },
    {
        "q": "How many usable IP addresses are available in a network with a /26 CIDR notation?",
        "options": ["254", "126", "62", "30"],
        "answer": "62",
        "exp": "A /26 leaves 6 bits for hosts. (2^6) - 2 = 64 - 2 = 62 usable addresses."
    },
    {
        "q": "Which type of fiber optic cable uses lasers and is meant for long-distance transmissions?",
        "options": ["Multi-mode Fiber", "Single-mode Fiber", "Cat 6a", "Coaxial"],
        "answer": "Single-mode Fiber",
        "exp": "Single-mode fiber (SMF) uses lasers to shoot a single beam of light over long distances (kilometers)."
    },
    {
        "q": "Which protocol uses port 3389?",
        "options": ["SSH", "RDP", "FTP", "Telnet"],
        "answer": "RDP",
        "exp": "Remote Desktop Protocol (RDP) uses port 3389."
    },
    {
        "q": "What is the second step in the DHCP DORA process?",
        "options": ["Discover", "Offer", "Request", "Acknowledge"],
        "answer": "Offer",
        "exp": "The DORA process is Discover, Offer, Request, Acknowledge."
    },
    {
        "q": "Which of the following is the Protocol Data Unit (PDU) at Layer 3 of the OSI model?",
        "options": ["Bit", "Frame", "Packet", "Segment"],
        "answer": "Packet",
        "exp": "Layer 3 (Network) handles Packets. Layer 2 handles Frames, and Layer 4 handles Segments/Datagrams."
    },
    {
        "q": "A technician needs to run a copper cable that can support 10 Gbps speeds over a distance of 100 meters. Which cable is required?",
        "options": ["Cat 5e", "Cat 6", "Cat 6a", "Cat 5"],
        "answer": "Cat 6a",
        "exp": "Cat 6a supports 10 Gbps up to 100 meters. Standard Cat 6 only supports 10 Gbps up to 55 meters."
    },
    {
        "q": "What layer of the OSI model is responsible for opening, maintaining, and closing communication between two devices?",
        "options": ["Layer 4 (Transport)", "Layer 5 (Session)", "Layer 6 (Presentation)", "Layer 7 (Application)"],
        "answer": "Layer 5 (Session)",
        "exp": "The Session layer (Layer 5) manages the dialogue and connections (sessions) between applications."
    },
    {
        "q": "Which port is used by DNS to resolve domain names to IP addresses?",
        "options": ["Port 25", "Port 53", "Port 67", "Port 110"],
        "answer": "Port 53",
        "exp": "DNS primarily uses Port 53 to translate hostnames into IP addresses."
    },
    {
        "q": "Which device makes forwarding decisions based on IP addresses and connects different networks together?",
        "options": ["Switch", "Hub", "Router", "Access Point"],
        "answer": "Router",
        "exp": "Routers operate at Layer 3 and forward packets based on logical IP addresses."
    },
    {
        "q": "What is the CIDR notation for a subnet mask of 255.255.255.0?",
        "options": ["/16", "/24", "/25", "/26"],
        "answer": "/24",
        "exp": "A /24 subnet mask uses 24 network bits, which translates to 255.255.255.0."
    },
    {
        "q": "In the DHCP DORA process, what does the client send out to initially find a DHCP server?",
        "options": ["Acknowledge", "Request", "Discover", "Offer"],
        "answer": "Discover",
        "exp": "The client broadcasts a DHCP Discover packet to locate available DHCP servers on the network."
    },
    {
        "q": "After testing a theory to determine the cause of a problem, what is the NEXT step in the CompTIA troubleshooting methodology?",
        "options": ["Document findings", "Verify full system functionality", "Establish a plan of action", "Implement the solution"],
        "answer": "Establish a plan of action",
        "exp": "Once a theory is confirmed, Step 4 is to establish a plan of action to resolve the problem and identify potential effects."
    },
    {
        "q": "What is the maximum standard distance for Cat 5e and Cat 6a cables before signal degradation occurs?",
        "options": ["100 meters", "55 meters", "10 meters", "500 meters"],
        "answer": "100 meters",
        "exp": "Cat 5e and Cat 6a have a maximum length of 100 meters (approx. 328 feet) for reliable data transmission."
    },
    {
        "q": "Which of the following ports is used for secure, encrypted terminal access?",
        "options": ["Port 21 (FTP)", "Port 22 (SSH)", "Port 23 (Telnet)", "Port 3389 (RDP)"],
        "answer": "Port 22 (SSH)",
        "exp": "Secure Shell (SSH) uses Port 22 to provide encrypted command-line access. Telnet (23) is unencrypted."
    },
    {
        "q": "Which DNS record acts as an alias, pointing one domain name to another domain name?",
        "options": ["A Record", "AAAA Record", "MX Record", "CNAME Record"],
        "answer": "CNAME Record",
        "exp": "A Canonical Name (CNAME) record maps an alias name to a true or canonical domain name."
    },
    {
        "q": "What is the Protocol Data Unit (PDU) at Layer 2 of the OSI model?",
        "options": ["Bit", "Frame", "Packet", "Segment"],
        "answer": "Frame",
        "exp": "Data is encapsulated into Frames at Layer 2 (Data Link layer)."
    }
]

class StudyTab(ttk.Frame):
    def __init__(self, parent, chapter_name):
        super().__init__(parent)
        self.chapter_name = chapter_name
        self.questions = QUIZ_DATA.get(chapter_name, [])
        self.current_q_index = 0
        
        # --- Interactive Flashcard Section (Anchored to BOTTOM, Fixed Height) ---
        quiz_frame = ttk.LabelFrame(self, text="Practice Flashcards")
        quiz_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False, padx=10, pady=(5, 10))
        
        text_frame = ttk.Frame(quiz_frame)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 10), pady=15)
        
        btn_frame = ttk.Frame(quiz_frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 20), pady=15)
        
        self.lbl_progress = tk.Label(text_frame, text="", font=("Helvetica", 9, "bold"), fg="#7f8c8d", justify="left")
        self.lbl_progress.pack(anchor="w", pady=(0, 2))

        self.lbl_question = tk.Label(text_frame, text="", font=("Helvetica", 12, "bold"), wraplength=450, justify="left", height=2)
        self.lbl_question.pack(anchor="w", pady=(2, 5))
        
        self.lbl_answer = tk.Label(text_frame, text="", font=("Helvetica", 12, "italic"), fg="#27ae60", wraplength=450, justify="left", height=2)
        self.lbl_answer.pack(anchor="w", pady=(0, 5))
        
        style = ttk.Style()
        style.configure('Action.TButton', font=('Helvetica', 10, 'bold'))
        
        self.btn_show = ttk.Button(btn_frame, text="Show Answer", command=self.show_answer, style='Action.TButton')
        self.btn_show.pack(fill=tk.X, pady=(5, 5))
        
        self.btn_next = ttk.Button(btn_frame, text="Next Question", command=self.next_question, style='Action.TButton')
        self.btn_next.pack(fill=tk.X, pady=(5, 5))

        # --- Study Notes Section (Anchored to TOP, Expands to fill rest) ---
        notes_frame = ttk.LabelFrame(self, text="Chapter Summary")
        notes_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        
        notes_text = tk.Text(
            notes_frame, 
            wrap=tk.WORD, 
            font=("Helvetica", 11), 
            bg="#ffffff", 
            fg="#2c3e50", 
            padx=20, 
            pady=20, 
            spacing1=6,
            spacing2=4,
            spacing3=6,
            relief=tk.FLAT
        )
        notes_text.insert(tk.END, CHAPTER_CONTENT.get(chapter_name, "No content available."))
        notes_text.config(state=tk.DISABLED)
        notes_text.pack(fill=tk.BOTH, expand=True)
        
        random.shuffle(self.questions)
        self.load_question()

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

class PracticeTestTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.test_size = 20 # Increased to 20 questions
        self.current_test = []
        self.current_q_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()
        
        # --- UI Setup ---
        self.header_lbl = tk.Label(self, text="CompTIA Practice Simulator", font=("Helvetica", 14, "bold"), fg="#2c3e50")
        self.header_lbl.pack(pady=(20, 5))
        
        self.progress_lbl = tk.Label(self, text="", font=("Helvetica", 10), fg="#7f8c8d")
        self.progress_lbl.pack(pady=(0, 20))
        
        # Question Area
        self.q_frame = ttk.Frame(self)
        self.q_frame.pack(fill=tk.BOTH, expand=True, padx=40)
        
        self.lbl_question = tk.Label(self.q_frame, text="", font=("Helvetica", 12, "bold"), wraplength=550, justify="left")
        self.lbl_question.pack(anchor="w", pady=(0, 20))
        
        # Radio buttons for options
        self.radio_btns = []
        for _ in range(4):
            rb = ttk.Radiobutton(self.q_frame, text="", variable=self.selected_answer, value="")
            rb.pack(anchor="w", pady=5)
            self.radio_btns.append(rb)
            
        # Feedback Area
        self.feedback_lbl = tk.Label(self.q_frame, text="", font=("Helvetica", 11, "bold"), wraplength=550, justify="left")
        self.feedback_lbl.pack(anchor="w", pady=(20, 5))
        
        self.exp_lbl = tk.Label(self.q_frame, text="", font=("Helvetica", 11, "italic"), fg="#34495e", wraplength=550, justify="left")
        self.exp_lbl.pack(anchor="w", pady=(0, 20))
        
        # Controls
        self.controls_frame = ttk.Frame(self)
        self.controls_frame.pack(fill=tk.X, padx=40, pady=20)
        
        style = ttk.Style()
        style.configure('Test.TButton', font=('Helvetica', 11, 'bold'))
        
        self.btn_submit = ttk.Button(self.controls_frame, text="Submit Answer", command=self.submit_answer, style='Test.TButton')
        self.btn_submit.pack(side=tk.LEFT, padx=(0, 10))
        
        self.btn_next = ttk.Button(self.controls_frame, text="Next Question", command=self.next_question, style='Test.TButton', state=tk.DISABLED)
        self.btn_next.pack(side=tk.LEFT)
        
        self.btn_restart = ttk.Button(self.controls_frame, text="Start New Test", command=self.start_new_test, style='Test.TButton')
        # We only pack the restart button when the test is over
        
        self.start_new_test()

    def start_new_test(self):
        # Pull a random subset of questions (up to the max in the bank)
        self.current_test = random.sample(PRACTICE_TEST_BANK, min(self.test_size, len(PRACTICE_TEST_BANK)))
        self.current_q_index = 0
        self.score = 0
        
        self.btn_restart.pack_forget()
        self.btn_submit.pack(side=tk.LEFT, padx=(0, 10))
        self.btn_next.pack(side=tk.LEFT)
        
        self.load_question()
        
    def load_question(self):
        self.selected_answer.set("") 
        self.feedback_lbl.config(text="")
        self.exp_lbl.config(text="")
        self.btn_submit.config(state=tk.NORMAL)
        self.btn_next.config(state=tk.DISABLED)
        
        for rb in self.radio_btns:
            rb.config(state=tk.NORMAL)
        
        q_data = self.current_test[self.current_q_index]
        self.progress_lbl.config(text=f"Question {self.current_q_index + 1} of {len(self.current_test)} | Current Score: {self.score}")
        self.lbl_question.config(text=q_data["q"])
        
        # Shuffle options so the correct answer isn't always in the same spot
        options = q_data["options"].copy()
        random.shuffle(options)
        
        for i, rb in enumerate(self.radio_btns):
            if i < len(options):
                rb.config(text=options[i], value=options[i])
                rb.pack(anchor="w", pady=5)
            else:
                rb.pack_forget() 

    def submit_answer(self):
        selected = self.selected_answer.get()
        if not selected:
            self.feedback_lbl.config(text="Please select an answer first!", fg="#e74c3c")
            return
            
        q_data = self.current_test[self.current_q_index]
        self.btn_submit.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL)
        
        # Lock radio buttons
        for rb in self.radio_btns:
            rb.config(state=tk.DISABLED)
            
        if selected == q_data["answer"]:
            self.score += 1
            self.feedback_lbl.config(text="✅ Correct!", fg="#27ae60")
        else:
            self.feedback_lbl.config(text=f"❌ Incorrect. The correct answer was: {q_data['answer']}", fg="#c0392b")
            
        self.exp_lbl.config(text=q_data["exp"])
        
        # Update score instantly
        self.progress_lbl.config(text=f"Question {self.current_q_index + 1} of {len(self.current_test)} | Current Score: {self.score}")
        
        # If it was the last question, change the Next button to complete
        if self.current_q_index >= len(self.current_test) - 1:
            self.btn_next.config(text="Finish Test")

    def next_question(self):
        self.current_q_index += 1
        
        if self.current_q_index < len(self.current_test):
            self.btn_next.config(text="Next Question")
            self.load_question()
        else:
            # End of test
            self.show_results()
            
    def show_results(self):
        self.lbl_question.config(text=f"Test Complete!\n\nFinal Score: {self.score} out of {len(self.current_test)}")
        
        percent = (self.score / len(self.current_test)) * 100
        if percent >= 80:
            msg = "Great job! You're ready for the exam."
            color = "#27ae60"
        else:
            msg = "Keep studying! Review the flashcards and try again."
            color = "#f39c12"
            
        self.feedback_lbl.config(text=msg, fg=color)
        self.exp_lbl.config(text="")
        self.progress_lbl.config(text="")
        
        # Hide all radio buttons
        for rb in self.radio_btns:
            rb.pack_forget()
            
        self.btn_submit.pack_forget()
        self.btn_next.pack_forget()
        
        self.btn_restart.pack(side=tk.LEFT)

def main():
    root = tk.Tk()
    root.title(f"Network+ Beginner's Study Guide - Build {APP_VERSION}")
    root.geometry("700x780")
    
    style = ttk.Style()
    style.theme_use('clam')
    
    # 1. Pack Header FIRST
    header_frame = tk.Frame(root, bg="#34495e", pady=15)
    header_frame.pack(fill=tk.X, side=tk.TOP)
    tk.Label(header_frame, text="CompTIA Network+ Foundations", font=("Helvetica", 16, "bold"), fg="white", bg="#34495e").pack()
    tk.Label(header_frame, text="Learn the core concepts with simple analogies and flashcards.", font=("Helvetica", 10), fg="#bdc3c7", bg="#34495e").pack()
    
    # 2. Pack Footer SECOND
    footer_frame = tk.Frame(root, bg="#ecf0f1", pady=5)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_text = f"Built by {AUTHOR} | {BUILD_DATE} | Build {APP_VERSION}"
    tk.Label(footer_frame, text=footer_text, font=("Helvetica", 8, "bold"), fg="#7f8c8d", bg="#ecf0f1").pack()

    # 3. Pack Notebook LAST
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Add Chapter Tabs
    for chapter in CHAPTER_CONTENT.keys():
        tab = StudyTab(notebook, chapter)
        notebook.add(tab, text=chapter)
        
    # Add Practice Test Tab
    test_tab = PracticeTestTab(notebook)
    notebook.add(test_tab, text="🎓 Practice Test")
        
    root.mainloop()

if __name__ == "__main__":
    main()
