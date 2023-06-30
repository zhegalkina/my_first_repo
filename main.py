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

def counter(word):
    count = 0
    count_2 = 0
    letters = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in word:
        if i in letters:
            count += 1
        else:
            count_2 += 1
    print(count, count_2)
counter(word = 'tarekioldgsqpozb')
