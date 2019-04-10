def media(n,num):
    media=(n+num)/2
    if media >=0.0 and  media <= 4.9:
        return"D"
    elif media >=5.0 and media <= 6.9:
        return"C"
    elif media >=7 and media <= 8.9:
        return"B"
    elif media >=7 and media >=10:
        return"A"
nota1=float(input("Digite a sua 1ª nota"))
n2=float(input("Digite a sua 2ª nota"))
if media(nota1,n2)=="D":
    print("MEDIA-D")
elif media(nota1,n2)=="C":
    print("MEDIA-C")
elif media(nota1,n2)=="B":
    print("MEDIA-B")
elif media(nota1,n2)=="C":
    print("MEDIA-A")

