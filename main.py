from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello():
  return 'Hello Ok'


@app.get('/gretting')
def gretting():
  return 'Good Night'