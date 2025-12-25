#!/bin/bash
echo
echo "Available builds: "
echo " 1 - calculator.py"
echo
echo -n "Choose a number to build > "
read choice
# Create dir if it doesnt exist, ignore error (idw use -p i like the violent ignore better)
mkdir builds 2> /dev/null
# Use python from path if available else use a path provided in argument 1 
# Can be sent as, say, `./builds.sh "$(which py3)"` or `./builds.sh "$(type py3 | grep bin/python3\ \$argv | awk '{print $1}')"`
# Here `which` checks $PATH and `type` checks imported scripts such as ~/.bashrc and checks for a bin path with arguments passed, then clips out the first whole string
# Thats also what the third option does with the second argument, given that it exists; you can force use the third option by passing an invalid path in argument 1 to force-fail it
if [ "$choice" = "1" ]; then
    if python -m nuitka --output-dir=builds --remove-output --output-filename=calculator --follow-imports calculator.py; then
        echo "Success building binary with system python"
    else
        if [ "$#" -lt 2 ]; then
            if "$1" -m nuitka --output-dir=builds --remove-output --output-filename=calculator --follow-imports calculator.py; then
                echo "Success building binary with provided python path"
        else
            py_path=$(type "$2" | grep 'bin/python3 \$argv' | awk '{print $1}')
            if "$py_path" -m nuitka --output-dir=builds --remove-output --output-filename=calculator --follow-imports calculator.py; then
                echo "Success building binary with resolved python path"
        fi
    fi
fi
