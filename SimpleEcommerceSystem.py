import tkinter as tk
from tkinter import messagebox

class ECommerceApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("E-Commerce Platform")

        # Variables
        self.cart = []
        self.products = [
            {"id": 1, "name": "Skincare", "price": 10.00},
            {"id": 2, "name": "Ramen", "price": 20.00},
            # Add more products as needed
        ]

        # User information
        self.user_name = tk.StringVar()
        self.user_phone = tk.StringVar()
        self.user_address = tk.StringVar()

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # User Entry
        user_frame = tk.Frame(self)
        tk.Label(user_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(user_frame, textvariable=self.user_name).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(user_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(user_frame, textvariable=self.user_phone).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(user_frame, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(user_frame, textvariable=self.user_address).grid(row=2, column=1, padx=5, pady=5)
        user_frame.pack(pady=10)

        # Product Listing
        self.product_listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=50)
        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product['name']} - RM {product['price']:.2f}")  # Use RM for Ringgit Malaysia
        self.product_listbox.pack(pady=10)

        # Add to Cart Button
        add_to_cart_button = tk.Button(self, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack()

        # Delete Cart Button
        delete_cart_button = tk.Button(self, text="Delete Cart", command=self.delete_cart)
        delete_cart_button.pack()

        # View Cart Button
        view_cart_button = tk.Button(self, text="View Cart", command=self.view_cart)
        view_cart_button.pack()

    def add_to_cart(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Error", "Please select a product.")
            return

        selected_product = self.products[selected_index[0]]
        self.cart.append(selected_product)
        messagebox.showinfo("Success", f"{selected_product['name']} added to the cart for {self.user_name.get()}.")

    def delete_cart(self):
        self.cart = []
        messagebox.showinfo("Cart Cleared", "Your cart has been cleared.")

    def view_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart Empty", "Your cart is empty.")
            return

        total_price = sum(product["price"] for product in self.cart)
        cart_content = "\n".join([f"{product['name']} - RM {product['price']:.2f}" for product in self.cart])  # Use RM for Ringgit Malaysia

        cart_summary = f"Cart Contents for {self.user_name.get()}:\n{cart_content}\n\nTotal Price: RM {total_price:.2f}"  # Use RM for Ringgit Malaysia
        messagebox.showinfo("View Cart", cart_summary)

if _name_ == "_main_":
    app = ECommerceApp()
    app.mainloop()

