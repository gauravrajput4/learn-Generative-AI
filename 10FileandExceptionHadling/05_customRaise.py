def brew(flavor):

    if flavor not in ["Masala","Ginger","Elaichi"]:
        raise ValueError("Flavor must be Masala, Ginger, Elaichi")
    print(f"Brewing {flavor} chai....")

brew("Mint")