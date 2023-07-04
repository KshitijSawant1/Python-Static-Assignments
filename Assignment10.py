from tkinter import ttk
import tkinter as tk
import webbrowser


def navigate_to_website():
    site_url = entry.get()
    print("Navigating to", site_url)
    webbrowser.open(site_url)


def navigate_to_website_for_button2():
    site_url = "https://www.youtube.com/"
    print("Navigating to", site_url)
    webbrowser.open(site_url)


def navigate_to_website_for_button3():
    site_url = "http://staticinteducare.in/"
    print("Navigating to", site_url)
    webbrowser.open(site_url)


def navigate_to_website_for_button4():
    site_url = "https://chat.openai.com/"
    print("Navigating to", site_url)
    webbrowser.open(site_url)


def navigate_to_website_for_button5():
    site_url = "https://github.com/KshitijSawant1/Python-Static-Assignments"
    print("Navigating to", site_url)
    webbrowser.open(site_url)


def button_clicked():
    label["text"] = entry.get()


root = tk.Tk()
root.title("Website Navigator")
root.title("Tkinter GUI Example")
frame = ttk.Frame(root, padding=20)
frame.pack()
label = ttk.Label(frame, text="Enter Website url")
label.grid(row=0, column=0, sticky="w")
entry = ttk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=10)
button1 = ttk.Button(frame, text="Navigate search")
button1.grid(row=1, column=0, pady=10)
button2 = ttk.Button(frame, text="Youtube")
button2.grid(row=1, column=1, pady=10)
button3 = ttk.Button(frame, text="Static Int Educare")
button3.grid(row=1, column=2, pady=10)
button4 = ttk.Button(frame, text="Chat GPT")
button4.grid(row=2, column=0, pady=10)
button5 = ttk.Button(frame, text="MY GIT REPOSITARY ")
button5.grid(row=2, column=1, pady=10)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 20), foreground="White")
style.configure("TButton", font=("Helvetica", 20),
                foreground="white", background="blue")

label["style"] = "TLabel"
button1["style"] = "TButton"
button2["style"] = "TButton"
button3["style"] = "TButton"
button4["style"] = "TButton"
button5["style"] = "TButton"

button1["command"] = navigate_to_website
button2["command"] = navigate_to_website_for_button2
button3["command"] = navigate_to_website_for_button3
button4["command"] = navigate_to_website_for_button4
button5["command"] = navigate_to_website_for_button5


root.mainloop()
