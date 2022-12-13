names = [ ]

phone_numbers = [ ]

num = 3

for i in range(num):
    name = input("name")
    phone_num = input("phone_num")

    names.append(name)
    phone_numbers.append(phone_num)

print("name\t\ phone_num ")

for i in range(num):
    print("{}\t\t\t{}".format(names[i],
                            phone_numbers[i]))

search_term = input("\n Enter search term:")

print("Search result:")

if search_term in names:
          index = names.index(search_term)
          phone_num = phone_numbers[index]
          print("names:{},phone number:{}".format(search_term,phone_num))

else:
    print("name not found")
