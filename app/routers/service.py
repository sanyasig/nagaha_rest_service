from fastapi import APIRouter

from app.nagaha_services.movieRulz import get_telugu_titles
from app.nagaha_services.notification import send_ntfy_message

router = APIRouter()

@router.get("/callservice/{service_name}", tags=["service"])
async def read_user(service_name: str):
    titles = get_telugu_titles()
    send_ntfy_message("\n  - ".join(titles), title='New Movies on Movie Rulz')

    return {"response": f'Calling Service {service_name}'}

