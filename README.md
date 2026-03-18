<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Status-Building-yellow?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/Platform-CodeCrafters-orange?style=for-the-badge" alt="CodeCrafters" />

  <br />

  <h1>🐚 Shell-Craft: A Systems Journey</h1>
  <p><i>Under Construction: Building a POSIX-compliant shell from the ground up.</i></p>
  
  <hr />
</div>

### 🏗️ Current Status: Stage 1 (The REPL)
I am currently implementing the core **Read-Evaluate-Print-Loop**. The shell can now display a prompt and wait for user input without exiting prematurely.

### 🛠️ The Tech Stack
* **Language:** Python 3.x
* **Core Modules:** `sys` (for I/O), `os` (for process handling)
* **Environment:** Windows / VS Code / PowerShell

### 🛤️ Project Roadmap
Below is the plan for the upcoming stages of development:

| Stage | Feature | Status |
| :--- | :--- | :--- |
| 1 | **The Prompt** | ✅ Completed |
| 2 | **Exit Command** | 🚧 In Progress |
| 3 | **Echo Built-in** | ⏳ Planned |
| 4 | **Type Command** | ⏳ Planned |
| 5 | **Program Execution** | ⏳ Planned |

### 🧠 The Build Log
> **Current Challenge:** Handling `stdout` buffering. 
> Because Python buffers output, the prompt `$ ` doesn't always appear immediately. I'm using `sys.stdout.flush()` to force the terminal to show the prompt before the user types.

### 📂 How to Run (Development Mode)
```bash
# Clone the build
git clone [https://github.com/Hamood-pixel/codecrafters-shell-python.git](https://github.com/Hamood-pixel/codecrafters-shell-python.git)

# Run the current iteration
python3 -m app.main