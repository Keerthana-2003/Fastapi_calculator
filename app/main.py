import logging
from fastapi import FastAPI, HTTPException
from app.operations import add, subtract, multiply, divide  # Import from app folder

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize FastAPI app
app = FastAPI(title="FastAPI Calculator", description="A simple calculator API")

# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI Calculator is running! Visit /docs for API documentation."}

# Add endpoint
@app.get("/add")
def api_add(a: float, b: float):
    result = add(a, b)
    logging.info(f"Adding {a} + {b} = {result}")
    return {"result": result}

# Subtract endpoint
@app.get("/subtract")
def api_subtract(a: float, b: float):
    result = subtract(a, b)
    logging.info(f"Subtracting {a} - {b} = {result}")
    return {"result": result}

# Multiply endpoint
@app.get("/multiply")
def api_multiply(a: float, b: float):
    result = multiply(a, b)
    logging.info(f"Multiplying {a} * {b} = {result}")
    return {"result": result}

# Divide endpoint
@app.get("/divide")
def api_divide(a: float, b: float):
    try:
        result = divide(a, b)
        logging.info(f"Dividing {a} / {b} = {result}")
        return {"result": result}
    except ValueError as e:
        logging.error(f"Error dividing {a} / {b}: {e}")
        raise HTTPException(status_code=400, detail=str(e))
