# func03.py

def show_items(*items):
    i = 1
    for item in items:
        print(i,':',item)
        i = i + 1
    print()


show_items(1,2,3)
show_items("ONE","TWO","THREE","FOUR")
show_items(1.23,3.5,5.1,8.01,-0.51)