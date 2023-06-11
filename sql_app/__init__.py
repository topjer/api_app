import uvicorn


def run_app():
    uvicorn.run("sql_app.app:app", host="127.0.0.1", port=8080)
