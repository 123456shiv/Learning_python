def list_data_type_function(lst):
    return [type(item) for item in lst]

list = [1, 'hello', 3.14, True, None]
result = list_data_type_function(list)

print(result)  

list_data_type_function
