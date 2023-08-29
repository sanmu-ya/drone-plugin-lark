import hashlib
import base64
import hmac
import time

import requests


def get_sign(timestamp, secret):
	# 拼接timestamp和secret
	string_to_sign = '{}\n{}'.format(timestamp, secret)
	hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
	# 对结果进行base64处理
	sign = base64.b64encode(hmac_code).decode('utf-8')
	return sign


def send_massage(webhook: str, sign: str, content: str):
	timestamp = str(int(time.time()))
	data = {
		"timestamp": timestamp,  # 时间戳。
		"sign": get_sign(timestamp, sign),  # 得到的签名字符串。
		"msg_type": "text",
		"content": {
			"text": content
		}
	}
	response = requests.post(url=webhook, json=data)
	print(response)
	print(response.text)


def check_required_parameter(parameter_name, parameter_value):
	if not parameter_value:
		raise Exception(f'{parameter_name} is a required parameter!')
	return parameter_value
