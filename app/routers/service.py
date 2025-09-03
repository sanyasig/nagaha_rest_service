from fastapi import APIRouter

from app.nagaha_services.movieRulz import get_telugu_titles
from app.nagaha_services.notification import send_ntfy_message
from app.nagaha_services.realtime_trains import get_next_train_status

router = APIRouter()

@router.get("/callservice/{service_name}", tags=["service"])
async def read_user(service_name: str):
    response = ""

    if service_name == 'telugu_movies':
        titles = get_telugu_titles()
        response = "\n  - ".join(titles)
        send_ntfy_message(response, title='New Movies on Movie Rulz')

    if service_name == 'train-status':
        next_trains = get_next_train_status('KNS', 'GLC') 
        response = "\n  - ".join([str(x) for x in next_trains]) 
        send_ntfy_message(response, title='next train for Kennishead')  
    return {"called Service ": f'{service_name}', 
            'response': response}

