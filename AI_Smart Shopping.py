import tkinter as tk

def handle_order():
    order_id = order_entry.get()
    try:
        if order_id == '11':
            order_label.config(text="Your order is out for delivery and your delivery pin is 122")
        elif order_id == '12':
            order_label.config(text="Your order might be delayed, sorry for the inconvenience")
        elif order_id == '13':
            order_label.config(text="Your order has already been delivered")
        else:
            order_label.config(text="Invalid order ID")
    except Exception as e:
        order_label.config(text="Error: " + str(e))

def handle_support():
    support_label.config(text="Phone - 12222\nTelephone - 13333\nEmail - Help@chatbot.com")

root = tk.Tk()

# UI elements
greeting_label = tk.Label(root, text="Can I have your name please?")
greeting_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

name_button = tk.Button(root, text="Submit", command=lambda: greeting_label.config(text=name_entry.get() + ", Hi, good afternoon! How may I help you?"))
name_button.pack()

option_label = tk.Label(root, text="Please select an option:")
option_label.pack()

order_button = tk.Button(root, text="Order", command=lambda: handle_order())
order_button.pack()

order_entry = tk.Entry(root)
order_entry.pack()

support_button = tk.Button(root, text="Contact Customer Support", command=lambda: handle_support())
support_button.pack()

order_label = tk.Label(root, text="")
order_label.pack()

support_label = tk.Label(root, text="")
support_label.pack()

root.mainloop()
