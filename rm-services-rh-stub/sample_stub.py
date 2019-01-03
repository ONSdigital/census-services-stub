import json

class Sample_Stub:

    def __init__(self, sampleid):
        self.sample_fixed_response = None
        self.sampleid = sampleid

    def get_sample_stub(self):

        sample_fixed_response = {
            "id": self.sampleid,
            "attributes": {
                "TLA": "OHS",
                "UPRN": "123456",
                "COUNTRY": "E",
                "LOCALITY": "Hampshire",
                "POSTCODE": "PO15 5RR",
                "REFERENCE": "000001",
                "TOWN_NAME": "Titchfield",
                "ADDRESS_LINE1": "FLAT 1A",
                "ADDRESS_LINE2": "THE HIGH STREET",
                "ORGANISATION_NAME": ""
            }}

        sample_json = json.dumps(sample_fixed_response)

        return sample_json