# joocer
Data Extracting library

## Installation steps
* brew install python3
* python3 get-pip.py

(make a virtual env using your own setup or following below steps)
* pip3 install virtualenvwrapper
* pip3 install virtualenv
* mkvirtualenv joocer -python=/usr/local/bin/python3
* workon joocer
(Activate the virtual env)

* pip3 install -r requirements.txt
* cp joocer/settings/.env.local joocer/settings/.env
* install and start redis-server locally
* restore joocer/services/test_service/data/joocer_local.sql into Local MySQL DB 'labs_core_development'

** E.g. command to run for synaptic owned data: python3 -m joocer denormalize -c -s test_service.employees.linkedin -sy -m employee_count

** E.g. command to run for org wise data: python3 -m joocer denormalize -c -s test_service.app_store.appannie -o 5 -d postgres_db -sy -m open_rate# samplePython
