import requests


class ReqresException(Exception):
    pass


class ReqresClient(object):
    def __init__(self):
        self.base_url = 'https://reqres.in/api'

    def get_user(self, user_id):
        url = f'{self.base_url}/users/{user_id}'
        return self.request(url, method='GET')

    def get_users(self, page):
        url = f'{self.base_url}/users'
        params = {'page': page}
        return self.request(url, method='GET', params=params)

    def create_user(self, name, job):
        url = f'{self.base_url}/users'
        json = {'name': name, 'job': job}
        return self.request(url, method='POST', json=json)

    def update_user(self, user_id, name, job):
        url = f'{self.base_url}/users/{user_id}'
        json = {'name': name, 'job': job}
        return self.request(url, method='PUT', json=json)

    def delete_user(self, user_id):
        url = f'{self.base_url}/users/{user_id}'
        return self.request(url, method='DELETE')

    def request(self, url, method, headers=None, params=None, json=None, timeout=30.0):
        try:
            response = requests.request(
                url=url,
                method=method,
                headers=headers,
                params=params,
                json=json,
                timeout=timeout)
            print(f'{method}: {response.url}')
            print(response.status_code)
            return response
        except requests.exceptions.RequestException:
            raise ReqresException('RequestException')
