if __name__ == '__main__':
    class User:
        def __init__(self, name, passw):
            self.Name = name
            self.Passw = passw
            self.Jog = 0


    Userek = [User("admin", "password"), User("superadmin", "pw123")]
    Userek[0].Jog = int(1)
    Userek[1].Jog = int(2)

    kilepunkE = False

    while (not kilepunkE):
        print("1 - login")
        print("2 - reg")
        print("9 - exit")

        menu = input("Válassz menüpontot: ")

        if int(menu) == 1:
            beName = input("Add meg a nevet: ")
            bePassw = input("Add meg a jelszavad: ")

            eredmeny = -99999

            for u in Userek:
                if u.Name == beName:
                    if u.Passw == bePassw:
                        eredmeny = 1
                    else:
                        eredmeny = 0
                else:
                    eredmeny = -1
            if eredmeny == 1:
                print("Beléptünk")
                beVagyunkELepve = True
                while (beVagyunkELepve):
                    if u.Jog >= 1:
                        print("1 - Új felhasználó regisztrálás")
                    if u.Jog >= 2:
                        print("2 - Felhasználó törlés")
                    print("3 - Felhasználók listázása")
                    print("9 - Kijelentkezés")

                    menuIn = input("Válassz menüpontot: ")

                    if int(menuIn) == 1 and u.Jog >= 1:
                        beName = input("Add meg a nevet: ")
                        bePassw = input("Add meg a jelszavad: ")

                        Userek.append(User(beName, bePassw))
                    elif int(menuIn) == 1 and u.Jog < 1:
                        print("Nincs jogod ehhez")
                    elif int(menuIn) == 2 and u.Jog >= 2:
                        beName = input("Add meg a felhasználónevet, amelyet törölni akarsz.")
                        if beName == u.Name:
                            print("Magad nem törölheted.")
                        else:
                            torolni = None
                            for uT in Userek:
                                if uT.Name == beName:
                                    torolni = uT
                            Userek.remove(torolni)
                    elif int(menuIn) == 2 and u.Jog < 2:
                        print("Ehhez nincs jogod!")
                    elif int(menuIn) == 3:
                        print("Felhasználók, azonos vagy kisebb szinten:")
                        for u2 in Userek:
                            if u2.Jog <= u.Jog:
                                print(u2.Name + " - " + str(u2.Jog))
                    elif int(menuIn) == 9:
                        beVagyunkELepve = False
                    else:
                        print("Nincs ilyen menüpont, válassz másikat")
            elif eredmeny == 0 or eredmeny == -1:
                print("Nem tudtunk beléptetni... Hibás felhasználónév vagy jelszó. Hibakód: " + str(eredmeny))
            else:
                print("Valami nem jó...")
        elif int(menu) == 2:
            beName = input("Add meg a nevet: ")
            bePassw = input("Add meg a jelszavad: ")

            Userek.append(User(beName, bePassw))
        elif int(menu) == 9:
            kilepunkE = True

    print("Kilépés...")
