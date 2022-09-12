number_of_cards, secret_card, number_of_steps = map(int,input().split())

for i in range(number_of_steps):
    raw_data = list(map(int,input().split()))
    data = raw_data[1::]
    if secret_card in data:
        print("KEEP")
    else:
        print("REMOVE")
