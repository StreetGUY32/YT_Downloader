from tkinter import *
import pathlib
from pytube import YouTube

from tkinter import messagebox, filedialog


# adding Widgets

def Widgets():
    link_label = Label(root, text="YouTube link: ", bg="#E8D579", width=20)
    link_label.grid(row=1, column=0, pady=5, padx=5)

    linkText = Entry(root, width=55, textvariable=video_Link)
    linkText.grid(row=1, column=0, pady=5, padx=5, columnspan=2)

    destination_label = Label(
        root, text="Destination : ", bg="#E8D579", width=20)
    destination_label.grid(row=1, column=0, pady=5, padx=5)

    destination_Text = Entry(root, width=40, textvariable=download_Path)
    destination_Text.grid(row=2, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Browse", command=Browse,
                      width=10, bg="#05E8E0")
    browse_B.grid(row=2, column=2, pady=1, padx=1)

    download_B = Button(root, text="Download",
                        command=Download, width=20, bg="#05E8E0")
    download_B.grid(row=3, column=1, pady=3, padx=3)


# browse function

def Browse():
    download_Directory = filedialog.askdirectory(initialdir=pathlib.Path.cwd())
    # displaying the directory in the directory text box
    download_Path.set(download_Directory)


# download function

def Download():
    # getting link from the user
    YouTube_link = video_Link.get()
    download_Folder = download_Path.get()
    # creating obj fot thr YT
    getVideo = YouTube(YouTube_link)
    # getting all the video quality and selecting the first
    videoStream = getVideo.streams.first()
    # downloading video to the destination
    videoStream.download(download_Folder)
    # Displaying the message of sucess
    messagebox.showinfo(
        "SUCCESSFULLY", "DOWNLOADED AND SAVED IN \n" + download_Folder)

# creating main window


root = Tk()
root.geometry("500x110")
root.resizable(0, 0)
root.title("YouTube downloader @StreetGUY32")
root.config(background="#000000")
# creating the Tkinter variables
video_Link = StringVar()
download_Path = StringVar()
# calling Widgets fucntion
Widgets()
root.mainloop()