#!/bin/bash

#get gmail account
read -p "Enter Your Gmail eMail: "  email
read -p "Enter Your Gmail Password: "  pass
read -p "Enter Your Gmail App Password: "  appPass

read -p "Enter Your the \"to\" cell phone number (Ex: 4105555555)"  number
read -p "Enter Your this numbers carrier (Ex: ATT)"  carrier

read -p "do you want to dd another phone number?"  cur

while [  $cur = "yes"]

do 
        read -p "Enter Your the \"to\" cel phone number (Ex: 4105555555)"  number
        read -p "Enter Your this numbers carrier (Ex: ATT)"  carrier
        read -p "do you want to dd another phone number?"  cur
done 
sudo apt-get install ssmtp mail utils

edit etc/ssmtp/ssmtp.conf

mailhub=smtp.gmail.com:587
AuthUser = youremail
AuthPass = yourpassword
UseSTARTTLS=YES
UseTLS=YES
