*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Resource  citation_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login


*** Test Cases ***
Create A New Citation With Valid Arguments
    Go To New Citation Page
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Year  1234
    Click Button  Luo viite
    References Page Should Be Open

Create A New Citation Without Authors
    Go To New Citation Page
    Set Title  Otsikko
    Set Year  1234
    Click Button  Luo viite
    Creation Should Fail With Message  Viitteestä puuttuu tietoja

Create A New Citation Without Title
    Go To New Citation Page
    Set Authors  Kirjoittaja
    Set Year  1234
    Click Button  Luo viite
    Creation Should Fail With Message  Viitteestä puuttuu tietoja

Create A New Citation With Already Used ID
    Go To New Citation Page
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Year  1234
    Set ID  1
    Click Button  Luo viite
    Go To New Citation Page
    Set Authors  Kirjoittaja2
    Set Title  Otsikko2
    Set Year  1235
    Set ID  1
    Click Button  Luo viite
    Creation Should Fail With Message  Annettu ID on jo käytössä


