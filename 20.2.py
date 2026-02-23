n = int(input())
my_dict = {}
answers=[]
for _ in range(n):
    parts = input().split()
    if parts[0] == "set":
        key = parts[1]
        value = parts[2]
        my_dict[key] = value
    elif parts[0] == "get":
        key = parts[1]
        if key in my_dict:
            answers.append(my_dict[key])
        else:
            answers.append("KE: no key", key, "found in the document")
for x in answers:
    print(x)