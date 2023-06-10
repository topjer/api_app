import uvicorn


def run_app():
    uvicorn.run("sql_app.app:app")
