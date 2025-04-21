print("--Welcome to the Pizza deliveries--")
print("Please enter the size of the pizza ")
size = input("small = S, Medium = M, Large = L : ")
pepperoni = input("Do you want to add pepperoni, Yes = Y, No = N : ")
extra_chees = input ("Do you want to add some extra chees, Yes = Y, No = N : ")

#Small pizza = $15
#Medium pizza = $20
#Large pizza = $25
#Added pepporoni = $2
#Added extra chees = $1

pizza = 0 # assign a global variable so that we can use it throughout the programme.

if size == 'S':
    pizza = 15
    print("Your small simple pizza bill is ${}".format(pizza))
    if pepperoni == 'Y':
        pizza = pizza + 2
        print("Your pizza bill with pepperoni is ${}".format(pizza))
    if extra_chees == 'Y':
        pizza = pizza + 1
        print("Your pizza bill with extra chees is ${}".format(pizza))
        if pepperoni == 'Y' and extra_chees == 'Y':
            print("Your pizza bill with Pepperoni + extra chees is ${}".format(pizza))
            
        
if size == 'M':
    pizza = 20
    print("Your small simple pizza bill is ${}".format(pizza))
    if pepperoni == 'Y':
        pizza = pizza + 2
        print("Your pizza bill with pepperoni is ${}".format(pizza))
    if extra_chees == 'Y':
        pizza = pizza + 1
        print("Your pizza bill with extra chees is ${}".format(pizza))
        if pepperoni == 'Y' and extra_chees == 'Y':
            print("Your pizza bill with Pepperoni + extra chees is ${}".format(pizza))
    
if size == 'L':
    pizza = 25
    print("Your small simple pizza bill is ${}".format(pizza))
    if pepperoni == 'Y':
        pizza = pizza + 2
        print("Your pizza bill with pepperoni is ${}".format(pizza))
    if extra_chees == 'Y':
        pizza = pizza + 1
        print("Your pizza bill with extra chees is ${}".format(pizza))
        if pepperoni == 'Y' and extra_chees == 'Y':
            print("Your pizza bill with Pepperoni + extra chees is ${}".format(pizza))
else:
    print("Chose the right size ")

