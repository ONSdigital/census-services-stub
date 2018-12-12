
import json
from uuid import uuid4


class Case_Stub:

    def __init__(self, case_id):
        self.case_fixed_response = None
        self.case_id = case_id

    def get_case_stub(self):

        case_fixed_response = {
            "state": "ACTIONABLE",
            "id": self.case_id,
            "actionPlanId": "22684ede-7d5f-4f53-9069-2398055c61b2",
            "collectionInstrumentId": "test",
            "partyId": None,
            "sampleUnitId": "test",
            "iac": None,
            "caseRef": "999999999",
            "createdBy": "SYSTEM",
            "sampleUnitType": "H",
            "createdDateTime": "2018-11-06T12:08:05.498Z",
            "caseGroup": {
                "collectionExerciseId": str(uuid4()),
                "id": "test",
                "partyId": None,
                "sampleUnitRef": "OHS000001",
                "sampleUnitType": "H",
                "caseGroupStatus": "INPROGRESS"
            },
            "responses": [],
            "caseEvents": None
        }

        case_json = json.dumps(case_fixed_response)

        return case_json

    def post_case_stub(self):

        case_fixed_response = {
            "state": "ACTIONABLE",
            "id": self.case_id,
            "actionPlanId": "22684ede-7d5f-4f53-9069-2398055c61b2",
            "collectionInstrumentId": "test",
            "partyId": None,
            "sampleUnitId": "134d94fa-bc39-44ba-8d08-4d39921a047b",
            "iac": None,
            "caseRef": "1000000000000001",
            "createdBy": "SYSTEM",
            "sampleUnitType": "H",
            "createdDateTime": "2018-11-06T12:08:05.498Z",
            "responses": [],
            "caseEvents": None
        }

        case_json = json.dumps(case_fixed_response)

        return case_json