*** Settings ***
Library  SeleniumLibrary
Library  AppLibrary.py
Library  OperatingSystem
Library  BuiltIn

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}/
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${REFERENCES URL}  http://${SERVER}/citations
${NEW CITATION URL}  http://${SERVER}/new_citation

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Set Window Size  800  600
    Set Selenium Speed  ${DELAY}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Registration Page
    Go To  ${REGISTER URL}

Go To References Page
    Go To  ${References URL}

Go To New Citation Page
    Go To  ${NEW CITATION URL}

Go To New Book Citation Page
    Go To  ${NEW CITATION URL}
    Select From List locator:id=dropdown  value=book
    Click Button  Valitse viite

Go To New Article Citation Page
    Go To  ${NEW CITATION URL}
    Select From List locator:id=dropdown  value=article
    Click Button  Valitse viite

Go To New Other Citation Page
    Go To  ${NEW CITATION URL}
    Select From List locator:id=dropdown  value=other
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