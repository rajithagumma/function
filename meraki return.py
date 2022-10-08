def add_numbers_more(number_x, number_y):
          number_sum = number_x + number_y
          print("Hello from NavGurukul ;)")
          return number_sum
          number_sum = number_x + number_x
          print("Will i reach here?")
          return number_sum
sum6 = add_numbers_more(100, 20)

def menu(day):
          if day == "monday":
                    return "Butter Chicken"
          elif day == "tuesday":
                    return "Mutton Chaap"
          else:
                    return "Chole Bhature"
                    print("Will I be able to print? :-(")

mon_menu = menu("monday")
print(mon_menu)
tues_menu = menu("tuesday")
print(tues_menu)
fri_menu = menu("friday")
print(fri_menu)

