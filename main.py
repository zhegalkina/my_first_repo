"""№ 1"""
#
# def calendar(year, month, date = ""):
#     print("it is {} {} {}".format(year, month, date))
# calendar(year = 2023, month = 6, date = 30)
#
#
#
# """№ 2"""
#
# def insect(*args):
#     print(args)
# insect('insect1', 'insect2', 'insect3')

# """№ 3"""
#
# def car(brand, model = "Q7"):
#     print('{} {}'.format(brand, model))
# car(brand="audi")


# """№ 4"""
#
# def fun():
#     phrase = "Привет, питонист!"
#     def fun_2():
#         print(phrase)
#     fun_2()
# fun()

"""№ 5"""

# def counter(word):
#     count = 0
#     count_2 = 0
#     letters = ['a', 'e', 'i', 'o', 'u', 'y']
#     # for i in word:
#     #     if i in letters:
#     #         count += 1
#     #     else:
#     #         count_2 += 1
#     # print(count, count_2)
#     list_1 = [i for i in word if i in letters]
#     answer = len(word) - len(list_1)
#     print(len(list_1))
#     print(answer)
#
#
# counter(word = 'tarekioldgsqpozb')


# """№ 6"""
#
# tallies = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# def roman_to_decimal(roman_number="XIV"):
#     sum = 0
#     for i in range(len(roman_number)-1):
#         left = roman_number[i]
#         right = roman_number[i+1]
#         if tallies[left] < tallies[right]:
#             sum-=tallies[left]
#         else:
#             sum+=tallies[left]
#     sum +=tallies[roman_number[-1]]
#     return sum
# print(roman_to_decimal())


"""№ 7"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        square = self.width*self.height
    def square (self):
        return self.width * self.height
print(Rectangle(width = int(input("Enter width: ")), height = int(input("Enter height: "))).square())


