# Ketonormal

Sovellus herokussa: https://ketonormal.herokuapp.com/
su 23.8.2020 Välipalautus 3
Sovellusta voi kokeilla käyttäjällä matti, salasanalla matti tai voi luoda uuden käyttäjän. Mypage sivulla näkyy oma profiili, jonka mukaan mypage sivulla näytetään myös raja-arvot labroille. Mypage sivulla näkee myös kyseisen käyttäjän lisäämät labratulokset sekä 3 viimeisintä viestiä, mitkä on lähetetty keskustelupalstalle. Klikkaamalla lisättyä labran nimeä sovellus näyttää arvot ja sen voi halutessaan poistaa. Klikkaamalla keskustelusta Replyä niin se vie sivulle, jossa näkyy kyseinen keskustelu. Siellä voi lähettää viestin kyseiseen keskusteluun. Forum sivulla näkyy kaikki keskustelut viimeisimmästä viestistä alkaen. Klikkaamalla otsikkoa pääsee lukemaan kyseisen ketjun viestejä sekä vastaamaan siihen. Submit Labs toimii niin kuin pitää ja se ilmoittaa jos joku tieto puuttuu. Make Queries toimii myös ja siinä voi lähes kaikilla mahdollisilla vaihtoehdoilla tutkia eri raja-arvoja.

Sovelluksesta puuttuu vielä toiminnallisuus joka antaa muokata omia viestejä sekä admin käyttäjälle oikeus poistaa viestejä sekä viestiketjuja. Login sivun keskiarvot eivät näy kuin kirjautuneille käyttäjille. Tämä meni mielestäni "rikki" kun tein layout.html ja Bootstrapin avulla tyylitellyt sivut. Kuvaajia en saanut piirrettyä, kun en keksinyt miten saisin tietokannasta haetun tiedon oikeanlaiseen json muotoon. 

Mielestäni sovellus toimii niinkuin pitää ja tekee kaikki haluamani asiat paitsi tuon viestien poiston. Mainitsemani muut puutteet eivät ominaisuuksiin vaikuta, mutta olivat sellaisia mitä alunperin tähän sovellukseen suunnittelin. Ulkoasua voi vielä hioa jonkin verran.



su 9.8.2020	Välipalautus 2

Sovelluksessa on toimiva rekisteröinti ja sisäänkirjautuminen. Kaikki sovelluksen sivut vaatii sisäänkirjautumisen paitsi infosivu. Jos yrittää rekisteröidä samalla käyttäjänimellä niin tulee virhe viesti(korjattu omalla koneella, ei herokussa).

Mypage sivulla pitäisi näkyä vain omat labrat, mutta nyt siellä näkyy kaikkien labrojen nimet. Klikatessa labran nimeä avautuu sivu missä on kyseisen labran kaikki arvot. Mypage sivulla tulee myös näkymään 3 viimeisintä keskustelua, joihin voi siirtyä suoraan otsikkoa klikkaamalla.

Submit Labs- toimii halutulla tavalla, paitsi jos ei täytä kaikkia kohtia. Se lisää tietokantaan annetut arvot

Make Queries toimii ja se laskee raja-arvot valituilla parametreilla, paitsi jos ei laita kaikki kysyttyjä arvoja.

Discuss ei sisällä vielä toiminnallisuuksia. Sinne tulee keskustelufoorumi. Siellä tavallinen käyttäjä voi osallistua keskusteluun ja poistaa omat viestinsä, mutta admin oikeuksilla varustettu käyttäjä voi poistaa kaikkien viestejä.

su 26.7.2020 Välipalautus 1
Tietokantasovellus, johon tallennetaan verikokeen tulokset ja se laskee kullekin arvolle uudet perusterveiden viitearvot tälle tietylle käyttäjäryhmälle.

-Nykyiset viite-arvot on määritelty koko väestön perusterveiden mukaan. Tämä sovellus kerää verikokeiden tuloksia ihmisiltä, jotka ovat vähähiilihydraattisella ruokavaliolla. Esimerkikisi kolesteroliarvot ovat tällaisilla ihmisillä usein korkeammat kuin vähärasvaista ruokavaliota noudattavilla. Haluan määritellä mitkä ovat viite-arvot tällaisellä ihmisryhmällä.

-haluan tehdä sovelluksesta turvallisen ja sellaisen minkä voin oikeasti julkaista ja ylläpitää. Tällainen tieto varmasti kiinnostaa näitä ihmisiä.

Sovellus vaatii rekisteröitymisen ja sisäänkirjautumisen, että tuloksia voi lisätä sekä tarkastella.

-peruskäyttäjä voi lisätä ja poistaa oman tuloksensa. Voi lisätä useamman kuin yhden verikokeen tuloksen 
-käyttäjältä kysytään kuinka paljon hän syö hiilihydraattia päivässä(low carb, keto, carnivore), ikä, sukupuoli, kokonaiskolesteroli, LDL, HDL, Triglyt, Hs-CRP, kuinka kauan paastoa ennen koetta 
-käyttäjä näkee miten hänen arvonsa sijoittuvat viitearvoihin -Hän voi tehdä erilaisia "hakuja" käyttöliittymässä, muuttamalla kriteereitä, esim haku koko tietokannasta, vain oman ikäisten ja oman sukupuolen perusteella, Hs-CRP < 1, yli vai alle 12h paasto jne -tulokset näytetään myös graafisesti

Info sivu

-miksi teen tämän ja kuka olen

ehkä: Sovellukseen tulee keskustelupalsta, jos aikataulu ja harjoitustyön vaativuus sitä edellyttää.

-vain kirjautuneet käyttäjät voivat lisätä ja nähdä viestejä 
-vain oman viestin voi poistaa 
-admin käyttäjä voi poistaa kaikkien viestejä
