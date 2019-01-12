print ("Use this document to change roman numerals to decimals. Enter in the roman numeral you want to convert:")
print ("Please note that this page also accepts invalid roman numerals, and these roman numerals may not be able to be used as actual roman numerals. i.e. IVXLCDM is not valid but wil output 334")
def convert_to_decimal(roman_numeral): #Converts from decimal to roman numeral
    decimal = 0 #Sets up value for output
    i = 0 #Sets up value for later usage in comparing to next character
    for char in roman_numeral: #Runs for each character in the roman numeral
        i += 1 #Sets the i value to one higher to choose character after current one being analyzed
        if char is 'M': #Check if the character is M
            decimal += 1000 #Always adds 1000 to value as there is no numeral bigger
        elif char is 'D': #Checks if the character is D
            if roman_numeral[i] == 'M':
                decimal -= 500 #If the next character is M, subtract 500
            else:
                decimal += 500 #Adds regular value of 500
        elif char is 'C': #Checks if the character is C
            if roman_numeral[i] == 'M':
                decimal -= 100 #If the next character is M, subtract 100
            elif roman_numeral[i] == 'D': 
                decimal -= 100 #If the next character is D, subtract 100
            else:
                decimal += 100 #Adds regular value of 100
        elif char is 'L': #Checks if the character is L
            if roman_numeral[i] == 'M':
                decimal -= 50 #If the next character is M, subtract 50
            elif roman_numeral[i] == 'D': 
                decimal -= 50 #If the next character is D, subtract 50
            elif roman_numeral[i] == 'C': 
                decimal -= 50 #If the next character is C, subtract 50
            else:
                decimal += 50 #Adds regular value of 50
        elif char is 'X': #Checks if the character is X
            if roman_numeral[i] == 'M':
                decimal -= 10 #If the next character is M, subtract 10
            elif roman_numeral[i] == 'D': 
                decimal -= 10 #If the next character is D, subtract 10
            elif roman_numeral[i] == 'C':
                decimal -= 10 #If the next character is C, subtract 10
            elif roman_numeral[i] == 'L':
                decimal -= 10 #If the next character is L, subtract 10
            else:
                decimal += 10 #Adds regular value of 10
        elif char is 'V': #Checks if the character is V
            if roman_numeral[i] == 'M':
                decimal -= 5 #If the next character is M, subtract 5
            elif roman_numeral[i] == 'D': 
                decimal -= 5 #If the next character is D, subtract 5
            elif roman_numeral[i] == 'C':
                decimal -= 5 #If the next character is C, subtract 5
            elif roman_numeral[i] == 'L':
                decimal -= 5 #If the next character is L, subtract 5
            elif roman_numeral[i] == 'X':
                decimal -= 5 #If the next character is X, subtract 5
            else:
                decimal += 5 #Adds regular value of 5
        elif char is 'I':
            if roman_numeral[i] == 'M':
                decimal -= 1 #If the next character is M, subtract 1
            elif roman_numeral[i] == 'D': 
                decimal -= 1 #If the next character is D, subtract 1
            elif roman_numeral[i] == 'C':
                decimal -= 1 #If the next character is C, subtract 1
            elif roman_numeral[i] == 'L':
                decimal -= 1 #If the next character is L, subtract 1
            elif roman_numeral[i] == 'X':
                decimal -= 1 #If the next character is X, subtract 1
            elif roman_numeral[i] == 'V':
                decimal -= 1 #If the next character is V, subtract 1
            else:
                decimal += 1 #Adds regular value of 1
        else:
            print ("One of the characters is invalid. Please, exit the program and try again.")
            break
    print ("This is the resulting decimal: " + str(decimal))
convert_to_decimal(raw_input())
            
                
            
            
        
    