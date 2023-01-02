from api import set_status

class Application():
    def __init__(self, json_data):
        self.agree=json_data['agree']
        self.agree_date=json_data['agree_date']
        self.app_number=json_data['app_number']
        self.changed=json_data['changed']
        self.code_status=json_data['code_status']
        self.comment=json_data['comment']
        self.created=json_data['created']
        self.education_form=json_data['education_form']
        self.education_level=json_data['education_level']
        self.education_source=json_data['education_source']
        self.entrant_fullname=json_data['entrant_fullname']
        self.entrant_snils=json_data['entrant_snils']
        self.id=json_data['id']
        self.id_campaign=json_data['id_campaign']
        self.id_competitive_group=json_data['id_competitive_group']
        self.id_status=json_data['id_status']
        self.name_status=json_data['name_status']
        self.need_hostel=json_data['need_hostel']
        self.registration_date=json_data['registration_date']
        self.uid=json_data['uid']
        self.uid_epgu=json_data['uid_epgu']
    
    def set_status(self):

        pass