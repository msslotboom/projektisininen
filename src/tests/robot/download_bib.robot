*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login


*** Test Cases ***
Download Bibliography Of References
    Go To References Page
    Click Link  Lataa
    Sleep  1s
    File Should Exist  ${CURDIR}/../../templates/download.html

Create Valid Sitation And Download Bibliography
    Go To References Page
    Create Valid Sitation
    Click Link  Lataa
    Sleep  1s
    File Should Not Be Empty  ${CURDIR}/../../templates/download.html