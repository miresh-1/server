import requests

computer = {
    'mac': 'AA:BB:CC:11:22:33',
    'name': 'PC-01'
}
response = requests.post('http://127.0.0.1:5000/register', json=computer)
print(response.json())