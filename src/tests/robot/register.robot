*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Mikko
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Registration Should Succeed
