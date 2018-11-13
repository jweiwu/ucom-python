numbers = [3, 14, 52, 37, 100, 82, 9, 30, 50, 200, 18, 40]
over30 = sorted(i for i in numbers if i > 30)
print over30
under40 = sorted((i for i in numbers if i < 40), reverse=True)
print under40
