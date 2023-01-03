import json


class Status:
    def __init__(self, json_data) -> None:
        self.data_body = json_data
        self.code = json_data['code']
        self.notification = json_data['notification']
        self.status_comment = json_data['status_comment']

    def is_final(self):
        return self.code in ['app_call_off']

    def to_json(self):
        return json.dumps(self.data_body)


ACCEPT = Status({
    'code': "app_call_off",
    'notification': None,
    'status_comment': None
})
REJECT = Status({})
