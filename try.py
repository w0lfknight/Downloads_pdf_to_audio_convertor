import tkinter as tk
from tkinter import filedialog
def upload_file():
    file = filedialog.askopenfilename()
    print(f"{file.split('.')[0]}.mp3")
    return file

root = tk.Tk()
root.title("File Uploader")

button = tk.Button(root, text="Upload File", command=upload_file)
button.pack()



root.mainloop()