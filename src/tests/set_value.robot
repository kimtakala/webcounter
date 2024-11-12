*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
When counter is set the value becomes the value input
    Go To  ${HOME_URL}
    Title Should Be  Laskuri
    Page Should Not Contain  nappia painettu 20 kertaa
    Input Text  set_value  20
    Click Button  Aseta
    Page Should Contain  nappia painettu 20 kertaa