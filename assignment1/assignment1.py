# Task 1
def hello():
    return "Hello!"
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Irelys"))

# Task 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        
        elif operation == "subtract":
            return a - b
        
        elif operation == "multiply":
            return a * b
        
        elif operation == "divide":
            return a / b
        
        elif operation == "modulo":
            return a % b
        
        elif operation == "int_divide":
            return a // b
        
        elif operation == "power":
            return a ** b
        
        else:
            return "Invalid operation"
        
    except ZeroDivisionError:
        return "You can't divide by 0!"
    
    except TypeError:
        return "You can't multiply those values!"
    
calc(5, 3, "add")
calc(5, 3, "multiply")
calc(10, 0, "divide")
calc("a", 3, "add")

# Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        
        if data_type == "int":
            return int(value)
        
        if data_type == "str":
            return str(value)
        
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    
print(data_type_conversion("25", "int"))
print(data_type_conversion("3.14", "float"))
print(data_type_conversion(100, "str"))
print(data_type_conversion("nonsense", "float"))

# Task 5
def grade (*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
    except TypeError:
        return"Invalid data was provided."
    
print(grade(95, 90, 100))
print(grade(80, 85, 82))
print(grade(70, 75, 72))
print(grade(60, 65, 68))
print(grade(40, 55, 50))
print(grade(90, "fail", 80))

# Task 6
def repeat(text, count):
    result = ""

    for i in range(count):
        result += text

    return result

print(repeat("Hi,", 3))


# Task 7
def student_scores(choice, **kwargs):
    if choice == "best":
        best_student = ""
        highest_score = -1

        for name, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = name

        return best_student
    
    elif choice == "mean":
        return sum(kwargs.values()) / len(kwargs)
    
print(student_scores("best", Ana = 90, Carlos = 85, Juan = 98))

# Task 8
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    words = title.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word
        else:
            words[i] = word.capitalize()

    return " ".join(words)

print(titleize("the lord of the rings"))
print(titleize("i know what you did last summer"))

# Task 9
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

print(hangman("python", "pto"))

#  Task 10
def pig_latin(text):
    vowels = "aeiou"
    result = []

    words = text.split()

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")

        else:
            index = 0

            while index < len(word):
                if word[index:index + 2] == "qu":
                    index += 2

                elif word[index] in vowels:
                    break
        
                else:
                 index += 1
            
            result.append(word[index:] + word[:index] + "ay")
        
    return " ".join(result)
    
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))

    
