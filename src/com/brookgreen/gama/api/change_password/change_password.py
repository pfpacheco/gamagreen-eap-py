from json import loads

from flask import request, make_response
from flask_cors import cross_origin

from com.brookgreen.gama.exe.app import app
from com.brookgreen.gama.factory.change_password.change_password_service_factory \
    import ChangePasswordServiceFactory


@app.context_processor
@app.route("/api/change-password/change", methods=["POST"])
@cross_origin(app, origins=["*"])
def change():
    if request.method != 'POST':
        return make_response({"code": 405, "status": "METHOD_NOT_ALLOWED"})
    else:
        try:
            if request.data is not None:
                data = loads(request.data)
                ''' Coding the call for factory '''
                response = ChangePasswordServiceFactory.get_instance().change(kwargs=data)
                return make_response(response)
            else:
                return make_response({"code": 400, "status": "BAD_REQUEST"})
        except Exception as e:
            print('Error on endpoint ChangePassword operation >> {}'.format(e))
            return make_response({"code": 500, "status": "INTERNAL_SERVER_ERROR", "message": e})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8083')
