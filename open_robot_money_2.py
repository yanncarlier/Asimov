import requests


# ACCESS_KEY = 'token-d9d4m' 
# ACCESS_SECRET = 'zfg77gtjsqpc4xxxxxxxxx7njtg79nsmggjmsmmx5wtddclq9t'


# config = {
#     "containers": [{
#         "imagePullPolicy": "IfNotPresent",
#         "image": "xxx/llb-admin:dev",
#         "name": "bbl-admin-dev"
#     }],
#     "namespaceId": "default",
#     "name": "llb-admin-dev"
# }

#requests.post('https://rancher2.example.com/v3/project/c-dwbgf:y-cfkx1/workloads', json=config, auth=(ACCESS_KEY, ACCESS_SECRET)

#requests.post('https://52.68.24.107/v3/project/c-7hsqj:p-5rg9s/workloads', json=config, auth=(ACCESS_KEY, ACCESS_SECRET), verify=False)

# requests.post(url, json=config, auth=(ACCESS_KEY, ACCESS_SECRET), verify=False)

config = {
	"Authorization":"DirectLogin token='eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.VgxxO2PSSz76Vgq6tIMMS2MeRftaKxxPHd1sN2aFqHI'",
	"Content-Type":"application/json"
	}

#url = 'https://openlab.openbankproject.com/obp/v3.0.0/banks/hsbc.01.hk.hsbc/accounts/f751de0f-18dd-46dc-8b36-5f9664cf0431/owner/account'

url = 'https://openlab.openbankproject.com/obp/v3.0.0/'

data = 'banks/hsbc.01.hk.hsbc/accounts/f751de0f-18dd-46dc-8b36-5f9664cf0431/owner/account'
data2 = 'my/accounts'



out = requests.get(url + data, json=config)

print(out)


