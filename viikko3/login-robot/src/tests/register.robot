*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  bbb  bbb12345
    Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  aaa  aaa12345
    Output Should Contain  User with username aaa already exists

    
Register With Too Short Username And Valid Password
    Input Credentials  aa  aaa12345
    Output Should Contain  Username must have at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  bbb  bbb123
    Output Should Contain  Password length must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  bbb  bbbbbbbb
    Output Should Contain  Password contain only letters a-z

*** Keywords ***
Input New Command And Create User
    Create User  aaa  aaa12345
    Input New Command


