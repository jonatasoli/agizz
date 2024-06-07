from fastapi import APIRouter, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
main = APIRouter()


def create_app():
    app = FastAPI()
    origins = [
        'localhost',
    ]
    app.include_router(
        main,
        responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return app


@main.get('/', status_code=200)
def read_root() -> dict:
    """Test route."""
    return {'message': 'Hello Template'}
