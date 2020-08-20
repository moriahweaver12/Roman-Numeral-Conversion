
input = input ("Input your archaic number:")

array1 = list(input)


one = "I"
five = "V"
ten = "X"
fifty = "L"
one_hundred = "C"
five_hundred = "D"
one_thousand = "M"

translatedArray = []

#convert letters to basic number equivalent
for romanNumeral in array1:
    if romanNumeral == one:
        equivalent = 1
        translatedArray.append(equivalent)
        
    elif romanNumeral == five:
        equivalent = 5
        translatedArray.append(equivalent)

    elif romanNumeral == ten:
        equivalent = 10
        translatedArray.append(equivalent)

    elif romanNumeral == fifty:
        equivalent = 50
        translatedArray.append(equivalent)

    elif romanNumeral == one_hundred:
        equivalent = 100
        translatedArray.append(equivalent)

    elif romanNumeral == five_hundred:
        equivalent = 500
        translatedArray.append(equivalent)

    elif romanNumeral == one_thousand:
        equivalent = 1000
        translatedArray.append(equivalent)
    
    else:
        print("Not a valid Roman Numeral.")


baseNumber = 0
rightNumber = 1

translatedFinal = []

#subtractive notation
for x in translatedArray[:-1]:    
    if translatedArray[baseNumber] < translatedArray[rightNumber]:
        equivalentFinal = translatedArray[rightNumber] - translatedArray[baseNumber]
        translatedFinal.append(equivalentFinal)
        baseNumber += 1
        rightNumber += 1
    else:
        equivalentFinal = translatedArray[baseNumber]
        translatedFinal.append(equivalentFinal)
        baseNumber += 1
        rightNumber += 1  


if len(translatedArray) > 1:
    if translatedArray[-1] <= translatedArray[-2]:
        translatedFinal.append(translatedArray[-1])


convertedRomanNumeral = sum(translatedFinal)

#If it's a single digit
if convertedRomanNumeral == 0:
    print(translatedArray[-1])
else:print (convertedRomanNumeral)
