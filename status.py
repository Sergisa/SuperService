import json


class Status:
    def __init__(self, json_data, id) -> None:
        self.id = id
        self.data_body = json_data
        self.code = json_data['code']
        self.notification = json_data['notification']
        self.status_comment = json_data['status_comment']

    def is_final(self):
        return self.code in ['app_call_off']

    def to_json(self):
        return json.dumps(self.data_body)


CALL_OFF: Status = Status({  # Отзыв
    'code': "app_call_off",
    'notification': None,
    'status_comment': None
}, 15)
REJECT = Status({  # Отклонено
    'code': "service_denied",
    'notification': None,
    'status_comment': None
}, 12)

CONSIDERED = Status({  # Рассмотрение
    'code': "considered",
    'notification': None,
    'status_comment': None
}, 4)

NEW = Status({  # Новое
    'code': "new",
    'notification': None,
    'status_comment': None
}, 1)

ENROLLED = Status({  # Зачислен
    'code': "enrolled",
    'notification': None,
    'status_comment': None
}, 19)

IN_COMPETITION = Status({  # Учавствует в конкурсе
    'code': "in_competition",
    'notification': None,
    'status_comment': None
}, 8)

OUT_COMPETITION = Status({  # Не прошло по конкурсу
    'code': "out_competition",
    'notification': None,
    'status_comment': None
}, 10)
