weather=input("plz enter r=the weather(rainy, sunny, cloudy): ")
temp=int(input("plz enter the temperature: "))
if weather=="rainy" and temp<20 :
    print("wearing a raincoat and bringing an umbrella")
elif weather=="rainy" and temp>=20 :
    print("wearing a light rain jacketa")
elif weather=="sunny" and temp<20 :
    print("wearing a light sweater")
elif weather=="sunny" and temp>=20 :
    print("wearing shorts and a t-shirt")
else:
    print("wearing something comfortable")
