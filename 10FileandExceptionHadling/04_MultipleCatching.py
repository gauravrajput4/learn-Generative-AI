def processOrder(item,quanity):

    try:
        price={"Masala":20}[item]
        cost=price*quanity
        print(f"{item} Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on Menu")
    except TypeError:
        print("Quantity must be an Number")

    finally:
            print("Next customer please..")

processOrder("Ginger",2)
processOrder("Masala","Two")

