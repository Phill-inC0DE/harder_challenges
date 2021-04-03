import datetime

#CLASSES
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " Menu avaliable from " + str(self.start_time.isoformat(timespec='minutes')) + " to " + str(self.end_time.isoformat(timespec='minutes'))
  
  def calculate_bill(self, purchased_items):
     bill = 0
     for item in purchased_items:
       if item in self.items:
         bill += self.items[item]
     return bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def avaliable_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return self.name + " Franchises: " + str(self.franchises)

#RESTURANTS & MENUS

#Basta Fazoolin Menus
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50,
}
brunch_menu = Menu("Brunch", brunch_items, datetime.time(11), datetime.time(16))

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
  }
early_bird_menu = Menu("Early Bird", early_bird_items, datetime.time(15), datetime.time(18))

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  }
dinner_menu = Menu("Dinner", dinner_items, datetime.time(17), datetime.time(23))

kids_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  }
kids_menu = Menu("Kids", kids_items, datetime.time(11), datetime.time(21))

all_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

#Arepas Menu
menu_dict = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a’ Arepa', menu_dict, datetime.time(10), datetime.time(20))

#The Bill
bill = early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
#print("Total: £{:.2f}".format(bill))


#FRANCHISES

#First Franchise
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
basta_fazoolin_fran = [flagship_store, new_installment]

#Second Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepas_place_fran = [arepas_place]
#print(new_installment.avaliable_menus(datetime.time(17)))


#BUSINESSES

basta_fazoolin = Business("Basta Fazoolin", basta_fazoolin_fran)
take_a_arepa = Business("Take a' Arepa", arepas_place_fran)

print(basta_fazoolin.franchises[0].menus[0].items)