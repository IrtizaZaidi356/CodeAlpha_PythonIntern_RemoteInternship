"""
Task No# 03: Basic ChatBot | Python Intern | Remote Internship | Code Alpha

Perform Task:
   - Create a text-based chatbot that can have conversations with users.
 You can use natural language processing libraries like NLTK or spaCy
 to make your chatbot more conversational.

"""

import tkinter as tk
from tkinter import PhotoImage, scrolledtext
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from nltk.chat.util import Chat, reflections


class ChatBotApp:
    def __init__(self, chat_master):
        self.chat_master = chat_master
        chat_master.title("Basic ChatBot")
        # this removes the maximize button
        chat_master.resizable(0,0)
        img = PhotoImage(file="chatbot.png")
        chat_master.iconphoto(False, img)  # Replace with the actual path to your icon file
        
        style = ttk.Style()
        style.theme_use("elegance") # Use the elegance theme for ttk widgets
        
        self.chatbot = Chat(self.pairs, reflections)
        
        self.chat_display = scrolledtext.ScrolledText(chat_master, wrap = tk.WORD, width=50, height=15,bg="#d5f4f7",fg = "black", font=("Helvetica", 12))
        self.chat_display.grid(row= 0, column=0, columnspan=2, padx=12, pady=12, sticky="nsew")
        
        self.user_input = tk.Entry(chat_master, width= 40, font=("Helvetica", 12))
        self.user_input.grid(row=1,column=0,padx=12,pady=12, sticky="w")
        
        self.user_input.bind("<Return>", self.send_message_event)  # Bind Enter key to send_message function
        
        self.send_button = tk.Button(chat_master, text="Send", command= self.send_message, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.send_button.grid(row=1,column=1,padx=12,pady=12, sticky="e")
        
        self.display_welcome_message()
        
        for row in range(2):
            chat_master.grid_rowconfigure(row, weight=1)
        chat_master.grid_columnconfigure(0, weight=1)
    
    def display_welcome_message(self):
        welcome_msg = "\nWelcome!!! I'm your ChatBot. How can I help you today. \n\n Type bye / quit / exit to end the conversation."
        self.chat_display.insert(tk.END, f"Bot: {welcome_msg}\n\n")
    
    def send_message(self):
        user_msg = self.user_input.get()
        if not user_msg:
            messagebox.showinfo("Input Error", "Please enter a message.")
            return
        
        self.user_input.delete(0, tk.END)
        response = self.get_response(user_msg)
        self.chat_display.insert(tk.END, f"User: {user_msg}\n")
        self.chat_display.insert(tk.END,f"Bot: {response}\n\n")

    def send_message_event(self, event):  # Accept event parameter for binding Enter key
        self.send_message()
    
    def get_response(self, user_msg):
        return self.chatbot.respond(user_msg)
    
    pairs = [
        [
            r"hi|hello|hey",
            [" Hello! "," Hi There! ", " Greeting! How are you doing today?"]
        ],
        [
            r"how are you|how's it going",
            ["I'm good, thank you!","I'm doing well, how about you?"]
        ],
        [
            r"I'm fine|i am fine",
            ["good"]
        ],
        [
            r"what is your name",
            ["I am a AliZar ChatBot.You can call me Ali.People call me Ali."]
        ],
        [
            r"what can you do",
            ["I can chat with you, answer questions or just keep you company.Feel free to ask me anything!"]
        ],
        [
            r"what do you like to do",
            ["I enjoy chatting with people, answering questions, and learning new things!, I don't have hobbies like humans, but I love our conversations."]
        ],
        [
            r"what's up",
            ["Not much, just chatting with you! What's up with you?", "Just hanging out. What's up with you?"]    
        ],
        [
            r"tell me a joke",
            ["Sure, here's one: Why don't scientists trust atoms? Because they make up everything!", "I told my wife she should embrace her mistakes. She gave me a hug."]
        ],
        [
            r"how old are you",
            ["I don't have an age. I exist in the realm of code.", "I'm ageless, like a digital vampire."]  
        ],
        [
            r"what's the weather like",
            ["I'm sorry, I don't have real-time data. You might want to check a weather website.", "I can't provide current weather information."]
        ],
        [
            r"tell me about your day|your day",
            ["I don't have days like humans, but I'm always here to chat with you! How was your day?", "Every day is the same for me, just waiting for our conversations! How was your day?"]
        ],
        [
            r"who created you",
            ["I was created by SYED IRTIZA ABBAS ZAIDI. He is a Good Python Delveoper, My creators is talented Boy."] 
        ],
        [
            r"thank you|thanks",
            ["You're welcome! If you have any questions or just want to chat, feel free to ask.", "No problem! If there's anything else you'd like to talk about, let me know."]
        ],
        [
            r"bye|quit|exit",
            ["Goodbye!","Bye, take care!"]
        ],
        [
            r"(.*)",
            ["I'm sorry, I don't Understand.","Can you please rehrase that?"]
        ]
    ]

if __name__ == "__main__":
    root = ThemedTk(theme="elegance")
    app = ChatBotApp(root)
    root.mainloop()