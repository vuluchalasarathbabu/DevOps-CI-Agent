from fastapi import FastAPI, Request
import logging
import uvicorn

# Configure logging (console + file)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),              # Console
        logging.FileHandler("jenkins_logs.log")  # File persistence
    ]
)

app = FastAPI()

@app.post("/jenkins-webhook")
async def receive_jenkins_logs(request: Request):
    payload = await request.json()
    logging.info("Received Jenkins webhook payload: %s", payload)
    return {"status": "ok", "message": "Logs received"}

# New GET endpoint for health check or simple test
@app.get("/health")
async def health_check():
    return {"status": "running", "message": "FastAPI Jenkins receiver is alive"}
@app.get("/logs")
async def get_logs(n: int = 10):
    with open("jenkins_logs.log", "r") as f:
        lines = f.readlines()
    return {"last_logs": lines[-n:]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)