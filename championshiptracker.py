
class Athlete:
    def __init__(self, name, age, sport):
      
        self.name = name
        self.age = age
        self.sport = sport
        self.championships=[]
       

    def addchampionship(self, year, venue, medals):
        
        championship_record = {"year": year, "venue": venue, "medals": medals}
        self.championships.append(championship_record)

    def displaydetails(self):
        
        print(f"\nName: {self.name}, Age: {self.age}, Sport: {self.sport}")
        print("Championship History:")
        for record in self.championships:
            print(f"  Year: {record['year']}, Venue: {record['venue']}, Medals: {record['medals']}")


athletes = []


def addathlete(name, age, sport):
    athlete = Athlete(name, age, sport)
    athletes.append(athlete)
    print(f"Athlete {name} added successfully.")


def displayathletes():
    if not athletes:
        print("No athletes found.")
    else:
        print("Athletes List:")
        for athlete in athletes:
            print(f"- {athlete.name}")

def displayathlete(name):
    for athlete in athletes:
        if athlete.name.lower() == name.lower():
            athlete.displaydetails()
            return
    print("Athlete not found.")

def editathlete(name, new_details):
    for athlete in athletes:
        if athlete.name.lower() == name.lower():
            athlete.age = new_details.get("age", athlete.age)
            athlete.sport = new_details.get("sport", athlete.sport)
            print(f"Athlete {name}'s details updated successfully.")
            return
    print("Athlete not found.")

def deleteathlete(name):
    global athletes
    athletes = [athlete for athlete in athletes if athlete.name.lower() != name.lower()]
    print(f"Athlete {name} deleted successfully.")


def main():
    while True:
        print("\nChampionship History Tracker")
        print("1. Add Athlete")
        print("2. Display All Athletes")
        print("3. Display Athlete Details")
        print("4. Edit Athlete")
        print("5. Delete Athlete")
        print("6. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter athlete's name: ")
            age = input("Enter athlete's age: ")
            sport = input("Enter athlete's sport: ")
            addathlete(name, age, sport)

        elif choice == "2":
            displayathletes()

        elif choice == "3":
            name = input("Enter athlete's name to display details: ")
            displayathlete(name)

        elif choice == "4":
            name = input("Enter athlete's name to edit: ")
            new_age = input("Enter new age (leave blank to keep current): ")
            new_sport = input("Enter new sport (leave blank to keep current): ")
            new_details = {}
            if new_age:
                new_details["age"] = new_age
            if new_sport:
                new_details["sport"] = new_sport
            editathlete(name, new_details)

        elif choice == "5":
            name = input("Enter athlete's name to delete: ")
            deleteathlete(name)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()