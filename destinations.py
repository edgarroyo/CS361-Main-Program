from storage import load_destinations, save_destinations

def add_destination():
    print("Add Destination\n")
    destination_name = input("Enter the name of the destination: ").strip()

    if not destination_name:
        print("Destination cannot be empty.")

    destinations = load_destinations()
    
    lower_existing = [d.lower() for d in destinations]
    if destination_name.lower() in lower_existing:
        print(f"\n'{destination_name}' is already in your destination list. Duplicate not added.")
        return

    destinations.append(destination_name)
    save_destinations(destinations)
    print(f"Added destination: {destination_name}")

def list_destinations():

    destinations = load_destinations()
    if not destinations:
        print("No destinations in your itinerary")
        return
    
    print("\nYour Itinerary:")
    
    for i, dest in enumerate(destinations, start=1):
        print(f"{i}. {dest}")

def remove_destination():
    print("Remove Destination\n")

    destinations = load_destinations()
    if not destinations:
        print("No destinations to remove.")
        return

    list_destinations()
    choice = input("\nEnter the number to remove (or just press Enter to cancel): ").strip()

    # INPUT CHECK
    if not choice:
        print("\nRemoval canceled.")
        return

    if not choice.isdigit():
        print("\nInvalid input.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(destinations):
        print("\nInvalid destination number.")
        return

    confirm = input(f"\nType 'YES' to confirm removal of {destinations[index]}: ").strip().lower()
    if confirm != "yes":
        print("Removal canceled.")
        return

    removed = destinations.pop(index)
    save_destinations(destinations)
    print(f"\nDestination removed successfully. \nRemoved destination: {removed}")