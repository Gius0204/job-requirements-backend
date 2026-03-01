from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Backend funcionando"}
    

@app.get("/jobs")
def get_jobs():
    return [
        {
            "career": "Ingeniería de Sistemas",
            "role": "Backend Developer",
            "requirements": [
                "Python",
                "SQL",
                "Docker"
            ]
        }
    ]

