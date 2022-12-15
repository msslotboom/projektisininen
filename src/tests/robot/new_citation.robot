*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Resource  citation_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application, Create User And Login


*** Test Cases ***
Create A New Book Citation With Valid Arguments
    Go To New Book Citation Page
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Editor  Kustannustoimittaja
    Set Publisher  Kustantaja
    Set Year  1236
    Click Button  Luo viite
    References Page Should Be Open

Create Valid Article Citation With Valid Arguments
    Go To New Article Citation Page
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Journal  Julkaisu
    Set Year  1237
    Click Button  Luo viite
    References Page Should Be Open

Create Valid Other Citation With Valid Arguments
    Go To New Other Citation Page
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Type  Muu
    Set Note  None
    Set Year  1238
    Click Button  Luo viite
    References Page Should Be Open

Create A New Citation Without Authors
    Go To New Book Citation Page
    Set Title  Otsikko
    Set Editor  Kustannustoimittaja
    Set Publisher  Kustantaja
    Set Year  1234
    Click Button  Luo viite
    Book Creation Should Fail With Message  Viitteestä puuttuu tietoja

Create A New Citation Without Title
    Go To New Book Citation Page
    Set Authors  Kirjoittaja
    Set Year  1234
    Click Button  Luo viite
    Book Creation Should Fail With Message  Viitteestä puuttuu tietoja

Create A New Citation With Already Used ID
    Go To New Book Citation Page
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Editor  Kustannustoimittaja
    Set Publisher  Kustantaja
    Set Year  1234
    Set ID  IiDee
    Click Button  Luo viite
    Go To New Book Citation Page
    Set Authors  Kirjoittaja2
    Set Title  Otsikko2
    Set Editor  Kustannustoimittaja
    Set Publisher  Kustantaja
    Set Year  1235
    Set ID  IiDee
    Click Button  Luo viite
    Book Creation Should Fail With Message  Annettu ID on jo käytössä


