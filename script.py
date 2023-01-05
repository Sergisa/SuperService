from application import Application
from api import get_applications, reject
from status import *

items_per_page = 200


def iterate_over_applications(func, status: Status = None, search_fullname=None):
    pages_count = get_applications(status=status, search_fullname=search_fullname)['paginator']['count_page']
    for page in range(1, pages_count + 1):
        for application in get_applications(status=status, search_fullname=search_fullname, page=page)['data']:
            func(Application(application))


def reject_duty(application):
    print(reject(application['id']))
    print(application.entrant_fullname + ' ' + application.comment + " " + str(application.id))


'''
application model
agree: false
agree_date: "2022-12-29T13:59:06.245395+03:00"
app_number: "1998865804" идентификатор заявления из анкеты
changed: "2022-12-29T13:59:06.245395+03:00"
code_status: "service_denied" // кодовое представление статуса
comment: "37.03.01 Психология (очн.-заочн. форма, ДОГОВОР) СО, ДО 2022 - 37.03.01 Психология (очн.-заочн. форма, ДОГОВОР) СО, ДО 2022"
created: "2022-06-20T09:20:59.268952+03:00"
education_form: "Очно-заочная форма обучения"
education_level: "Бакалавриат"
education_source: "С оплатой обучения"
entrant_fullname: "Михайлова Вероника Михайловна"
entrant_snils: "12556807469"
id: 1694 //идентификатор заявления из ссылки
id_campaign: 791 // идентификатор приемной кампании
id_competitive_group: 53883 // идентификатор конкурсоной группы
id_status: 12 иднтификатор статуса
name_status: "Отклонено" //тектовое представение статуса
need_hostel: false 
registration_date: "2022-06-20T09:20:55+03:00"
uid: "b96124a6-2099-4073-b362-2c7701c1bd95"
uid_epgu: 1998865804 // идентификатор заявления из анкеты
'''


def echo_duty(application):
    print("{} {} {}".format(application.comment, application.entrant_fullname, application.name_status))


iterate_over_applications(echo_duty, status=ENROLLED)
