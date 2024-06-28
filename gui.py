import tkinter as tk
from tkinter import ttk
from logic import POSLogic

class POSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Punto de Ventas")
        self.geometry("800x600")
        self.logic = POSLogic()
        
        self.create_widgets()

    def create_widgets(self):
        self.product_label = tk.Label(self, text="Producto:")
        self.product_label.pack(pady=10)
        
        self.product_entry = tk.Entry(self)
        self.product_entry.pack(pady=10)
        
        self.quantity_label = tk.Label(self, text="Cantidad:")
        self.quantity_label.pack(pady=10)
        
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=10)
        
        self.add_button = tk.Button(self, text="Agregar", command=self.add_product)
        self.add_button.pack(pady=10)
        
        self.cart_tree = ttk.Treeview(self, columns=("Producto", "Cantidad"), show="headings")
        self.cart_tree.heading("Producto", text="Producto")
        self.cart_tree.heading("Cantidad", text="Cantidad")
        self.cart_tree.pack(pady=20, fill=tk.BOTH, expand=True)
        
        self.total_label = tk.Label(self, text="Total: $0.00")
        self.total_label.pack(pady=10)

    def add_product(self):
        product = self.product_entry.get()
        quantity = self.quantity_entry.get()
        
        if product and quantity:
            self.logic.add_to_cart(product, int(quantity))
            self.update_cart()
            self.update_total()

    def update_cart(self):
        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)
        
        for product, quantity in self.logic.cart.items():
            self.cart_tree.insert("", tk.END, values=(product, quantity))
    
    def update_total(self):
        total = self.logic.calculate_total()
        self.total_label.config(text=f"Total: ${total:.2f}")
