# Crea la clase menu_item con los atributos nombre y precio
class menu_item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

# Crea una subclase beverage que herede de menu_item
class beverage(menu_item):
    def __init__(self, name: str, price: float, type: str, size: str, flavor: str):
        super().__init__(name, price)
        self.type = type
        self.size = size
        self.flavor = flavor
    
    #Todas las bebidas y sus respectivos atributos
    def agua():
        return(beverage(name = "Agua", price = 1500, type = "beverage",
                         size = "250ml", flavor = "Sin gas"))
    def gaseosa_Cocacola():
        return(beverage(name = "Cocacola",price = 2500, type = "beverage",
                         size = "250ml",flavor = "Clasica"))
    def jugo_de_naranja():
        return(beverage(name = "Jugo de Naranja", price = 4000, type = "beverage",
                         size = "350ml", flavor = "Natural"))
    def cerveza():
        return(beverage(name = "Cerveza", price = 3500, type = "beverage",
                         size = "330ml", flavor = "Malta"))
    
# Crea una subclase appetizer que herede de menu_item
class appetizer(menu_item):
    def __init__(self, name: str, price: float, type: str, size: str):
        super().__init__(name, price)
        self.type = type
        self.type = "appetizer"
        self.size = size
    
    #Todas las entradas y sus respectivos atributos
    def nachos():
        return(appetizer(name = "Nachos", price = 9000, type = "appetizer",
                          size = "mediano"))
    def papitas():
        return(appetizer(name = "Papitas", price = 7000, type = "appetizer",
                          size = "grande"))
    def patacones():
        return(appetizer(name = "Patacones", price = 8000, type = "appetizer",
                          size = "grande"))
    def arepas():
        return(appetizer(name = "Arepas", price = 6000, type = "appetizer",
                          size = "mediano"))
    
# Crea una subclase main_course que herede de menu_item
class main_course(menu_item):
    def __init__(self, name: str, price: float, type: str, size: str):
        super().__init__(name, price)
        self.type = type
        self.type = "main_course"
        self.size = size

    #Los platos fuertes y sus respectivos atributos
    def hamburguesa():
        return(main_course(name = "Hamburguesa", price = 17000, type = "main_course",
                            size = "1/4 libra"))
    def pizza():
        return(main_course(name = "Pizza", price = 20000, type = "main_course",
                            size = "grande"))
    def pasta():
        return(main_course(name = "Pasta", price = 15000, type = "main_course",
                            size = "personal"))
    def pollo():
        return(main_course(name = "Pollo", price = 18000, type = "main_course",
                            size = "grande"))

# Crea una subclase dessert que herede de menu_item
class dessert(menu_item):
    def __init__(self, name: str, price: float, type: str, size: str):
        super().__init__(name, price)
        self.type = type
        self.type = "dessert"
        self.size = size

    #Los postres y sus respectivos atributos
    def helado():
        return(dessert(name = "Helado", price = 5000, type = "dessert",
                        size = "personal"))
    def torta():
        return(dessert(name = "Torta", price = 8000, type = "dessert",
                        size = "mediano"))
    def galletas():
        return(dessert(name = "Galletas", price = 3000, type = "dessert",
                        size = "personal"))
    def flan():
        return(dessert(name = "Flan", price = 4000, type = "dessert",
                        size = "personal"))

#Crea la clase order 
class order:
    #Crea una lista vacia para almacenar los items
    def __init__(self, order_number: int, mesa: int = 0):
        self.order_number = order_number
        self.mesa = mesa
        self.items = []

    #Crea los metodos para agregar y eliminar items
    def add_item(self, menu_item):
        self.items.append(menu_item)
    
    def remove_item(self, menu_item):
        self.items.remove(menu_item)

    #Crea el metodo para calcular el descuento
    def descuento(self):
        total = 0
        beverage = 0
        appetizer = 0
        main_course = 0
        dessert = 0

        #Contamos la cantidad de cada tipo de item
        for i in self.items:
            if i.type == "beverage":
                beverage = beverage + 1
            if i.type == "appetizer":
                appetizer = appetizer + 1
            if i.type == "main_course":
                main_course = main_course + 1
            if i.type == "dessert":
                dessert = dessert + 1
        
        #Combo. Por comprar 1 de cada tipo de item, se le da un descuento de 5000
        if beverage >= 1 and appetizer >= 1 and main_course >= 1 and dessert >= 1:
            total = total + 5000
        #Combo Grande. Por comprar 3 de cada tipo de item, se le da un descuento de 20000
        if beverage >= 3 and appetizer >= 3 and main_course >= 3 and dessert >= 3:
            total = total + 20000
        #Combo Bebida. Por comprar 5 bebidas, se le da un descuento de 10000
        if beverage >= 5:
            total = total + 10000
        #Combo Pizza. Por la compra de la primera pizza, se le da un descuento de 10000
        for i in self.items:
            if i.name == "Pizza":
                total = total + 10000

        return total
    
    def calculate_total_bill(self):
        #Calcula el total de la cuenta sumando el precio de cada item y restando el descuento
        total = 0
        descuento = self.descuento()
        for item in self.items:
            total += item.price
        return total - descuento

#Ejemplo de uso
order1 = order(order_number = 1, mesa = 4)
order1.add_item(beverage.agua())
order1.add_item(main_course.pizza())
order1.add_item(appetizer.nachos())

print(order1.items[0].name)
print(order1.calculate_total_bill())