data = {'apple': 5, 'banana': 2, 'cherry': 7}
item_list=list(data.items())
item_list.sort(key=lambda x: x[1])
sorted_data = dict(item_list)
print(sorted_data)