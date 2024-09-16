# product-management

Install Python 3.12


Create a virtual environment: `python3.12 -m venv .venv`

Activate it: `source .venv/bin/activate`

Install dependencies: `pip install -r requirements.txt`

Make migrations example: `python manage.py makemigrations products`

Run migrations: `python manage.py migrate`

Create superuser (dev mode): `python manage.py createsuperuser`

- username: admin
- email address: admin@example.com
- password: password

Run server: `python manage.py runserver`

## Configure Client App:

### Options
- Redirect uris: http://127.0.0.1:8000/
- Client type: Public
- Authorization Grant type: Authorization code
- Skip authorization: true

Save the following data:
- Redirect uris
- Client-id
- Client-secret

EYlpjccPGkcSrpxJWuMWsRAhEDAiqEHAJHklznEz
s1ZeHM3qyAOrsXTSUlgzUOEwseXRoJT03FFPpEBf0XiG9zGsWfRFS0uhYu4nrFLiGlcfS7eP3FDFNHezMYbntDenOE3O4hthljrjrLsJgXBKChVO67uGa5oT2JGip5Kt


You can deactivate a virtual environment with: `deactivate`

Back office: `/admin/`

Add current dependencies to requirements.txt: `pip freeze > requirements.txt`




## Registrarse

POST {{base_url}}/products/register

```json
{
  "username": "harib",
  "password": "1234",
  "email": "harib@example.com"
}
```

## Hacer login en la UI

Dado que no tenemos una app frontend y para simplificar proceso...

## Hacer login en la API

### Step 1

In a browser, go to:

`GET http://127.0.0.1:8000/o/authorize?client_id=EYlpjccPGkcSrpxJWuMWsRAhEDAiqEHAJHklznEz&response_type=code&redirect_uri=http://127.0.0.1:8000/&scope=read write&code_challenge=J4NzDMb_PMmc2Vu25zsGcbv-Ezmun5qXxbwI9JztYVU&code_challenge_method=S256`

with your specific values:

client_id=\[YOUR CLIENT ID\] 
response_type=code
redirect_url=\[YOUR REDIRECT URI\]
scope=read write
code_challenge=\[YOUR CODE CHALLENGE\]
code_challenge_method=S256

Code verifier: nw2F7ZlMo_7BZRLoChjtZI6ARm2Ni_AOOmGyaRuh2pc
Code Challenge: q8VeE3Oy0Seu_WNbPnwL8ou7Sva1Uvuyn45d7gaaJ9o 

### Step 2

{
"access_token": "lzosRF6uh60gu75bdH7BngBPr192qV",
"expires_in": 3600,
"token_type": "Bearer",
"scope": "read write",
"refresh_token": "6eQmI6r7Lwc1Qs6PNxKWvglTUn9phR"
}