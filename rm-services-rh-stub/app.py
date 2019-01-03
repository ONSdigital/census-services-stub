from flask import Flask
from flask import Response
from sample_stub import Sample_Stub
from collex_stub import Collex_Stub
from collex_instr_stub import Collex_Instr_Stub
from case_stub import Case_Stub
from iac_stub import Iac_Stub

import logging
app = Flask(__name__)

#override the default logging configuration so that info messages get output

logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello():
    return "Hello from the RM services stub for RH"

""" Route handler to deal with getting sample attributes from the sample service. 
The sampleid could be any sampleid that is passed in """

@app.route('/samples/<sampleid>/attributes')
def get_sample_attributes(sampleid):
    my_sample_stub = Sample_Stub(sampleid)
    json_data = Sample_Stub.get_sample_stub(my_sample_stub)
    logging.info('Retrieved sample attributes for sampleid ' + str(sampleid))

    return Response(json_data, mimetype='application/json')


""" Route handler to deal with getting collection exercise details from the collection exercise service. 
The collexid could be any collexid that is passed in """

@app.route('/collectionexercises/<collexid>')
def get_collex_details(collexid):
    my_collex_stub = Collex_Stub(collexid)
    json_data = Collex_Stub.get_collex_stub(my_collex_stub)
    logging.info('Retrieved details for collection exercise :  ' + str(collexid))

    return Response(json_data, mimetype='application/json')


""" Route handler to deal with getting collection exercise event details from the collection exercise service. 
The collexid could be any collexid that is passed in """


@app.route('/collectionexercises/<collexid>/events')
def get_collex_events(collexid):
    my_collex_stub = Collex_Stub(collexid)
    json_data = Collex_Stub.get_collex_events_stub(my_collex_stub)
    logging.info('Retrieved events for  collection exercise : ' + str(collexid))

    return Response(json_data, mimetype='application/json')


""" Route handler to deal with getting collection instruemnt  details from the collection instrument service. 
The collexinstrid could be any collexinstrid that is passed in """

@app.route('/collection-instrument-api/<version>/collectioninstrument/id/<collexinstrid>')
def get_collex_instr_details(version, collexinstrid):
    my_collex_instr_stub = Collex_Instr_Stub(collexinstrid)
    json_data = Collex_Instr_Stub.get_collex_instr_stub(my_collex_instr_stub)
    logging.info('Retrieved details for  collection instrument : ' + str(collexinstrid))

    return Response(json_data, mimetype='application/json')

""" Route handler to deal with getting caseid  details from the case service. 
The caseid could be any caseid that is passed in """

@app.route('/cases/<caseid>')
def getcasedetails(caseid):
    my_case_stub = Case_Stub(caseid)
    data = Case_Stub.get_case_stub(my_case_stub)

    return Response(data, mimetype='application/json')


@app.route('/cases/<caseid>/events', methods = ['POST'])
def postcaseevent(caseid):
    my_case_stub = Case_Stub(caseid)
    data = Case_Stub.post_case_stub(my_case_stub)


    return Response(data, mimetype='application/json')

""" Route handler to deal with getting details from the iac service. 
The iaccode could be any iaccode that is passed in """

@app.route('/iacs/<iaccode>')
def get_case_details_from_iac(iaccode):
    my_iac_stub = Iac_Stub(iaccode)
    data = Iac_Stub.get_iac_stub_for_all(my_iac_stub)

    return Response(data, mimetype='application/json')


if __name__=='__main__':
    app.run(host='localhost', port=8125)

