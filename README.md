# llm-fastapi

## Local env setup 

### First time set up
1. Install python3.9 first. I use pyenv to maintain several python runtime in my local laptop `pyenv install python 3.9`. 
2. cd into this repo and run `pyenv local 3.9`, this will create `.python-version` file so that your `pyenv` know to use `python 3.9` for this folder.
3. Install `pip install pipenv`.
4. To install package run `pipenv install`. This will generate `Pipfile` and `Pipfile.lock`. Pipenv will install dependencies into the virtualenv for you.
5. Enter the virtual env `pipenv shell`. And exit when you are done `exit`

### Install dependencies 
Run `pipenv install package-name`. This should update `Pipfile` and `Pipfile.lock`

### Deploy to Vercel
