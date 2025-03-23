#!/usr/bin/bash

main(){
 
    sudo apt update
    sudo apt upgrade -Y
    
    sudo apt install python3
    sudo apt-get update -y
    sudo apt-get install python3-pip -y
    sudo apt-get install python3-serial -y
	pip install opencv-contrib-python
	sudo apt install python3-gpiozero
	sudo apt-get install -y python-smbus
	sudo apt-get install -y i2c-tools
	sudo apt install v4l-utils
	

}

welcome(){ #Fonction vérifiant si on veut bien executer le script
	echo "Script d'installation du RasberryPi"
	echo "Etes-vous sûr de vouloir procéder à l'installation (Y/n)? "
	read -r answer
	if [[ $answer == "n" || $answer == "N" ]]
	then
	echo "Annulée !" #Si non, on annule
	else
	echo "C'est parti" #Si oui, on appelle main
	main
	fi
}

welcome