*** Keywords ***

Creation Should Fail With Message
    [Arguments]  ${message}
    New Citation Page Should Be Open
    Page Should Contain  ${message}

Book Creation Should Fail With Message
    [Arguments]  ${message}
    New Book Page Should Be Open
    Page Should Contain  ${message}

Set Authors
    [Arguments]  ${authors}
    Input Text  authors  ${authors}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Type
    [Arguments]  ${type}
    Input Text  type  ${type}

Set Note
    [Arguments]  ${note}
    Input Text  note  ${note}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set ID
    [Arguments]  ${id}
    Input Text  given_id  ${id}

Create Valid Book Citation
    Go To New Citation Page
    Select From List By Label  dropdown  Kirja
    Click Button  Valitse viite
    Set Authors  Kirjoittaja
    Set Title  Otsikko
    Set Editor  Kustannustoimittaja
    Set Publisher  Kustantaja
    Set Year  1234
    Click Button  Luo viite
