from tkinter import messagebox
import Grafica
radio, n = Grafica.obtener_datos()
longitud, x, y, z = Grafica.Longitud_traza(radio, n)
messagebox.showinfo("Resultado", f"La longitud de la traza es aproximadamente {round(longitud,3)} cm.")
Grafica.Graficar(radio,x,y,z,longitud)