# age = 19
# money = 20000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20:
#     print("성인이고 맥주를 드실수 있습니다.")
# if money >= drink:
#     print("음료수를 먹는다.")



# age = 19
# money = 25000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨 구매 가능.")
# elif money >= drink:
#     print("음료 구매 가능")
# elif money >= beer and age >= 20:
#     print("치킨과 을료수 모두 구매 가능")
# else:
#     print("치킨 성인이라 술과 음료 구매 가능.")

# age = 20
# money = 25000
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨 구매 가능.")
# elif money >= drink:
#     print("음료 구매 가능")
# elif money >= beer and age >= 20:
#     print("치킨과 을료수 모두 구매 가능")
# else:
#     print("치킨 성인이라 술과 음료 구매 가능.")

# if money >= chicken:
#     print("치킨 구매.")
# if money - chicken >= drink:
#     print("성인이고 맥주를 드실수 있습니다.")
# if money % beer and age <= 20:
#     print("음료수를 먹는다.")
# else:
#     print("미성년자이기 때문에 술은 안되요")
    
# if money >= chicken:
#     print("치킨을 먹는다.")
     #money = money - chicken
# if money >= beer and age >= 20:
#     print("성인이고 맥주를 드실수 있습니다.")
#    money = money - beer
# if money >= drink:
#     print("음료수를 먹는다.")
#    money = money - drink

# if money >= chicken + beer + drink and age >= 20:
#     print("치킨, 맥주, 음료수 먹는다.")
# elif money >= chicken + beer and age >= 20:
#     print("치킨, 맥주 먹는다.")
# elif money >= chicken + drink:
#     print("치킨, 음료수 먹는다.")
# elif money >= beer + drink and age >= 20:
#     print("맥주, 음료수 먹는다.")
# elif money >= beer and age >= 20:
#     print("맥주 먹는다.")
# elif money >= drink:
#     print("음료수 먹는다.")
# else:
#     print("")

age = 20
money = 25000
chicken = 20000
beer = 10000
drink = 5000

if money >= chicken:
    print("치킨구매 가능")
    if money - chicken >= beer and age >= 20:
        print("맥주를 먹는다")
        if money - chicken - beer >= drink:
            print("음료수를 먹는다")
    if money - chicken >= drink:
elif money >= beer and age >= 20:
    print("맥주를 먹는다.")
    if money - beer >= drink:
        print("음료수를 먹는다")
elif money >= drink:
    print("음료수를 먹는다.")