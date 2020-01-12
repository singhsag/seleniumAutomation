import logging
import utilities.custom_logger as cl
import time
from traceback import print_stack
import string
import random


class Util:
    log = cl.customLogger(logging.DEBUG)

    def sleep(self, sec, info=""):
        """

        :param sec: how many seconds you want to waot
        :param info: for what element or page are waiting
        :return: Nothing
        """
        try:
            if info is not None:
                time.sleep(sec)
        except InterruptedError:
            self.log.error("Exception Occured")
            print_stack()

    def getAlphaNumeric(self, length, types="letters"):
        """
        To generate a random chracters of strings
        :param length: length of the chracter string
        :param types: type of the string can be lower, uppper, mix, digits only
        :return: retuns a random chracters of strings
        """
        alpha_num = ''
        if types == 'lower':
            case = string.ascii_lowercase
        elif types == 'upper':
            case = string.ascii_uppercase
        elif types == 'digits':
            case = string.digits
        elif types == 'mex':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueCode(self, length=5):
        return self.getAlphaNumeric(length, 'mix')

    def verifyTextContains(self, actual_title, expected_title):
        if expected_title in actual_title:
            self.log.info(f'Expected title {expected_title} is in {actual_title}')
            return True
        else:
            self.log.error(f'Expected title {expected_title} is not in {actual_title}')
            return False

    def verifyTextMatch(self, actual_title, expected_title):
        if str(expected_title).lower() == str(actual_title).lower():
            self.log.info(f'Expected title {expected_title} matches {actual_title}')
            return True
        else:
            self.log.error(f'Expected title {expected_title} not matches {actual_title}')
            return False
