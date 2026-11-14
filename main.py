# ==============================================================================
# MÓDULO: main.py
# Archivo principal de ejecución y pruebas del sistema SHEIN.
# ==============================================================================

# Importamos las clases desde modelos.py (Modularización)
from modelos import ProductoShein, RopaShein, CarritoShein

# --- PRUEBAS DE HERENCIA, ENCAPSULAMIENTO Y POLIMORFISMO (Avance 2) ---
print("--- PRUEBA 1: Objeto de la Clase Base ---")
producto1 = ProductoShein("Funda de Celular", 100, 50)
producto1.describir()
producto1.aplicar_descuento(10)  # Queda en $90
print()

print("--- PRUEBA 2: Primer Objeto de la Subclase ---")
ropa1 = RopaShein("Vestido Rojo", 300, 15, "M", "Rojo")
ropa1.describir()
ropa1.actualizar_stock(20)
print()

print("--- PRUEBA 3: Segundo Objeto de la Subclase ---")
ropa2 = RopaShein("Chamarra de Mezclilla", 600, 8, "L", "Azul")
ropa2.describir()
ropa2.actualizar_stock(-5)  # Prueba de validación
print()

# --- PRUEBA 4: COMPOSICIÓN ("Tiene-un") (Avance 3) ---
print("--- PRUEBA 4: Composición con CarritoShein ---")
mi_carrito = CarritoShein("Melanie")

# Agregamos los objetos creados anteriormente al carrito
mi_carrito.agregar_producto(producto1)
mi_carrito.agregar_producto(ropa1)
mi_carrito.agregar_producto(ropa2)

# Mostramos el resumen delegando los métodos a cada producto
mi_carrito.mostrar_resumen_pedido()