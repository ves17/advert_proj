from fastapi import HTTPException, status
class BookingException(HTTPException): # <-- наследуемся от HTTPException,

    status_code = 500 # <-- задаем значения по умолчанию
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
class UserAlreadyExistsException(BookingException): # <-- обязательно

    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"