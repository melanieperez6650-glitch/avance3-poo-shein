# ==============================================================================
# MÓDULO: modelos.py
# Contiene la Clase Base, Subclase y la Clase Auxiliar para Composición.
# ==============================================================================

# --- 1. CLASE BASE ---
class ProductoShein:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        # Encapsulamiento: atributo protegido
        self._stock = stock

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        print(f"Descuento aplicado a {self.nombre}. Nuevo precio: ${self.precio}")

    def describir(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self._stock} piezas")


# --- 2. SUBCLASE (Herencia y Polimorfismo) ---
class RopaShein(ProductoShein):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def actualizar_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self._stock = nuevo_stock
            print(f"El nuevo stock de '{self.nombre}' es: {self._stock}")
        else:
            print("Error: No puedes poner un stock negativo.")

    # Sobrescritura de método (Polimorfismo)
    def describir(self):
        print(f"Ropa: {self.nombre} | Talla: {self.talla} | Color: {self.color} | Precio: ${self.precio} | Stock: {self._stock}")


# --- 3. CLASE AUXILIAR PARA COMPOSICIÓN ("Tiene-un") ---
class CarritoShein:
    def __init__(self, usuario):
        self.usuario = usuario
        # COMPOSICIÓN: Un CarritoShein "tiene" una lista de objetos ProductoShein / RopaShein
        self.productos = []

    def agregar_producto(self, producto):
        # Verificamos el atributo protegido _stock antes de agregarlo
        if producto._stock > 0:
            self.productos.append(producto)
            print(f"-> '{producto.nombre}' agregado al carrito de {self.usuario}.")
        else:
            print(f"-> No hay stock disponible para '{producto.nombre}'.")

    def mostrar_resumen_pedido(self):
        print("\n=======================================================")
        print(f"RESUMEN DEL CARRITO SHEIN - Usuario: {self.usuario}")
        print("=======================================================")
        total = 0
        for item in self.productos:
            # DELEGACIÓN + POLIMORFISMO: El carrito invoca el método describir() de cada objeto guardado
            item.describir()
            total += item.precio
        print("-------------------------------------------------------")
        print(f"TOTAL A PAGAR: ${total:.2f}")
        print("=======================================================\n")