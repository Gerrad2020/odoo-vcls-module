from ETL import ETL
from abc import ABC, abstractmethod
from simple_salesforce import Salesforce
userSF = 'itsupport@voisinconsulting.com'
passwordSF = 'VCLS-2019'
token = '4sFAK8v7SiWBo2aYcRhFQbSn'
class ETL_SF(ETL):
    __instance = None
    @staticmethod
    def getInstance():
        if ETL_SF.__instance == None:
            ETL_SF()
        return ETL_SF.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if ETL_SF.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ETL_SF.__instance = self

    def getConnection(self):
        instance = Salesforce(password=passwordSF, username=userSF, security_token=token)
        print('Successful connection to Salesforce.')
        return instance