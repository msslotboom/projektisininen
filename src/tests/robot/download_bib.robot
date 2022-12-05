*** Settings ***
Resource  resource.robot
Resource  user_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login


#*** Test Cases ***
#Download Bibliography Of References
    #Go To References Page
    #Click Link  Lataa
    #Sleep  10s
    #File Should Exist  templates/download.html