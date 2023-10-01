#Import required Libraries
from tkinter import *
from tkinter import ttk
from pytube import YouTube

# Create Display Window
root = Tk()
root.resizable(0, 0)
root.geometry('500x450')
root.configure(bg='red')
root.title('Youtube Downloader')

# Label which displays text on the GUI
Label(root, text='Youtube Video Downloader\n Enter Link to download video below...', font='arial 15 bold', bg='red', fg='black').pack()

# Background Image to be displayed on created GUI
photo = PhotoImage(file="Youtube.png")
lbl = Label(image=photo).pack()

# Variable to store user entered link
link = StringVar()

# Create an entry field which accepts link from user
enter_link = Entry(root, width=70, textvariable=link).place(x=50, y=100)

qualities = ["High Definition (HD)", "Low Definition (SD)"]
quality_label = Label(root, text="Select Video Quality:", font="arial 12 bold", bg="red", fg="black")
quality_label.place(x=50, y=150)

quality_var = StringVar()
quality_var.set(qualities[0])  # Set the default quality to HD

quality_options = OptionMenu(root, quality_var, *qualities)
quality_options.config(width=18)
quality_options.place(x=230, y=150)


# Function to download the user entered link
def downloader():
    url = YouTube(str(link.get()))
    video_quality = quality_var.get()

    if video_quality == "High Definition (HD)":
        video = url.streams.filter(file_extension="mp4", res="720p").first()
    elif video_quality == "Low Definition (SD)":
        video = url.streams.filter(file_extension="mp4", res="360p").first()

    video.download()
    Label(root, text="Downloaded").place(x=215, y=390)


# Button to start the downloading the video of provided url
Button(root, text='Download Here', command=downloader, fg='white', bg='black').place(x=200, y=360)

# To start the interface and display the properties in it
mainloop()
