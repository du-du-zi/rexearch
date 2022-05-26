import requests

url = "http://10.17.23.228:7799/analyze"

data={'text': '문재인 대통령은 30일 “정부는 지자체와 협력해 중산층을 포함한 소득하위 70% 가구에 대해 4인 가구 기준으로 가구 당 100만원을 긴급재난지원금을 지급하기로 결정했다“고 말했다.'}
files=[

]
headers = {
  'apikey': 'JQZh6G92wfceymIfvBlu674LIWIQXVe0'
}

response = requests.request("POST", url, headers=headers, data=data)
print(response.text)
# print(response["sentence"][0]["entity"])
