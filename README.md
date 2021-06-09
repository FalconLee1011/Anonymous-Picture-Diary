# NTOU-mongoDB-project <br>Anonymous Picture Diary | 匿名照片日記

## Overview
It's a homework but also a quick demonstration of how Flask + Vue + mongoDB works.

[Demo videos here](https://www.youtube.com/playlist?list=PLVmsdNL1JymYLNyFr4ZEqFtWRxNgYcf4w)

## Requirements
### Backend
- pyenv (optional)
- pipenv or install the packages listed below
  - Python packages
    - flask
    - flask-cors
    - pymongo
    - python-magic

### Frontend
- npm 
- @vue/cli >= 4.5.8

## Before anything
### Backend
- Run `pipenv install` to install all dependencies if you are using pipenv
- Prepare a mongoDB
- Copy `config.example.py` to `config.py`
- Modify the connection string (host variable) in `config.py`
- Make a directory named "cache" under `<repo>/backend/`

### Frontend
- Run `npm install` to install all dependencies.

## How to use
### Setup a development environment.
#### Backend
- Run `pipenv run python server.py`

#### Frontend
- Run `npm run serve`
- Then visit http://localhost:8080 to see the result.

### Deploy the app
- This project is not designed for deployment but for a quick demonstration of how Flask + Vue + mongoDB works.