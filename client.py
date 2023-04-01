from app import client

res = client.post('/api/v1/auth/signup', json={'login': 'login', 'email': 'email', 'password': 'password'})
print(res.get_json())
