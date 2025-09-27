
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import FastAPIError, RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHttpException
import uvicorn

from api.v1.responses.error_responses import ErrorResponse, ValidationErrorResponse
from api.v1.responses.success_response import success_response
from api.v1.utils.storage import Base, engine
from api.v1.routes import version_one

app = FastAPI(title="E commerce API", redoc_url=None, summary="API for performing ecommerce like operation fully")

# Create all database tables
Base.metadata.create_all(engine)

# Setup CORS
origins = ["*"]

app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_methods=["*"],
        allow_headers=["*"]
        )


app.include_router(version_one)


# Setup Exception handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:

    errors = []
    for error in exc.errors():
        errors.append(
            {
                "field": error.get("loc")[-1],
                "message": error.get("msg")
            }
        )

    response = ValidationErrorResponse(errors=errors)
    return JSONResponse(content=response.model_dump(), status_code=status.HTTP_422_UNPROCESSABLE_CONTENT)


@app.exception_handler(StarletteHttpException)
async def starlette_http_handler(request: Request, exc: StarletteHttpException) -> JSONResponse:
    response: ErrorResponse = ErrorResponse(status_code=exc.status_code, message=exc.detail)
    return JSONResponse(content=response.model_dump(), status_code=exc.status_code)


@app.exception_handler(FastAPIError)
async def http_exception_handler(request: Request, exc: FastAPIError) -> JSONResponse:

    response: ErrorResponse = ErrorResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="Internal Server Error")

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=response.model_dump())



@app.get("/")
async def index() -> JSONResponse:
    return success_response("Welcome to e commerce api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
