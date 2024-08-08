import tkinter as tk
from tkinter import messagebox
from plyer import notification

def send_notification():
    title = title_entry.get()
    message = message_entry.get()
    if title and message:
        notification.notify(
            title=title,
            message=message,
            app_name='Notification App',
            timeout=10
        )
        messagebox.showinfo("Notification", "Notification sent!")
    else:
        messagebox.showerror("Error", "Both title and message are required.")

# Create the main window
root = tk.Tk()
root.title("Desktop Notification App")

# Create and place the widgets
tk.Label(root, text="Notification Title:").pack(pady=5)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

tk.Label(root, text="Notification Message:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Button(root, text="Send Notification", command=send_notification).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
