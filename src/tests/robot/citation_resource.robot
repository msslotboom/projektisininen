*** Keywords ***

Creation Should Fail With Message
    [Arguments]  ${message}
    New Citation Page Should Be Open
    Page Should Contain  ${message}

Set Authors
    [Arguments]  ${authors}
    Input Text  authors  ${authors}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set ID
    [Arguments]  ${id}
    Input Text  given_id  ${id}