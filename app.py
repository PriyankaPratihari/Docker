import uvicorn
from script.config import service_data
# from script.config import service_data

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True,host=service_data.host,port=service_data.host)
