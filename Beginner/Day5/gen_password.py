#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_random_elements_from_collection(number, collection):
    result = []
    while number > 0:
        result.append(random.choice(collection))
        number -= 1
    
    return result

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = get_random_elements_from_collection(nr_letters, letters)
easy_password.extend(get_random_elements_from_collection(nr_symbols, symbols))
easy_password.extend(get_random_elements_from_collection(nr_numbers, numbers))
print(''.join(easy_password))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Initial attempt.
#hard_password = [easy_password[0]]
#for index in range(1, len(easy_password)):
#    rand_position = random.randint(0, len(hard_password)-1)
#    hard_password.insert(rand_position, easy_password[index])

#Based on course guidance.
hard_password = easy_password
random.shuffle(hard_password)
random.shuffle(hard_password)
print(''.join(hard_password))