# 1
my_dict = {'Denis': 2005, 'Max': 2007, 'Anton': 2023}
print (my_dict)
print(my_dict['Denis'])
print(my_dict.get('Lizz', 'Такого нет'))
my_dict.update({'Kate': 1991,
                'Alex': 2003})
print (my_dict)
a = my_dict.pop('Max')
print(a)
print (my_dict)
# 2
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 3}
print(my_set)
my_set.add(6)
print(my_set) #если делать по примеру, выводит None

