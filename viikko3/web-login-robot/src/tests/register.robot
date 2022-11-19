*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***


Register With Valid Username And Password
    Set Username  janne
    Set Password  janne123
    Password Confirmation  janne123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jk
    Set Password  janne123
    Password Confirmation  janne123
    Submit Credentials
    Register Should Fail With Message  Username must have at least 3 characters
# ...

Register With Valid Username And Too Short Password
    Set Username  janne
    Set Password  jk123
    Password Confirmation  jk123
    Submit Credentials
    Register Should Fail With Message  Password length must be at least 8 characters long


Register With Nonmatching Password And Password Confirmation
    Set Username  janne
    Set Password  janne123
    Password Confirmation  janne234
    Submit Credentials
    Register Should Fail With Message  Different passwords

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open


Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

