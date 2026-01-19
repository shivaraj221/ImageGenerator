"""
🚀 AI Image Generator - Backend
"""

import os
import io
import time
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from huggingface_hub import InferenceClient

# ================== SETUP ==================
app = FastAPI(title="AI Image Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Your HuggingFace token
HF_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXX"

# Initialize clients
clients = {}
MODELS = {}

try:
    # nscale provider models
    nscale_client = InferenceClient(provider="nscale", api_key=HF_TOKEN)
    clients["nscale"] = nscale_client
    
    # nscale models - ONLY 2 MODELS
    MODELS["flux-schnell"] = {"client": "nscale", "model": "black-forest-labs/FLUX.1-schnell"}
    MODELS["sd-xl"] = {"client": "nscale", "model": "stabilityai/stable-diffusion-xl-base-1.0"}
    
    print("✅ nscale client ready")
except Exception as e:
    print(f"❌ nscale client failed: {e}")
    clients["nscale"] = None

# ================== REQUEST MODEL ==================
class GenerateRequest(BaseModel):
    prompt: str
    model_key: str = "flux-schnell"
    steps: int = 25

# ================== ROUTES ==================
@app.get("/")
async def home():
    """Serve the HTML page"""
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/api/generate")
async def generate_image(req: GenerateRequest):
    """Generate image using the selected provider"""
    
    print(f"Generating: {req.prompt[:50]}... with {req.model_key}")
    
    # Get model info
    model_info = MODELS.get(req.model_key)
    if not model_info:
        raise HTTPException(status_code=400, detail="Model not found")
    
    provider = model_info["client"]
    model_id = model_info["model"]
    
    # Get client
    client = clients.get(provider)
    if not client:
        raise HTTPException(status_code=500, detail=f"Client for provider '{provider}' not available")
    
    try:
        # Generate image
        start = time.time()
        image = client.text_to_image(
            req.prompt,
            model=model_id,
        )
        
        # Convert to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        
        elapsed = time.time() - start
        print(f"✅ Generated in {elapsed:.1f}s with {provider}/{model_id}")
        
        return StreamingResponse(
            img_bytes,
            media_type="image/png",
            headers={"X-Time": f"{elapsed:.1f}s"}
        )
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error with {provider}/{model_id}: {error_msg}")
        
        # Provide better error messages
        if "quota" in error_msg.lower():
            error_msg = "API quota exceeded. Try again later or use a different model."
        elif "timeout" in error_msg.lower():
            error_msg = "Request timeout. The model might be busy. Try again."
        elif "unauthorized" in error_msg.lower():
            error_msg = "Authentication failed. Check your API token."
        
        raise HTTPException(status_code=500, detail=error_msg)

@app.get("/api/status")
async def status():
    """Check server and models status"""
    
    models_status = []
    ready = False
    
    # Check each model
    for key, info in MODELS.items():
        provider = info["client"]
        client = clients.get(provider)
        
        if client:
            status = "✅ Ready"
            ready = True
        else:
            status = "❌ Client not available"
        
        models_status.append({
            "name": key,
            "model": info["model"],
            "provider": provider,
            "status": status
        })
    
    return JSONResponse({
        "status": "✅ Server running" if any(clients.values()) else "❌ No providers available",
        "ready": any(clients.values()),
        "models": models_status,
        "token_set": bool(HF_TOKEN)
    })

@app.get("/api/models")
async def get_models():
    """Get list of available models"""
    return JSONResponse({
        "models": MODELS,
        "clients": {k: v is not None for k, v in clients.items()}
    })

if __name__ == "__main__":
    import uvicorn
    
    print("\n" + "="*60)
    print("🚀 AI IMAGE GENERATOR - BACKEND")
    print("="*60)
    print("📌 Open: http://localhost:8000")
    print(f"🔑 Token: {'✅ Set' if HF_TOKEN else '❌ Missing'}")
    print("\n📋 Available Models (Only 2):")
    
    for key, info in MODELS.items():
        provider = info["client"]
        client = clients.get(provider)
        status = "✅ Ready" if client else "❌ Failed"
        print(f"   • {key} ({info['model']}) - {provider}: {status}")
    
    print("\n⚡ Providers Status:")
    for provider, client in clients.items():
        print(f"   • {provider}: {'✅ Connected' if client else '❌ Failed'}")
    
    print("\n📁 Folder structure:")
    print("   ├── main.py (this file)")
    print("   ├── templates/")
    print("   │   └── index.html (frontend)")
    print("   └── static/ (optional for CSS/JS)")
    print("="*60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)