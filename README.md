![actions_badge](https://github.com/msslotboom/projektisininen/workflows/build/badge.svg)  

[Linkki sovellukseen](https://projektisininen.fly.dev)  
[Testikattavuus](https://app.codecov.io/github/msslotboom/projektisininen)  
  
## Backlogit
[Product ja sprint backlogit](https://docs.google.com/spreadsheets/d/190t4pxaOxAFbWoXax1XO7td4qyt_bBqrh0JbS_d_AtI)  

## Definition of Done
- Hyväksymiskriteerit täyttyvät
- Sivu toimii tuotannossa (fly.io)
- Sopivasti yksikkötestejä
- Sopivasti end-to-end -testejä
- Asiakas on hyväksynyt

## Ohjeita kehittäjille

### Asennus
1. Asenna PostgreSQL
    (ohjeita: [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart) ja [PostgreSQL:n dokumentaatio](https://www.postgresql.org/docs/current/installation.html))
2. Asenna riippuvuudet komennolla ```poetry install```
3. Luo projektin juureen tiedosto nimeltä `.env`, johon määrittelet PostgreSQL-tietokannan osoitteen `DATABASE_URL=postgresql:///tietokannan_nimi_tähän`. Tietokannan osoitteen muodostumisesta lisää [täällä](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING)
4. Lisää `.env` tiedostoon myös generoitu `SECRET_KEY` ja `FLASK_DEBUG=1`
5. Alusta tietokanta ajamalla tiedosto `initialize_db.py`
6. Käynnistä sovellus ajamalla tiedosto `start.py`

### Yksikkötestit
Testeille kannattaa tehdä oma tietokanta. Tee projektin juureen tiedosto `.env.test`, johon kopioit sisällön tiedostosta `.env`. Muuta tietokannan osoiote luomasi testitietokannan osoitteeksi. Yksikkötestit voi ajaa komennolla `pytest src`.

### Robot-testit
Robot-testien suorittamista varten avaa sovellus toisessa terminaalissa komennolla `dotenv -f .env.test run -- python3 src/start.py`. Sen jälkeen testit voi ajaa normaalisti komennolla `robot src/tests/robot`.


