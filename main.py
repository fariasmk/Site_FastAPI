from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from views import home_view, error_view
from views.admin import admin_view


app = FastAPI(docs_url=None, redoc_url=None, exception_handlers=error_view.exception_handlers)
app.include_router(home_view.router)
app.include_router(admin_view.router)
app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')






if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level="info")

