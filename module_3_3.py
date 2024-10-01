def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()                              
print_params(5, 'ветер', False)   
print_params(7, 'снег')           
print_params(b = 'дождь')               
print_params(c = [1, 2, 3])

values_list = [3.2, 'листва', False]
values_dict = {'a': 4, 'b': 'дерево', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [22.33, 'часы']
print_params(*values_list_2, 42)
