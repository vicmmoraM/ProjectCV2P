import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def obtener_datos():
    while True:
        entrada = simpledialog.askstring("Ingreso de datos", "Ingrese el valor a: ")
        entrada1 = simpledialog.askstring("Ingreso de datos", "Ingrese el valor de n: ")
        if entrada is None:
            return None
        if entrada1 is None:
            return None

        try:
            radio = float(entrada)
            if radio <= 0:
                raise ValueError("El radio debe ser un número positivo.")
            
            n = int(entrada1)
            if n <= 0:
                raise ValueError("La cantidad de subintervalos no puede ser negativo")   
            return radio,n
        except (ValueError, TypeError) as e:
            messagebox.showerror("Error", f"Entrada no válida. Por favor, ingrese un valor numérico positivo.")

def Longitud_traza(radio, n):
    theta = np.linspace(0, 2 * np.pi, n)
    dtheta = theta[1] - theta[0]

    #Circunferencia Parametrizada
    x = radio * np.cos(theta)
    y = radio * np.sin(theta)
    z = (8 - x - y)/2

    #Derivadas uwu
    dx = -radio * np.sin(theta)
    dy = radio * np.cos(theta)
    dz = - radio * (np.cos(theta) + np.sin(theta)) / 2

    ds = np.sqrt(dx**2 * dy**2 + dz**2)

    lg = np.sum(ds * dtheta)
    return lg, x, y, z

def Graficar(radio,x,y,z,lg):
    figura = plt.figure()
    ejes = figura.add_subplot(111, projection='3d')
    
    
    altura = 150  
    num_puntos = 100
    theta = np.linspace(0, 2 * np.pi, num_puntos)
    z_cilindro = np.linspace(-altura / 2, altura / 2, num_puntos)
    theta, Z_cilindro = np.meshgrid(theta, z_cilindro)
    X_cilindro = radio * np.cos(theta)
    Y_cilindro = radio * np.sin(theta)
    
    ejes.plot_surface(X_cilindro, Y_cilindro, Z_cilindro, alpha=0.6, color='b', rstride=10, cstride=10)
    # Graficar la curva de intersección
    ejes.plot(x, y, z, color='k', lw=2)
    # Graficar el plano
    margen = radio * 1.5  
    x_plano = np.linspace(-margen, margen, 100)
    y_plano = np.linspace(-margen, margen, 100)
    x_plano, y_plano = np.meshgrid(x_plano, y_plano)
    z_plano = (8 - x_plano - y_plano) / 2
    
    ejes.plot_surface(x_plano, y_plano, z_plano, alpha=0.3, color='r', rstride=10, cstride=10)
    
    
    # Configurar los límites y etiquetas
    ejes.set_xlim([-margen, margen])
    ejes.set_ylim([-margen, margen])
    ejes.set_zlim([-altura / 2 - 10, altura / 2 + 10])  # Ajustar el límite para el cilindro más alto
    ejes.set_xlabel('X')
    ejes.set_ylabel('Y')
    ejes.set_zlabel('Z')
    ejes.set_title("nya")
    ejes.set_title(f"La Longitud del arco es: {round(lg,2)}")
    ejes.legend()
    
    # Vista 
    ejes.view_init(elev=20, azim=30)  
    
    plt.show()
