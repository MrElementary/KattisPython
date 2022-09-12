card_types = list(map(int,input().split()))

gold_cards = card_types[0]
silver_cards = card_types[1]
copper_cards = card_types[2]

gold_value = gold_cards*3
silver_value = silver_cards*2

total_value = gold_value+silver_value+copper_cards

if total_value <= 1:
    print("Copper")
if total_value == 2:
    print("Estate or Copper")
if total_value == 3 or total_value == 4:
    print("Estate or Silver")
if total_value == 5:
    print("Duchy or Silver")
if total_value == 6 or total_value == 7:
    print("Duchy or Gold")
if total_value >= 8:
    print("Province or Gold")
