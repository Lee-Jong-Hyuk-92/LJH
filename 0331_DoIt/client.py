import requests  # ✅ 반드시 requests (복수형!)

url = 'http://127.0.0.1:9999/predict'

input_data = [{
    'V1': -2, 'V2': -1,
    'V27': -1, 'V28': -4,
}]

try:
    res = requests.post(url, json=input_data)
    print('result:', res.json())

    if res.status_code == 200:
        print('ok')
    else:
        print(res.status_code)

except Exception as err:
    print(err)
