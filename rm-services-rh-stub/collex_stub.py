import json

class Collex_Stub:

    def __init__(self, collexid):
        self.collex_fixed_response = None
        self.collexid = collexid


    def get_collex_stub(self):

        collex_fixed_response = {
            "id": self.collexid,
            "surveyId": "test",
            "name": None,
            "actualExecutionDateTime": "2018-11-06T12:08:01.744Z",
            "scheduledExecutionDateTime": "2018-07-23T00:00:00.000Z",
            "scheduledStartDateTime": "2018-07-23T00:00:00.000Z",
            "actualPublishDateTime": None,
            "periodStartDateTime": "2018-07-23T00:00:00.000Z",
            "periodEndDateTime": "2020-07-31T00:00:00.000Z",
            "scheduledReturnDateTime": "2018-08-04T00:00:00.000Z",
            "scheduledEndDateTime": "2020-07-31T00:00:00.000Z",
            "executedBy": None,
            "state": "LIVE",
            "caseTypes": [{
                "actionPlanId": "test",  #not needed for payload
                "sampleUnitType": "A"    #not needed for payload
            }],
            "exerciseRef": "9999",       #period_id in payload
            "userDescription": "Test 1",
            "created": "2018-11-06T12:01:35.226Z",
            "updated": "2018-11-06T12:08:03.379Z",
            "deleted": None,
            "validationErrors": None,
            "events": [{
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "mps",
                "timestamp": "test"
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "go_live",
                "timestamp": "test"

            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "return_by",
                "timestamp": "test"
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "exercise_end",
                "timestamp": "test"
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "ref_period_start",
                "timestamp": "test"
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "ref_period_end",
                "timestamp": "test"
            }]
        }

        collex_json = json.dumps(collex_fixed_response)

        return collex_json


    def get_collex_events_stub(self):

        collex_events_fixed_response = [{
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "mps",
                "timestamp": "test"
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "go_live",
                "timestamp": "test"
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "return_by",
                "timestamp": "2018-10-04T00:00:00.000Z"  #used in payload
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "exercise_end",
                "timestamp": "2020-07-31T00:00:00.000Z" #used in payload
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "ref_period_start",
                "timestamp": "2018-07-24T00:00:00.000Z" #used in payload
            }, {
                "id": "test",
                "collectionExerciseId": "test",
                "tag": "ref_period_end",
                "timestamp": "2018-08-04T00:00:00.000Z"   #used in payload
            }]
        collex_events_json = json.dumps(collex_events_fixed_response)

        return collex_events_json