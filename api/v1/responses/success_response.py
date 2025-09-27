from typing import Optional
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def success_response( message: str, status_code: int = status.HTTP_200_OK, data: Optional[dict] = None) -> JSONResponse:

    response = {
            "status_code": status_code,
            "message": message
    }

    if data is not None:
        response["data"] = data

    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))

