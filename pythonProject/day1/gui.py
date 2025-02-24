import tkinter as tk
import requests

def change_text():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            random_quote = data[0]["q"]
            label.config(text=random_quote)
        else:
            label.config(text=("Could not fatch quote, Try again"))
    except requests.exceptions.RequestException:
        label.config(text=("No internet connection!"))

root = tk.Tk()
root.title("Lets make your day with great qutos")
root.geometry("500x400")
root.configure(bg="#2c3e50")

label = tk.Label(root, text="Click the button for your quto", font=("Arial",16), wraplength=350,bg="#ecf0f1", fg="#2c3e50", padx=20, pady=20, relief="ridge", borderwidth=5)
label.pack(pady=20)

    
button = tk.Button(root, text="Get a quto!", command=change_text, font=("Arial,14"), bg="blue", fg="white",  padx=10, pady=5, relief="raised", borderwidth=3)
button.pack()

root.mainloop()