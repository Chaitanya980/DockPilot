import ollama
import os

PROMPT = """
ONLY Generate an ideal Dockerfile for {language} with best practices. Do not provide any description.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
- Multi Stage docker build
"""

DOCKERIGNORE_CONTENT = """
# Ignore Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore Node modules
node_modules/

# Ignore logs
*.log

# Ignore environment files
.env

# Ignore Git files
.git
"""

def generate_dockerfile(language):
    response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': PROMPT.format(language=language)}])
    if 'message' in response:
        return response['message']['content']
    else:
        raise Exception("Error: No valid response from model.")

def save_files(project_name, dockerfile_content):
    os.makedirs(project_name, exist_ok=True)
    
    # Save the Dockerfile
    dockerfile_path = os.path.join(project_name, "Dockerfile")
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile_content)
    
    # Save  the .dockerignore
    dockerignore_path = os.path.join(project_name, ".dockerignore")
    with open(dockerignore_path, "w") as f:
        f.write(DOCKERIGNORE_CONTENT)
    
    print(f"\nFiles created successfully in ./{project_name}/")
    print(f"- Dockerfile")
    print(f"- .dockerignore")

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    project_name = input("Enter your project name: ").strip().replace(" ", "_") 
    
    try:
        dockerfile = generate_dockerfile(language)
        save_files(project_name, dockerfile)
        
        print("\nGenerated Dockerfile:\n")
        print(dockerfile)
    
    except Exception as e:
        print(f"Error occurred: {e}")
