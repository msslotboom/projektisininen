*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Resource  citation_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application, Create User And Login


*** Test Cases ***
Download Bibliography Of References
    Go To References Page
    Click Link  Lataa viitetiedosto
    Sleep  1s
    File Should Exist  ${CURDIR}/../../templates/download.html

Create Valid Citation And Download Bibliography
    Go To References Page
    Create Valid Book Citation
    Click Link  Lataa viitetiedosto
    Sleep  1s
    File Should Not Be Empty  ${CURDIR}/../../templates/download.html