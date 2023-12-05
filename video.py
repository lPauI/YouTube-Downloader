from tkinter import *
from tkinter import filedialog, messagebox, ttk

from pytube import YouTube

from pytube.exceptions import RegexMatchError


class Video:
    def __init__(self):
        self.video = None
        self.download_location = None
        self.resolution_box = None
        self.resolution_label = None
        self.resolution_chose = None
        self.resolutions = None

    def set_location(self, location_entry):
        temp_location = filedialog.askdirectory()
        
        if temp_location:
            self.download_location = temp_location
            location_entry.config(text=self.download_location)

    def convert(self, window, link_entry):
        try:
            self.video = YouTube(url=link_entry.get())

        except RegexMatchError:
            messagebox.showerror(title="Invalid Link", message="The video link is invalid.")

        else:
            self.resolutions = []

            for stream in self.video.streams:
                resolution = stream.resolution
                if resolution and resolution not in self.resolutions:
                    self.resolutions.append(resolution)

            self.resolutions.sort()

            self.resolution_label = Label(text="Resolution:")
            self.resolution_label.grid(row=3, column=0)

            self.resolution_chose = StringVar()
            self.resolution_box = ttk.Combobox(window, width=27, textvariable=self.resolution_chose)

            self.resolution_box['values'] = self.resolutions

            self.resolution_box.grid(column=1, row=3)
            self.resolution_box.current()

    def download(self):
        if self.video == None:
            messagebox.showerror(title="Video not converted",
                                 message="The video was not converted so you can't download it.")
            return
        
        if self.video.age_restricted:
            messagebox.showerror(title="Age Restricted",
                                 message="This video is age restricted so you can't download it.")

        else:
            resolution = self.resolution_chose.get()

            if resolution in self.resolutions:
                video_filtered = self.video.streams.filter(
                    res=self.resolution_chose.get(),
                    file_extension="mp4"
                )

            else:
                video_filtered = self.video.streams.filter(
                    file_extension="mp4"
                )

            video_filtered.first().download(output_path=self.download_location)

            messagebox.showinfo(
                title="Successful Download",
                message="The video has been downloaded successfully."
            )
