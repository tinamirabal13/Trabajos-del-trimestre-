foo = input("Cuantas tazas de harina quieres usar")
print(foo)
foo=int(foo)
bar= input ("Cuantas tazas de agua necesitas?")
print(bar)
bar= int(bar)
sal= input ("Cuantas cdtas de sal quieres usar?")
print(sal) 
sal= int(sal)
tazasdesal= sal/48 
print("Eso equivale a ", tazasdesal)
aceite= input("Cuantas cucharadas de aceite quieres usar?")
print(aceite)
aceite=int(aceite)
tazasdeaceite = aceite/16
print("Eso equivale a", tazasdeaceite)
resultado= foo + bar + tazasdesal + tazasdeaceite 
print("Equivale a", resultado)