def flatten_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            lst[i:i+1] = lst[i]

list_a = [1,2,3,[4],5,[6,[7,[],8,[9]]]]
flatten_list(list_a)
print("Плоский список: ", list_a)