'''
Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m = ",m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m,pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")
code = input("Введите Ваш номер по списку группы: ")
n1, n2 = input("Введите два числа через пробел: ").split()
d, m, y = input("Введите дату Вашего рождения\
(Формат: \"DD.MM.YYYY\") - ").split('.')
print("{} + {} ={}".format(n1,n2,float(n1)+float(n2)))
print("Ваш день рождения %s.%s.%s и Вы %d в \
списке учебной группы" % (d,m,y,int(code)) )
m = input("Введите число \"m\": ")
pi = input("Введите число \"Pi\": ")
print("{}, {}".format(m,pi,float(n1)+float(n2)))
year = input("Введите год вашего поступления в ВУЗ: ")


examResults={
  "math":0,
  "russian_language":0,
  "computer_science":0
}
examResults["math"] = input("Введите количество ваших баллов \
по ЕГЭ по Математике: ")
examResults["russian_language"] = input("Введите количество \
ваших баллов по ЕГЭ по Русскому языку: ")
examResults["computer_science"] = input("Введите количество \
ваших баллов по ЕГЭ по Информатике: ")


print(examResults)