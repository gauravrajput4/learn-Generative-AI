chaiMenu={
    "Masala":30,
    "Ginger":40
}
try:
    chaiMenu["elaichi"]
except KeyError:
    print("The key that you are trying to access is 'elaichi' is not exist")

