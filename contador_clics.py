import tkinter as tk
from tkinter import messagebox
import threading

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Clics")
        
        self.click_count = 0
        self.time_left = 30
        
        # Etiqueta para mostrar el número de clics
        self.click_label = tk.Label(root, text=f"Clics: {self.click_count}", font=('Helvetica', 16))
        self.click_label.pack(pady=10)
        
        # Etiqueta para mostrar el tiempo restante
        self.time_label = tk.Label(root, text=f"Tiempo restante: {self.time_left} segundos", font=('Helvetica', 16))
        self.time_label.pack(pady=10)
        
        # Botón para hacer clic
        self.click_button = tk.Button(root, text="Hacer clic", font=('Helvetica', 16), command=self.increment_click)
        self.click_button.pack(pady=20)
        
        # Iniciar el temporizador en un hilo separado
        self.timer_thread = threading.Thread(target=self.start_timer)
        self.timer_thread.start()
    
    def increment_click(self):
        self.click_count += 1
        self.click_label.config(text=f"Clics: {self.click_count}")
    
    def start_timer(self):
        while self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Tiempo restante: {self.time_left} segundos")
            self.root.after(1000)
        
        # Al finalizar el tiempo, deshabilitar el botón y mostrar el resultado final
        self.click_button.config(state=tk.DISABLED)
        messagebox.showinfo("Tiempo Finalizado", f"El tiempo ha terminado. Total de clics: {self.click_count}")

# Crear la ventana principal
root = tk.Tk()
app = ClickCounterApp(root)
root.mainloop()
