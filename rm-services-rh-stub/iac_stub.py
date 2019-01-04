import json
import logging
from uuid import uuid4

class Iac_Stub:

    def __init__(self, iac):
        self.iac_fixed_response = None
        self.iac = iac

    def get_iac_stub_for_all(self):
        new_case_id = str(uuid4())
        if (self.iac == 'vvvvvvvvvvvv') or (self.iac == 'wwwwwwwwwwww'):
            iac_fixed_response = {"caseId": new_case_id, "caseRef": "1000000000000001", "iac": self.iac, "active": True,
                          "questionSet": None, "lastUsedDateTime": 1542361992207}
        else:
            logging.info("The iac code is not a valid one. It needs to be either vvvvvvvvvvvv or wwwwwwwwwwww")

        iac_json = json.dumps(iac_fixed_response)

        return iac_json


    # def get_iac_stub_for_all(self):
    #     new_case_id = str(uuid4())
    #     iac_fixed_response = {"caseId": new_case_id, "caseRef": "1000000000000001", "iac": self.iac, "active": True,
    #                           "questionSet": None, "lastUsedDateTime": 1542361992207}
    #
    #     iac_json = json.dumps(iac_fixed_response)
    #
    #     return iac_json