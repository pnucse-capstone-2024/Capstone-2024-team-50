from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from core.config import settings, AuthJWTSettings

from model.database import engine, SessionLocal
from model.init_database import init_database
from model.attack.init_database_tactic import init_database as init_database_tactic
from model.attack.init_database import init_database as init_database_attack
from model.attack.init_database_cve import init_database as init_database_cve
from model.record.init_database import init_database as init_database_record
from model.CVEResult.init_database import init_database as init_database_cveResult
from model.pentest_tool.init_database import init_database as init_database_pentest_tool

from api.v1 import auth
from api.v1 import user
from api.v1 import agent
from api.v1 import attack_map
from api.v1 import cve
from api.v1 import record
from api.v1 import cveResult
from api.v1 import attack
from api.v1 import result
from api.v1 import kali_pentest
from api.v1 import file_upload
from api.v1 import kali_result

from agent_server import agent_server


init_database(engine, SessionLocal())
init_database_tactic(engine, SessionLocal())
init_database_attack(engine, SessionLocal())
init_database_cve(engine, SessionLocal())
init_database_record(engine, SessionLocal())
init_database_cveResult(engine, SessionLocal())
init_database_pentest_tool(engine, SessionLocal())

app = FastAPI(title=settings.PROJECT_NAME,
              openapi_url=f"{settings.API_V1_STR}/openapi.json")

@AuthJWT.load_config
def get_auth_jwt_config() -> AuthJWTSettings:
    return AuthJWTSettings()


@app.exception_handler(AuthJWTException)
def auth_jwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


# # CORS
# # this section is for allowing the frontend to access the backend during development
# # this section must be removed in production
# # origins = [
# #     'http://localhost:3000',
# #     'http://localhost:8000',
# # ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['http://localhost:3000'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )
# # End CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 요청 허용
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# app.include_router(test.router, prefix=settings.API_V1_STR)
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(user.router, prefix=settings.API_V1_STR)
app.include_router(agent.router, prefix=settings.API_V1_STR)
app.include_router(attack_map.router, prefix=settings.API_V1_STR)
app.include_router(cve.router, prefix=settings.API_V1_STR)
app.include_router(record.router, prefix=settings.API_V1_STR)
app.include_router(cveResult.router, prefix=settings.API_V1_STR)
app.include_router(attack.router, prefix=settings.API_V1_STR)
app.include_router(result.router, prefix=settings.API_V1_STR)
app.include_router(kali_pentest.router, prefix=settings.API_V1_STR)
app.include_router(file_upload.router, prefix=settings.API_V1_STR)
app.include_router(kali_result.router, prefix=settings.API_V1_STR)

app.include_router(agent_server.router, prefix=settings.API_AGENT_SERVER_STR)

@app.get('/')
def root():
    return {'message': 'Hello World'}