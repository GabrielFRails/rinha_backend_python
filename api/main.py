from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_path():
    return {
		"msg": "Saudações ser pensante"
    }
    