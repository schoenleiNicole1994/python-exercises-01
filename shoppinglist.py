shoppinglist = [Einkaufsliste]
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    shoppinglist.append(item)
    print(f"{item} wurde der Einkaufsliste hinzugefügt.")
    
    def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste:")
        for item in shoppinglist:
            print(f"- {item}")
    else:
        print("Deine Einkaufsliste ist leer.")