country = ('Nigeria', 'Cameroun', 'Ghana', 'Austrailia', 'France')
tuplepractice = ('True', 'False')
print(country)

print(len(country)) # Identified the amount of items in the tuple, country

print(type(tuplepractice)) # to confirm if this data type is a tuple
print(type(country)) # the result shows that this is a tuple too

print(country[-2]) # Indexing to call the -2 as Austrailia
print(country[1:3]) # Indexing which will return position 1 and 2 as 3 won't be included, so it will return ( Cameroun, Ghana)
print(country[:3]) # This will return all countries from begining and stop at 2 (0, 1, 2) except country 3 and 4

if 'Ghana' in country:
    print("yes, 'Ghana' is in the country tuple")

country += tuplepractice # This is to add two tuples together into one
print(country) # both contents are now in one tuple 'country'

# since a tuple is unchangeable, I will have to convert it to a list before I can add an item, then convert it back to a tuple after that
Faith = list(country) 
print(Faith) # here 'Faith' is now the list of the tuple 'country'
Faith.append('Yes') #append
print(Faith) # This confirms yes has been successfully added, now let's convert back to tuple
country = tuple(Faith)
print(country) # Yes has been successfully added to the tuple 'country'

x = ('farmer', 'labourer', 'carpenter', 'mechanic') # method to unpack a tuple
(young, old, adult, aged) = x
print(young)
print(old)
print(aged)
print(adult)
(green, blue, *black) = x
print(black) # the asterisks at before the black will print black as the last two list, since there is no fourth name to match mechanic
(green, *blue, black) = x
print(blue)
print(black) # in this case blue will list the lists after the first name and before the last one which is labourer and carpenter

Increase = country * 2
print(Increase) #the increase is a multiple 2 of the tuple country

z = country.count('Ghana')
print(z) #This counted the number of times Ghana appeared in the tuple Increase
result = Increase.count('Austrailia')
print(result)