import tkinter as tk
from tkinter import ttk, messagebox

class restaurantOrderManagement():
    def __init__(self, root):

        self.root = root
        self.root.title("Restaurant Management App")

        self.menuItems = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchangeRate = 82

        self.setupBackground(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Restaurant Order Management", font=("Arial", 20, "bold"))

        self.menuLabels = {}
        self.menuQuantities = {}

        for i, (item, price) in enumerate(self.menuItems.items(), start=1):
            label = ttk.Label(frame, text=f"{item}: (${price}): ", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menuLabels[item] = label
        
            quantityEntry = ttk.Entry(frame, width=5)
            quantityEntry.grid(row=i, column=1, padx=10, pady=5)
            self.menuQuantities[item] = quantityEntry

        self.currency = tk.StringVar()
        ttk.Label(frame, text="Currency: ", font=("Arial", 12)).grid(row=len(self.menuItems) + 1, column=0, padx=10, pady=5)

        currencyDropdown = ttk.Combobox(frame, textvariable=self.currency, state="readonly", width=18, values=("USD", "INR"))
        self.currency.trace("w", self.updateMenuPrices)

        orderButton = ttk.Button(frame, text="Place Order", command=self.placeOrder)
        orderButton.grid(row=len(self.menuItems) + 2, columnspan=3, padx=10, pady=10)

        def setupBackground(self, root):
            bgWidth, bgHeight = 800, 600
            canvas = tk.Canvas(root, width=bgWidth, height=bgHeight)
            canvas.pack()

            originalImage = tk.PhotoImage(file="background.png")
            backgroundImage = originalImage.subsample(originalImage.width() // bgWidth, originalImage.height() // bgHeight)

            canvas.create_image(0, 0, anchor=tk.NW, image=backgroundImage)
            canvas.image = backgroundImage

        def updateMenuPrices(self, *args):
            currency = self.currency.get()
            symbol = "₹" if currency == "INR" else "$"
            rate = self.exchangeRate if currency == "INR" else 1

            for item, label in self.menuLabels.items():
                price = self.menuItems[item] * rate
                label.config(text=f"{item} ({price}{rate}): ")
        
        def placeOrder(self):
            total = 0
            orderSummary = "Order Summary:\n"
            currency = self.currency.get()
            symbol = "₹" if currency == "INR" else "$"
            rate = self.exchangeRate if currency == "INR" else 1

            for item, entry in self.menuQuantites.items():
                quantity = entry.get()
                if quantity.isdigit():
                    quantity = int(quantity)
                    price = self.menuItems[item] * rate
                    cost = quantity * price
                    total += cost

                    if quantity > 0:
                        orderSummary += (

                            f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"

                        )

            if total > 0:

                    orderSummary += f"\nTotal Cost: {symbol}{total}"

                    messagebox.showinfo("Order Placed", orderSummary)

            else:

                messagebox.showerror("Error", "Please order at least one item.")

# Main block to run the app

if __name__ == "__main__":

    root = tk.Tk()

    app = restaurantOrderManagement(root)

    root.geometry("800x600") # Set the size of the window

    root.mainloop()