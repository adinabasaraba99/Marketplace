- 👋 Hi, I’m @adinabasaraba99
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
adinabasaraba99/adinabasaraba99 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
Basarabă Adina, 336CB

Tema 1 ASC

ORGANIZARE

In rezolvarea temei, am pornit de la scheletul dat pentru
problema Multi Producer, Multi Consumer.

IMPLEMENTARE

Producer

Un producător produce produse noi care sunt publicate mai apoi pe piață.
Dacă lista de care dispune producatorul sau dacă am reușit să publicăm
produsul, folosesc sleep pentru a aștepta o perioadă de timp.

Consumer

Cumpărătorul primește un coș de cumpărături(carts), căruia îi este asociat un
anumit id. Atunci când pune un anumit produs în coș, acesta devine indisponibil
pentru ceilalți cumpărători (este șters din Marketplace). Atunci când șterge
produse din coș, acestea devin disponibile pentru restul cumpărătorilor.
De asemenea, plasează comenzi.

Marketplace

Am definit urmatoarele structuri:
dicționarul stock în care rețin pentru fiecare producător,produsele, lista
products în care rețin toate produsele, lista carts, lock-uri pentru
lock_register, lock_publish, lock_new_cart.

Metode:
- register_producer: nu este o zona thread-safe, așa că
apelez un lock; returnez id-ul prod_id
- publish: am pus produsul primit in lista producătorului cât timp
aceasta nu depașea limita de elemente permise.
- new_cart: adaug id pentru fiecare nou cart
- add_to_cart && remove_from_cart: am adăugat elementul dorit
după ce l-am căutat printre produse && am șters elementul din market
după ce l-am pus în coș
- place_order: returnează o listă cu toate produsele din coș.
