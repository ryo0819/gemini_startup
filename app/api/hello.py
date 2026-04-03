from fastapi import APIRouter
from app.schemas.hello import HelloRequest, HelloResponse

router: APIRouter = APIRouter()


@router.get("/", response_model=HelloResponse)
async def get_hello() -> HelloResponse:
    return HelloResponse(message="Hello World")


@router.post("/", response_model=HelloResponse)
async def post_hello(request: HelloRequest) -> HelloResponse:
    return HelloResponse(message=f"Hello World, {request.name}")
