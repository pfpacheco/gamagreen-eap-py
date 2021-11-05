from json import loads

from flask import request, make_response
from flask_cors import cross_origin

from com.brookgreen.gama.exe.app import app
from com.brookgreen.gama.factory.recover.recover_password_factory import RecoverPasswordFactory


@app.context_processor
@app.route("/api/recover/password", methods=["POST"])
@cross_origin(app, origins=["*"])
def recover_password():
    if request.method != "POST":
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            if request.data is not None:
                data = loads(request.data)
                response = RecoverPasswordFactory.get_instance().recover_password(data=data)
                return make_response(response)
            else:
                return make_response({"code": 400, "status": "BAD_REQUEST"})
        except Exception as e:
            print("Error on endpoint RecoverPassword operation >> {}".format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": e})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)
