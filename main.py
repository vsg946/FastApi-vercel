from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import requests
import git
import openai
import os

# ===============================
# CONFIGURATION (from ENV VARIABLES)
# ===============================
SECRET_KEY = os.getenv("SECRET_KEY"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("USERNAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

app = FastAPI()

# ===============================
# BASIC VALIDATION ENDPOINT
# ===============================
@app.post("/validate")
async def validate_secret(request: Request):
    data = await request.json()
    secret = data.get("secret")

    if secret != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid secret key")

    # Mock workflow for Vercel testing (GitHub push optional)
    repo_data = {
        "repo_url": f"https://github.com/{USERNAME}/tds_auto_project",
        "pages_url": f"https://{USERNAME}.github.io/tds_auto_project/"
    }

    return JSONResponse(status_code=200, content={
        "message": "Secret key validated successfully",
        "repo_url": repo_data["repo_url"],
        "pages_url": repo_data["pages_url"]
    })

# ===============================
# OPTIONAL: LLM code generation function (mock for now)
# ===============================
def generate_code_and_readme():
    brief = "Create a FastAPI app that validates a secret and returns JSON."
    checks = "Ensure HTTP 200 response and proper validation."
    code = "# Auto-generated code here"
    readme = f"# Auto-generated FastAPI Project\n\nBrief:\n{brief}\nChecks:\n{checks}"
    return code, readme

# ===============================
# MAIN ENTRY POINT (for local testing, ignored by Vercel)
# ===============================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
