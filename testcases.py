'''
Created on Sep 18, 2018

@author: Ji Li
'''
import requests
class testcases():
    
    """constructor"""
    def __init__(self, url):
        self.url = url
    
    """
    ##########################################
    negative payment method test cases
    ##########################################
    """
    
    def test_payment_method(self):
        bankCountryCode = 'US'
        accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = 'ICBCUSBJ'
        bsb = ''
        aba = '11122233A'
        
        """payment method is blank"""
        testCaseName = "payment method is blank"
        response = self.call_endpoint("", bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'payment_method' field required, the value should be either 'LOCAL' or 'SWIFT'")
        
        """payment method is not required word"""
        testCaseName = "payment method is not required word"
        response = self.call_endpoint("aaa", bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'payment_method' field required, the value should be either 'LOCAL' or 'SWIFT'")
          
    
    """
    ##########################################
    negative bank country code test cases
    ##########################################
    """
    
    def test_bank_country_code(self):
        
        paymentMethod = 'SWIFT'
        accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = 'ICBCUSBJ'
        bsb = ''
        aba = '11122233A'
        
        """bank country code is blank"""
        testCaseName = "payment method is blank"
        response = self.call_endpoint(paymentMethod, "", accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'bank_country_code' is required, and should be one of 'US', 'AU', or 'CN'")
        
        """bank country code is not required word"""
        testCaseName = "payment method is not required word"
        response = self.call_endpoint(paymentMethod, 'aaa', accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'bank_country_code' is required, and should be one of 'US', 'AU', or 'CN'")
         
    """
    ##########################################
    negative account name test cases
    ##########################################
    """
    
    def test_account_name(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        #accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = 'ICBCUSBJ'
        bsb =''
        aba = '11122233A'
        
        """account name less than 2"""
        testCaseName = "account name less than 2"
        response = self.call_endpoint(paymentMethod, bankCountryCode, "a", accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of account_name should be between 2 and 10")
        
        """account name more than 10"""
        testCaseName = "account name more than 10"
        response = self.call_endpoint(paymentMethod, bankCountryCode, '12345678901', accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of account_name should be between 2 and 10")
         
         
    
    """
    ##########################################
    negative account number test cases
    ##########################################
    """
    
    def test_account_number(self):
        
        paymentMethod = 'SWIFT'
        #bankCountryCode = 'US'
        accountName = 'John Smith'
        #accountNum = '123456789'
        swiftCode = 'ICBCUSBJ'
        bsb =''
        aba = '11122233A'
        
        """account number is blank"""
        testCaseName = "account number is blank"
        response = self.call_endpoint(paymentMethod, 'US', accountName, "", swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'account_number' is required")
        
        
        """US account number less than 1"""
        testCaseName = "US account number less than 1"
        response = self.call_endpoint(paymentMethod, 'US', accountName, "", swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'account_number' is required")
        
        """US account number more than 17"""
        testCaseName = "US account number more than 17"
        response = self.call_endpoint(paymentMethod, 'US', accountName, '123456789012345678', swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of account_number should be between 1 and 17 when bank_country_code is 'US'")
         
    
        """AU account number less than 6"""
        bsb = 'XXXYYY'
        swiftCode = 'ICBCAUBJ'
        testCaseName = "AU account number less than 6"
        response = self.call_endpoint(paymentMethod, 'AU', accountName, "12345", swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'account_number' is required")
        
        """AU account number more than 9"""
        testCaseName = "AU account number more than 9"
        response = self.call_endpoint(paymentMethod, 'AU', accountName, '1234567890', swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of account_number should be between 1 and 17 when bank_country_code is 'US'")
         
        """CN account number less than 8"""
        bsb =''
        swiftCode = 'ICBCCNBJ'
        testCaseName = "CN account number less than 8"
        response = self.call_endpoint(paymentMethod, 'CN', accountName, "1234567", swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'account_number' is required")
        
        """CN account number more than 20"""
        testCaseName = "CN account number more than 20"
        response = self.call_endpoint(paymentMethod, 'CN', accountName, '1234567890123456789', swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of account_number should be between 1 and 17 when bank_country_code is 'US'")
         
        

    """
    ##########################################
    negative swift_code test cases
    ##########################################
    """
    
    def test_swift_code(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = 'ICBCUSBJ'
        bsb = ''
        aba = '11122233A'
        
        """when payment method = SWIFT, swift_code = blank"""
        testCaseName = "when payment method = SWIFT, swift_code = blank"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, '', bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'swift_code' is required when payment method is 'SWIFT'")
        
        """when swift code doesn't match bank country code"""
        testCaseName = "when swift code does not match bank country code"
        response = self.call_endpoint(paymentMethod, 'CN', accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "The swift code is not valid for the given bank country code: CN")
     
             
        """swift code is less than 8"""
        testCaseName = "swift code length is less than 8"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, "ICBCUSB", bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of 'swift_code' should be either 8 or 11")
           
        """swift code is more than 11"""
        testCaseName = "swift code length is more than 11"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, "ICBCUSBJJJJJ", bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of 'swift_code' should be either 8 or 11") 
        
        """swift code is between 8 and 11"""
        testCaseName = "swift code length is between 8 and 11"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, "ICBCUSBJJ", bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of 'swift_code' should be either 8 or 11")    
       
    
    """
    ##########################################
    negative bsb test cases
    ##########################################
    """
    
    def test_bsb(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'AU'
        accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = 'ICBCAUBJ'
        bsb =''
        aba = '11122233A'
        
        """when bank country=AU but bsb= blank"""
        testCaseName = "when bank country=AU but bsb= blank"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "'bsb' is required when bank country code is 'AU'")

        """when bsb length is not 6"""
        bsb = 'XXXYY'
        testCaseName = "when bsb length is not 6"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.nagative_response_verification(testCaseName, response, "Length of 'bsb' should be 6")
        
    """
    ##########################################
    negative aba test cases
    ##########################################
    """
    
    def test_aba(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = 'ICBCUSBJ'
        bsb =''

        
        """when bank country= US but aba=blank"""
        testCaseName = "when bank country= US but aba=blank"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,'')
        self.nagative_response_verification(testCaseName, response, "when bank country= US but aba=blank")
    
        """aba is not 9"""
        testCaseName = "aba length is not 9"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,'123')
        print response
        self.nagative_response_verification(testCaseName, response, "Length of 'aba' should be 9")

    """
    ##########################################
    positive test cases
    ##########################################
    """
    def test_special_characters(self):
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = '!@!#@!#!@$'
        accountNum = '!@$#$$#%*$#%&#'
        swiftCode = '#$%^US&*'
        bsb = ''
        aba = '!@#$%^&*('
        
        testCaseName = "special characters"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.postive_response_verification(testCaseName, response)
        
    def test_swift_code_length_8_11(self):
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = 'John Smith'
        accountNum = '123456789'
        swiftCode = ['ICBCUSBJ','ICBCUSBJJJJ']
        bsb = ''
        aba = '11122233A'
        
        """swift code length is 8 or 11"""
        testCaseName = "swift code length is 8 or 11"
        for sc in swiftCode:
            response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, sc, bsb,aba)
            self.postive_response_verification(testCaseName + " swift code is " + sc, response)
        
    
    def test_payment_method_country_code_combinations(self):

        paymentMethod = ['SWIFT','LOCAL']
        bankCountryCode = ['US','AU','CN']
        accountName = 'John Smith'
        accountNum = '123456789'
        aba = '11122233A'
        
        """payment method and country code combination"""
        testCaseName = "payment method and country code combination"
        for pm in paymentMethod:

            for bcc in bankCountryCode:
                if pm == 'SWIFT':
                    swiftCode = self.build_swift_code(bcc)
                else:
                    swiftCode =''
                if bcc == 'AU':
                    bsb = 'XXXYYY'
                else:
                    bsb =''
                response = self.call_endpoint(pm, bcc, accountName, accountNum, swiftCode, bsb,aba)
                self.postive_response_verification(testCaseName +" " + pm + " " + bcc + " " + swiftCode, response)

    def test_aba_blank(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'CN'
        accountName = 'John Smith'
        accountNum = '123456789'
        bsb = ''
        swiftCode = 'ICBCCNBJ'
  
        testCaseName = "aba=blank when country code <> US"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,'')
        self.postive_response_verification(testCaseName, response)

    def test_aba_length_9(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'CN'
        accountName = 'John Smith'
        accountNum = '123456789'
        bsb = ''
        swiftCode = 'ICBCCNBJ'
        aba = '11122233A'
  
        testCaseName = "aba length is 9"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.postive_response_verification(testCaseName, response)

    def test_bsb_blank(self):
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = 'John Smith'
        accountNum = '123456789'
        bsb = ''
        swiftCode = 'ICBCUSBJ'
        aba = '11122233A'
  
        testCaseName = "bsb=blank when country code <>AU"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.postive_response_verification(testCaseName, response)

    def test_bsb_length_6(self):
        paymentMethod = 'SWIFT'
        bankCountryCode = 'AU'
        accountName = 'John Smith'
        accountNum = '123456789'
        bsb = 'XXXYYY'
        swiftCode = 'ICBCAUBJ'
        aba = '11122233A'
  
        testCaseName = "bsb length is 6"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.postive_response_verification(testCaseName, response)
        
        
    def test_low_boundary_combination_touch(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = 'Jo'
        accountNum = '1'
        swiftCode = 'ICBCUSBJ'
        bsb =''
        aba = '11122233A'
  
        testCaseName = "low boundary touch"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.postive_response_verification(testCaseName, response)

    def test_upper_boundary_combination_touch(self):
        
        paymentMethod = 'SWIFT'
        bankCountryCode = 'US'
        accountName = 'ABCDEFGHJH'
        accountNum = '12345678901234567'
        swiftCode = 'ICBCUSBJJJ'
        bsb =''
        aba = '11122233A'
  
        testCaseName = "upper boundary touch"
        response = self.call_endpoint(paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba)
        self.postive_response_verification(testCaseName, response)

    def test_all_account_name_length(self):
        
        paymentMethod = 'LOCAL'
        bankCountryCode = ['US','AU','CN']
        accountName = 'John Smith'
        accountNums = {"US":"1|12345678901234567","AU":"123456|123456789","CN":"12345678|12345678901234567890"}
        swiftCode = ''
        aba = '11122233A'
  
        testCaseName = "all_account_name_length"
        for bcc in bankCountryCode:
            if bcc =='AU':
                bsb = 'XXXYYY'
            else:
                bsb = ''
            accountNumList = accountNums[bcc].split('|')
            for accountNum in accountNumList:
                response = self.call_endpoint(paymentMethod, bcc, accountName, accountNum, swiftCode, bsb,aba)
                self.postive_response_verification('{} country code-{},account number-{}'.format(testCaseName,bcc,accountNum), response)
    
    
    def call_endpoint(self,paymentMethod, bankCountryCode, accountName, accountNum, swiftCode, bsb,aba):
        payload = {
            "payment_method": paymentMethod,
            "bank_country_code": bankCountryCode,
            "account_name": accountName,
            "account_number": accountNum,
            "swift_code": swiftCode,
            "bsb":bsb,
            "aba": aba
            }
    
        response = requests.post(self.url, json=payload)
        return response
    
    def nagative_response_verification(self,testCaseName,response,expectedErrorMessage):
        testCaseName = "'" + testCaseName + "'"

        
        actualErrorCode = response.status_code
        
        if str(actualErrorCode) == '400':
            print "{} test case 1 PASSED! Received 400 error.".format(testCaseName)
        else:
            print "{} test case 1 ***FAILED***! Expected 400 error, but received {} error.".format(testCaseName,actualErrorCode)
        
        try:
            actualErrorMessage = response.json()['error']
            if actualErrorMessage == expectedErrorMessage:
                print "{} test case 2 PASSED! Received the expected error message.".format(testCaseName)
            else:
                print "{} test case 2 ***FAILED***! The actual error message received was {}".format(testCaseName,actualErrorMessage)
        except:
            print "{} test case 2 ***FAILED***! Did not received any error message".format(testCaseName)
        
    def postive_response_verification(self,testCaseName,response):
        testCaseName = "'Positive case:" + testCaseName + "'"
        
        actualCode = response.status_code

        
        if str(actualCode) == '200':
            print "{} PASSED! Processed successfully.".format(testCaseName)
        else:
            print "{}  ***FAILED***! Received {} error. Error message-{}".format(testCaseName,actualCode,response.text)
        
    def build_swift_code(self,countryCode):
        return 'ICBK'+ countryCode + 'BJ'
    




        

if __name__ == '__main__':
    from testcases import testcases
    import sys
    try:
        t = testcases(sys.argv[1])
    except IndexError:
        t = testcases("http://preview.airwallex.com:30001/bank")
    print "###################################################"
    print "           Negative Tests                          "
    print "####################################################"
    t.test_payment_method()
    t.test_bank_country_code()
    t.test_account_name()
    t.test_account_number()
    t.test_swift_code()
    t.test_bsb()
    t.test_aba()
    print "###################################################"
    print "           Positive Tests                          "
    print "####################################################"
    t.test_special_characters()
    t.test_payment_method_country_code_combinations()
    t.test_swift_code_length_8_11()
    t.test_aba_blank()
    t.test_aba_length_9()
    t.test_bsb_blank()
    t.test_bsb_length_6()
    t.test_low_boundary_combination_touch()
    t.test_upper_boundary_combination_touch()
    t.test_all_account_name_length()
    
