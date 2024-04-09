from fastapi import HTTPException, status

class UserNotFoundException(HTTPException):
    def __init__(self, user_id: int):
        detail = f"User with ID {user_id} not found"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class EmailAlreadyExistsException(HTTPException):
    def __init__(self, email: str):
        detail = f"Email '{email}' already exists. Please sign up with a new email."
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class InvalidCredentialsException(HTTPException):
    def __init__(self):
        detail = "Invalid credentials"
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class PermissionDeniedException(HTTPException):
    def __init__(self, detail="Permission denied"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
