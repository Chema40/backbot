from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    contact_method_url: str = "https://6759cb2b099e3090dbe2f3c6.mockapi.io/channel/mail/contact_method"

    class Config:
        env_file = ".env"

settings = Settings()