data = []

mod_list = []

for i in range(10):
    data.append(int(input()))

for i in data:
    mod_value = i % 42
    if mod_value not in mod_list:
        mod_list.append(mod_value)
    else:
        continue

print(len(mod_list))
