*** Keywords ***
Registration Should Succeed
    Main Page Should Be Open

Submit Registration Credentials
    Click Button  Rekisteröidy

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirm  ${password_confirmation}

Create User And Go To Register Page
    Create User  Jaakko  salasana1
    Go To Registration Page
    Registration Page Should Be Open
