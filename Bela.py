x,y = input().split()
numberofcards = (int(x)*4)

card_dict_non = {"A":11,"K":4,"Q":3,"J":2,"T":10,"9":0,"8":0,"7":0}

card_dict_dom = {"A":11,"K":4,"Q":3,"J":20,"T":10,"9":14,"8":0,"7":0}

total = 0

for i in range(numberofcards):
    card_data = list(input())
    card_one = card_data[0]
    card_two = card_data[1]
    if card_two == y:
            total += card_dict_dom[card_one]
    else:
            total += card_dict_non[card_one]
               
print(total)
        
