birth_y=int(input("plz enter your birth year: "))
generation=""
if birth_y>=1928 and birth_y<=1945 :
    generation="Silent Generation."
elif birth_y>=1946 and birth_y<=1964 :
    generation="Baby Boomers."
elif birth_y>=1965 and birth_y<=1980 :
    generation="Generation X."
elif birth_y>=1981 and birth_y<=1996 :
    generation="Millennials (Gen Y)."
elif birth_y>=1997 and birth_y<=2012 :
    generation="Generation Z (Gen Z)."
elif birth_y>=2013 :
    generation="Generation Alpha."
print("You are a "+generation)
