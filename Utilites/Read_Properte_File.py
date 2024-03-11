import configparser

config = configparser.RawConfigParser()
config.read(".\\Configeration\\config.ini")


class Read_Congig:

    @staticmethod
    def getApplicationURL():
        url = config.get('Common Info', 'baseURL')
        return url

    @staticmethod
    def windowProp():
        cap = config.get('common Info', 'cap')
        return cap


    # @staticmethod
    # def getUserName():
    #     userName = config.get('Common Info', 'userName')
    #     return userName