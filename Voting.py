from tkinter import *
from PIL import ImageTk, Image

def jagte_raho():
    jagte_party = Toplevel()
    jagte_party.grab_set()
    jagte_party.geometry("1150x1000+200+50")
    jagte_party.config(bg="#FFEFDB")
    pic13 = Image.open("/Users/namansisodia/Downloads/2fcb3743-e452-4d22-ac1b-b976a7002947.png")
    img13 = pic13.resize((500, 450))
    img13_tk = ImageTk.PhotoImage(img13)

    # Create and place the image label
    img13_label = Label(jagte_party, image=img13_tk)
    img13_label.place(x=300, y=30)
    jagte_menifest = """Welcome to the Ultimate Jagte Raho Party!
        Mr.Rahul Mandal.k

    Get ready to stay up all night in the most hilariously sleepless celebration ever! Our mission? 
    To laugh until dawn, fueled by endless chai and snacks that defy the laws of midnight cravings. 
    Wear your comfiest pajamas or go wild with quirky nightwear—bonus points for eye masks worn as 
    headbands. We'll play games that keep us awake, from "Sleepy Charades" to "Midnight Karaoke," 
    and swap ghost stories that end in punchlines, not nightmares. Expect pillow fights, impromptu 
    dance-offs, and the best part: watching the sunrise together, bleary-eyed but with hearts full 
    of laughter. At the Jagte Raho Party, sleep is optional, but fun is mandatory!"""
    gtext = Label(jagte_party, text=jagte_menifest, font=("Garamond", 28, "bold"), bg="#FFEFDB",
                  fg="Black")
    gtext.place(x=5, y=510)

    jagte_button = Button(jagte_party, text="Vote\nवोट", font=("Garamond", 25, "bold"), width=10, height=3)
    jagte_button.place(x=450, y=850)



    jagte_party.mainloop()
def gym_party():
    gym_party = Toplevel()
    gym_party.grab_set()
    gym_party.geometry("1150x1000+200+50")
    gym_party.config(bg="#FFEFDB")

    pic12 = Image.open("/Users/namansisodia/Downloads/483edeb4-9fe2-425a-9d45-96e92685e2ea.png")
    img12 = pic12.resize((500, 450))
    img12_tk = ImageTk.PhotoImage(img12)

    # Create and place the image label
    img12_label = Label(gym_party, image=img12_tk)
    img12_label.place(x=300, y=30)
    gym_menifest = """Welcome to the Ultimate Gym Party Pump-up!
        Mrs.Gauravi Kamarkar

    Get ready to lift your spirits (and maybe a few dumbbells) in the most hilarious workout 
    session ever! Our mission? To sweat out the stress and laugh off the calories. Dress in your 
    wildest workout gear—neon spandex, leg warmers, or a superhero costume if you're feeling extra 
    strong. We'll tackle burpees with a side of giggles, plank while telling our worst dad jokes, 
    and turn treadmill sprints into dance-offs. Protein shakes will be served with a dash of humor, 
    and the only thing heavier than our weights will be the belly laughs. Remember, here at the Gym 
    Party, we're flexing our funny muscles and getting fit for fun!"""
    gtext = Label(gym_party, text=gym_menifest, font=("Garamond", 28, "bold"), bg="#FFEFDB",
                  fg="Black")
    gtext.place(x=5, y=510)
    gym_button = Button(gym_party, text="Vote\nवोट", font=("Garamond", 25, "bold"), width=10, height=3)
    gym_button.place(x=450, y=850)



    gym_party.mainloop()
def meme_party():
    meme_party = Toplevel()
    meme_party.grab_set()
    meme_party.geometry("1150x1000+200+50")
    meme_party.config(bg="#FFEFDB")


    pic11 = Image.open("/Users/namansisodia/Downloads/bjp.jpeg")
    img11 = pic11.resize((500, 450))
    img11_tk = ImageTk.PhotoImage(img11)

    # Create and place the image label
    img11_label = Label(meme_party, image=img11_tk)
    img11_label.place(x=300, y=30)

    meme_menifest = """Welcome to the Ultimate Meme Party Extravaganza!
          Mr.Harsh Tomar

    Prepare for a night where the WiFi is strong, the memes are stronger, and laughter is the universal 
    currency! Dress code: meme-inspired attire, from "Distracted " to "Mocking SpongeBob." Our 
    goal? To out-meme each other with viral videos, dank memes, and meme-tastic games like "Caption 
    This" and "Meme Charades." Expect a playlist of meme songs, snacks that are as random as the 
    internet itself,and a meme wall where you can pin your all-time favorites. Remember, the
     only rule is: there are no rules—just endless scrolling, tagging, and LOLs. Let’s make 
     this party so epic, it becomes a meme itself!"""
    mtext = Label(meme_party, text=meme_menifest, font=("Garamond", 28, "bold"), bg="#FFEFDB",
                  fg="Black")
    mtext.place(x=5, y=510)
    meme_button = Button(meme_party, text="Vote\nवोट", font=("Garamond", 25, "bold"), width=10, height=3)
    meme_button.place(x=450, y=850)



    meme_party.mainloop()

def chai_party():
    chai_root = Toplevel()
    chai_root.grab_set()
    chai_root.geometry("1150x1000+200+50")
    chai_root.config(bg="#FFEFDB")
    pic10 = Image.open("/Users/namansisodia/Downloads/ae02c0bc-4a5f-484e-8a8b-d488cd8681e2.png")
    img10 = pic10.resize((500, 450))
    img10_tk = ImageTk.PhotoImage(img10)

    # Create and place the image label
    img10_label = Label(chai_root, image=img10_tk)
    img10_label.place(x=300, y=30)
    chai_menifest = """Welcome to the Ultimate Chai Party Bash!
      Mr.Naman Sisodia

    Prepare your taste buds and funny bones for a night where chai flows like a river and laughter bubbles 
    over like a perfectly brewed pot! Dress in your finest kurta pajamas, chai-themed tees, or even a teapot
     hat if you're feeling adventurous. Our tea selection, ranging from classic masala to exotic flavors that
      make you go "What the...?", is here to keep you sipping and smiling all night long. With endless refills
      , hilarious tea-related games, and conversations that start with "Chai pe charcha" and end with belly
       laughs, this party is all about celebrating the magic of tea and the joy of good company. Cheers to 
       chai and chuckles!"""
    chaitext = Label(chai_root, text=chai_menifest, font=("Garamond", 28, "bold"), bg="#FFEFDB",
                  fg="Black")
    chaitext.place(x=5, y=510)
    chai_button = Button(chai_root, text="Vote\nवोट", font=("Garamond", 25, "bold"), width=10, height=3)
    chai_button.place(x=450, y=850)

    chai_root.mainloop()
def pajma_party():
    proot = Toplevel()
    proot.grab_set()
    proot.geometry("1150x1000+200+50")
    proot.config(bg="#FFEFDB")
    pic9 = Image.open("/Users/namansisodia/Downloads/Spa.png")
    img9 = pic9.resize((500, 450))
    img9_tk = ImageTk.PhotoImage(img9)

    # Create and place the image label
    img9_label = Label(proot, image=img9_tk)
    img9_label.place(x=300, y=30)
    menifest = """Welcome to the Ultimate Pajama Party Extravaganza!
          Mr.Shubham Yadav 

    Get ready for a night where comfort reigns supreme, and laughter is non-negotiable. 
    Embrace your fluffiest, quirkiest pajamas and prepare for snack attacks that defy bedtime rules. 
    Pillow fights are not just allowed—they're mandatory, with bonus points for the most feathers in 
    your hair. Expect impromptu dance-offs in slippers, Netflix marathons interrupted by giggle fits, 
    and a lot of photo evidence you’ll probably regret (but secretly cherish). Leave your worries at 
    the door, and let’s turn our sleepwear into party gear for a night of legendary fun!"""
    ptext = Label(proot, text=menifest, font=("Garamond", 28, "bold"), bg="#FFEFDB",
                  fg="Black")
    ptext.place(x=5, y=510)
    vote_button = Button(proot, text="Vote\nवोट", font=("Garamond", 25,"bold"),width=10,height=3)
    vote_button.place(x=450, y=800)


    proot.mainloop()
def new_regis():
    nroot =Toplevel()
    nroot.grab_set()
    nroot.geometry("700x400+200+50")
    nroot.config(bg="#FFEFDB")
    ntext = Label(nroot, text="Registration Form\nपंजीकरण फॉर्म ", font=("Garamond", 30, "bold"), bg="#CDC0B0",
                  fg="Black")
    ntext.place(x=230, y=10)
    name =Label(nroot, text="Name:\nनाम", font=("Garamond", 20), bg="#FFEFDB", fg="Black")
    name.place(x=50, y=100)
    name_entry = Entry(nroot, font=("Garamond", 20))
    name_entry.place(x=230, y=100, width=300)

    age = Label(nroot, text="Age:\nआयु", font=("Garamond", 20), bg="#FFEFDB", fg="Black")
    age.place(x=50, y=150)
    age_entry = Entry(nroot, font=("Garamond", 20))
    age_entry.place(x=230, y=150, width=300)

    adhar_card = Label(nroot, text="Aadhaar Number:\nआधार कार्ड नंबर", font=("Garamond", 20), bg="#FFEFDB", fg="Black")
    adhar_card.place(x=50, y=200)
    aadhaar_entry = Entry(nroot, font=("Garamond", 20))
    aadhaar_entry.place(x=230, y=200, width=300)

    phn=Label(nroot, text="Phone Number:\nफ़ोन नंबर", font=("Garamond", 20), bg="#FFEFDB", fg="Black")
    phn.place(x=50, y=250)
    phone_entry = Entry(nroot, font=("Garamond", 20))
    phone_entry.place(x=230, y=250, width=300)

    def submit():
        name = name_entry.get()
        age = age_entry.get()
        aadhaar = aadhaar_entry.get()
        phone = phone_entry.get()
        # Here you can add the code to process/store the registration information
        print(f"Name: {name}, Age: {age}, Aadhaar: {aadhaar}, Phone: {phone}")
        # Optionally, clear the fields after submission
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        aadhaar_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

    submit_button = Button(nroot, text="Submit", font=("Garamond", 20), command=submit)
    submit_button.place(x=250, y=350)



    nroot.mainloop()
def candidate():
    croot = Toplevel()
    croot.grab_set()
    croot.geometry("1000x1000+200+50")
    croot.config(bg="#FFEFDB")
    ctext=Label(croot,text="Candidate List: \nउम्मीदवार सूची  ",font=("Garamond", 30, "bold"), bg="#FFEFDB", fg="Black")
    ctext.place(x=50,y=10)

    ctext1 = Label(croot, text="1. The Pajama Party Politicians \nपायजामा पार्टी के राजनेता  ", font=("Garamond", 30, "bold"), bg="#FFEFDB",
                  fg="Black")
    ctext1.place(x=20, y=110)
    pic3 = Image.open("//Users/namansisodia/Downloads/Spa.png")
    img3 = pic3.resize((150, 150))
    img3_tk = ImageTk.PhotoImage(img3)

    # Create and place the image label
    img3_label = Label(croot, image=img3_tk)
    img3_label.place(x=500, y=50)
    btn1 = Button(croot, text="Read Menifesto , Vote \nमेनिफेस्टो पढ़ें, वोट करें", width=20, command=pajma_party, height=3,
                      font=("Garamond", 20), bg="#CDC0B0", fg="black")
    btn1.place(x=700, y=110)
    ctext2 = Label(croot, text="2.The Chai Charcha Party\nचाय चर्चा कबीला   ",font=("Garamond", 30, "bold"), bg="#FFEFDB", fg="Black")
    ctext2.place(x=20, y=260)
    pic4 = Image.open("/Users/namansisodia/Downloads/ae02c0bc-4a5f-484e-8a8b-d488cd8681e2.png")
    img4 = pic4.resize((150, 150))
    img4_tk = ImageTk.PhotoImage(img4)

    # Create and place the image label
    img4_label = Label(croot, image=img4_tk)
    img4_label.place(x=500, y=220)
    btn2 = Button(croot, text="Read Menifesto , Vote \nमेनिफेस्टो पढ़ें, वोट करें", width=20, command=chai_party, height=3,
                  font=("Garamond", 20), bg="#CDC0B0", fg="black")
    btn2.place(x=700, y=260)
    ctext3 = Label(croot, text="3.The Meme Masters Party\nमेमे मास्टर्स पार्टी   ", font=("Garamond", 30, "bold"),
                   bg="#FFEFDB", fg="Black")
    ctext3.place(x=20, y=420)
    pic5 = Image.open("/Users/namansisodia/Downloads/bjp.jpeg")
    img5 = pic5.resize((150, 150))
    img5_tk = ImageTk.PhotoImage(img5)

    # Create and place the image label
    img5_label = Label(croot, image=img5_tk)
    img5_label.place(x=500, y=390)
    btn3 = Button(croot, text="Read Menifesto , Vote \nमेनिफेस्टो पढ़ें, वोट करें", width=20, command=meme_party,height=3,
                  font=("Garamond", 20), bg="#CDC0B0", fg="black")
    btn3.place(x=700, y=420)
    ctext4 = Label(croot,text="4.The GYM party \nजिम पार्टी",font=("Garamond",30,"bold"),bg="#FFEFDB",fg="black")
    ctext4.place(x=20,y=580)
    pic7 = Image.open("/Users/namansisodia/Downloads/483edeb4-9fe2-425a-9d45-96e92685e2ea.png")
    img7 = pic7.resize((150, 150))
    img7_tk = ImageTk.PhotoImage(img7)

    # Create and place the image label
    img7_label = Label(croot, image=img7_tk)
    img7_label.place(x=500, y=560)
    btn4 = Button(croot, text="Read Menifesto , Vote \nमेनिफेस्टो पढ़ें, वोट करें", width=20, command=gym_party, height=3,
                  font=("Garamond", 20), bg="#CDC0B0", fg="black")
    btn4.place(x=700, y=580)
    ctext5 = Label(croot, text="5.The Jagte Raho Party\nजागते रहो पार्टी ", font=("Garamond", 30, "bold"), bg="#FFEFDB", fg="black")
    ctext5.place(x=20, y=740)
    pic8 = Image.open("/Users/namansisodia/Downloads/2fcb3743-e452-4d22-ac1b-b976a7002947.png")
    img8 = pic8.resize((150, 150))
    img8_tk = ImageTk.PhotoImage(img8)

    # Create and place the image label
    img8_label = Label(croot, image=img8_tk)
    img8_label.place(x=500, y=730)
    btn5 = Button(croot, text="Read Menifesto , Vote \nमेनिफेस्टो पढ़ें, वोट करें", width=20, command=jagte_raho,height=3,
                  font=("Garamond", 20), bg="#CDC0B0", fg="black")
    btn5.place(x=700, y=740)












    croot.mainloop()

def login_here():
    lroot = Toplevel()
    lroot.grab_set()
    lroot.geometry("1000x850+200+50")
    lroot.config(bg="#FFEFDB")
    pic2 = Image.open("/Users/namansisodia/Downloads/icon.jpg")
    img2 = pic2.resize((1000, 321))
    img2_tk = ImageTk.PhotoImage(img2)

    # Create and place the image label
    img2_label = Label(lroot, image=img2_tk)
    img2_label.place(x=0, y=0)

    description_text = """The Terms and Conditions for participating in the voting process are as follows:
    By engaging in the voting process, voters affirm their eligibility as registered members of the organization 
    and commit to verifying their identity and membership status as necessary. Voters will receive a unique 
    voting link or access to the voting platform during the specified voting period and agree to cast their 
    vote within this timeframe, understanding that only one vote is allowed per voter.
    Voters agree to maintain the confidentiality of their vote and refrain from disclosing their choice to 
    others, acknowledging the organization's commitment to ensuring the integrity and confidentiality of the 
    voting process. Voters also pledge not to engage in any fraudulent activities, including vote tampering, 
    buying votes, or coercing others to vote in a particular manner. Any such activities will result in 
    disqualification and potential disciplinary measures.
    Upon completion of the voting period, the organization will announce the results through official communication 
    channels on the designated announcement date. Voters recognize that the organization's decision regarding 
    the results of the vote is final and binding.
    In the event of disputes related to the voting process or this agreement, voters agree to participate in mediation
    facilitated by an independent third party appointed by the organization. Should mediation fail to resolve the dispute,
    the organization's decision will be considered conclusive.
    By participating in the voting process, voters affirm their understanding and acceptance of all terms and conditions
    outlined in this agreement and any additional rules or guidelines provided by the organization. The organization 
    reserves the right to modify these terms and conditions with prior notice to voters through official channels."""
    ltext2 = Label(lroot, font=("Garamond", 20, "bold"), bg="#FFEFDB", fg="Black", text=description_text, justify=LEFT)
    ltext2.place(x=15, y=330)

    terms_checkbox = Checkbutton(lroot, text="I agree to the Terms and Conditions",font=("Garamond", 20,"bold"), bg="#FFEFDB",fg="Black")
    terms_checkbox.place(x=15, y=750)
    term_btn = Button(lroot, text="Proceed Further\nजारी रखें", width=11,command=candidate, height=2,font=("Garamond", 20), bg="grey", fg="black")
    term_btn.place(x=350,y=760)




    lroot.mainloop()
def Hindime():
    hroot = Tk()
    hroot.geometry("930x330")
    hroot.configure(bg="#FFEFDB")
    htext_main = "मतदान लोकतांत्रिक समाजों की आधारशिला है, जो व्यक्तियों को चुनाव, जनमत \nसंग्रह, कॉर्पोरेट वोट और ऑनलाइन मतदान जैसे विभिन्न माध्यमों से अपनी \nप्राथमिकताएं व्यक्त करने और निर्णय लेने में सक्षम बनाता है। यह \nसुनिश्चित करता है कि नेताओं को बहुमत द्वारा चुना जाता है,\nनीतियां लोगों की इच्छा को प्रतिबिंबित करती हैं, और \nमहत्वपूर्ण मुद्दों का निर्णय सीधे मतदाताओं द्वारा किया जाता है"
    text1 = Label(hroot, text=htext_main, font=("Garamond", 32, "bold"), bg="#FFEFDB", fg="Black")
    text1.place(x=15, y=30)
    hroot.mainloop()



root = Tk()
root.geometry("1500x1500+100+50")
root.configure(bg="#FFEFDB")

pic1 = Image.open("/Users/namansisodia/Downloads/VVPAT-Election-voting-2-scaled.jpg")
img1 = pic1.resize((1500, 321))
img1_tk = ImageTk.PhotoImage(img1)

# Create and place the image label
img1_label = Label(root, image=img1_tk)
img1_label.place(x=0, y=0)

text_main = "Welcome To Online Voting Booth \nऑनलाइन वोटिंग बूथ में आपका स्वागत है"
text1 = Label(root, text=text_main, font=("Garamond", 32, "bold"), bg="#FFEFDB", fg="Black")
text1.place(x=470, y=300)

description_text="Voting is a cornerstone of democratic societies, enabling individuals to express their preferences and make decisions through various \nmeans such as elections, referendums, corporate votes, and online polls. It ensures that leaders are chosen by the majority,\npolicies reflect the will of the people, and important issues are decided directly by the electorate."
text2 = Label(root, font=("Garamond", 28, "bold"), bg="#FFEFDB", fg="Black", text=description_text, justify=LEFT)
text2.place(x=15, y=370)

Hindi = Button(root, text="In हिन्दी", width=8, height=1, font=("Garamond", 20), command=Hindime, bg="grey", fg="black")
Hindi.place(x=1070, y=440)

text3 = Label(root, font=("Garamond", 28, "bold"), bg="#FFEFDB", fg="Black", text="Please Mention Your Login Credentials \n(कृपया अपने लॉगिन क्रेडेंशियल का उल्लेख करें );")
text3.place(x=20, y=480)

text4 = Label(root, font=("Garamond", 28, "bold"), bg="#FFEFDB", fg="Black", text="Aadhaar Card Number = \nआधार कार्ड नंबर")
text4.place(x=20, y=550)
text4_entry = Entry(root, width=40, fg="Black", bg="#F0F8FF",font=("Garamond",20 , "bold"))
text4_entry .place(x=320, y=560)

text5 = Label(root, font=("Garamond", 28, "bold"), bg="#FFEFDB", fg="Black", text="Voter Id Card Number = \nवोटर आई कार्ड ")
text5.place(x=20, y=620)
text5_entry = Entry(root, width=40, fg="Black", bg="#F0F8FF",font=("Garamond",20 , "bold"))
text5_entry .place(x=320, y=630)

text6 = Label(root, font=("Garamond", 28, "bold"), bg="#FFEFDB", fg="Black", text="Phone Number     = \nफ़ोन नंबर")
text6.place(x=20, y=690)
text6_entry = Entry(root, width=40, fg="Black", bg="#F0F8FF",font=("Garamond",20 , "bold"))
text6_entry .place(x=320, y=700)

text7 = Label(root, font=("Garamond", 28, "bold"), bg="#FFEFDB", fg="Black", text="Login to Vote Your Favourite Candidate \n  अपने पसंदीदा उम्मीदवार को वोट करने के लिए लॉगिन करें")
text7.place(x=20, y=770)

Login_btn = Button(root, text="LOGIN HERE \nयहां लॉगिन करें", width=11, height=2, command=login_here,font=("Garamond", 20), bg="grey", fg="black")
Login_btn.place(x=640, y=770)


frame = Frame(root, bg="#CDC0B0",border=10)
frame.place(x=850, y=500, width=650, height=550)
ftext = Label(frame,text="Login for New Registration\nनए पंजीकरण के लिए लॉगिन करें",font=("Garamond",28,"bold"),bg="#CDC0B0", fg="Black")
ftext.place(x=150,y=10)
fbtn = Button(frame,text="New Ragistration", width=11, height=2, command=new_regis,font=("Garamond", 20), bg="grey", fg="black")
fbtn.place(x=220, y=100)

pic6 = Image.open("/Users/namansisodia/Downloads/great-indian-general-election-concept-with-evm-machine-inked-finger-chair-vector-illustration_1076263-1870.jpg")
img6 = pic6.resize((620, 330))
img6_tk = ImageTk.PhotoImage(img6)

# Create and place the image label
img6_label = Label(frame, image=img6_tk)
img6_label.place(x=5,y=180)

result = Button(root,text="Live Result\nलाइव परिणाम",width=21, height=2,font=("Garamond", 28,"bold"), bg="grey", fg="black")
result.place(x=270,y=900)


root.mainloop()