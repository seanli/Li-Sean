#!/bin/bash

python2.7 /home/lisean/webapps/lisean/Li-Sean/manage.py generate_static_dajaxice > /home/lisean/webapps/lisean/Li-Sean/lisean/assets/js/dajaxice.core.js
python2.7 /home/lisean/webapps/lisean/Li-Sean/manage.py collectstatic 
/home/lisean/webapps/lisean/apache2/bin/./restart
