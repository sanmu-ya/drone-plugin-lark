# This is a sample Python script.
import json
import os
from json import JSONDecodeError
from pprint import pprint



# Press the green button in the gutter to run the script.
from plugin import send_massage, check_required_parameter

if __name__ == '__main__':

    webhook = check_required_parameter('WEBHOOK', os.environ.get('PLUGIN_WEBHOOK'))
    message = check_required_parameter('MESSAGE', os.environ.get('PLUGIN_MESSAGE'))
    sign = check_required_parameter('SECRET', os.environ.get('PLUGIN_SECRET'))

    try:
        message = json.loads(message)
    except JSONDecodeError as e:
        pass

    content_list = []
    if isinstance(message, str):
        if ',' in message:
            for row in message.split(','):
                content_list.append(row)
    elif isinstance(message, list):
        for row in message:
            if isinstance(row, dict):
                for key in row:
                    content_list.append(f"{key}: {row[key]}")
            else:
                content_list.append(row)
    elif isinstance(message, dict):
        for key in message:
            content_list.append(f"{key}: {message[key]}")
    else:
        content_list.append(message)

    content = "\n".join(content_list)

    send_massage(webhook, sign, content)

