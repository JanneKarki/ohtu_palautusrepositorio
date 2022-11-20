*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***


Register With Valid Username And Password
    Set Username  janne
    Set Password  janne123
    Password Confirmation  janne123
    Submit Credentials For Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jk
    Set Password  janne123
    Password Confirmation  janne123
    Submit Credentials For Register
    Register Should Fail With Message  Username must have at least 3 characters
# ...

Register With Valid Username And Too Short Password
    Set Username  janne
    Set Password  jk123
    Password Confirmation  jk123
    Submit Credentials For Register
    Register Should Fail With Message  Password length must be at least 8 characters long


Register With Nonmatching Password And Password Confirmation
    Set Username  janne
    Set Password  janne123
    Password Confirmation  janne234
    Submit Credentials For Register
    Register Should Fail With Message  Different passwords


Login After Successful Registration
    Set Username  janne
    Set Password  janne123
    Password Confirmation  janne123
    Submit Credentials For Register
    Go To Login Page
    Set Username  janne
    Set Password  janne123
    Submit Credentials
    Login should succeed



Login After Failed Registration
    Set Username  jk
    Set Password  janne123
    Password Confirmation  janne123
    Submit Credentials For Register
    Go To Login Page
    Set Username  jk
    Set Password  janne123
    Submit Credentials
    Login should Fail With Message  Invalid username or password



