import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The specified folder does not exist!")
        return

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Others': []
    }

    for folder in file_types.keys():
        folder_path_type = os.path.join(folder_path, folder)
        if not os.path.exists(folder_path_type):
            os.makedirs(folder_path_type)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, 'Others'))

    messagebox.showinfo("Success", "Files organized successfully!")

def browse_folder():
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    if folder_path:
        organize_files(folder_path)

# Create the main GUI window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")
root.resizable(False, False)

# Create a label
label = tk.Label(root, text="Organize your files by type", font=("Helvetica", 14))
label.pack(pady=20)

# Create a button to browse for a folder
button = tk.Button(root, text="Select Folder", command=browse_folder, font=("Helvetica", 12))
button.pack(pady=20)

# Start the GUI loop
root.mainloop()
