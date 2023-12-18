from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from controllers import excel_controller, csv_controller, graph_controller
from service import remove_user_data
app = FastAPI()

app.router.redirect_slashes = True

app.include_router(excel_controller.router, prefix="/excel", tags=["excel"])
app.include_router(csv_controller.router, prefix="/csv", tags=["csv"])
app.include_router(graph_controller.router, prefix="/graph", tags=["graph"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows only requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/ping")
async def api_test_endpoint():
    status = 200
    content={
        "Is Successful": "True"
    }
    return JSONResponse(status_code=status, content=content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    