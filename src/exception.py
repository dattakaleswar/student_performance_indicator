import sys #sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.


def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #Super is for calling from the parent class since excpetion we are taking from parent class
        self.error_message=error_message




