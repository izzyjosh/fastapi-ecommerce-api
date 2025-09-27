from pydantic import BaseModel
from fastapi import status

class ValidationErrorResponse(BaseModel):
    status_code: int = status.HTTP_422_UNPROCESSABLE_CONTENT
    messag3: str = "Validation Error"
    errors: list 

class ErrorResponse(BaseModel):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str
