import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4', only_video=True).first()
        if video:
            video.download()
            messagebox.showinfo("Success", f"Downloaded: {yt.title}")
        else:
            messagebox.showerror("Error", "No suitable video stream found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Shorts Downloader")

# Create and place the URL entry
url_label = tk.Label(root, text="Enter YouTube Shorts URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Create and place the download button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()