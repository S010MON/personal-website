from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"<b> This is Leon's Website </b>"}

