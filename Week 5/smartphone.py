# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage   # in GB
        self.battery = battery   # in mAh

    def phone_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

    def charge(self):
        return f"{self.model} is charging 🔋"

    def take_photo(self):
        return f"{self.model} takes a photo 📸"


# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Polymorphism: override take_photo
    def take_photo(self):
        return f"{self.model} takes a gaming-optimized high-resolution photo 🎮📸"

    def activate_game_mode(self):
        return f"{self.model} activates Game Mode with {self.cooling_system} cooling ❄️"


# Another Child Class (for encapsulation demo)
class BusinessPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, secure_folder=True):
        super().__init__(brand, model, storage, battery)
        self.__secure_folder = secure_folder  # private attribute (encapsulation)

    def access_secure_folder(self):
        if self.__secure_folder:
            return f"{self.model}: Secure Folder accessed 🔒"
        else:
            return f"{self.model}: Secure Folder not available"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 3700)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, 6000, "Liquid Cooling")
phone3 = BusinessPhone("Apple", "iPhone 14 Pro", 256, 3200)

# Test methods
print(phone1.phone_info())
print(phone1.take_photo())
print(phone2.phone_info())
print(phone2.take_photo())   # overridden method
print(phone2.activate_game_mode())
print(phone3.phone_info())
print(phone3.access_secure_folder())
