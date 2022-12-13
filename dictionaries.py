alien_0 = {'color': 'green', 'point': '5'}
print(alien_0['color'])
print(alien_0['point'])


subhash = {'color': ' brown ' , 'age': '21'}
print(subhash['color'])
print(subhash['age'])


phone = {'company': 'oppo', 'ram': '3'}
print(phone['company'])
print(phone['ram'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("you have scored" +" "+ str(new_points)+ " " + "points" + "!")

phone = {'company': 'oppo', 'ram': '5'}
new_phone= phone['ram']
print("This phone is good because it has" + " " + str(new_phone)+ " " + "ram" + "!")

alien_0 = {'color': 'red', 'point': '5'}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'color': 'green'}
print("The alien is" + " "+ alien_0['color']+ '.')

alien_0 = {'color': 'yellow'}
print("the alien is now" + " " + alien_0['color']+ '.')

phone = {'company': 'oppo', 'ram':'3'}
print(phone)
new_phone = phone['company']
print(new_phone)

phone ={'company': 'apple', 'ram': '5'}
print(phone)
new_phone = phone['ram']
print('This phone has ' + " " +  str(new_phone) + " " + 'gb of ram' + '.' )

phone = {'company': 'apple'}
print('Now this phone company name is' + " " + phone['company']+  '.')

phone = {'company':'motto'}
print('first the company name was' + " " + phone['company'] + '.')

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium' }
print("original x-position:" + str(alien_0['x_position']))
if alien_0['speed'] == 'medium':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_position: " + str(alien_0['x_position']))    

alien_0 = {'color':'green', 'points':'5'}
print(alien_0)
del alien_0 ['points']
print(alien_0)

favourite_language = {
    'sara' : 'python',
    'sky'  : 'java',
    'phil' : 'c',
    'mike' : 'html'

}

print("sky's favourite langauge is " + favourite_language['sky'].title() + '.')


first_name = ('subhash')
print(first_name)
last_name = ('yadav')
print(last_name)
age = ('21')
print(age)
city = ('bangalore')
print(city)

person = {
    'first_name' : 'subhash',
    'last_name' : 'yadav',
    'age'  : '21',
    'city' : 'bangalore'
}

print(person['first_name'].title())
print(person['last_name'])
print(person['age'].title())
print(person['city'].title())

favourite_numbers = {
    'mike' : '100',
    'sky' :  '50',
    'mike' : '200',
    'ric'  : '400',
    'asus' : '500',
}

print("favourite number of mike is" + " " +favourite_numbers['mike']+'.')
print("favourite number of sky is" + " " +favourite_numbers['sky']+'.')
print("favourite number of mike is" + " " +favourite_numbers['mike']+'.')
print("favourite number of ric is" + " " +favourite_numbers['ric']+'.')
print("favourite number of asus is" + " " +favourite_numbers['asus']+'.')


glossary = {
    'int' : 'integer',
    'num' : 'number',
    'float': 'decimal',
    'boolean': 'yes/no',
    'string' : 'special character',
    }

word = 'int'
print(f"\n{word.title()}: {glossary[word]}")

word = 'num'
print(f"\n{word.title()}: {glossary[word]}")

word = 'float'
print(f"\n{word.title()}: {glossary[word]}")

word = 'boolean'
print(f"\n{word.title()}: {glossary[word]}")

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")