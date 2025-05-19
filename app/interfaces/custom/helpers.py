from app.interfaces.custom.response_model import ResponseModel

def success_response(message: str, data: any = None):
    return ResponseModel(success=True, message=message, data=data)

def error_response(message: str):
    return ResponseModel(success=False, message=message, data=None)