import azure.functions as func
import logging
from urllib import request


def recommend_article(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    userID = req.params.get('userID')
    if not userID:
        return func.HttpResponse("[ERROR] : User ID not provided !")
    else:
        request_url = 'http://SekelMadness.pythonanywhere.com/get_recommendation/{}'.format(userID)
        req = request.Request(request_url, method="POST")
        r = request.urlopen(req)
        content = r.read().decode()

        return func.HttpResponse(content)
    