def search_elements(list, n):
    for i in range(len(list)):
        if n == list[i]:
            return i
        else:
            return None

print(search_elements([12,13,14], 12))