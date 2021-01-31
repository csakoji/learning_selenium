import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common data', 'baseURL')

    @staticmethod
    def getUseremail():
        return config.get('common data', 'username')

    @staticmethod
    def getPassword():
        return config.get('common data', 'password')
