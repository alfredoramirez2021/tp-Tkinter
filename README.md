Esquema del Sistema de Kiosko

    Archivos principales:
        main.py: El punto de entrada del programa.
        gui.py: Maneja la interfaz gráfica del usuario.
        database.py: Maneja las operaciones de la base de datos.
        kiosk.py: Contiene la lógica principal del kiosko.

    Clases principales:
        KioskApp en main.py
        MainWindow en gui.py
        Database en database.py
        Kiosk en kiosk.py

        Explicación Detallada de Cada Clase y Método
Clase: KioskApp (Archivo: main.py)

    __init__(self): Inicializa la aplicación creando una instancia de MainWindow.
    run(self): Ejecuta el método mainloop de MainWindow para iniciar la aplicación.

Clase: MainWindow (Archivo: gui.py)

    __init__(self): Inicializa la ventana principal, configura el título y el tamaño, crea una instancia
    de Kiosk y llama a setup_ui para configurar la interfaz.
    
    setup_ui(self): Configura los elementos de la interfaz gráfica como etiquetas y botones.
    
    on_buy(self): Método que maneja la compra de un producto llamando a buy_product de Kiosk 
    y muestra un mensaje con el resultado de la compra.
    on_load_stock(self): Método que maneja la carga de stock llamando a load_stock de Kiosk 
    y muestra un mensaje con el resultado de la carga.

Clase: Database (Archivo: database.py)

    __init__(self): Inicializa la base de datos con algunos productos y sus detalles,
    y una lista para registrar transacciones.
    get_product(self, name): Devuelve los detalles del producto si existe.
    update_stock(self, name, quantity): Actualiza el stock del producto restando 
    la cantidad comprada.
    add_stock(self, name, quantity, buy_price): Añade stock a un producto existente
    o lo crea si no existe.
    add_transaction(self, name, quantity, sell_price, date_of_sale, date_of_purchase):
    Registra una transacción incluyendo el producto, cantidad, precio de venta, fecha de venta, 
    fecha de compra y ganancia.

Clase: Kiosk (Archivo: kiosk.py)

    __init__(self): Inicializa la clase con una instancia de Database.
    buy_product(self, name, quantity, sell_price, date_of_sale): Realiza la compra de un producto 
    verificando el stock disponible, actualizándolo en la base de datos y registrando la transacción.
    load_stock(self, name, quantity, buy_price, date_of_purchase): Carga stock de un producto, actualizando
    la base de datos.
