import json


class Collex_Instr_Stub:

    def __init__(self, collex_instr_id):
        self.collex_instr_id_fixed_response = None
        self.collex_instr_id = collex_instr_id

    def get_collex_instr_stub(self):

        collex_instr_id_fixed_response = {
            "businesses": [],
            "classifiers": {
                "collection_exercise": "test",
                "eq_id": "lms",
                "form_type": "2"
            },
            "exercises": ["test"],
            "file_name": "2",
            "id": "test",
            "len": None,
            "stamp": "Tue, 06 Nov 2018 12:06:16 GMT",
            "survey": "test",
            "type": "EQ"
        }

        collex_instr_json = json.dumps(collex_instr_id_fixed_response)

        return collex_instr_json
