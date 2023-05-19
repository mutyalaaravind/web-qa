import uvicorn
from fastapi import FastAPI
from crawl_service import crawl
from awss3 import upload_folder_to_s3

app = FastAPI()


@app.post("/process")
async def process(data: dict):
    bucket_name = "bterai"
    try:
        folder_path = crawl(data["url"])
        upload_folder_to_s3(bucket_name, folder_path)
        return {"message": "Processing completed and Uploaded to S3 successfully"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
