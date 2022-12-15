*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Mikkoo
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Registration Should Succeed

Register With Short Username
    Set Username  M
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Registration Should Fail With Message  Käyttäjänimi on liian lyhyt

Register With Long Username
    Set Username  Mikkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkko
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Registration Should Fail With Message  Käyttäjänimi on liian pitkä

Register With Short Password
    Set Username  Mikko
    Set Password  s
    Set Password Confirmation  s
    Submit Registration Credentials
    Registration Should Fail With Message  Salasana on liian lyhyt

Register With Long Password
    Set Username  Mikko
    Set Password  ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    Set Password Confirmation  ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    Submit Registration Credentials
    Registration Should Fail With Message  Salasana on liian pitkä

Register With Nonmatching Passwords
    Set Username  Mikko
    Set Password  salasana123
    Set Password Confirmation  salasana456
    Submit Registration Credentials
    Registration Should Fail With Message  Salasanat eivät täsmää

Register With No Username Or Password
    Submit Registration Credentials
    Registration Should Fail With Message  Käyttäjänimi ja salasana vaaditaan

Register With Taken Username
    Create User  Mikko  salasana123
    Set Username  Mikko
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Registration Should Fail With Message  Käyttäjänimi Mikko on jo käytössä


