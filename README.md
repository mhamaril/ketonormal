# Ketonormal

Sovellus herokussa: https://ketonormal.herokuapp.com/

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
