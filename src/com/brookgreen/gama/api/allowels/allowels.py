from json import loads

from flask import request, make_response
from flask_cors import cross_origin

from com.brookgreen.gama.exe.app import app
from com.brookgreen.gama.factory.allowels.allowels_service_factory import AllowelsServiceFactory


@app.context_processor
@app.route("/api/allowels/get_list", methods=["GET"])
@cross_origin(app, origins=["*"])
def get_list():
    if request.method != "GET":
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            """ Call the service factory from here """
            response = AllowelsServiceFactory.get_instance().get_list()
            return make_response(response)
        except Exception as e:
            print('Error on endpoint GetApprovals operation >> {}'.format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": e})


@app.context_processor
@app.route("/api/allowels/set_action", methods=["POST"])
@cross_origin(app, origins=["*"])
def set_action():
    if request.method != "POST":
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            if request.data is not None:
                data = loads(request.data)
                if data["action"] == "approve":
                    """ Call the service factory from here """
                    response = AllowelsServiceFactory.get_instance().set_approved(data=data["users"])
                    return make_response(response)
                elif data["action"] == "reprove":
                    """ Call the service factory from here """
                    response = AllowelsServiceFactory.get_instance().set_reproved(data=data["users"])
                    return make_response(response)
        except Exception as e:
            print("Error on endpoint GetApprovals operation >> {}".format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": e})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8084, debug=True)
