*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN URL}

Go To Main Page
    Go To  ${HOME URL}

Register Page Should Be Open
    Title Should Be  Register

Input New Command
    Input  new

Go To Register Page
    Go To  ${REGISTER URL}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials For Register
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

