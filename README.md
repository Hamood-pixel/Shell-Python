<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Status-Building-yellow?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/Platform-CodeCrafters-orange?style=for-the-badge" alt="CodeCrafters" />

  <br />

  <h1>🐚 Shell-Craft: A Systems Journey</h1>
  <p><i>Under Construction: Building a POSIX-compliant shell from the ground up.</i></p>
  
  <hr />
</div>

### 🏗️ Current Status: Stage 4 (Built-ins & Executables)
The shell is now capable of identifying commands. It distinguishes between internal **shell built-ins** and **external programs** by crawling the system's `PATH` environment variable.

### 🛠️ The Tech Stack
* **Language:** Python 3.x
* **Core Modules:** `sys` (I/O & Buffering), `os` (Environment variables & File permissions)
* **Environment:** Windows / VS Code / PowerShell / CodeCrafters CLI

### 🛤️ Project Roadmap
I've successfully implemented the core command identification logic:

| Stage | Feature | Status |
| :--- | :--- | :--- |
| 1 | **The Prompt (REPL)** | ✅ Completed |
| 2 | **Exit Command** | ✅ Completed |
| 3 | **Echo Built-in** | ✅ Completed |
| 4 | **Type Command** (Built-ins) | ✅ Completed |
| 5 | **PATH Search** (`os.pathsep`) | ✅ Completed |
| 6 | **External Program Execution** | 🚧 In Progress |

### 🧠 The Build Log
> **Latest Milestone:** Just implemented a cross-platform `PATH` lookup using `os.pathsep`. 
> 
> **Challenge:** Correctly identifying if a command exists in the system directories. I'm now using `os.environ.get("PATH")` to split directories and `os.access(path, os.X_OK)` to verify that found files are actually executable.

### 📂 How to Run (Development Mode)
```bash
# Clone the build
git clone [https://github.com/Hamood-pixel/Shell-Python.git](https://github.com/Hamood-pixel/Shell-Python.git)

# Run the current iteration
python3 -m app.main
