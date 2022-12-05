*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application, Create User And Go To Login

*** Test Cases ***
Login With Valid Username And Password
    Set Username  Mikko
    Set Password  salasana123
    Submit Login Credentials
    Login Should Succeed  Mikko

Login With Nonexistent Username
    Set Username  Jaakko
    Set Password  salasana123
    Submit Login Credentials
    Login Should Fail With Message  Väärä käyttäjänimi tai salasana

Login With Incorrect Password
    Set Username  Mikko
    Set Password  salasana456
    Submit Login Credentials
    Login Should Fail With Message  Väärä käyttäjänimi tai salasana

Login With No Username Or Password
    Submit Login Credentials
    Login Should Fail With Message  Käyttäjänimi ja salasana vaaditaan
