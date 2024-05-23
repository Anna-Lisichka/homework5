immutable_var = 'car', 12, 4, 'clock'
print(immutable_var)

# immutable_var[2] = 1000
# print(immutable_var)    # кортеж это неизменяемый список. Изменению не подлежат такие элементы как строки и числа, однако если внутри кортежа будет изменяемый элемент (например, список), то элементы внутри списка можно будет менять.

mutable_list = [17, 'or', 30, 'yars']
mutable_list[1] = 'and'
print(mutable_list)