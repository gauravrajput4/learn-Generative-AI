class InvalidChaiError(Exception):
    pass

def bill(flavor,cups):
    menu={
        "Masala Chai":20,
        "Ginger Chai":40
    }

    try:
        if flavor not in menu:
            raise InvalidChaiError("That flavor isn't available")
        if not isinstance(cups,int):
            raise TypeError("That cups isn't an integer")
        total=cups*menu[flavor]
        print(f"Your bill for {cups} cups of {flavor}: rupees {total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you for visiting..")

bill("Masala Chai",5)
bill("Mint Chai",5)
bill("Ginger Chai","Two")

