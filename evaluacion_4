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
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_concepcion:
        return False
    codigo = input("Código de confirmación: ")
    if len(codigo) < 6 or not any(c.isupper() for c in codigo) or not any(c.isdigit() for c in codigo) or ' ' in codigo:
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
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_puente_alto:
        return False
    try:
        cantidad = int(input("Cantidad de entradas (máx 3): "))
        if cantidad < 1 or cantidad > 3:
            return False
    except ValueError:
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
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_muelle_baron:
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
    nombre = input("Nombre del comprador: ")
    if nombre in clientes_muelle_vergara:
        return False
    tipo_entrada = input("Tipo de entrada (Sun=Sunset, Ni=Night): ").lower()
    if tipo_entrada not in ["sun", "ni"]:
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
    while True:
        respuesta = input("¿Quieres volver a comprar? (sí/no): ").lower()
        if respuesta == "sí":
            return True
        elif respuesta == "no":
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
