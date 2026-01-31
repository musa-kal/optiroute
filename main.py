from fastapi import FastAPI, UploadFile, File
import pandas as pd
from sklearn.cluster import KMeans
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OptiRoute Logic Engine v1.0"}

@app.post("/optimize")
async def optimize_routes(file: UploadFile = File(...), n_drivers: int = 5):
    """
    Ingests a CSV of orders and uses K-Means clustering 
    to assign them to drivers based on proximity.
    """
    # 1. Read the uploaded CSV
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    
    # 2. Extract Coordinates for Clustering
    # X = Lat, Lon pairs
    X = df[['lat', 'lon']].values
    
    # 3. Apply K-Means Algorithm (The "AI" Part)
    # We cluster the orders into 'k' groups, where k = number of drivers
    kmeans = KMeans(n_clusters=n_drivers, random_state=42)
    df['driver_id'] = kmeans.fit_predict(X)
    
    # 4. Return the data with assignments
    # Convert to list of dicts for JSON response
    result = df.to_dict(orient="records")
    
    return {"status": "optimized", "data": result}

# To run: uvicorn main:app --reload