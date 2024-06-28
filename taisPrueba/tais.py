import csv
import subprocess

lista_pedidos=[]
Windows = 0

def validar_entrada(mensaje,condicion):
    while True:
        entrada = input(mensaje)
        if condicion(entrada):
            return entrada
        print("entrada no valida")

def mostrar_menu():
    print(
    """
        PRODUCTOS
producto:       cantidad:     valor:
1.Abono             50        1200
2.Tierra            35        1000
3.Lirio             40        1100
4.Rosas Rojas       43        1700
5.Margaritas        10        1100
0.SALIR
          """)
    
def gestionar_pedido():
    cliente={}
    productos = []
    total_venta = 0

    print("ingrese datos del cliente")
    cliente ['nombre'] = validar_entrada ("nombre",lambda x: x.isalpha())
    cliente ['telefono'] = validar_entrada ("telefono(debe contener 9 dijitos)",lambda x: x.isdigit() and len(x)==9)
    cliente ['direccion'] = input("direccion: ")
    
    while True:
        mostrar_menu()
        producto = validar_entrada("ingrese el numero del producto('m' para meno, '0' para salir: ",lambda x: x.isdigit() or x.lower() in ['m','0'])

        if producto == '0':
            break
        if producto.lower() == 'm':
            continue

        producto = int(producto)
        if producto <1 or producto >5:
            print("peoducto no disponible. intente nuevamente :p")
            continue

        unidades = validar_entrada("unidades: ",lambda x: x.isdigit() and int(x)>0)
        valor = producto * 1000
        total_venta += valor*int(unidades)


        productos.append(f"producto{producto} - cantidad:{unidades}")
        cliente['productos'] = productos
        cliente['total'] = f"${total_venta}"
        lista_pedidos.append(cliente)
        print("pedido registrado correctamente")

    guardar_en_csv()

    abrir_data_csv()

def abrir_data_csv():
    try:
        subprocess.run(['xdg-open','data.csv'])
    except FileNotFoundError:
        try:
            subprocess.run(['open','data.csv'])
        except FileNotFoundError:
            subprocess.run(['start','data.csv'],shell=True)
Windows
    
def listar_pedido():
    if not lista_pedidos:
        print("no hay pedidos registrados")
        return
    
    print("\nLISTA DE PEDIDOS   ")
    for idx, pedido in enumerate(lista_pedidos,1):
        print(f"pedido{idx}")
        print(f"nombre: {pedido['nombre']}")
        print(f"telefono: {pedido['telefono']}")
        print(f"direccion: {pedido['direccion']}")
        print("productos")
        print(f"--------------")
        
        for prod in pedido['productos']:
            print(f" - {prod}")
        print(f"total a pagar: {pedido['total']}\n")


def generar_factura():
    listar_pedido()

    if not lista_pedidos:
        print("no hay pedidos registrados para generar facturas")
        return
    
    num_pedido = validar_entrada("ingrese el numero del pedido para generar la factura('0'= cancelar): ",lambda x: x.isdigit() and 0 <= int(x) <= len(lista_pedidos))
    if num_pedido == '0':
        return
    
    pedido_seleccionado = lista_pedidos[int(num_pedido) -1]

    print("---------------------------")
    print("---------FACTURA-----------")
    print("---------------------------")
    print("detalles del pedido: ")
    print(f"nombre: {pedido_seleccionado['nombre']}")
    print(f"telefono: {pedido_seleccionado['telefono']}")
    print(f"direccion: {pedido_seleccionado['direccion']}")
    print("productos: ")

    for prod in pedido_seleccionado['prodcutos']:
        print(f" - {prod}")
    print(f"total a pagar: {pedido_seleccionado['total']}")
    print("")

def guardar_en_csv():
    if lista_pedidos:
        with open ('data.csv','w',newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['nombre','telefono','direccion','producto','total'])
            for pedido in lista_pedidos:
                escritor_csv.writerow([pedido['nombre'],pedido['telefono'],pedido['direccion'],";".join(pedido['productos']),pedido['total']])
        print("datos guardados correctamente en data.csv")

while True:

    print(
"""
===================
sistema de pedidos
===================
1.registrar pedido
2.listar productos
3.generar factura
4.salir
""")
                    
    opcion = validar_entrada("ingrese su opcion: ", lambda x: x.isdigit() and 1 <= int(x)<= 4)
    if opcion == '1':
        gestionar_pedido()
    elif opcion == '2':
        listar_pedido()
    elif opcion == '3':
        generar_factura()
    elif opcion == '4':
        print("saliendo del programa.....")
    break

print("programa finalizado")
                





