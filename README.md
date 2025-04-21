# DockPilot - Your AI-Powered Dockerfile Generator

DockPilot is a Python-based tool that automatically generates production-ready Dockerfiles using a Large Language Model (LLM) — specifically, the LLaMA model via the Ollama platform.  
It makes it easy and fast to create clean Docker environments for any programming language, following industry best practices like multi-stage builds!

---

##  About DockPilot

DockPilot allows you to:

- Enter any programming language (e.g., Python, Node.js, Java)
- Automatically generate an ideal Dockerfile using a local LLM (Ollama)
- Create a project folder with:
  - A complete `Dockerfile`
  - A `.dockerignore` file containing standard exclusions

⚡ **No manual Dockerfile writing needed anymore!**

---

## ✨ Features

- Automatically generates optimized **multi-stage Dockerfiles**.
- Saves the Dockerfile inside a cleanly organized **project folder**.
- Also creates a helpful **`.dockerignore`** file.
- User-friendly prompts and clean error handling.
- Fast local generation via **Ollama**.

---

## ⚙️ Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.com/) installed and running locally
- A pulled LLaMA model (example: `llama3:2`)
- Python Ollama client installed:
  ```bash
  pip install ollama
  ```

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dockpilot.git
   cd dockpilot
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install ollama
   ```

4. Pull the required model:
   ```bash
   ollama pull llama3:2
   ```

---

## 🚀 Running DockPilot

Run the script:
```bash
python3 generate_dockerfile.py
```

You will be prompted to:
- Enter a programming language
- Enter a project name

Example:
```
Enter the programming language: Python
Enter your project name: my_python_app
```

After a few seconds, DockPilot will create:
- A folder named `my_python_app/`
- A `Dockerfile` and `.dockerignore` inside that folder

---

## 📂 Example Folder Structure

```
my_python_app/
│
├── Dockerfile
└── .dockerignore
```

---

## 🎯 Example Generated Dockerfile

```Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

## 🚧 Future Improvements (Ideas)

- Allow choosing **different base images** manually.
- Support **offline caching** of generated Dockerfiles.
- Build and run Docker images automatically after generation.

---

## 🧑‍💻 Author

**Chaitanya Chaudhari**

- [LinkedIn](https://www.linkedin.com/in/chaudhari-chaitanya)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> **DockPilot — Navigate your Docker builds effortlessly! 🚢**
