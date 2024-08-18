from cx_Freeze import setup, Executable

# Opcional
build_exe_options = {"packages": [], "excludes": [], "include_files": []}

# Configuración del ejecutable con icono
executables = [
    Executable(
        "Grafica.py",
        base= "Win32GUI",  
        icon="C:\\Users\\ASUS\\OneDrive\\Escritorio\\ProjectCV\\elprimo.ico"
    )
]

setup(
    name="PorjectCV",
    version="0.1",
    description="Calcular la longitud de la traza :D",
    options={"build_exe": build_exe_options},
    executables=executables
)