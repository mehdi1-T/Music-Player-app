import tkinter as tk
from tkinter import filedialog

def upload_file():
    file_pack = filedialog.askopenfilename()
    if file_pack:
        print("Selected file:", file_pack)
    else: return 'Error'

root = tk.Tk()
root.title("Upload File")
root.geometry("400x400")

# upload file via a button that call updload file function
uploadButton = tk.Button(root, text="Upload File", command=upload_file)
uploadButton.pack(pady=20)


root.mainloop()