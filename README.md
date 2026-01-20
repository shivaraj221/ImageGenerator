# 🎨 AI Image Generator

Create stunning AI-generated images from text descriptions using state-of-the-art models. This web application provides an easy way to generate images through a clean, user-friendly interface.

---

## 📋 What It Does

Turn your imagination into reality. Simply describe what you want to see, and our AI will create it for you. Choose between two powerful models:

- **🚀 FLUX.1 Schnell**: Fast generation with good quality (10-20 seconds)
- **🎨 Stable Diffusion XL**: Higher quality images with more detail (20-40 seconds)

---

## 🚀 Getting Started

### 📦 What You'll Need

- Python 3.8 or newer
- A free HuggingFace account

### 📝 Step 1: Get Your API Key

1. Visit [HuggingFace](https://huggingface.co/settings/tokens)
2. Sign up for a free account if you don't have one
3. Create a new access token
4. Copy the token to use later

### ⚙️ Step 2: Set Up the Project

First, download and prepare the project:

```bash
# Download the project
git clone https://github.com/yourusername/ai-image-generator.git
cd ai-image-generator

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 🔑 Step 3: Add Your API Key

Open the `main.py` file and find this line (around line 30):

```python
HF_TOKEN = "YOUR_HUGGINGFACE_TOKEN_HERE"
```

Replace `"YOUR_HUGGINGFACE_TOKEN_HERE"` with the token you copied from HuggingFace.

### 🚀 Step 4: Run the Application

Start the server with this simple command:

```bash
python main.py
```

You'll see some information in your terminal, and if everything is set up correctly, you'll see a message saying the server is ready.

### 🌐 Step 5: Open in Your Browser

Open your web browser and go to:
```
http://localhost:8000
```

---

## 🎮 How to Use It

### 👀 First Look

When you open the application, you'll see:
- ✅ Status indicators showing if everything is working
- 🎯 Two model cards to choose from
- 📝 A text box for your description
- ⚡ A generate button

### 🖼️ Creating Your First Image

1. **Choose a model**: Click on either "FLUX.1 Schnell" (faster) or "Stable Diffusion XL" (higher quality)
2. **Write your prompt**: Be descriptive! For example: "A beautiful sunset over mountains with a lake reflection"
3. **Click Generate**: The system will start creating your image
4. **Wait**: Generation takes 10-40 seconds depending on the model
5. **Save your image**: Once it's ready, download it with the download button

### 💡 Tips for Better Images

The more descriptive you are, the better the results:

| ❌ **Instead of:** | ✅ **Try:** |
|-------------------|-------------|
| "A cat" | "A fluffy orange cat sleeping on a windowsill with sunbeams shining through" |
| "A landscape" | "Mountain landscape at sunset with a river flowing through the valley, photorealistic style" |

You can also add style descriptions:
- 🎨 "in the style of digital art"
- 🖌️ "oil painting style"
- 📸 "photorealistic, 8k resolution"
- ⚪ "minimalist design"

---

## 📁 Project Files Explained

Here's what each file does:

| File | Purpose |
|------|---------|
| `main.py` | The main application that runs everything |
| `requirements.txt` | Lists all Python packages needed |
| `templates/index.html` | The web page you see in your browser |
| `static/style.css` | Optional styling for the webpage |

---

## ⚠️ If Something Goes Wrong

### 🔧 Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| **"Server not starting"** | Make sure port 8000 isn't already being used by another program. Try running: `python main.py --port 8001` |
| **"Generation failed" error** | Check your internet connection. Verify your HuggingFace token is correct. Try waiting a few minutes and trying again. |
| **"Client not available"** | Your HuggingFace token might be invalid. Go back to HuggingFace and make sure you copied the token correctly. |
| **Slow image generation** | The FLUX.1 model is generally faster than SD-XL. Complex descriptions take longer to process. |

---

## 👨‍💻 For Developers

### 🔄 Running in Development Mode

For automatic reloading when you make changes:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 🌐 Available API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | `GET` | The main web interface |
| `/api/generate` | `POST` | Generate images (send JSON with "prompt" and "model_key") |
| `/api/status` | `GET` | Check if the system is working |
| `/api/models` | `GET` | See which models are available |

### 📡 Example API Request

You can also use the API directly:

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "astronaut on mars", "model_key": "flux-schnell"}'
```

---

## 🤔 Why This Project Exists

This tool makes AI image generation accessible to everyone. Instead of dealing with complex installations or expensive services, you can run your own image generator with just a few setup steps.

---

## 🤝 Contributing

Found a bug or have an idea for improvement? Feel free to:
- 📝 Report issues you encounter
- 💡 Suggest new features
- 🔧 Submit improvements through pull requests

---

## 📝 Final Notes

Remember that AI image generation uses cloud resources, and free tiers have limits. If you use it extensively, you might need to wait between generations or consider upgrading your HuggingFace account.

Now you're ready to create! Open your browser, type your imagination into words, and watch as AI brings your ideas to life. 🎨✨

---

<div align="center">

### **⭐ Star this repository if you found it useful!**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/ai-image-generator?style=social)](https://github.com/yourusername/ai-image-generator)

</div>
