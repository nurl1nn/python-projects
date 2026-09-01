import qrcode
daxil=input("What do you want to create? wifi/url/vCard\n").upper()
if daxil=="WIFI":
        wifi = f"WIFI:T:WPA;S:{input('Add your wifi name: ')};P:{input('Add your password')};;"
        kod=qrcode.QRCode()
        kod.add_data(wifi)
        kod.make()
        sekil = kod.make_image(fill_color="black",back_color="white")
        sekil.save("sekil.png")
elif daxil=="VCARD":
        card=(
        f"BEGIN:VCARD\n"
        f"VERSION:3.0\n"
        f"FN:{input('Input a name or full name: ')}\n"
        f"TEL:{input('Input a number: ')}\n"
        f"EMAIL:{input('Input an email: ')}\n"
        f"END:VCARD"
        )
        kod=qrcode.QRCode()
        kod.add_data(card)
        kod.make()
        sekil = kod.make_image(fill_color="black",back_color="white")
        sekil.save("sekil.png")
elif daxil=="URL":
        url= input("Input your url adress: ")
        kod=qrcode.QRCode()
        kod.add_data(url)
        kod.make()
        sekil = kod.make_image(fill_color="black",back_color="white")
        sekil.save("sekil.png")