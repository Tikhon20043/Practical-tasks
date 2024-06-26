#Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
#Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
#Австралия.
#Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США

# Создаем множества для каждого турагентства
voyage = {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'}
reina_tour = {'Англия', 'Япония', 'Канада', 'ЮАР'}
raduga = {'США', 'Испания', 'Швеция', 'Австралия'}

# Проверяем, в каких множествах содержатся нужные страны
tours_to_canada = []
tours_to_usa = []

if 'Канада' in voyage:
    tours_to_canada.append('Вояж')
if 'Канада' in reina_tour:
    tours_to_canada.append('РейнаТур')
if 'Канада' in raduga:
    tours_to_canada.append('Радуга')

if 'США' in voyage:
    tours_to_usa.append('Вояж')
if 'США' in reina_tour:
    tours_to_usa.append('РейнаТур')
if 'США' in raduga:
    tours_to_usa.append('Радуга')

# Выводим результаты
print("Туры в Канаду можно приобрести в следующих турагентствах:")
for agency in tours_to_canada:
    print("- " + agency)

print("Туры в США можно приобрести в следующих турагентствах:")
for agency in tours_to_usa:
    print("- " + agency)