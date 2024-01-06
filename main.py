import pyttsx3
import pdfplumber
import PyPDF2
import tkinter as tk
from tkinter import filedialog


def upload_file():
    file = filedialog.askopenfilename()
    file = file
    f = open(file, "rb")
    pdfR = PyPDF2.PdfReader(f)
    pages = len(pdfR.pages)


    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            print(text)

            s = pyttsx3.init()
            s.save_to_file(text, f'{file.split(".")[0]}.mp3')
            s.runAndWait()

    f.close()

    print(f'{file.split(".")[0]}.mp3')

root = tk.Tk()
root.title("File Uploader")

button = tk.Button(root, text="Upload File", command=upload_file)
button.pack()




root.mainloop()



