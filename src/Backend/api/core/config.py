from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = 'MITRE - API'
    API_V1_STR: str = '/api/v1'
    API_AGENT_SERVER_STR: str = '/api/agent_server'

    # Database Settings
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_NAME: str = 'db_417'
    USER: str = 'user_417'
    PASSWORD: str = '5KaAme3BT1dHAOimu9lFF05ceR4Bx9fjHB2mbWtbXQDVIaYt0C3KWOqOIHdRzGS55sJ1RLg5evoMscapQeGJwGLodlUz7yTIICMPqEtQdkbHjTfkQmftrWHuI9M93jUp'
    SQLALCHEMY_DATABASE_URI: str = f'postgresql://{USER}:{PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # JWT Settings
    SECRET_KEY: str = '26mpViW3rldpRIrlqhPlzXSqbMscYMd8MCJHk6ipxus3YzAGXPS2PGQl2FqjDEyxH5OAHmFEAThkyGXJYetG1iY0byF32Slc6Tv3AHRtStHWec9UwK9HdSHQL2V0c5w94GzcAxlqg9udRcZ3tMwlLdMF63BZefU0TCYHBbmksI8vXIUXqc9LbxigEXpGG5GQjd009DxVGAEXU40yMJdCgX3mkJjDBtl4XM0Sa29HfWhdk8fL6I6Jdk5w5Krbd3Ie'
    TOKEN_LOCATION: set = {'cookies'}
    CSRF_PROTECT: bool = False
    COOKIE_SECURE: bool = False  # should be True in production
    COOKIE_SAMESITE: str = 'lax'  # should be 'lax' or 'strict' in production

    # ADMIN Settings
    ADMIN_USERNAME: str = 'admin'
    ADMIN_EMAIL: str = 'admin@417.co.kr'
    ADMIN_PASSWORD: str = 'qwe123123'

settings = Settings()

class AuthJWTSettings(BaseModel):
    authjwt_secret_key: str = settings.SECRET_KEY
    authjwt_token_location: set = settings.TOKEN_LOCATION
    authjwt_cookie_csrf_protect: bool = settings.CSRF_PROTECT
    authjwt_cookie_secure: bool = settings.COOKIE_SECURE
    authjwt_cookie_samesite: str = settings.COOKIE_SAMESITE