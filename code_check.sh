#!/bin/bash

for i in core lisean
do
	echo "Checking: $i"
	pylint --rcfile=tools/pylint.rc $i
	pep8 --repeat --ignore=E501 --exclude='migrations' $i
done
