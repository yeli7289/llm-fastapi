# llm-fastapi

## Local env setup 
### First time set up
- Install `python3.9` first. I use pyenv to maintain several python runtimes in my local laptop `pyenv install python 3.9`. 
- cd into this repo and run `pyenv local 3.9`, this will create `.python-version` file so that your `pyenv` know to use `python 3.9` for this repo.
- Install `pip install pipenv`.
- Run `pipenv install`. This will generate `Pipfile` and `Pipfile.lock` and install dependencies into the virtualenv for you.
- Enter the virtual env `pipenv shell`. And exit when you are done with `exit`.

### Install dependencies 
Run `pipenv install package-name`. This should update `Pipfile` and `Pipfile.lock`

### Test locally
- Test on your local machine: Run `uvicorn main:app --host 0.0.0.0 --port 8000`. This will run the application at localhost on port `8000`. 
- Test on the Dev Vercel Serverless env: Run `vercel`. This will deploy our local code into a dev env, so you can test with your local change. 

### Deploy to Vercel
- Set up vercel account and install vercel CLI.
- Once ready you can commit and push the code. By default Vercel will deploy to prod with new commit merged to `main` branch. 
