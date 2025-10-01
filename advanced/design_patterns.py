"""
Title: Advanced Design Patterns in Python
Author: Python-Basics-to-Advanced Contributors
Difficulty: Advanced
Description: Implementation of common design patterns with real-world examples
Date: October 2025
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
import threading
from enum import Enum

print("=== Advanced Design Patterns in Python ===\n")

# =============================================================================
# 1. SINGLETON PATTERN
# =============================================================================

print("--- Singleton Pattern ---")
print("Ensures a class has only one instance and provides global access to it.\n")

class DatabaseConnection:
    """
    Singleton pattern implementation for database connection.
    Ensures only one database connection exists throughout the application.
    """
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.connection_string = "postgresql://localhost:5432/mydb"
            self.is_connected = False
            self._initialized = True
            print(f"Database connection created: {self.connection_string}")
    
    def connect(self):
        if not self.is_connected:
            self.is_connected = True
            print("Connected to database")
        else:
            print("Already connected to database")
    
    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            print("Disconnected from database")
        else:
            print("Not connected to database")
    
    def execute_query(self, query: str):
        if self.is_connected:
            print(f"Executing query: {query}")
            return f"Result of {query}"
        else:
            print("Cannot execute query: Not connected to database")
            return None

# Demonstration
print("Creating database connections...")
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"db1 is db2: {db1 is db2}")  # True - same instance
print(f"ID of db1: {id(db1)}")
print(f"ID of db2: {id(db2)}")

db1.connect()
db2.execute_query("SELECT * FROM users")  # Works because db1 and db2 are the same instance
print()

# =============================================================================
# 2. FACTORY PATTERN
# =============================================================================

print("--- Factory Pattern ---")
print("Creates objects without specifying their exact classes.\n")

class Vehicle(ABC):
    """Abstract base class for vehicles."""
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def get_info(self):
        pass

class Car(Vehicle):
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year
        self.engine_running = False
    
    def start_engine(self):
        self.engine_running = True
        return f"Car {self.model} engine started"
    
    def stop_engine(self):
        self.engine_running = False
        return f"Car {self.model} engine stopped"
    
    def get_info(self):
        return f"{self.year} {self.model} (Car)"

class Motorcycle(Vehicle):
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year
        self.engine_running = False
    
    def start_engine(self):
        self.engine_running = True
        return f"Motorcycle {self.model} engine started with a roar!"
    
    def stop_engine(self):
        self.engine_running = False
        return f"Motorcycle {self.model} engine stopped"
    
    def get_info(self):
        return f"{self.year} {self.model} (Motorcycle)"

class Truck(Vehicle):
    def __init__(self, model: str, year: int, capacity: int):
        self.model = model
        self.year = year
        self.capacity = capacity
        self.engine_running = False
    
    def start_engine(self):
        self.engine_running = True
        return f"Truck {self.model} diesel engine started"
    
    def stop_engine(self):
        self.engine_running = False
        return f"Truck {self.model} engine stopped"
    
    def get_info(self):
        return f"{self.year} {self.model} (Truck, {self.capacity}kg capacity)"

class VehicleType(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"

class VehicleFactory:
    """Factory class to create different types of vehicles."""
    
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType, model: str, year: int, **kwargs) -> Vehicle:
        """Create a vehicle based on the specified type."""
        if vehicle_type == VehicleType.CAR:
            return Car(model, year)
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle(model, year)
        elif vehicle_type == VehicleType.TRUCK:
            capacity = kwargs.get('capacity', 1000)
            return Truck(model, year, capacity)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Demonstration
print("Creating vehicles using Factory Pattern...")
vehicles = [
    VehicleFactory.create_vehicle(VehicleType.CAR, "Toyota Camry", 2023),
    VehicleFactory.create_vehicle(VehicleType.MOTORCYCLE, "Harley Davidson", 2022),
    VehicleFactory.create_vehicle(VehicleType.TRUCK, "Ford F-150", 2023, capacity=2000)
]

for vehicle in vehicles:
    print(f"Created: {vehicle.get_info()}")
    print(f"  {vehicle.start_engine()}")
    print(f"  {vehicle.stop_engine()}")
print()

# =============================================================================
# 3. OBSERVER PATTERN
# =============================================================================

print("--- Observer Pattern ---")
print("Defines a one-to-many dependency between objects.\n")

class Subject(ABC):
    """Abstract subject class."""
    
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class Observer(ABC):
    """Abstract observer class."""
    
    @abstractmethod
    def update(self, subject):
        pass

class WeatherStation(Subject):
    """Concrete subject - Weather Station."""
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0
    
    def attach(self, observer: Observer):
        print(f"Weather Station: Attached observer {observer.__class__.__name__}")
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        print(f"Weather Station: Detached observer {observer.__class__.__name__}")
        self._observers.remove(observer)
    
    def notify(self):
        print("Weather Station: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        print(f"Weather Station: New measurements - Temp: {temperature}°C, "
              f"Humidity: {humidity}%, Pressure: {pressure}hPa")
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()
    
    @property
    def temperature(self):
        return self._temperature
    
    @property
    def humidity(self):
        return self._humidity
    
    @property
    def pressure(self):
        return self._pressure

class CurrentConditionsDisplay(Observer):
    """Display current weather conditions."""
    
    def __init__(self, name: str):
        self.name = name
        self.temperature = 0
        self.humidity = 0
    
    def update(self, subject: WeatherStation):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.display()
    
    def display(self):
        print(f"{self.name} Display: Current conditions - {self.temperature}°C, "
              f"{self.humidity}% humidity")

class StatisticsDisplay(Observer):
    """Display weather statistics."""
    
    def __init__(self):
        self.temperatures = []
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        self.temp_sum = 0
    
    def update(self, subject: WeatherStation):
        temp = subject.temperature
        self.temperatures.append(temp)
        self.temp_sum += temp
        self.max_temp = max(self.max_temp, temp)
        self.min_temp = min(self.min_temp, temp)
        self.display()
    
    def display(self):
        avg_temp = self.temp_sum / len(self.temperatures)
        print(f"Statistics Display: Avg/Max/Min temperature = "
              f"{avg_temp:.1f}/{self.max_temp}/{self.min_temp}°C")

class ForecastDisplay(Observer):
    """Display weather forecast."""
    
    def __init__(self):
        self.current_pressure = 0
        self.last_pressure = 0
    
    def update(self, subject: WeatherStation):
        self.last_pressure = self.current_pressure
        self.current_pressure = subject.pressure
        self.display()
    
    def display(self):
        if self.current_pressure > self.last_pressure:
            forecast = "Improving weather on the way!"
        elif self.current_pressure == self.last_pressure:
            forecast = "More of the same"
        else:
            forecast = "Watch out for cooler, rainy weather"
        
        print(f"Forecast Display: {forecast}")

# Demonstration
print("Creating Weather Station and Observers...")
weather_station = WeatherStation()

current_display = CurrentConditionsDisplay("Mobile App")
statistics_display = StatisticsDisplay()
forecast_display = ForecastDisplay()

# Attach observers
weather_station.attach(current_display)
weather_station.attach(statistics_display)
weather_station.attach(forecast_display)

print("\nSimulating weather updates...")
weather_station.set_measurements(25.0, 65.0, 1013.25)
print()
weather_station.set_measurements(27.0, 70.0, 1015.50)
print()
weather_station.set_measurements(23.0, 75.0, 1010.00)
print()

# Detach an observer
weather_station.detach(statistics_display)
print("After detaching statistics display:")
weather_station.set_measurements(26.0, 68.0, 1012.75)
print()

# =============================================================================
# 4. STRATEGY PATTERN
# =============================================================================

print("--- Strategy Pattern ---")
print("Defines a family of algorithms and makes them interchangeable.\n")

class PaymentStrategy(ABC):
    """Abstract strategy for payment processing."""
    
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.cvv = cvv
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Credit Card ending in {self.card_number}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal account {self.email}"

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str, currency: str):
        self.wallet_address = wallet_address[:8] + "..."  # Truncate for display
        self.currency = currency
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using {self.currency} to wallet {self.wallet_address}"

class ShoppingCart:
    """Context class that uses payment strategies."""
    
    def __init__(self):
        self.items: Dict[str, float] = {}
        self.payment_strategy: PaymentStrategy = None
    
    def add_item(self, item: str, price: float):
        self.items[item] = price
        print(f"Added {item} (${price:.2f}) to cart")
    
    def remove_item(self, item: str):
        if item in self.items:
            price = self.items.pop(item)
            print(f"Removed {item} (${price:.2f}) from cart")
        else:
            print(f"Item {item} not found in cart")
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy
        print(f"Payment method set to {strategy.__class__.__name__}")
    
    def calculate_total(self) -> float:
        return sum(self.items.values())
    
    def checkout(self):
        if not self.payment_strategy:
            return "No payment method selected"
        
        total = self.calculate_total()
        if total == 0:
            return "Cart is empty"
        
        result = self.payment_strategy.pay(total)
        self.items.clear()  # Clear cart after payment
        return result

# Demonstration
print("Creating shopping cart and adding items...")
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)
cart.add_item("Keyboard", 79.99)

print(f"\nTotal: ${cart.calculate_total():.2f}")

# Try different payment strategies
print("\nTesting different payment methods:")

# Credit Card
cart.set_payment_strategy(CreditCardPayment("1234567890123456", "123"))
result = cart.checkout()
print(result)

# Add more items
cart.add_item("Monitor", 299.99)
cart.add_item("Webcam", 89.99)

# PayPal
cart.set_payment_strategy(PayPalPayment("user@example.com"))
result = cart.checkout()
print(result)

# Add more items
cart.add_item("Headphones", 149.99)

# Cryptocurrency
cart.set_payment_strategy(CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "Bitcoin"))
result = cart.checkout()
print(result)
print()

# =============================================================================
# 5. DECORATOR PATTERN
# =============================================================================

print("--- Decorator Pattern ---")
print("Adds new functionality to objects without altering their structure.\n")

class Coffee(ABC):
    """Abstract component for coffee."""
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        pass

class SimpleCoffee(Coffee):
    """Concrete component - basic coffee."""
    
    def get_description(self) -> str:
        return "Simple Coffee"
    
    def get_cost(self) -> float:
        return 2.00

class CoffeeDecorator(Coffee):
    """Base decorator class."""
    
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def get_description(self) -> str:
        return self._coffee.get_description()
    
    def get_cost(self) -> float:
        return self._coffee.get_cost()

class MilkDecorator(CoffeeDecorator):
    """Concrete decorator - adds milk."""
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50

class SugarDecorator(CoffeeDecorator):
    """Concrete decorator - adds sugar."""
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Sugar"
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.25

class WhipCreamDecorator(CoffeeDecorator):
    """Concrete decorator - adds whip cream."""
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Whip Cream"
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75

class ExtraShotDecorator(CoffeeDecorator):
    """Concrete decorator - adds extra espresso shot."""
    
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Extra Shot"
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.00

# Demonstration
print("Building custom coffee orders...")

# Simple coffee
coffee = SimpleCoffee()
print(f"Order 1: {coffee.get_description()} - ${coffee.get_cost():.2f}")

# Coffee with milk
coffee_with_milk = MilkDecorator(SimpleCoffee())
print(f"Order 2: {coffee_with_milk.get_description()} - ${coffee_with_milk.get_cost():.2f}")

# Complex coffee order
complex_coffee = WhipCreamDecorator(
    SugarDecorator(
        MilkDecorator(
            ExtraShotDecorator(
                SimpleCoffee()
            )
        )
    )
)
print(f"Order 3: {complex_coffee.get_description()} - ${complex_coffee.get_cost():.2f}")

# Another complex order
deluxe_coffee = WhipCreamDecorator(
    WhipCreamDecorator(  # Double whip cream
        ExtraShotDecorator(
            ExtraShotDecorator(  # Double shot
                MilkDecorator(
                    SimpleCoffee()
                )
            )
        )
    )
)
print(f"Order 4: {deluxe_coffee.get_description()} - ${deluxe_coffee.get_cost():.2f}")
print()

# =============================================================================
# 6. REAL-WORLD APPLICATION EXAMPLE
# =============================================================================

print("--- Real-World Application: E-commerce System ---")
print("Combining multiple design patterns in a practical scenario.\n")

class Product:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.products: List[Product] = []
        self.total_amount = 0.0
        self.status = "Created"
    
    def add_product(self, product: Product):
        self.products.append(product)
        self.total_amount += product.price
    
    def __str__(self):
        products_str = ", ".join([str(p) for p in self.products])
        return f"Order {self.order_id}: [{products_str}] - Total: ${self.total_amount:.2f}"

class ECommerceSystem:
    """Singleton e-commerce system using observer pattern for notifications."""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.orders: Dict[str, Order] = {}
            self.observers: List[Observer] = []
            self._initialized = True
    
    def attach_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self, order: Order):
        for observer in self.observers:
            observer.update(order)
    
    def create_order(self, order_id: str, products: List[Product], payment_strategy: PaymentStrategy):
        order = Order(order_id)
        for product in products:
            order.add_product(product)
        
        # Process payment
        payment_result = payment_strategy.pay(order.total_amount)
        order.status = "Paid"
        
        self.orders[order_id] = order
        print(f"Order created: {order}")
        print(f"Payment: {payment_result}")
        
        # Notify observers
        self.notify_observers(order)
        
        return order

class EmailNotificationService(Observer):
    def update(self, order: Order):
        print(f"Email Service: Sending confirmation email for order {order.order_id}")

class InventoryService(Observer):
    def update(self, order: Order):
        print(f"Inventory Service: Updating stock for order {order.order_id}")
        for product in order.products:
            print(f"  - Reduced stock for {product.name}")

class ShippingService(Observer):
    def update(self, order: Order):
        print(f"Shipping Service: Preparing shipment for order {order.order_id}")

# Demonstration
print("Setting up e-commerce system...")
ecommerce = ECommerceSystem()

# Attach services (observers)
email_service = EmailNotificationService()
inventory_service = InventoryService()
shipping_service = ShippingService()

ecommerce.attach_observer(email_service)
ecommerce.attach_observer(inventory_service)
ecommerce.attach_observer(shipping_service)

# Create products
products = [
    Product("P001", "Laptop", 999.99),
    Product("P002", "Mouse", 29.99),
    Product("P003", "Keyboard", 79.99)
]

# Create order with payment
payment_method = CreditCardPayment("1234567890123456", "123")
order = ecommerce.create_order("ORD001", products, payment_method)

print(f"\nFinal order status: {order.status}")

print("\n=== End of Design Patterns Tutorial ===")
print("These patterns help create maintainable, flexible, and reusable code!")
print("Each pattern solves specific design problems and improves code quality.")