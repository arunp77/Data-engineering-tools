from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# request Get method url: "/"
@app.get("/")
def root():
    return {"message" : "Welcome to my api"}

# get post data
@app.get("/posts")
def get_posts():
    return {"data" : "This is your posts"}

@app.post("/createposts")
def create_posts(payload : dict = Body(...)):
    print(payload)
    return {"new_post" : f"title {payload['title']} content : {payload['content']}"}