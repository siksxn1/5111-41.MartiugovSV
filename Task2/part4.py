vowels = "aouie"
simvol = input("напишите букву:")
if vowels.upper().__contains__(simvol.upper()):
    print("гласная")
elif simvol.upper()=='Y':
    print("гласная или согласная")
else:
    print('согласня')
    


