import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '2459eebf28ec8aa0afbb5e3e1dbc033c'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'C3ax-5tyGz751dxZxJ7Hg3LUizQFrck2V6ZOtMDO06Bi43almawUrgAAAAQKKwzUAAABkC3zBcq2W8wW6V7rJg'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)