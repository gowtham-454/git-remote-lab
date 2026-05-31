SERVICE_NAME = "devops-platform"

def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "uptime": "running",
        "service": SERVICE_NAME
    }
