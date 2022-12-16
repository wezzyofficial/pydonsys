import requests
from pydonsys.settings import QIWI_SECRET
from datetime import datetime, timezone, timedelta


class Qiwi:
    def __init__(self):
        self.create_session()

    __session = None
    __url = 'https://api.qiwi.com/partner/bill/v1/bills/'

    __token = QIWI_SECRET
    __headers = {
        'Authorization': f'Bearer {QIWI_SECRET}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def create_session(self):
        self.__session = requests.Session()
        self.__session.headers = self.__headers

        return self.__session

    def r(self, url: str = '', params: dict = {}, r_type: str = 'post'):
        s = self.__session.put
        if r_type == 'GET':
            s = self.__session.get
        elif r_type == 'POST':
            s = self.__session.post

        error = ''

        try:
            sr = s(url=url, json=params)
        except Exception as error:
            sr = None
            error = error

        if sr is not None:
            try:
                answer_json = sr.json()
            except Exception as error:
                answer_json = None
                error = error

            if answer_json is not None:
                return {
                    'status': True,
                    'data': answer_json
                }
            else:
                return {
                    'status': False,
                    'msg': error
                }
        else:
            return {
                'status': False,
                'msg': error
            }


    def new_invoice(self, payment):
        add_one_day = datetime.now(timezone.utc) + timedelta(days=1)
        add_one_day_text = add_one_day.strftime('%Y-%m-%dT%H:%M:%S')

        options = {
            'amount': {
                'currency': 'RUB',
                'value': f'{payment.cost}'
            },
            'expirationDateTime': f'{add_one_day_text}+00:00'
        }

        sr = self.r(url=f'{self.__url}{payment.id}', params=options, r_type='PUT')
        if sr['status']:
            return {
                'status': True,
                'data': sr['data']
            }
        else:
            return {
                'status': False,
                'msg': sr['msg']
            }