### Challenge: How many drinks do you need to buy to throw a great party?
# you will have a list of your friends, and their favorite drink.
# you will also know how many drinks of a certain type are drunk per hour per person. 

#list of your friends and their favorite drink
favorite_drinks = {'Adam':'Gin and Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
                    'Michael':'White Wine','Ariana':'Gin and Tonic','Thomas':'beer','Eduardo':'White Wine',
                    'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water'}

#types of drinks people drink, with lists of examples
cocktails = ['Gin and Tonic', 'Mate Vodka', 'Rum and Coke']
wines = ['Red Wine', 'White Wine']
liquors = ['whiskey', 'gin', 'vokda']
nonalcoholic = ['tea', 'water', 'orange juice']

# number of drinks per hour people drink, depeneding on the type.
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3,'wines':2,'liquors':2,'nonalcoholic':3}

party_duration_hours = int(input("How many hours you think you'll paaartaaay: "))

cocktailsToBuy = 0
winesToBuy = 0
liquorsToBuy = 0
nonalcoholicToBuy = 0

##Loops through favorite_drinks 'values'.
# Checks if value is in type of drink list.
# upates '...toBuy' list variables
for drink in favorite_drinks.values():
    if drink in cocktails:
        cocktailsToBuy += party_duration_hours
        #print(cocktailsToBuy)
    elif drink in wines:
        winesToBuy += party_duration_hours
        #print(winesToBuy)
    elif drink.lower() in liquors:
        liquorsToBuy += party_duration_hours
        #print(liquorsToBuy)
    elif drink.lower() in nonalcoholic:
        nonalcoholicToBuy += party_duration_hours
        #print(nonalcoholicToBuy)

print("""
\n"You bunch of heavy drinkers..."
You need to puchase:
'{}' Cocktails,
'{}' Wines,
'{}' Liquors,
'{}' Nonalcoholic Drinks.
""".format(cocktailsToBuy, winesToBuy, liquorsToBuy, nonalcoholicToBuy))
