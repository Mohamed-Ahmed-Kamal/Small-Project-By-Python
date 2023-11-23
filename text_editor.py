import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def openFile():
    filePath = askopenfilename(
        filetypes=[("text.file", "*.txt"), ("all.file", "*.*")])
    if not filePath:
        return
    text_edit.delete("1.0", tk.END)
    with open(filePath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)

    window.title = f"text Editor - {filePath}"


def saveAs():
    filePath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("text.file", "*.txt"), ("all.file", "*.*")])
    if not filePath:
        return

    with open(filePath, "w") as output_file:
        text = text_edit.get("1.0", tk.END)
        output_file.write(text)

    window.title = f"text Editor - {filePath}"


# _----------------------------------_
window = tk.Tk()
window.title = ("Mohamed Kamal ")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=850)
text_edit = tk.Text(window)
frame_bottun = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_bottun, text="Open File", command=openFile)
btn_save = tk.Button(frame_bottun, text="Save As", command=saveAs)
btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=0, row=1, sticky="ew", padx=5, pady=5)
frame_bottun.grid(column=0, row=0, sticky="ns")
text_edit.grid(column=1, row=0, sticky="nsew", padx=7)


window.mainloop()
