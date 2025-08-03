import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import csv
import json
from twilio.rest import Client
from tkinter import ttk


# Load Twilio credentials from config.json
def load_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            return config
    except Exception:
        return {
            "TWILIO_ACCOUNT_SID": "",
            "TWILIO_AUTH_TOKEN": "",
            "TWILIO_PHONE_NUMBER": ""
        }

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

config = load_config()
TWILIO_ACCOUNT_SID = config["userConfig"]["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["userConfig"]["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = config["userConfig"]["TWILIO_PHONE_NUMBER"]

def send_messages():
    csv_path = csv_file_var.get()
    message = message_text.get("1.0", tk.END).strip()
    if not csv_path or not message:
        messagebox.showerror("Error", "Please select a CSV file and enter a message.")
        return

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        for idx in range(tree.get_children().__len__()):
            item = tree.get_children()[idx]
            phone_number = tree.item(item, 'values')[1]
            try:
                client.messages.create(
                    body=message,
                    from_=TWILIO_PHONE_NUMBER,
                    to=phone_number
                )
                tree.set(item, column="Status", value="Sent")
            except Exception:
                tree.set(item, column="Status", value="Failed")
        messagebox.showinfo("Success", "Processed all messages.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send messages: {e}")

def browse_csv():
    filename = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    if filename:
        csv_file_var.set(filename)
        # Load CSV and display in table
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                tree.delete(*tree.get_children())
                for idx, row in enumerate(reader):
                    if row:
                        tree.insert("", "end", values=(idx+1, row[0], "Uninitiated"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

root = tk.Tk()
root.title("SandeshX")
# Set window size to 80% of screen and center it
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
root.resizable(True, True)

# Set window icon (favicon)
try:
    icon_img = PhotoImage(file="sandeshx_icon.png")
    root.iconphoto(False, icon_img)
except Exception:
    pass  # If icon not found, ignore

# Branding: Top left icon and app name
branding_frame = tk.Frame(root)
branding_frame.pack(pady=10)
try:
    logo_img = PhotoImage(file="sandeshx_icon.png")
    # Resize image to desired width and height (e.g., 40x40 pixels)
    desired_width, desired_height = 150, 150
    logo_img = logo_img.subsample(
        max(1, logo_img.width() // desired_width),
        max(1, logo_img.height() // desired_height)
    )
    logo_label = tk.Label(branding_frame, image=logo_img)
    logo_label.pack(side=tk.LEFT, padx=5)
except Exception:
    logo_label = tk.Label(branding_frame, text="🟦", font=("Arial", 20))
    logo_label.pack(side=tk.LEFT, padx=5)
# app_name_label = tk.Label(branding_frame, text="SandeshX", font=("Arial", 18, "bold"))
# app_name_label.pack(side=tk.LEFT)

# CSV file selection
csv_file_var = tk.StringVar()
csv_frame = tk.Frame(root)
csv_frame.pack(pady=15)
csv_label = tk.Label(csv_frame, text="CSV File:")
csv_label.pack(side=tk.LEFT)
csv_entry = tk.Entry(csv_frame, textvariable=csv_file_var, width=25)
csv_entry.pack(side=tk.LEFT, padx=5)
csv_button = tk.Button(csv_frame, text="Browse", command=browse_csv)
csv_button.pack(side=tk.LEFT)

# Message textbox
msg_label = tk.Label(root, text="Message:")
msg_label.pack()
message_text = tk.Text(root, height=5, width=40)
message_text.pack(pady=5)

def reset_all():
    csv_file_var.set("")
    message_text.delete("1.0", tk.END)
    tree.delete(*tree.get_children())

def open_settings():
    def save_settings():
        global TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, config
        TWILIO_ACCOUNT_SID = sid_entry.get()
        TWILIO_AUTH_TOKEN = token_entry.get()
        TWILIO_PHONE_NUMBER = phone_entry.get()
        config["userConfig"]["TWILIO_ACCOUNT_SID"] = TWILIO_ACCOUNT_SID
        config["userConfig"]["TWILIO_AUTH_TOKEN"] = TWILIO_AUTH_TOKEN
        config["userConfig"]["TWILIO_PHONE_NUMBER"] = TWILIO_PHONE_NUMBER
        save_config(config)
        settings_win.destroy()

    def reset_to_default():
        default = config.get("defaultConfig", {})
        sid_entry.delete(0, tk.END)
        sid_entry.insert(0, default.get("TWILIO_ACCOUNT_SID", ""))
        token_entry.delete(0, tk.END)
        token_entry.insert(0, default.get("TWILIO_AUTH_TOKEN", ""))
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, default.get("TWILIO_PHONE_NUMBER", ""))

    settings_win = tk.Toplevel(root)
    settings_win.title("Settings")
    settings_win.grab_set()
    settings_win.geometry("600x300")

    tk.Label(settings_win, text="Twilio Account SID:").pack(pady=5)
    sid_entry = tk.Entry(settings_win, width=40)
    sid_entry.pack()
    sid_entry.insert(0, TWILIO_ACCOUNT_SID)

    tk.Label(settings_win, text="Twilio Auth Token:").pack(pady=5)
    token_entry = tk.Entry(settings_win, width=40, show="*")
    token_entry.pack()
    token_entry.insert(0, TWILIO_AUTH_TOKEN)

    tk.Label(settings_win, text="Twilio Phone Number:").pack(pady=5)
    phone_entry = tk.Entry(settings_win, width=40)
    phone_entry.pack()
    phone_entry.insert(0, TWILIO_PHONE_NUMBER)

    btn_frame = tk.Frame(settings_win)
    btn_frame.pack(pady=10)
    save_btn = tk.Button(btn_frame, text="Save", command=save_settings)
    save_btn.pack(side=tk.LEFT, padx=5)
    reset_btn = tk.Button(btn_frame, text="Reset to Default", command=reset_to_default)
    reset_btn.pack(side=tk.LEFT, padx=5)



# Send, Reset, and Settings buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=5)
send_button = tk.Button(button_frame, text="Send", font=("Arial", 12, "bold"), command=send_messages)
send_button.pack(side=tk.LEFT, padx=5)
reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 12, "bold"), command=reset_all)
reset_button.pack(side=tk.LEFT, padx=5)
settings_button = tk.Button(button_frame, text="Settings", font=("Arial", 12, "bold"), command=open_settings)
settings_button.pack(side=tk.LEFT, padx=5)

# Table for CSV contents
table_frame = tk.Frame(root)
table_frame.pack(pady=10)
columns = ("Index", "Phone Number", "Status")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(side=tk.LEFT)


# Add scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Export Results to CSV button
def export_to_csv():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Save Results As"
    )
    if file_path:
        try:
            with open(file_path, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(columns)
                for item in tree.get_children():
                    writer.writerow(tree.item(item, 'values'))
            messagebox.showinfo("Success", f"Results exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")

export_btn = tk.Button(root, text="Export Results to CSV", font=("Arial", 12, "bold"), command=export_to_csv)
export_btn.pack(pady=10)

root.mainloop()