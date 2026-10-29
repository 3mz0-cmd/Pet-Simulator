pet_stats = {"name": "Buddy", "hunger": 0, "happiness": 0, "energy": 0 , "level": 1, "experience": 0}

def menu():
    print("Welcome to the Pet Simulator!")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Rest your pet")
    print("4. View pet stats")
    print("5. Exit")

def feed_pet():
    if pet_stats["hunger"] < 100:
        pet_stats["hunger"] = min(100, pet_stats['hunger']+10)
        pet_stats["experience"] += 5
        print(f"{pet_stats['name']}'s hunger level is {pet_stats['hunger']}\n")
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
        pet_stats["happiness"] = min(100, pet_stats["happiness"]+10)
        pet_stats["hunger"] = max(0, pet_stats["hunger"]-10)
        pet_stats["energy"] = max(0, pet_stats["energy"]-10)
        pet_stats["experience"] += 10
        print(f"{pet_stats['name']}'s happiness level is {pet_stats['happiness']}\n")


def rest_pet():
    if pet_stats["energy"] < 100:
            pet_stats["energy"] = min(100, pet_stats["energy"] + 10)
            pet_stats["experience"] += 5
            print(f"{pet_stats['name']}'s energy level is {pet_stats['energy']}\n")
    else:
        print(f"{pet_stats['name']} is already well rested\n")

def view_stats():
    for stats, value in pet_stats.items():
            print(f"{stats.title()}: {value}")
    print(f"Successfully viewed {pet_stats['name']}'s stats\n")

def level_up():
     if pet_stats["experience"] >= 50:
          pet_stats["level"] += 1
          print (f"{pet_stats['name']} is now level {pet_stats['level']}")
          pet_stats["experience"] -= 50

def save_stats():
     with open ("pet_stats.txt" , "w") as file:
        for stats, value in pet_stats.items():
            stats = str(stats)
            value = str(value)
            file.write(stats + ":" + value + "\n")

def load_stats():
     with open("pet_stats.txt" , "r") as file:
        for line in file :
            parts = line.strip().split(":")
            stat = parts[0]
            value = parts[1]
            if stat == "name":
                pet_stats[stat] = value
            else:
                 pet_stats[stat] = int(value)

def main():
    load_stats()
    while True:
        menu()
        option = input("Enter your option(1-5): ")
        if option == "1":
            feed_pet()
            save_stats()
        elif option == "2":
            play_with_pet()
            save_stats()
        elif option == "3":
            rest_pet()
            save_stats()
        elif option == "4":
            view_stats()
            save_stats()
        elif option == "5":
            print("Thanks for playing!")
            save_stats()
            break

        level_up()
        save_stats()

main()