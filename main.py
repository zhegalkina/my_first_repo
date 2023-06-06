# a = int(input("a: "))
# b = int(input("b: "))
# answer_1 = a + b
# answer_2 = a - b
# answer_3 = a * b
# print(answer_1, answer_2, answer_3)


# value = int(input("enter first digit: "))
# value_2 = int(input("enter second digit: "))
# # if else
# if value_2 == 0:
#     print("Zero division problem!")
# else:
#     answer = value / value_2
#     print(answer)


# fingers = int(input("Input number of fingers "))
# if fingers == 1:
#     print("Штрафной бросок")
# elif fingers == 3:
#     print("Трехочковый бросок")
# elif fingers == 2:
#     print("Обычный бросок")
# else:
#     print("А в баскетбол ли там играют вообще??")


a = int(input("Input digit 1: "))
b = int(input("Input digit 2: "))
if a < b:
    print(a)
    print(b)
elif a > b:
    print(b)
    print(a)
else:
    print("digit 1 = digit 2")
