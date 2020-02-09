'''1) Scrieti o functie care se foloseste de for sa parcurga numerele de la 0 la 100.
Daca numarul este par, va fi adunat intr-o alta variabila, si se va trece la urmatorul numar.
Daca numarul este mai mic decat 10, va fi afisat pe ecran.
Daca numarul este intre 10 si 20, vom trece la urmatorul numar.
'''

x=0
for i in range(1,100):
    if i>10 and i<20:
        continue
    elif i<10:
        if i%2==0:
            print(i)
            x+=i
        else:
            print(i)
    elif i%2==0:
        x+=i
print(x)   


# numerele pare dintre 10 si 20 nu sunt adunate in variabila x


'''2) Scrieti o functie care afiseaza pe ecran numerele de la 1 la 100, fiecare pe un rand.
Daca numarul este multiplu de 3, afisati "Fizz" in loc de acel numar.
Daca numarul este multiplu de 5, afisati "Buzz" in loc de acel numar.
Daca numarul este multiplu si de 3 si de 5, afisati "FizzBuzz" in loc de acel numar.
'''

for i in range(1,100):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
