import sympy as sp

def trazaConSum(a,n):
    #declaración de variables
    pi = sp.pi.evalf()
    t, i = sp.symbols('t i', integer = True)
    #parametrizar con la curva 0<t<2pi
    x = a * sp.cos(t)
    y = a * sp.sin(t)
    z = 4 - (a/2)*(sp.cos(t) + sp.sin(t))
    #derivadas con respecto a t nya
    dx_dt = sp.diff(x,t)
    dy_dt = sp.diff(y,t)
    dz_dt = sp.diff(z,t)
    #expresion longitud de arco
    expresion = sp.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    delta_t = 2*pi/n
    #definimos variables para la Sumatoria de Riemman
    t_i = i*delta_t
    funcion = expresion.subs(t,t_i)
    #sumatoria
    sumt = sp.Sum(funcion,(i,1,n))
    return (sumt.evalf()*delta_t)