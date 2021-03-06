import logging

from structlog import wrap_logger
from structlog import PrintLogger #added by EC

logger = wrap_logger(logging.getLogger("case-stub"))

class Case_Stub:

    def __init__(self):
        self.case_fixed_response = None

    def get_case_stub(self):
        """Create the fixed case response as a Python dictionary object. This can then be converted to a json object later on."""
        case_fixed_response = {'state':'ACTIONABLE',
                               'id':'0337c579-ce9d-4357-a620-5e4c565cfac1',
                               'actionPlanId':'2cf85a97-8945-453b-a6e8-17668b44f93d',
                               'collectionInstrumentId':'d7f20945-97d4-48c3-9037-532de6dca8fc',
                               'partyId':None,
                               'sampleUnitId':'16cd8fad-b048-46ac-952c-52afc30b47de',
                               'iac':None,
                               'caseRef':'1000000000000002',
                               'createdBy':'SYSTEM',
                               'sampleUnitType':'H',
                               'createdDateTime':'2018-11-01T14:32:00.202Z',
                               'caseGroup': {'collectionExerciseId':'8f604e2c-2e80-421d-8222-8702105ce668',
                                             'id':'cb1f82d1-bc01-4f32-a290-1527df7d8cfc',
                                             'partyId':None,
                                             'sampleUnitRef':'OHS000002',
                                             'sampleUnitType':'H',
                                             'caseGroupStatus':'INPROGRESS'},
                               'responses':[],
                               'caseEvents':None}
        PrintLogger().info("Now returning the case fixed response: " + repr(case_fixed_response))
        return case_fixed_response


    def get_reponse_for_eq_stub(self):
        """Create the fixed response, to forward to EQ, as a Python dictionary object. This can then be converted to a json object later on."""
        fixed_response_for_eq =  {'client_ip': None,
                                  'event': 'Redirecting to eQ',
                                  'level': 'info',
                                  'service': 'respondent-home',
                                  'created_at': '2018-11-27T12:331543322028'}
        PrintLogger().info("Now returning the fixed response for EQ: " + repr(fixed_response_for_eq))
        return fixed_response_for_eq

