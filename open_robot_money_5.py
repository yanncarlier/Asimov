import requests

url = "https://openlab.openbankproject.com/obp/v3.0.0/banks/hsbc.01.hk.hsbc/accounts/f751de0f-18dd-46dc-8b36-5f9664cf0431/owner/account"

payload = "funds-available"
headers = {
    'Authorization': 'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.VgxxO2PSSz76Vgq6tIMMS2MeRftaKxxPHd1sN2aFqHI"',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "98e81d93-da8c-436b-a477-3f97b174553c"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)