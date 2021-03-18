# Домашнее задание 1

# задача номер 1
print("Задача номер 1")

seconds_in_minute = 60
seconds_in_hour = seconds_in_minute * 60
seconds_in_day = seconds_in_hour * 24

user_answer = int(input("введите количество секунд: "))

if user_answer < seconds_in_minute:
    print(user_answer, "сек")
elif user_answer < seconds_in_hour:
    minutes = user_answer / seconds_in_minute
    seconds = user_answer % seconds_in_minute
    print(int(minutes), "min", seconds, "sec")
elif user_answer < seconds_in_day:
    hours = user_answer / seconds_in_hour
    minutes = user_answer % seconds_in_hour / seconds_in_minute
    seconds = user_answer % seconds_in_hour % seconds_in_minute
    print(int(hours), "h", int(minutes), "min", seconds, "sec")
else:
    days = user_answer / seconds_in_day
    hours = user_answer % seconds_in_day / seconds_in_hour
    minutes = user_answer % seconds_in_day % seconds_in_hour / seconds_in_minute
    seconds = user_answer % seconds_in_day % seconds_in_hour % seconds_in_minute
    print(int(days), "d", int(hours), "h", int(minutes), "min", seconds, "sec")



# Задача номер 2
print("Задача номер 2")

# создание листа из куба нечетных числе от 0 до 1000
cube_odd_numbers = []
max_number = 1000
counter = 0

while max_number != counter:
    counter += 1
    if counter % 2 != 0:
        cube_odd_numbers.append(counter ** 3)

print("начальный лист", cube_odd_numbers)

# решение задачи 2.a
answer_a_list = []

for a in cube_odd_numbers:
    total = 0
    while a > 0:
        digit = a % 10
        total = total + digit
        a = a // 10
    if total % 7 == 0:
        answer_a_list.append(total)
print("Ответ на задание 2.а", answer_a_list)

# решение задачи 2.b
b_list = []
answer_b_list = []

for a in cube_odd_numbers:
    b_list.append(a + 17)

for b in b_list:
    total = 0
    while b > 0:
        digit = b % 10
        total = total + digit
        b = b // 10
    if total % 7 == 0:
        answer_b_list.append(total)
print("Ответ на задание 2.b", answer_b_list)

# решение задачи 2.c
for i in range(len(cube_odd_numbers)):
    cube_odd_numbers[i] += 17
print("Новый лист 2.c", cube_odd_numbers)

answer_c_list = []
for c in cube_odd_numbers:
    total = 0
    while c > 0:
        digit = c % 10
        total = total + digit
        c = c // 10
    if total % 7 == 0:
        answer_c_list.append(total)
print("Ответ на задание 2.c", answer_c_list)


# задача номер 3
print("Задача номер 3")

user_answer_3 = int(input("Пожалуйста, введите цифру от 1 до 20: "))
percent_name_list = ["процент", "процента", "процентов"]
if user_answer_3 == 1:
    print("Вы ввели", user_answer_3, percent_name_list[0])
elif user_answer_3 < 5:
    print("Вы ввели", user_answer_3, percent_name_list[1])
elif user_answer_3 <= 20:
    print("Вы ввели", user_answer_3, percent_name_list[2])
