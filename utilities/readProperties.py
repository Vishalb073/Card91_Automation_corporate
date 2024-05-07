import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getusermail():
        email = config.get('common info', 'phone')
        return email

    @staticmethod
    def getuserpassword():
        password = config.get('common info', 'otp')
        return password

    @staticmethod
    def getComapny_name():
         companyname = config.get('common info', 'Comapny_name')
         return companyname

    @staticmethod
    def getBuisnesstype():
        buisnesstype =config.get('common info', 'Comapny_name')
        return buisnesstype

    @staticmethod
    def  getlogo():
        logo = config.get('common info', 'Logo')
        return logo

    @staticmethod
    def getsecuritynum():
        securitynumber=  config.get('common info', 'Security_num')
        return securitynumber

    @staticmethod
    def getsecurityamount():
        securityamount = config.get('common info', 'Security_amt')
        return securityamount

    @staticmethod
    def getaddress():
        addresss = config.get('common info' , 'address')
        return addresss

    @staticmethod
    def getaddress2():
        address1 = config.get('common info' , 'address2')
        return address1

    @staticmethod
    def getcity():
        lcity = config.get('common info' , 'city')
        return lcity

    @staticmethod
    def getstate():
        states = config.get('common info' , 'state')
        return states

    @staticmethod
    def getpin():
        pin =  config.get('common info' , 'pincode')
        return pin

    @staticmethod
    def getadmin():
        adminname = config.get('common info' , 'Admin')
        return adminname

    @staticmethod
    def geturl():
        url = config.get('ccms info','base_Url')
        return url

    @staticmethod
    def getph():
        ph = config.get('ccms info','phone_nu')
        return ph

