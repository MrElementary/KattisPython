x = int(input())

layer = 1

count = 0

def pyramid():
    global layer, count, x
    compound = (layer*layer)
    if x >= compound:
        x = x - compound
        layer = layer + 2
        count += 1
        pyramid()
    else:
        print(count)
        
        
pyramid()
