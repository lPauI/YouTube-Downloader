from tkinter import *

from video import Video

window = Tk()
window.title("YouTube Downloader")
window.config(padx=50, pady=50)

canvas = Canvas(window)
video = Video()

logo = PhotoImage(file="logo.png")
canvas.create_image(200, 130, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

link_label = Label(text="YouTube Link:")
link_label.grid(row=1, column=0)

link_entry = Entry(width=36)
link_entry.grid(row=1, column=1, padx=10, pady=20)

convert_button = Button(text="Convert", command=lambda: video.convert(window, link_entry))
convert_button.grid(row=1, column=2)

location_entry = Button(text="Click me to set the location", width=50,
                        command=lambda: video.set_location(location_entry))
location_entry.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

download_entry = Button(text="Download", width=20, command=lambda: video.download())
download_entry.grid(row=5, column=0, columnspan=2)

window.mainloop()
