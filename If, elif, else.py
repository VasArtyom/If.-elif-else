first = input("Введите первое целое число: ")
second = input("Введите второе целое число: ")
third = input("Введите третье целое число: ")
if (first == second
        and first == third
        and second == third):
    print("3")
else:
    print("Все три числа не равны между собой!")

if (first == second
            or first == third
            or second == third):
    print("2")
else:
     print("Все три числа не равны между собой! Даже 2 из 3 ведённых числе не равны между собой")

if not first == second and not first == third and not second == third:
      print("0")
else:
    print("Хотя бы 2 из 3 ведённых чисел равны между собой!")