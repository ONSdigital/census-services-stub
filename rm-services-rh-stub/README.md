#RM Services RH Stub

This application can be run to mimic the calls to the RM services by Census Respondent Home. By running the application there will be no need to spin up all of the RM services. The application is a Flask app so this needs to be installed before the application can be run. (pip install Flask==0.10.1). 


The services are configured to run on the port specified in app.py (currently set to 8125). The services stubbed are CASE, COLLECTION INSTRUMENT, COLLECTION EXERCISE, IAC and SAMPLE.

Census Respondent Home is currently set to use defaults for service ports if none are specified. In order to ensure the stub is used the environment variables for Census Respondent Home need to be configured. This can be done as follows in pycharm.

Run -> Edit Configurations -> Run -> Environment Variables

and add the following
 
NAME						VALUE
* COLLECTION_INSTRUMENT_URL 	http://localhost:8125
* SAMPLE_URL					http://localhost:8125
* COLLECTION_EXERCISE_URL		http://localhost:8125
* CASE_URL						http://localhost:8125
* IAC_URL						http://localhost:8125

##Services and Calls handled by the stub
The following route handlers are implemented in the stub application.

GET /samples/{id}/attributes

GET /collectionexercises/{id}

GET /collectionexercises/{id}/events

GET /collection-instrument-api/{version}/collectioninstrument/id/{id}	

GET /cases/{caseId}

POST /cases/{caseId}/events

GET /iacs/{iac}



