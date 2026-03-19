Absolutely! Let’s go **module by module** and explain exactly what each of these does in the context of **DevOps scripting**, with examples of how you’d use them in real scenarios.

---

## 1️⃣ `os` – Operating System Interaction

**Purpose:**

* Access **environment variables**
* Work with **file paths handling** and **File System Operations**
* Interact with the OS (like checking if a file exists, creating directories)
* And process management (less effective than psutils)

**DevOps Use Cases:**

* Read secrets stored as environment variables
* Check if config files exist
* Get home directory, temp directory paths

**Example:**

```python
import os

# Get environment variable
kube_context = os.getenv("KUBE_CONTEXT", "default")
print(f"Using Kubernetes context: {kube_context}")

# Check if a file exists
if os.path.exists("/tmp/config.yaml"):
    print("Config exists")
```
Ah! Now I understand — you want to know **how many useful “commands” (functions/attributes) are available in the `os` module**, especially those used in **DevOps scripting**. Let’s go **deep and structured**.

---

# 🔹 1️⃣ Environment Variables Functions

| Function / Usage                 | Purpose                                         |
| -------------------------------- | ----------------------------------------------- |
| `os.environ`                     | Dictionary-like access to environment variables |
| `os.environ.get("VAR", default)` | Read env variable safely                        |
| `os.environ.items()`             | Iterate over all env vars                       |
| `os.environ.keys()`              | Get list of env var names                       |
| `os.environ.values()`            | Get list of env var values                      |
| `os.environ["VAR"] = value`      | Set/update env var                              |
| `os.environ.pop("VAR", None)`    | Delete env var safely                           |
| `del os.environ["VAR"]`          | Delete env var (raises KeyError if not exists)  |

---

# 🔹 2️⃣ File & Directory Handling

| Function / Usage                   | Purpose                             |
| ---------------------------------- | ----------------------------------- |
| `os.path.exists(path)`             | Check if file or folder exists      |
| `os.path.isfile(path)`             | Check if path is a file             |
| `os.path.isdir(path)`              | Check if path is a directory        |
| `os.path.join(path1, path2, …)`    | Safely join paths                   |
| `os.path.abspath(path)`            | Absolute path of a file             |
| `os.path.basename(path)`           | Get file name                       |
| `os.path.dirname(path)`            | Get directory name                  |
| `os.makedirs(path, exist_ok=True)` | Create directories recursively      |
| `os.remove(path)`                  | Delete a file                       |
| `os.rmdir(path)`                   | Delete empty directory              |
| `os.rename(src, dst)`              | Rename file/directory               |
| `os.listdir(path)`                 | List all files/folders in directory |

---

# 🔹 3️⃣ Process & System Functions

| Function / Usage | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| `os.system(cmd)` | Run a shell command (simple, returns exit code) |
| `os.getpid()`    | Get current Python process ID                   |
| `os.getppid()`   | Get parent process ID                           |
| `os.name`        | OS name (`posix`, `nt`, etc.)                   |
| `os.uname()`     | Detailed OS info (Linux/Unix only)              |
| `os.getcwd()`    | Current working directory                       |
| `os.chdir(path)` | Change working directory                        |
| `os.cpu_count()` | Number of CPUs                                  |
| `os.getlogin()`  | Logged-in username                              |

---

# 🔹 4️⃣ Permissions & File Metadata

| Function / Usage           | Purpose                                           |
| -------------------------- | ------------------------------------------------- |
| `os.chmod(path, mode)`     | Change file permissions                           |
| `os.chown(path, uid, gid)` | Change file owner (Linux)                         |
| `os.stat(path)`            | Get file metadata (size, created, modified, etc.) |
| `os.utime(path, times)`    | Update file timestamps                            |

---

# 🔹 5️⃣ Path & Temporary File Utilities

| Function / Usage             | Purpose                             |
| ---------------------------- | ----------------------------------- |
| `os.path.expanduser("~")`    | Get home directory                  |
| `os.path.expandvars("$VAR")` | Expand env variables in a string    |
| `os.path.splitext(path)`     | Split filename and extension        |
| `os.path.normpath(path)`     | Normalize path (removes `..`, `//`) |

---

# 🔹 6️⃣ Advanced OS Functions (Optional but useful in DevOps)

| Function / Usage       | Purpose                                       |
| ---------------------- | --------------------------------------------- |
| `os.fork()`            | Fork a new process (Unix only)                |
| `os.execvp()`          | Replace process with another process          |
| `os.kill(pid, signal)` | Kill a process                                |
| `os.pipe()`            | Create a pipe for inter-process communication |
| `os.walk(path)`        | Recursively walk directories                  |

---

### ✅ Key Takeaways for DevOps Scripting

In **real DevOps automation**, the most commonly used are:

1. **Env vars:** `os.environ`, `os.getenv()`, `os.environ.items()`
2. **File/Directory:** `os.path.exists()`, `os.listdir()`, `os.makedirs()`, `os.remove()`
3. **Run commands:** `os.system()` (though `subprocess` is preferred)
4. **Paths:** `os.path.join()`, `os.path.expanduser()`

Everything else (`chmod`, `stat`, `fork`) is **advanced or platform-specific**.

---
---

## 2️⃣ `sys` – System-Specific Parameters

**Purpose:**

* Read **command-line arguments**
* Control script **exit status**
* Access Python runtime info

**DevOps Use Cases:**

* Accept environment name, version, or branch as arguments
* Exit the script with an error if a deployment fails

**Example:**

```python
import sys

# Read CLI argument
if len(sys.argv) < 2:
    print("Usage: python deploy.py <environment>")
    sys.exit(1)

env = sys.argv[1]
print(f"Deploying to {env}")
```
Absolutely! First, here’s a **clear statement describing the role of `sys` in DevOps Python scripting**, similar to what we did for `os`:

---

**Statement:**

> “In DevOps Python scripts, the `sys` module is used to access command-line arguments, control script exit behavior, interact with the Python runtime environment, and get system-level information such as the platform, module paths, and interpreter details, allowing automation scripts to be dynamic, robust, and environment-aware.”

---

Now, let’s go **deep and structured** for `sys` just like we did for `os`.

---

# 🔹 1️⃣ Command-Line Arguments

| Function / Usage            | Purpose                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| `sys.argv`                  | List of arguments passed to the script (first item is script name) |
| `len(sys.argv)`             | Number of arguments                                                |
| `sys.argv[1], sys.argv[2]…` | Access individual arguments                                        |

**Example:**

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python deploy.py <environment>")

env = sys.argv[1]
print(f"Deploying to {env}")
```

---

# 🔹 2️⃣ Script Exit Control

| Function / Usage            | Purpose                                                          |
| --------------------------- | ---------------------------------------------------------------- |
| `sys.exit([status])`        | Exit script with optional status code (0 = success, 1 = failure) |
| `sys.exit("error message")` | Print error and exit                                             |

**Example:**

```python
import sys

if not config_exists:
    sys.exit("Config file missing. Exiting script.")
```

---

# 🔹 3️⃣ Python Runtime Info

| Function / Usage   | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| `sys.version`      | Python version string                           |
| `sys.version_info` | Python version tuple (major, minor, micro)      |
| `sys.executable`   | Path to Python interpreter being used           |
| `sys.platform`     | Current platform (Linux, Windows, etc.)         |
| `sys.path`         | List of directories Python searches for modules |
| `sys.modules`      | Dictionary of currently loaded modules          |

**Example:**

```python
import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Interpreter path:", sys.executable)
```

---

# 🔹 4️⃣ Standard Streams

| Function / Usage | Purpose                       |
| ---------------- | ----------------------------- |
| `sys.stdout`     | Default output stream (print) |
| `sys.stderr`     | Error output stream           |
| `sys.stdin`      | Standard input stream         |

**Example:**

```python
import sys

sys.stdout.write("Deploying application...\n")
sys.stderr.write("Warning: Pod not ready!\n")
```

---

# 🔹 5️⃣ Module & Resource Management

| Function / Usage       | Purpose                                |
| ---------------------- | -------------------------------------- |
| `sys.getsizeof(obj)`   | Get memory size of object              |
| `sys.getrefcount(obj)` | Reference count for debugging          |
| `sys.modules`          | Access all loaded modules              |
| `sys.path`             | Dynamically modify module search paths |

**Example:**

```python
import sys

sys.path.append("/custom/lib")
```

---

# 🔹 6️⃣ Exception & Traceback Handling

| Function / Usage                                        | Purpose                                             |
| ------------------------------------------------------- | --------------------------------------------------- |
| `sys.exc_info()`                                        | Get current exception info (type, value, traceback) |
| `sys.last_type`, `sys.last_value`, `sys.last_traceback` | Last exception info in interactive mode             |

**Example:**

```python
import sys

try:
    1 / 0
except:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(f"Error: {exc_type} - {exc_value}")
```

---

### ✅ Key Takeaways for DevOps

In **real DevOps scripting**, the most commonly used parts of `sys` are:

1. **CLI arguments:** `sys.argv`
2. **Exit control:** `sys.exit()`
3. **Runtime info:** `sys.platform`, `sys.version`
4. **Streams:** `sys.stdout`, `sys.stderr`

Other functions (`sys.modules`, `sys.path`, `sys.getsizeof`) are **advanced or for debugging/automation frameworks**.

---


## 3️⃣ `subprocess` – Running Shell Commands ⭐

**Purpose:**

* Run **external commands** from Python
* Capture their **output** and **errors**

**DevOps Use Cases:**

* Run `kubectl get pods` or `docker build`
* Automate deployments, CI/CD tasks
* Check status of servers or pods

**Example:**

```python
import subprocess

# Run a shell command
result = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
print(result.stdout)
```

---

## 4️⃣ `shutil` – File Operations

**Purpose:**

* Copy, move, delete files or directories
* Manage file system operations that are more than just reading/writing

**DevOps Use Cases:**

* Backup config files before editing
* Move logs to archive folder
* Clean up temp directories after deployment

**Example:**

```python
import shutil

# Copy a config file
shutil.copy("config.yaml", "/tmp/config_backup.yaml")

# Move a log file
shutil.move("app.log", "/var/logs/app.log")
```

---

## 5️⃣ `pathlib` – Modern File Path Handling

**Purpose:**

* Work with **paths in an object-oriented way**
* Easier and safer than string-based paths (`os.path`)

**DevOps Use Cases:**

* Combine paths without worrying about slashes (`/` vs `\`)
* Check if files or directories exist
* Create directories

**Example:**

```python
from pathlib import Path

# Define a path
config_path = Path("/etc/myapp/config.yaml")

# Check if it exists
if config_path.exists():
    print("Config file is present")

# Create directory if not exists
Path("/var/log/myapp").mkdir(parents=True, exist_ok=True)
```

---

### ✅ Summary of Roles in DevOps

| Module       | Role in DevOps Scripts                    |
| ------------ | ----------------------------------------- |
| `os`         | Env vars, basic OS interaction            |
| `sys`        | CLI args, script exit handling            |
| `subprocess` | Run shell commands (kubectl, docker, git) |
| `shutil`     | Copy/move/delete files or directories     |
| `pathlib`    | Handle file paths cleanly and safely      |

---
