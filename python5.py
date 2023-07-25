"welcome to pizzeria bella napoli"

print("vegetarian")
print("no vegetarian")
tipe =input("insert the tipe")
if tipe == "vegetarian":
    print("pimiento")
    print("tofu")
    ingredients = input("select your ingredients")
    if ingredients == "pimiento":
        print("pimiento")

    elif ingredients == "tofu":
        print("tofu")
elif tipe == "no vegetarian":
    print("pepperoni")
    print("jamon")
    print("salmon")
    ingredients = input("select your ingredients")
    if ingredients == "pepperoni":
        print("pepperoni")
    elif ingredients == "jamon":
        print("jamon")
    elif ingredients == "salmon":
        print("salmon")

else:
    print("choise an ingredients!")




