
from fastapi import APIRouter, Depends, HTTPException
from users_api.models.user import User
from users_api.schemas.users import UserResponse, UserCreate
from users_api.database import LocalSession, get_db

router = APIRouter()
@router.post('users/profile', response_model=UserResponse, status_code=201)
def create_profile(profile: UserCreate, db: LocalSession = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == profile.username).first()

    if existing_user:
        raise HTTPException(status_code=409, detail='Пользователь уже существует')

    user = User(**profile.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/users/profile', response_model=UserResponse)
def get_profile(id: int, db: LocalSession = Depends(get_db)):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user
