# Create the class that defines the attribues each Menu will have.
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return self.name
# Defines a method to help with calculating the bills for a list of purchases items
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total

# Creates a class that defines the attributes each Franchise will have. This will inherit the Menu objects passed in to display the available menues depending on the time of day.
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# Creates a class that is just used to fully complete a Business, inheriting franchises that are specified for each object.
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Defining the menu items
brunch_menu = {
  'pancake': 7.50, 'waffles': 9.00, 'burger':11.0, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }
early_bird_menu = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
  }
dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
  }
kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  }
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# Passing the menu items into the Menu class to create objects for each menu.
brunch = Menu("brunch", brunch_menu, 1100, 1600)
early_bird = Menu("Early Bird", early_bird_menu, 1500, 1800)
dinner = Menu("Dinner", dinner_menu, 1700, 2300)
kids = Menu("Kids", kids_menu, 1100, 2000)

# Calculates the bill for items that were eaten, as long as those items are on the same menu.
order = brunch.calculate_bill(['pancake', 'home fries', 'coffee'])
print(order)
order2 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(order2)

# Puts all the menus into one combined menu list for easy referencing in the upcoming Franchises. 
all_menus = [brunch, early_bird, dinner, kids]

# Creates 3 franchises
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

# Lists the available menus at the flagship store.
flagship_store_available_menus = flagship_store.available_menus(1700)
print(flagship_store_available_menus)

# Defines 2 businesses using previously used franchises.
arepas_business = Business("Take a\' Arepa", arepas_place)
basta_fazoolin = Business("Basta Fazoolin\' with my Heart", [flagship_store, new_installment])
