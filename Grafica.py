import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import simpledialog
import traza
#
#
# @author Victor Morales, José Adrian, Jeycop Navarrete, Andres Saltos :D
#
#
root = tk.Tk()
root.withdraw() #Ocultar la ventana principal
#radio de la circunferencia ---> Un cilindro en 3D
a = simpledialog.askfloat("Ingreso de datos","Ingrese el valor de a: ")
n = simpledialog.askinteger("Ingreso de datos","¿Cuántos sub-intervalos n desea en su sumatoria?: ")
#Cerrar la ventana
root.destroy()

#Validaciones de datos
if a is not None and n is not None:
    valorTraza = traza.trazaConSum(a,n)

    #interfaz :D
    figura = plt.figure(figsize=(16,8))
    ax = figura.add_subplot(111, projection = '3d')

    def GraficarCilindro(a):
        #Coordenas Polares
        theta_ = np.linspace(0, 2*np.pi, 100)
        z_ = np.linspace(-10*a,10*a,100)
        theta, z_cili = np.meshgrid(theta_,z_)
        r = a 

        x_cilindro = r*np.cos(theta)
        y_cilindro = r*np.sin(theta)

        ax.plot_surface(x_cilindro,y_cilindro,z_cili, color = 'm',zorder = 0,alpha = 0.15)

    def GraficarPlano(a):
        def z(x,y):
            return (8-x-y)/2
        x_plano = np.linspace(-10*a/2,10*a/2)
        y_plano = np.linspace(-10*a/2,10*a/2)
        x_plano,y_plano = np.meshgrid(x_plano,y_plano)
        z_plano = z(x_plano,y_plano)
        ax.plot_surface(x_plano,y_plano,z_plano, color = 'g', zorder = 2, alpha = 0.45)
    
    def traza(a):
        t = np.linspace(0,2*np.pi)
        exprx = a*np.cos(t)
        expry = a*np.sin(t)
        exprz = 4 - (1/2)*(exprx + expry)
        ax.plot(exprx,expry,exprz,color = 'black', zorder = 1, label = 'Traza :D')

    GraficarCilindro(a)
    GraficarPlano(a)
    traza(a)
    a_nya = a**2
    ax.text2D(0.05, 0.95, f"El valor de la traza es: {round(valorTraza,4)}", transform=ax.transAxes)
    #Configurar aspecto nya
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"Calculo de Traza $x^2 + y^2 = {a_nya}$ y x+y+2z = 8")
    

    ax.legend()
    plt.show()