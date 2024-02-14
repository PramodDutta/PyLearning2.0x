def make_pizza(*topings):
    print(topings)
    for toping in topings:
        print(toping)
    
    
pramod = make_pizza("mushroom","onion","tomato")
santosh = make_pizza("mushroom","pineapple","paneer","tomato")
vinay = make_pizza("mushroom","pineapple","paneer","seetcorn")



def make_pizza_base(*topings,base):
    print(topings,base)
    for toping in topings:
        print(toping)
        
amit = make_pizza_base("mushroom","onion","tomato",base="thin")


# def make_pizza_base(*topings,*base):
