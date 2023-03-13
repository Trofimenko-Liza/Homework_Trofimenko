
# task 1
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
e = float(input("Enter e: "))

if  ((a*a) + (b*b)) == ((c*c) + (e*e)):                             # перевірка чи це прямокутник
    rectange_sqrt = a*b
    print("Rectange square is :", +rectange_sqrt)

elif a == b and b == c  and c == e and a ==c and a == e and b == e: # перевірка чи це квадрат
    print("It is square")

else:                                                               # опрацювання помилки
    print("Incorrect value. It is not Rectange and not Square")




#task 2
import random

name = ["Anna", "Serhii", "Maxim", "Inna", "Maria", "Ivan", "Matvei", "Maya", "Makar", "Kirill"]
domain = ["com", "net", "org", "ua", "biz", "info"]
email_name = (random.choice(name))                                 # генерування випадкового ім'я
email_domain = (random.choice(domain))                             # генерування випадкового домейну
email_data = (str(random.randint(99,1000)))                        # генерування випадкового числа
email_letter = [random.choice('abcdefghijklm') for i in range(7)]  # генерування набору випадкових літер
email_letter2 = ''.join(email_letter)                              # приведення випадковіх літер до читабельного вигляду
full_email = str(email_name +"." + email_data + "@" + email_letter2 +"." +  email_domain) # компанування всіх значень
print(full_email)
