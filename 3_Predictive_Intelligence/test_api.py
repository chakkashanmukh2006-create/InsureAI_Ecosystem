import requests

# 1. Register a user
requests.post('http://127.0.0.1:8002/register', json={'username':'admin2', 'email':'a@a.com', 'password':'password'})

# 2. Login
res_login = requests.post('http://127.0.0.1:8002/login', data={'username':'admin2', 'password':'password'})
token = res_login.json()['access_token']

# 3. Request top20 leads
res_leads = requests.get('http://127.0.0.1:8002/leads/top20', headers={'Authorization': f'Bearer {token}'})
print("STATUS CODE:", res_leads.status_code)
print("RESPONSE:", res_leads.text[:500])
