def makepizza(*toppings, base="Wheat"):
    print(toppings, base)
    for topping in toppings:
        print(topping)
    return toppings, base


swathi_t, swathi_b = makepizza("onion", "tomato", "sweetcorn")
# pramod = makepizza("onion", "tomato", "sweetcorn", base="thin crust")
print(swathi_t)
print(swathi_b)
