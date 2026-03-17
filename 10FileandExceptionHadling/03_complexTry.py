def serveChai(flavor):

    try:
        print(f"Preparing {flavor} chai....")
        if flavor == "unkonwn":
            raise ValueError("We dont know that flavor")
    except ValueError as e:
        print("Error: ",e)
    else:
        print(f"{flavor} chai served")
    finally:
        print("Next customer please..")

serveChai("Masala Chai")
serveChai("unknown")