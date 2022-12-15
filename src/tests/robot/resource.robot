*** Settings ***
Library  SeleniumLibrary
Library  AppLibrary.py
Library  OperatingSystem

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}/
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${REFERENCES URL}  http://${SERVER}/citations
${NEW CITATION URL}  http://${SERVER}/new_citation
${NEW BOOK URL}  http://${SERVER}/new_book

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Set Window Size  1600  900
    Set Selenium Speed  ${DELAY}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Registration Page
    Go To  ${REGISTER URL}

Go To References Page
    Go To  ${REFERENCES URL}

Go To New Citation Page
    Go To  ${NEW CITATION URL}

Go To New Book Citation Page
    Go To  ${NEW CITATION URL}
    Select From List By Label  dropdown  Kirja
    Click Button  Valitse viite

Go To New Article Citation Page
    Go To  ${NEW CITATION URL}
    Select From List By Label  dropdown  Artikkeli
    Click Button  Valitse viite

Go To New Other Citation Page
    Go To  ${NEW CITATION URL}
    Select From List By Label  dropdown  Muu
    Click Button  Valitse viite

Main Page Should Be Open
    Location Should Be  ${HOME URL}

Login Page Should Be Open
    Location Should Be  ${LOGIN URL}

Registration Page Should Be Open
    Location Should Be  ${REGISTER URL}

New Citation Page Should Be Open
    Location Should Be  ${NEW CITATION URL}

References Page Should Be Open
    Location Should Be  ${REFERENCES URL}
    
New Book Page Should Be Open
    Location Should Be  ${NEW BOOK URL}