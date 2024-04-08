#!/bin/bash

# Replace <your_vm_ip_addr> with your actual vm ip address

if [ "$#" -ne 1 ]; then
	echo "Don't forget to replace <your_vm_ip_addr> with your actual vm ip address"
	echo "How to replace that : ./init.sh <your_vm_ip_addr>"
else
	sed -i "s/<your_vm_ip_addr>/$1/g" docker-compose.yml consumer.py producer.py
	echo "Adding your actual VM IP address to the concerned files"
fi


# Init python virtual environment

function create_py_venv {
	echo "Creating python virtual environment"
	python3 -m venv venv
	echo "Installing packages"
	venv/bin/python -m pip install -r requirements.txt > /dev/null
	echo "Python virtual environment created and configured"
}

if [ -d "venv" ];then
	echo "Python virtual environment already exist"
else
	create_py_venv
fi

check_1=$(grep "<your_vm_ip_addr>" docker-compose.yml consumer.py producer.py)
check_2=$(ls | grep venv)

if [[ $check_1 -eq "" ]] && [[ $check_2 -eq "venv" ]];then
	echo "Demo is ready !"
	echo "Enter your python virtual to execute *.py files with : source venv/bin/activate"
fi
