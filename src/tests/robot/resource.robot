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

Main Page Should Be Open
    Location Should Be  ${HOME URL}

Login Page Should Be Open
    Location Should Be  ${LOGIN URL}

Registration Page Should Be Open
    Location Should Be  ${REGISTER URL}
