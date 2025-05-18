
## Reto 3
1. Create a repo with the class exercise
2. **Restaurant scenario:** You want to design a program to calculate the bill for a customer's order in a restaurant.
- Define a base class *MenuItem*: This class should have attributes like name, price, and a method to calculate the total price.
- Create subclasses for different types of menu items: Inherit from *MenuItem* and define properties specific to each type (e.g., Beverage, Appetizer, MainCourse). 
- Define an Order class: This class should have a list of *MenuItem* objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.

Create a class diagram with all classes and their relationships. 
The menu should have at least 10 items.
The code should follow PEP8 rules.


```mermaid
---
config:
  look: classic
  theme: dark
---
classDiagram
direction TB
    class Menu_item {
	    +str name
	    +int price
	    +calculate_total_price()
    }
    class appetizer {
	    +str type
	    +str size
	    anchos()
	    papitas()
	    patacones()
	    arepas()
    }
    class main_course {
	    +str type
	    +str size
	    hamburguesa()
	    pizza()
	    pasta()
	    pollo()
    }
    class beverage {
	    +str type
	    +str size
	    +str flavor
	    agua()
	    cocacola()
	    jugo_de_naranja()
	    cerveza()
    }
    class dessert {
	    +str type
	    +str size
	    +str flavor
	    helado()
	    torta()
	    galletas()
	    flan()
    }
    class order {
	    +int order_number
	    +int mesa
	    add_item()
	    remove_item()
	    descuesto()
	    calculate_total_bill()
    }

    Menu_item --* beverage
    Menu_item --* appetizer
    Menu_item --* main_course
    Menu_item --* dessert
    order <|-- Menu_item
```
