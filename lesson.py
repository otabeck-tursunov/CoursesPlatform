# yosh = int(input("Yoshingizni kiriting: "))

# if yosh >= 18:
#     print("Kirish mumkin!")
# else:
#     print("Kirish mumkin emas!")


# son = int(input("Son kiriting: "))  # -15, 0, 24, 1
#
# if son > 0:  # -> Musbat
#     print("Musbat son!")  # -3, -2, -1, 0, 1, 2, 3, 4
# elif son == 0:
#     print("Son nolga teng!")
# elif son < 0:
#     print("Manfiy son!")

# bal = int(input("Balingizni kiriting: "))
#
# if 85 < bal:
#     print("5 baho")
# elif 71 < bal:
#     print("4 baho")
# elif 56 < bal:
#     print("3 baho")
# else:
#     print("2 baho")



# if kun_raqami == 1:
#     print("Dushanba")
# elif kun_raqami == 2:
#     print("Seshanba")
# elif kun_raqami == 3:
#     print("Chorshanba")


kun_raqami = int(input("Kun raqamini kiriting: "))

match kun_raqami:   # match: case -> tanlash operatori
    case 1:
        print("Dushanba")
    case 2:
        print("Seshanba")
    case 3:
        print("Chorshanba")
    case 4:
        print("Payshanba")
    case 5:
        print("Juma")
    case 6:
        print("Shanba")
    case 7:
        print("Yakshanba")
    case _:
        print("Bunday hafta kuni mavjud emas!")

soha = input("Sohangizni kiriting: ")

match soha:
    case "backend":
        print("Ajoyib backend yaxshi yo'nalish")
    case "mobile":
        print("Mobil qurilmalar hozirda yaxshi rivojlanmoqda")
    case _:
        print("Bunday soha haqida bilmayman!")



