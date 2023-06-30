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

def counter(letters):
    count = 0
    count_2 = 0
    letters_2 = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in letters:
        if i in letters_2:
            count += 1
    print(count)
    for i in letters:
        if i not in letters_2:
            count_2 += 1
    print(count_2)
counter(letters = 'tarekioldgsqpozb')
