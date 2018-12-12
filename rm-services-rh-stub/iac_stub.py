import logging
import json
from uuid import uuid4


from structlog import PrintLogger  # added by EC
from structlog import wrap_logger

logger = wrap_logger(logging.getLogger("iac-stub"))

class Iac_Stub:

    def __init__(self, iac):
        self.iac_fixed_response = None
        self.iac = iac

    def get_iac_stub(self):
        PrintLogger().info("Now in the get_iac_stub function")
        iac_fixed_response = {"caseId": "71adfc12-8853-4bb4-92c5-d441095aca16", "caseRef": "1000000000000001", "iac": "4lnfbdf9djx9", "active": True, "questionSet": None, "lastUsedDateTime": 1542361992207}

        PrintLogger().info("Now returning the iac fixed response: " + repr(iac_fixed_response))
        iac_json = json.dumps(iac_fixed_response)

        return iac_json

    def get_iac_stub_for_all(self):
        PrintLogger().info("Now in the get_iac_stub for all function")
        new_case_id = str(uuid4())
        #iac_fixed_response = {"caseId": "99999999999", "caseRef": "1", "iac": self.dummy, "active": True, "questionSet": None, "lastUsedDateTime": 1542361992207}

        iac_fixed_response = {"caseId": new_case_id, "caseRef": "1000000000000001", "iac": self.iac, "active": True,
                              "questionSet": None, "lastUsedDateTime": 1542361992207}

        PrintLogger().info("Now returning the iac fixed for all response: " + repr(iac_fixed_response))
        iac_json = json.dumps(iac_fixed_response)

        return iac_json