import requests

#url = 'https://openlab.openbankproject.com/obp/v3.0.0/banks/hsbc.01.hk.hsbc/accounts/f751de0f-18dd-46dc-8b36-5f9664cf0431/owner/account'
# /obp/v3.1.0/banks/BANK_ID/accounts/ACCOUNT_ID/VIEW_ID/funds-available

#url = 'https://openlab.openbankproject.com/obp/v3.0.0/'
BASE_URL = 'https://openlab.openbankproject.com/obp/'
API_VERSION = 'v3.0.0/'
URL = BASE_URL + API_VERSION
BANK = 'banks/hsbc.01.hk.hsbc/'
ACCOUNT = 'accounts/f751de0f-18dd-46dc-8b36-5f9664cf0431/owner/account/VIEW_ID/funds-available'


config = {
	"Authorization":"DirectLogin token='eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.VgxxO2PSSz76Vgq6tIMMS2MeRftaKxxPHd1sN2aFqHI'",
	"Content-Type":"application/json"
	}



out = requests.get(URL + BANK + ACCOUNT, json=config)

print(out)


