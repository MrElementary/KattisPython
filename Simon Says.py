lines = int(input())

for i in range(lines):
    data = input()
    blank = ""
    if "Simon says" in data:
        blank = data.replace("Simon says", "")
        print(blank)
        
