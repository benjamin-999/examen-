#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],}
#stock = {modelo: [precio, stock],]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

def stock_marca(tipo):
    total = 0;
    for codigo, dato in productos.items():
        if(dato[1].lower()==tipo.lower()):
            total += inventario[codigo][1];
        print(f"el stock total para {tipo} es: {total}");
#funcion para busqueda por precio 
def buscar_por_precio(precio_min,precio_max):
    resultados = [];
    for codigo, datos in productos.items():
        precio = datos[4];
        if(precio>=precio_min and precio <=precio_max)and(inventario[codigo][1]>0):
            resultados.append(codigo+ "--"+datos[2]);
        if resultados:
        resultados.sort();
        print("el producto encontrado:" resultados):
    else:
        print("no hay productos en ese rango de precio.");
#funcion para listado de productos 
def listado_de_productos(codigo,nuevo_stock):
    if(codigo in inventario):
        inventario[codigo][1] = nuevo_stock;
        return True;
    return False;
#programa principal 
def main():
    while True:
    print("n7-----MENU PRINCIPAL");
    print("1) stock marca");
    print("2) busqueda por precio");
    print("3) listado de productos");
    print("4) salir");
    opc = int(input("ingrese una opcion:"));

    if(opc == 1):
        marca = input("ingrese el tipo de marca");
        stock_marca(marca);
    elif(opc == 2):
        try:
            precio_min = float(input("ingrese el precio minimo "));
            precio_max = float(input("ingrese el precio maximo"));
            buscar_por_precio(precio_min,precio_max);
        except ValueError:
            print("debes ingresar numeros validos!!");
    elif(opc == 3):
        while True:
            codigo = input("ingrese listado del producto");
            try:
                nuevo_stock = int(input("ingrese el nuevo stock"));
                if actualizar_stock(codigo, nuevo_stock):
                    print("stock atualizado");
                else:
                    print("el codigo no existe!");
            except ValueError:
                print("debe ingresar un numero entero para el stock");
    elif(opc == 4):
        print("programa finalizado");
        break;
    else:
        print("debes ingresar una opcion valida")

        


        
        