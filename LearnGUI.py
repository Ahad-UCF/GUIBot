from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import tkinter as  tk
import time

# A bot that logs into facebook 
class Fbbot:
    # Note that this code will need to be modified to use your own geckodriver path
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path=r'C:\Users\Ahad\AppData\Local\Programs\Python\Python37-32\geckodriver.exe')
    
    # Logs into an account, the sleeps are simply to wait for the page to load
    def login(self):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        time.sleep(5) 
        email = bot.find_element_by_name("email")
        password = bot.find_element_by_name("pass")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    
# Creates a bot which logs in 
def log(username, password):
    TestBot = Fbbot(username, password)
    TestBot.login()    


HEIGHT = 300
WIDTH = 400

# Initialize a tkinter 
root = tk.Tk()

# Create a canvas for our gui
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


frame = tk.Frame(root, bg = "#0249ba")
frame.place(relwidth = 1, relheight = 1)

entry1 = tk.Entry(frame, font = 16, bd = 0)
entry1.place(relx = 0.25, rely = 0.05, relwidth = 0.7, relheight = 0.25)

label1 = tk.Label(frame, font = 16, text = "Email: ", anchor = 'w')
label1.place(relx = 0.05, rely = 0.05, relwidth = 0.2, relheight = 0.25)

entry2 = tk.Entry(frame, font = 16, bd = 0)
entry2.place(relx = 0.25, rely = 0.37, relwidth = 0.7, relheight = 0.25)
entry2.config(show ='*')

label2 = tk.Label(frame, font = 16, text = "Password: ", anchor = "w")
label2.place(relx = 0.05, rely = 0.37, relwidth = 0.2, relheight = 0.25)

# Pressing this button will create the bot
button = tk.Button(frame, text = "Open FaceBook", bg = 'white', font = 16, command = lambda: log(entry1.get(), entry2.get()))
button.place(relx = 0.05, rely = 0.68, relwidth = 0.9, relheight = 0.25)

# Start our GUI 
root.mainloop()


