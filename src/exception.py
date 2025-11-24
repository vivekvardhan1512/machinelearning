import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    """It gives Three outputs. We are interested in Third one (exc_tb) \n
    which talks about on which file name, line number and what is the error"""
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in Python script name [{0}], ' \
    'line number [{1}] and error message [{2}]'.format(file_name, exc_tb.tb_lineno,str(error)) 
    
    """In format we will call all the places holders that we mentioned (0,1,2) \n
    as 0 -> file_name, 1 -> Line Number and 2 -> Error message"""
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

    
    