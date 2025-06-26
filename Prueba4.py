stock_concepcion = 500
stock_puente_alto = 1300
stock_muelle_baron = 100
stock_muelle_vergara = 50

clientes_concepcion = []
clientes_puente_alto = []
clientes_muelle_baron = []
clientes_muelle_vergara = []

def comprar_concepcion():
    global stock_concepcion
    if stock_concepcion <= 0:
        return False
    print("\n-- Compra en Concepción --")
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_concepcion:
        print("Error: el nombre ya ha sido registrado.")
        return False
    codigo = input("Código de confirmación: ")
    if len(codigo) < 6 or not any(c.isupper() for c in codigo) or not any(c.isdigit() for c in codigo) or ' ' in codigo:
        print("Error: código de confirmación inválido.")
        return False
    clientes_concepcion.append(nombre)
    stock_concepcion -= 1
    print(f"Entrada registrada! Stock restante: {stock_concepcion}")
    print("¡Gracias por tu compra!")
    return True

def comprar_puente_alto():
    global stock_puente_alto
    if stock_puente_alto <= 0:
        return False
    print("\n-- Compra en Puente Alto --")
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_puente_alto:
        print("Error: el nombre ya ha sido registrado.")
        return False
    try:
        cantidad = int(input("Cantidad de entradas (máx 3): "))
        if cantidad < 1 or cantidad > 3:
            print("Error: solo se permiten entre 1 y 3 entradas por persona.")
            return False
    except ValueError:
        print("Error: debes ingresar un número válido.")
        return False
    clientes_puente_alto.append(nombre)
    stock_puente_alto -= cantidad
    print(f"Entradas registradas! Stock restante: {stock_puente_alto}")
    print("¡Gracias por tu compra!")
    return True

def comprar_muelle_baron():
    global stock_muelle_baron
    if stock_muelle_baron <= 0:
        return False
    print("\n-- Compra en Muelle Barón, Valparaíso --")
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_muelle_baron:
        print("Error: el nombre ya ha sido registrado.")
        return False
    tipo_entrada = "G"
    print(f"Tipo de entrada asignado: {tipo_entrada}")
    clientes_muelle_baron.append(nombre)
    stock_muelle_baron -= 1
    print(f"Entrada registrada! Stock restante: {stock_muelle_baron}")
    print("¡Gracias por tu compra!")
    return True

def comprar_muelle_vergara():
    global stock_muelle_vergara
    if stock_muelle_vergara <= 0:
        return False
    print("\n-- Compra en Muelle Vergara, Viña del Mar --")
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_muelle_vergara:
        print("Error: el nombre ya ha sido registrado.")
        return False
    tipo_entrada = input("Tipo de entrada (Sun=Sunset, Ni=Night): ").lower()
    if tipo_entrada not in ["sun", "ni"]:
        print("Error: tipo de entrada inválido.")
        return False
    clientes_muelle_vergara.append(nombre)
    stock_muelle_vergara -= 1
    print(f"Entrada registrada! Stock restante: {stock_muelle_vergara}")
    print("¡Gracias por tu compra!")
    return True

def mostrar_menu():
    print("\nTOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE")
    print("1.- Comprar entrada en Concepción.")
    print("2.- Comprar entrada en Puente Alto.")
    print("3.- Comprar entrada en Muelle Barón, Valparaíso.")
    print("4.- Comprar entrada en Muelle Vergara, Viña del Mar.")
    print("5.- Salir.")

def preguntar_si_o_no():
    respuestas_positivas = ["sí", "si", "SI", "Si", "Sí", "yes", "s"]
    respuestas_negativas = ["no", "NO", "nó", "n"]
    while True:
        respuesta = input("¿Quieres volver a comprar? (sí/no): ").strip().lower()
        if respuesta in [r.lower() for r in respuestas_positivas]:
            return True
        elif respuesta in [r.lower() for r in respuestas_negativas]:
            print("Programa terminado...")
            return False
        else:
            print("Por favor, ingresa una respuesta válida (sí/no).")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if comprar_concepcion():
                if not preguntar_si_o_no():
                    break
        elif opcion == "2":
            if comprar_puente_alto():
                if not preguntar_si_o_no():
                    break
        elif opcion == "3":
            if comprar_muelle_baron():
                if not preguntar_si_o_no():
                    break
        elif opcion == "4":
            if comprar_muelle_vergara():
                if not preguntar_si_o_no():
                    break
        elif opcion == "5":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    main()
