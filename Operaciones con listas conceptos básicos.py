
user_input = input("Ingresa números enteros separados por comas: ")


original_list = [int(num) for num in user_input.split(",")]


unique_list = []


for number in original_list:
    
    if number not in unique_list:
        unique_list.append(number)


print("Lista original:", original_list)
print("Lista sin repeticiones:", unique_list)
