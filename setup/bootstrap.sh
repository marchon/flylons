#!/bin/bash
OUTPUT_DIR="env"

exit_on_failure() {
  if [ "$?" -ne "0" ]; then
    echo " 
UH-OH! YOU'VE BEEN HIT BY THE

|^^^^^^^^^^^^^^^^|
|   FAIL TRUCK   | ‘|””;.., ___.
|_…_…______========|= _|__|…, ] |
(@ )’(@ )””””*|(@ )(@ )******(@)

"
    echo "Here's the problem: $1"
    echo "It's been real..."
    exit 1
  fi
}

MY_PYTHON=`which python`
echo $MY_PYTHON

echo "><><><><><><><><><><><><><><><><><"
echo "Step 1: Creating a virtualenv"
echo "><><><><><><><><><><><><><><><><><"
virtualenv ../$OUTPUT_DIR
exit_on_failure "Couldn't install a virtualenv. You probably don't have that shit installed..."

echo "><><><><><><><><><><><><><><><><><><><><><><><><><><><><"
echo "Step 2: Installling your packages...that's what SHE said"
echo "><><><><><><><><><><><><><><><><><><><><><><><><><><><><"
source ../$OUTPUT_DIR/bin/activate
for PACKAGE in `grep -v "^#" requirements.txt`
do
  easy_install $PACKAGE
  exit_on_failure "Got hung up on package $PACKAGE...name might be wrong brah"
done

echo "><><><><><><><><><><><><><><><><><><><><><><"
echo "Step 3: Making things relocatable...why not"
echo "><><><><><><><><><><><><><><><><><><><><><><"
virtualenv ../$OUTPUT_DIR --relocatable

echo "><><><><><><><><><><><><><><><><><><><><><"
echo "Step 4: Making tmp and log directories..."
echo "><><><><><><><><><><><><><><><><><><><><><"
mkdir ../$OUTPUT_DIR/log
mkdir ../$OUTPUT_DIR/tmp

echo "
 _______                                          _       _ 
(_______)                                  _     (_)  _  | |
 _       ___  ____  _____     ____ _____ _| |_    _ _| |_| |
| |     / _ \|    \| ___ |   / _  | ___ (_   _)  | (_   _)_|
| |____| |_| | | | | ____|  ( (_| | ____| | |_   | | | |_ _ 
 \______)___/|_|_|_|_____)   \___ |_____)  \__)  |_|  \__)_|
                            (_____|    
"
