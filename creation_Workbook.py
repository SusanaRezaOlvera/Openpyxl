import openpyxl

def crearInventario():
    papeleria=openpyxl.Workbook()
    hoja=papeleria.active

    #A
    hoja["A1"]="Productos"
    hoja["A2"]="Libretas"
    hoja["A3"]="Colores"
    hoja["A4"]="Resistol"
    hoja["A5"]="Plumones"

    #B
    hoja["B1"]="Stock"

    for i in range(2,6):
        celda="B"+str(i)
        hoja[celda]=20

    #C
    hoja["C1"]="Precios"
    hoja["C2"]=35.00
    hoja["C3"]=15.00
    hoja["C4"]=10.50
    hoja["C5"]=20.0

    #D
    nuevoProducto=["Calculadora Casio",20,200.0]
    hoja.append(nuevoProducto)
    hoja.title="La Pape"


    #E
    hoja.delete_rows(4)
    papeleria.save("papeleria.xlsx")


#Menu
opc=0
while opc !=2:
    print("Menu de la pape")
    print("1-Inicializar inventario")
    print("2-Salir")

    opc=int(input("Ingresar opcion:"))

    if opc == 1:
        crearInventario()
    if opc == 2:
        print("Saliendo del programa...")



    


