price = 0
while True:
    try:
        tickets = int(input("Введите количество билетов для онлайн-конференции: "))
        if type(tickets) == int:
            break
    except:
        print("Введите корректное количество!")
for i in range(tickets):
    i += 1
    while True:
        try:
            age = int(input(f"Возраст посетителя (полных лет) № {i} : "))
            if age >= 100 or age <=0:
                print("Такой возраст не подходит, попробуйте заново")
                continue
            elif 25 <= age < 100:
                price += 1390
                print(f"Цена билета посетителя № {i} : 1390 руб.")
            elif 25 > age >= 18:
                price += 990
                print(f"Цена билета посетителя № {i} : 990 руб.")
            else:
                print(f"Проход для посетителя № {i} бесплатный")
            if type(age) == int:
               break
        except:
            print("Неверный формат ввода, попробуйте ввести заново")

if tickets > 3:
    discount_price = int(price * 0.9)
    print(f"Сумма к оплате: {discount_price} руб."'\n'"Скидка 10% за регистрацию группы больше трех человек.")
else:
    print(f"Сумма к оплате: {price} руб.")