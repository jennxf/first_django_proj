# first_django_proj
Markdown syntax documentation: http://vi.stackexchange.com/editing-help
- source activate myvenv
	- source deactivate
	- docs for venv http://conda.pydata.org/docs/using/envs.html#list-all-environment
	- if error running, del the virtual env and create a new one:
	- rm -rf  /Users/jennxf/anaconda/envs/myvenv
	- conda create --name myvenv python=3
	- re-install django: pip install django
	- otherwise just do:source activate myvenv

- to work on pythonanywhere.com
	- use "https" when git clone the repo
	- have to use virtualenv for linux and not conda
	- re-install django

- If changes are made to models.py:
	- Locally you need to run ./manage.py makemigrations blog
	- Then ./manage.py migrate
	- git add, commit and push
	- in other machines after git pull, they need to run ./manage.py migrate so changes are stored in the their DB.

- How to Make a pull request:
	1. fork the repo.
	2. git clone the forked repo and make sure its the SSH URL and not the https one
	3. create a branch. git checkout -b 	
