a = list(map(int, input().split()))
print(a)


"""
используя input().split() мы разделяем строку то есть
4 5 6 8 9 == ["4", "5", "6", "8", "9"]
для того чтобы сделать из str в int нужно применить функцию int
int("4") == 4
Используя map() применяем функцию int() ко всем элементам списка
"""