
from fastapi import FastAPI

from users_api.routers.user import router as user_router
app = FastAPI()

app.include_router(user_router)





@app.get('/healthz')
def health_check():                         # проверка сервера
    return {'status': 'ok'}

