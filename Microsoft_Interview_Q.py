numbers = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6,"seven":7,"eight":8,"nine":9,"zero":0}
teens = {"eleven":11, "twelve":12, "fifteen":15, "thirteen":13, "eighteen":18}
bases = {"million":1000000, "thousand":1000, "hundred":100}

wordToNumber = ""

def word_to_number(word:str) -> int:
    '''
        A function that converts the written English form of a number between 0 and 999999 inclusive into it's integer form

        Args:
            word (str): The written form to be converted
        
        Returns:
            int: The integer form of the number
    '''
    def word_formatter(user_input:str) -> list:
        '''
        Alters the inputted word by removing any whitespace, then removes all instances of and, commas,
        and converts the string to lowercase. Then splits the string into a list to be translated
        
        Args:
            user_input (str): The string that the user inputs to be translated
        
        Returns:
            list: The list of the inputted string that needs to be translated
        '''
        user_input = user_input.lower()
        user_input = user_input.strip()
        user_input = user_input.replace("and ", "")
        user_input = user_input.replace(",", "")
        return user_input.split()
    
    listOfWords = word_formatter(word)

    result = 0
    temp = 0
    for word in listOfWords:
        if word in numbers:
            temp += numbers[word]
        elif word in teens:
            temp += teens[word]
        elif word in bases:
            temp = temp * bases[word]
            if bases[word] != 100:
                result += temp
                temp = 0
        elif word[-2:] == "ty":
            for num in numbers:
                if num.startswith(word[:2]):
                    temp += numbers[num] * 10
        elif word[-4:] == "teen":
            temp += numbers[word[:-4]] + 10
    result += temp
    return result


print(word_to_number("one million, two hundred and thirty four thousand, five hundred and sixty seven"))