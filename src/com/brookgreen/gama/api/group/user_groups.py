from json import loads

from flask import request, make_response
from flask_cors import cross_origin

from com.brookgreen.gama.exe.app import app
from com.brookgreen.gama.factory.group.user_groups_service_factory import UserGroupsServiceFactory


@app.context_processor
@app.route("/api/groups/get_list", methods=["GET"])
@cross_origin(app, origins=["*"])
def get_list():
    if request.method != "GET":
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            """ Call the service factory from here """
            response = UserGroupsServiceFactory.get_instance().get_list()
            return make_response(response)
        except Exception as e:
            print('Error on endpoint Get Users Group operation >> {}'.format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": "{}".format(e)})


@app.context_processor
@app.route("/api/groups/set_user_group", methods=["POST"])
@cross_origin(app, origins=["*"])
def set_group():
    if request.method != "POST":
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            if request.data is not None:
                data = loads(request.data)
                if data:
                    """ Call the service factory from here """
                    response = UserGroupsServiceFactory.get_instance().set_group(data=data["users"])
                    return make_response(response)
        except Exception as e:
            print("Error on endpoint Set Users Group >> {}".format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": "{}".format(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085, debug=True)
