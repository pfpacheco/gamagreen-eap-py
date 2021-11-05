from json import loads

from flask import request, make_response
from flask_cors import cross_origin

from com.brookgreen.gama.exe.app import app
from com.brookgreen.gama.factory.login.login_service_factory import LoginServiceFactory


@app.context_processor
@app.route("/api/login/signon", methods=["POST"])
@cross_origin(app, origins=["*"])
def sign_on():
    if request.method != "POST":
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            if request.data is not None:
                data = loads(request.data)
                response = LoginServiceFactory.get_instance().sign_on(data=data)
                return make_response(response)
            else:
                return make_response({"code": 400, "status": "BAD_REQUEST"})
        except Exception as e:
            print("Error on endpoint SignOn operation >> {}".format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": e})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
