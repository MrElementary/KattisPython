friends = int(input())

date_dict = {}

for i in range(friends):
    data = list(map(str,input().split()))
    name = data[0]
    friend_rating = int(data[1])
    b_date = data[2]
    if b_date in date_dict:
        if friend_rating > date_dict[b_date][1]:
            date_dict.update({b_date:[name,friend_rating]})
        else:
            pass
    else:
        date_dict[b_date] = [name,friend_rating]
 
print(len(date_dict))
for i in sorted(date_dict.values()):
    print(i[0])
    

# https://stackoverflow.com/questions/35420617/update-value-in-dictionary-with-multiple-values-per-key
# https://thispointer.com/python-dictionary-with-multiple-values-per-key/
# https://www.digitalocean.com/community/tutorials/python-add-to-dictionary
# https://stackoverflow.com/questions/50493838/fastest-way-to-sort-a-python-3-7-dictionary
