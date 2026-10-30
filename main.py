pet_stats = {"name": "Buddy", "hunger": 0, "happiness": 0, "energy": 0 , "level": 1, "experience": 0 , "coin": 0}
inventory = {}

def menu():
    print("Welcome to the Pet Simulator!")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Rest your pet")
    print("4. View pet stats")
    print("5. View your inventory")
    print("6. Visit the Shop")
    print("7. Exit")

def feed_pet():
    if pet_stats["hunger"] < 100:
        if inventory["pet food"] == 0:
            pet_stats["hunger"] = min(100, pet_stats['hunger']+10)
            pet_stats["experience"] += 5
            pet_stats["coin"] += 5
            print(f"{pet_stats['name']}'s hunger level is {pet_stats['hunger']}")
            print("You earned 5 coins!\n")
        else:
            inventory["pet food"] -= 1
            pet_stats["hunger"] = min(100, pet_stats['hunger']+30)
            pet_stats["experience"] += 10
            pet_stats["coin"] += 10
            print("You used a pet food!")
            print(f"{pet_stats['name']}'s hunger level is {pet_stats['hunger']}")
            print("You earned 10 coins!\n")
    else:
        print(f"{pet_stats['name']} is not hungry!\n")

def play_with_pet():
    if pet_stats["happiness"] == 100:
        print(f"{pet_stats['name']} is already very happy!\n")
    elif pet_stats["hunger"] == 0:
         print(f"{pet_stats['name']} is too hungry to play! Feed him!\n")
    elif pet_stats["energy"] == 0:
             print(f"{pet_stats['name']} is too tired to play! Rest him!\n")
    else:
        if inventory["toy ball"] == 0:
            pet_stats["happiness"] = min(100, pet_stats["happiness"]+10)
            pet_stats["hunger"] = max(0, pet_stats["hunger"]-10)
            pet_stats["energy"] = max(0, pet_stats["energy"]-10)
            pet_stats["experience"] += 10
            pet_stats["coin"] += 10
            print(f"{pet_stats['name']}'s happiness level is {pet_stats['happiness']}")
            print("You earned 10 coins!\n")
        else:
            inventory["toy ball"] -= 1
            pet_stats["happiness"] = min(100, pet_stats["happiness"]+30)
            pet_stats["hunger"] = max(0, pet_stats["hunger"]-10)
            pet_stats["energy"] = max(0, pet_stats["energy"]-10)
            pet_stats["experience"] += 20
            pet_stats["coin"] += 15
            print("You used a toy ball!")
            print(f"{pet_stats['name']}'s happiness level is {pet_stats['happiness']}")
            print("You earned 15 coins!\n")

def rest_pet():
    if pet_stats["energy"] < 100:
        if inventory["pet bed"] == 0:
            pet_stats["energy"] = min(100, pet_stats["energy"] + 10)
            pet_stats["experience"] += 5
            pet_stats["coin"] += 5
            print(f"{pet_stats['name']}'s energy level is {pet_stats['energy']}")
            print("You earned 5 coins!\n")
        else:
            pet_stats["energy"] = min(100, pet_stats["energy"] + 20)
            pet_stats["experience"] += 10
            pet_stats["coin"] += 10
            print(f"{pet_stats['name']}'s energy level is {pet_stats['energy']}")
            print("You earned 10 coins!\n")
    
    else:
        print(f"{pet_stats['name']} is already well rested\n")

def view_stats():
    for stats, value in pet_stats.items():
            print(f"{stats.title()}: {value}")
    print(f"Successfully viewed {pet_stats['name']}'s stats\n")

def view_inventory():
    if not inventory:
         print("Your inventory is empty!\n")
    else:
        for item, amount in inventory.items():
            print(f"{item.title()}: {amount}")
        print("Succesfully viewed your inventory!\n")

def shop():
    print("\nWelcome to the Shop!")
    print("1.Pet Food (Consumable: Restore 30 hunger|15 coins)")
    print("2.Toy Ball (Consumable: Restore 30 happiness|15 coins)")
    print("3.Comfy Pet Bed (Permanent upgrade: Restore 20 energy|30 coins)")
    print(f"Your coins: {pet_stats['coin']}")

    shop_input = input("What would you like to buy?(1-3): ")

    if shop_input == "1":
        if pet_stats["coin"] >= 15:
            pet_stats["coin"] -= 15
            print("You bought a pet food for 15 coins!\n")
            inventory["pet food"] = inventory.get("pet food" , 0) + 1
        else:
            print("You don't have enough coins!\n")
    elif shop_input == "2":
            if pet_stats["coin"] >= 15:
                pet_stats["coin"] -= 15
                inventory["toy ball"] = inventory.get("toy ball" , 0) + 1
                print("You bought a toy ball for 15 coins!\n")
            else:
                print("You don't have enough coins!\n")
    elif shop_input == "3":
            if inventory["pet bed"] == 1:
                print("You already bought a bed!\n")
            elif pet_stats["coin"] >= 30:
                pet_stats["coin"] -= 30
                inventory["pet bed"] = inventory.get("pet bed" , 0) + 1
                print("You bought a comfy pet bed for 30 coins!\n")
            else:
                print("You don't have enough coins!\n")
    else:
        print("Invalid option!")

def level_up():
     xp_needed = 50 + (pet_stats["level"]-1) * 15
     if pet_stats["experience"] >= xp_needed:
          pet_stats["level"] += 1
          print (f"{pet_stats['name']} is now level {pet_stats['level']}\n")
          pet_stats["experience"] -= xp_needed

def save_stats():
     with open ("pet_stats.txt" , "w") as file:
        for stats, value in pet_stats.items():
            stats = str(stats)
            value = str(value)
            file.write(stats + ":" + value + "\n")

def load_stats():
    try:
        with open("pet_stats.txt" , "r") as file:
            for line in file :
                parts = line.strip().split(":")
                stat = parts[0]
                value = parts[1]
                if stat == "name":
                    pet_stats[stat] = value
                else:
                    pet_stats[stat] = int(value)
    except FileNotFoundError:
             pass

def save_inventory():
    with open ("inventory.txt" , "w") as file:
        for item, amount in inventory.items():
            amount = str(amount)
            file.write(item + ":" + amount + "\n")

def load_inventory():
    try:
        with open("inventory.txt" , "r") as file:
                for line in file :
                    parts = line.strip().split(":")
                    item = parts[0]
                    amount = parts[1]
                    inventory[item] = int(amount)
    except FileNotFoundError:
         pass

def main():
    load_stats()
    load_inventory()
    while True:
        menu()
        option = input("Enter your option(1-7): ")
        if option == "1":
            feed_pet()
            save_stats()
            save_inventory()
        elif option == "2":
            play_with_pet()
            save_stats()
            save_inventory()
        elif option == "3":
            rest_pet()
            save_stats()
            save_inventory()
        elif option == "4":
            view_stats()
        elif option == "5":
             view_inventory()
        elif option == "6":
             shop()
             save_inventory()
             save_stats()
        elif option == "7":
            print("Thanks for playing!")
            save_stats()
            save_inventory()
            break
        else:
            print("Invalid option!")

        level_up()
        save_stats()

main()