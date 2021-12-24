from api_folder.API_key import ApiData


class Api:
    server = 'http://172.17.128.22/api/v4'  # хост вашего API

    class Endpoint:
        login = '/auth/login/'
        logout = '/auth/logout'
        admins_folder = f'/folders/{ApiData.folderID_admins}/passwords'
        users_folder = f'/folders/{ApiData.folderID_users}/passwords'
        securities_folder = f'/folders/{ApiData.folderID_security}/passwords'
        passwords = '/passwords'
