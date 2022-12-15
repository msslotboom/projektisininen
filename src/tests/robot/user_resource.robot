*** Keywords ***

# Checks and validations

Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    [Arguments]  ${username}
    Main Page Should Be Open
    Page Should Contain  ${username}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


# Actions

Submit Registration Credentials
    Click Button  Rekisteröidy

Submit Login Credentials
    Click Button  Kirjaudu sisään

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirm  ${password_confirmation}

Reset Application And Go To Register Page
    Reset Application
    Go To Registration Page
    Registration Page Should Be Open

Reset Application, Create User And Go To Login
    Reset Application
    Create User  Mikko  salasana123
    Go To Login Page

Create User And Login
    Create User  Paavo2  salasana1
    Go To Login Page
    Set Username  Paavo2
    Set Password  salasana1
    Click Button  Kirjaudu sisään
    Main Page Should Be Open