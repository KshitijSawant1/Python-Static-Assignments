import tkinter as tk
import webbrowser


def submit_form():
    course = entry.get()
    source = sourcevar.get()
    if source == "Facbook Ads":
        webbrowser.open(
            "https://developers.facebook.com/docs/app-ads/support/")
    elif source == "YouTube Ads":
        webbrowser.open(
            "https://support.google.com/youtube/thread/677314/%F0%9F%94%8D-youtube-faqs-need-help-start-here?hl=en")
    elif source == "Instgram Ads":
        webbrowser.open("https://help.instagram.com/")


window = tk.Tk()
window.title("Course Enrollment Form")
label1 = tk.Label(window, text="Course:")
label1.pack()
entry = tk.Entry(window)
entry.pack()
label2 = tk.Label(window, text="Source:")
label2.pack()
sources = ["Facebook Ads", "YouTube Ads", "Instagram Ads"]
sourcevar = tk.StringVar(window)
sourcevar.set(sources[0])
dropdown = tk.OptionMenu(window, sourcevar, *sources)
dropdown.pack()
button = tk.Button(window, text="Submit", command=submit_form)
button.pack()
window.mainloop()
