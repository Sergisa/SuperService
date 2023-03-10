import requests
import json
from status import REJECT, Status

url = 'http://sergisa-net.ru:8080/api/'
cookies = {
    'login': 'frolovaea@mgppu.ru',
    'password': '61b6ea291a42cafa16f902dd8e7feaf08f97e7ccede615c26aaa7fa80113363c',
    'current-org': '168'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def make_post_request(api_path='', data=None):
    return requests.get(url + api_path, cookies=cookies, headers=headers, data=json.dumps(data)).json()


def make_get_request(api_path='', data=None):
    return requests.get(url + api_path, cookies=cookies, headers=headers, data=json.dumps(data)).json()


def get_applications(page=1, search_fullname=None, items_per_page=100, status: Status = None):
    link = 'applications/list?page={0}&limit={1}'.format(page, items_per_page)
    if status is not None:
        link += '&filter_status={0}'.format(status.id)
    if search_fullname is not None:
        link += '&search_fullname={0}'.format(search_fullname)
    return make_get_request(link)


def get_people(page=1, search_surname=None, items_per_page=100):
    link = 'entrants/list?page={0}&limit={1}'.format(page, items_per_page)
    if search_surname is not None:
        link += '&search_surname={0}'.format(search_surname)
    return make_get_request(link)


def set_status(id, status):
    result_reject = make_post_request('applications/{0}/status/set'.format(id), data=status)
    return result_reject


def reject(id):
    result_reject = make_post_request('applications/{0}/status/set'.format(id), data=REJECT.data_body)
    return result_reject
