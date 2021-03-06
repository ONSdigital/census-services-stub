import logging
import time

from structlog import wrap_logger
from structlog import PrintLogger

logger = wrap_logger(logging.getLogger("iac-stub"))

class Iac_Stub:

    def __init__(self):
        self.iac_fixed_response = None

    def get_iac_stub(self):
        PrintLogger().info("Now in the get_iac_stub function")
        time_in_UTC = time.time() + time.timezone
        time_UTC_millis = round(time_in_UTC * 1000)
        iac_fixed_response = {'caseId':'0337c579-ce9d-4357-a620-5e4c565cfac1',
                              'caseRef':'1000000000000002',
                              'iac':'b4t7g3xby5bx',
                              'active':True,
                              'questionSet':None,
                              'lastUsedDateTime':time_UTC_millis}
        PrintLogger().info("Now returning the iac fixed response: " + repr(iac_fixed_response))
        return iac_fixed_response