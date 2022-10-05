sup=float(input('Магнитуда змелетресения по шкале Рихтера:'))
if(sup<2.0):
    print('минимальное')
elif(sup>=2.0) and (sup<3.0):
    print("Очень слабое")
elif(sup>=3.0) and (sup<4.0):
    print("Слабое")
elif(sup>=4.0) and (sup<5.0):
    print("Промежуточное")
elif(sup>=5.0) and (sup<6.0):
    print("Умеренное")
elif(sup>=6.0) and (sup<7.0):
    print("Сильное")
elif(sup>=7.0) and (sup<8.0):
    print("Очень сильное")
elif(sup>=8.0) and (sup<10.0):
    print("Огромное")
else:
    print("Разрушительное")
