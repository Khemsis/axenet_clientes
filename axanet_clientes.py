import os
import datetime

# Directorio donde se guardarán los archivos de clientes
DIRECTORIO_CLIENTES = "axanet_clientes_python"

# Aseguramos que el directorio exista
if not os.path.exists(DIRECTORIO_CLIENTES):
    os.makedirs(DIRECTORIO_CLIENTES)

# Diccionario para asociar clientes con sus archivos
clientes = {}

# Cargar clientes existentes al iniciar
def cargar_clientes():
    for archivo in os.listdir(DIRECTORIO_CLIENTES):
        if archivo.endswith(".txt"):
            nombre = archivo.replace(".txt", "")
            clientes[nombre] = os.path.join(DIRECTORIO_CLIENTES, archivo)

def generar_id(nombre):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    iniciales = "".join([parte[0].upper() for parte in nombre.split()])
    return f"{iniciales}_{timestamp}"

def crear_cliente():
    nombre = input("Nombre completo del cliente: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    servicio = input("Descripción del primer servicio: ").strip()
    fecha = datetime.date.today().isoformat()
    id_cliente = generar_id(nombre)
    archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombre.replace(' ', '_')}.txt")

    with open(archivo, "w", encoding="utf-8") as f:
        f.write(f"Nombre: {nombre}\n")
        f.write(f"ID_Cliente: {id_cliente}\n")
        f.write(f"Telefono: {telefono}\n")
        f.write(f"Correo: {correo}\n")
        f.write(f"FechaRegistro: {fecha}\n")
        f.write("Servicios:\n")
        f.write(f"- {servicio} ({fecha})\n")

    clientes[nombre] = archivo
    print(f"Cliente {nombre} creado exitosamente.\n")

def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    print("Clientes registrados:")
    for nombre in clientes:
        print(f"- {nombre}")
    print()

def ver_cliente():
    nombre = input("Ingrese el nombre del cliente: ").strip()
    archivo = clientes.get(nombre)
    if archivo and os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            print("\nInformación del cliente:")
            print(f.read())
    else:
        print("Cliente no encontrado.\n")

def agregar_servicio():
    nombre = input("Nombre del cliente: ").strip()
    archivo = clientes.get(nombre)
    if archivo and os.path.exists(archivo):
        servicio = input("Descripción del nuevo servicio: ").strip()
        fecha = datetime.date.today().isoformat()
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"- {servicio} ({fecha})\n")
        print("Servicio agregado correctamente.\n")
    else:
        print("Cliente no encontrado.\n")

def eliminar_cliente():
    nombre = input("Nombre del cliente a eliminar: ").strip()
    archivo = clientes.get(nombre)
    if archivo and os.path.exists(archivo):
        confirm = input(f"¿Seguro que desea eliminar a {nombre}? (s/n): ").lower()
        if confirm == "s":
            os.remove(archivo)
            del clientes[nombre]
            print("Cliente eliminado correctamente.\n")
    else:
        print("Cliente no encontrado.\n")

def menu():
    cargar_clientes()
    while True:
        print("=== SISTEMA DE GESTIÓN DE CLIENTES AXANET ===")
        print("1. Crear nuevo cliente")
        print("2. Ver información de cliente")
        print("3. Listar todos los clientes")
        print("4. Agregar servicio a cliente existente")
        print("5. Eliminar cliente")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            ver_cliente()
        elif opcion == "3":
            listar_clientes()
        elif opcion == "4":
            agregar_servicio()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
