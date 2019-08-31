# while_06.py

num = 7
i = 0

while i < num:
    i = i + 1
    if i == 2 or i == 5:
        print('スキップします')
        continue
    print(i)
print('ループ処理終了')