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
Perfect! Let’s do the **same deep-dive for `subprocess`** as we did for `os` and `sys`. I’ll first give you a **statement** describing its role, then go module by module with **all the commonly used commands/functions, purpose, and examples**.

---

# 🔹 Statement for `subprocess`

> “In DevOps Python scripts, the `subprocess` module is used to execute and control external system commands and programs, capture their output or errors, and manage return codes. It allows automation scripts to interact with CLI tools like `kubectl`, `docker`, `git`, or any shell command, making Python scripts capable of full system-level automation.”

---

# 🔹 1️⃣ Running Simple Commands

| Function / Usage                          | Purpose                                                                 |
| ----------------------------------------- | ----------------------------------------------------------------------- |
| `subprocess.run(args, **kwargs)`          | Run a command, wait for completion, returns a `CompletedProcess` object |
| `subprocess.call(args, **kwargs)`         | Run a command, returns exit code only (simpler, legacy)                 |
| `subprocess.check_call(args, **kwargs)`   | Run command, raises exception if exit code != 0                         |
| `subprocess.check_output(args, **kwargs)` | Run command, returns output, raises exception if exit code != 0         |

**Example:**

```python id="svq9h2"
import subprocess

# Run kubectl get pods
result = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
print(result.stdout)
```

---

# 🔹 2️⃣ Capture Output

| Parameter                | Purpose                              |
| ------------------------ | ------------------------------------ |
| `capture_output=True`    | Capture stdout and stderr as strings |
| `stdout=subprocess.PIPE` | Redirect stdout                      |
| `stderr=subprocess.PIPE` | Redirect stderr                      |
| `text=True`              | Return strings instead of bytes      |

**Example:**

```python id="7i9klo"
result = subprocess.run(
    ["docker", "ps"],
    capture_output=True,
    text=True
)
print("Containers running:\n", result.stdout)
```

---

# 🔹 3️⃣ Handling Return Codes

| Attribute                       | Purpose                                                               |
| ------------------------------- | --------------------------------------------------------------------- |
| `result.returncode`             | Exit code of command (0 = success)                                    |
| `subprocess.CalledProcessError` | Exception raised by `check_call` or `check_output` if returncode != 0 |

**Example:**

```python id="v4r9pl"
try:
    subprocess.check_call(["kubectl", "apply", "-f", "deployment.yaml"])
    print("Deployment successful")
except subprocess.CalledProcessError as e:
    print(f"Deployment failed with code {e.returncode}")
```

---

# 🔹 4️⃣ Running Shell Commands

| Parameter    | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `shell=True` | Run command in the shell (allows pipes, redirects) |

**Example:**

```python id="c1d4zr"
subprocess.run("kubectl get pods | grep Running", shell=True)
```

⚠️ **Warning:** Only use `shell=True` if you trust input to avoid security issues.

---

# 🔹 5️⃣ Passing Environment Variables

| Parameter | Purpose                                                   |
| --------- | --------------------------------------------------------- |
| `env`     | Pass a dictionary of environment variables to the command |

**Example:**

```python id="h7m4yz"
import os

env_vars = os.environ.copy()
env_vars["MY_ENV"] = "dev"

subprocess.run(["echo", "$MY_ENV"], env=env_vars, shell=True)
```

---

# 🔹 6️⃣ Advanced: Communicating with Process

| Function / Usage                   | Purpose                                         |
| ---------------------------------- | ----------------------------------------------- |
| `subprocess.Popen()`               | Start process, allows **real-time interaction** |
| `proc.communicate(input)`          | Send/receive data to process stdin/stdout       |
| `proc.terminate()` / `proc.kill()` | Stop process                                    |

**Example:**

```python id="l2r8jk"
from subprocess import Popen, PIPE

proc = Popen(["kubectl", "logs", "my-pod"], stdout=PIPE, stderr=PIPE, text=True)
stdout, stderr = proc.communicate()
print("Logs:", stdout)
```

---

# 🔹 7️⃣ Other Useful Parameters

| Parameter    | Purpose                                          |
| ------------ | ------------------------------------------------ |
| `cwd`        | Run command in specific directory                |
| `timeout`    | Timeout for process execution                    |
| `check=True` | Automatically raise exception if returncode != 0 |

**Example:**

```python id="k4p9mz"
subprocess.run(
    ["docker", "build", "-t", "myapp:latest", "."],
    cwd="/home/user/project",
    timeout=300,
    check=True
)
```

---

# ✅ Key Takeaways for DevOps

1. **Most commonly used:** `subprocess.run()` with `capture_output=True` and `text=True`
2. **Check status:** Use `returncode` or `check=True`
3. **Env variables:** Use `env` parameter to pass runtime environment
4. **Advanced:** `Popen` for real-time stdout/stderr streaming or interactive processes
5. **Shell commands:** Only use `shell=True` if necessary

---

# 🔹 Real DevOps Scenario Using `subprocess`

```python id="y4v7ml"
import subprocess

# Deploy app
result = subprocess.run(["kubectl", "apply", "-f", "deployment.yaml"], capture_output=True, text=True)
if result.returncode != 0:
    print("Deployment failed!")
    print(result.stderr)
else:
    print("Deployment successful!")
    # Get pods
    pods = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
    print(pods.stdout)
```

This is exactly **how DevOps scripts automate deployments, check pod status, and log results**.

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
Perfect! Let’s do the **same in-depth explanation for `shutil`** as we did for `os`, `sys`, and `subprocess`. I’ll start with a **statement**, then go through **all commonly used functions with purpose and examples**, so you can use it confidently in **DevOps Python scripting**.

---

# 🔹 Statement for `shutil`

> “In DevOps Python scripts, the `shutil` module is used for **high-level file and directory operations** such as copying, moving, deleting, and archiving files or folders. It simplifies file management tasks like backing up configuration files, moving logs, cleaning temporary directories, or preparing deployment packages.”

---

# 🔹 1️⃣ Copying Files and Directories

| Function / Usage            | Purpose                                                      |
| --------------------------- | ------------------------------------------------------------ |
| `shutil.copy(src, dst)`     | Copy a file to a destination (metadata may not be preserved) |
| `shutil.copy2(src, dst)`    | Copy a file and preserve metadata (timestamps)               |
| `shutil.copytree(src, dst)` | Recursively copy a directory to a new location               |

**Example:**

```python id="sht1"
import shutil

# Copy single file
shutil.copy("config.yaml", "/tmp/config_backup.yaml")

# Copy entire directory
shutil.copytree("myapp/", "/tmp/myapp_backup")
```

---

# 🔹 2️⃣ Moving or Renaming Files and Directories

| Function / Usage        | Purpose                                                        |
| ----------------------- | -------------------------------------------------------------- |
| `shutil.move(src, dst)` | Move a file or directory (can also rename)                     |
| `os.rename(src, dst)`   | Can also rename (but less flexible for cross-filesystem moves) |

**Example:**

```python id="sht2"
# Move a log file to archive
shutil.move("/var/log/app.log", "/var/log/archive/app.log")
```

---

# 🔹 3️⃣ Deleting Files and Directories

| Function / Usage      | Purpose                                             |
| --------------------- | --------------------------------------------------- |
| `os.remove(path)`     | Delete a single file (from `os` module)             |
| `shutil.rmtree(path)` | Delete a directory and all its contents recursively |

**Example:**

```python id="sht3"
# Remove a temp directory and all its contents
shutil.rmtree("/tmp/myapp_logs")
```

---

# 🔹 4️⃣ Archiving and Compressing

| Function / Usage                                   | Purpose                                            |
| -------------------------------------------------- | -------------------------------------------------- |
| `shutil.make_archive(base_name, format, root_dir)` | Create a zip, tar, or other archive of a directory |
| `shutil.unpack_archive(filename, extract_dir)`     | Extract an archive                                 |

**Example:**

```python id="sht4"
# Create a zip archive of deployment files
shutil.make_archive("/tmp/deployment_backup", "zip", "deployment_folder")

# Extract the archive
shutil.unpack_archive("/tmp/deployment_backup.zip", "/tmp/deployment_restore")
```

---

# 🔹 5️⃣ Disk Usage and File System Info

| Function / Usage          | Purpose                                             |
| ------------------------- | --------------------------------------------------- |
| `shutil.disk_usage(path)` | Returns total, used, and free space of filesystem   |
| `shutil.which(cmd)`       | Locate a command in the PATH (like `which kubectl`) |

**Example:**

```python id="sht5"
# Check disk space
total, used, free = shutil.disk_usage("/")
print(f"Total: {total}, Free: {free}")

# Check if docker is installed
docker_path = shutil.which("docker")
print("Docker path:", docker_path)
```

---

# 🔹 6️⃣ Other Useful Functions

| Function / Usage                                            | Purpose                                             |
| ----------------------------------------------------------- | --------------------------------------------------- |
| `shutil.chown(path, user=None, group=None)`                 | Change ownership of file/directory                  |
| `shutil.move()` + `os.makedirs()`                           | Combine to move files and ensure destination exists |
| `shutil.copytree()` with `dirs_exist_ok=True` (Python 3.8+) | Merge directories instead of error                  |

---

# ✅ Key Takeaways for DevOps

1. **Backup / Restore configs:** `shutil.copy`, `shutil.copytree`
2. **Archive deployments:** `shutil.make_archive`, `shutil.unpack_archive`
3. **Move / Organize logs:** `shutil.move`
4. **Clean temp directories:** `shutil.rmtree`
5. **Check disk space or commands:** `shutil.disk_usage`, `shutil.which`

---

# 🔹 Real DevOps Scenario Using `shutil`

```python id="sht6"
import shutil
from pathlib import Path

# Backup deployment configs
Path("/tmp/backups").mkdir(exist_ok=True)
shutil.copy("deployment.yaml", "/tmp/backups/deployment.yaml")

# Archive current deployment folder
shutil.make_archive("/tmp/deployment_backup", "zip", "deployment_folder")

# Move logs to archive
shutil.move("/var/log/app.log", "/var/log/archive/app.log")

# Clean old temp logs
shutil.rmtree("/tmp/temp_logs", ignore_errors=True)
```

✅ This is exactly how DevOps scripts **automate backup, archiving, moving, and cleanup tasks**.

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
Perfect! Let’s do the **same deep-dive for `pathlib`**, just like we did for `os`, `sys`, `subprocess`, and `shutil`. I’ll first give a **statement**, then go function by function with **purpose, examples, and DevOps use cases**.

---

# 🔹 Statement for `pathlib`

> “In DevOps Python scripts, the `pathlib` module is used for **modern, object-oriented file system path handling**. It simplifies operations like creating directories, checking file existence, joining paths, and reading/writing files, while making scripts **cross-platform** (Linux, Windows, Mac) safe and clean.”

---

# 🔹 1️⃣ Creating Path Objects

| Function / Usage     | Purpose                                   |
| -------------------- | ----------------------------------------- |
| `Path("filename")`   | Create a path object for a file or folder |
| `Path("/some/path")` | Absolute or relative paths                |
| `Path.home()`        | Get home directory of the current user    |
| `Path.cwd()`         | Get current working directory             |

**Example:**

```python id="plb1"
from pathlib import Path

config = Path("deployment.yaml")        # relative path
home_dir = Path.home()                  # /home/user or C:\Users\User
current_dir = Path.cwd()                # current working directory
```

---

# 🔹 2️⃣ Checking Existence and Type

| Function / Usage | Purpose                      |
| ---------------- | ---------------------------- |
| `path.exists()`  | Check if file/folder exists  |
| `path.is_file()` | Check if path is a file      |
| `path.is_dir()`  | Check if path is a directory |

**Example:**

```python id="plb2"
if config.exists() and config.is_file():
    print("Deployment config found")
```

---

# 🔹 3️⃣ Creating Directories

| Function / Usage                            | Purpose                                             |
| ------------------------------------------- | --------------------------------------------------- |
| `path.mkdir(parents=False, exist_ok=False)` | Create a directory                                  |
| `parents=True`                              | Create intermediate directories if they don’t exist |
| `exist_ok=True`                             | Don’t raise error if directory exists               |

**Example:**

```python id="plb3"
logs_dir = Path("/var/log/myapp")
logs_dir.mkdir(parents=True, exist_ok=True)
```

---

# 🔹 4️⃣ Joining Paths

| Operator / Function                      | Purpose                                            |
| ---------------------------------------- | -------------------------------------------------- |
| `path / "subfolder"`                     | Join paths safely (overrides `/` issues across OS) |
| `path.joinpath("subfolder", "file.txt")` | Same as `/` operator                               |

**Example:**

```python id="plb4"
file_path = logs_dir / "app.log"
file_path2 = logs_dir.joinpath("app2.log")
print(file_path, file_path2)
```

---

# 🔹 5️⃣ Reading and Writing Files

| Function / Usage         | Purpose                |
| ------------------------ | ---------------------- |
| `path.read_text()`       | Read text file content |
| `path.read_bytes()`      | Read file as bytes     |
| `path.write_text(data)`  | Write text to file     |
| `path.write_bytes(data)` | Write bytes to file    |

**Example:**

```python id="plb5"
# Read deployment config
content = config.read_text()
print(content)

# Write logs
file_path.write_text("Deployment started...\n")
```

---

# 🔹 6️⃣ File Properties and Metadata

| Function / Usage | Purpose                                   |
| ---------------- | ----------------------------------------- |
| `path.name`      | File or folder name                       |
| `path.stem`      | Filename without extension                |
| `path.suffix`    | File extension                            |
| `path.parent`    | Parent directory path                     |
| `path.stat()`    | File metadata (size, modified time, etc.) |

**Example:**

```python id="plb6"
print("File name:", config.name)
print("Extension:", config.suffix)
print("Parent folder:", config.parent)
print("Size:", config.stat().st_size, "bytes")
```

---

# 🔹 7️⃣ Iterating Over Directories

| Function / Usage      | Purpose                                 |
| --------------------- | --------------------------------------- |
| `path.iterdir()`      | Iterate over files/folders in directory |
| `path.glob("*.yaml")` | Find files matching pattern             |
| `path.rglob("*.log")` | Recursive glob (all subdirectories)     |

**Example:**

```python id="plb7"
for file in Path("/tmp/backups").glob("*.yaml"):
    print("Backup file:", file)
```

---

# 🔹 8️⃣ Deleting Files or Folders

| Function / Usage      | Purpose                                                       |
| --------------------- | ------------------------------------------------------------- |
| `path.unlink()`       | Delete a file                                                 |
| `shutil.rmtree(path)` | Delete a directory recursively (use with pathlib Path object) |

**Example:**

```python id="plb8"
# Delete old log
if file_path.exists():
    file_path.unlink()
```

---

# 🔹 Key Takeaways for DevOps

1. **Cross-platform safe path handling** → Use `/` operator
2. **Check existence before operations** → `exists()`, `is_file()`, `is_dir()`
3. **Create directories automatically** → `mkdir(parents=True, exist_ok=True)`
4. **File read/write operations** → `read_text()`, `write_text()`
5. **Glob and iterate directories** → Useful for backups, configs, or logs
6. **Combine with `shutil`** → Move, copy, delete directories

---

# 🔹 Real DevOps Scenario Using `pathlib`

```python id="plb9"
from pathlib import Path
import shutil

# Paths
config = Path("/etc/myapp/deployment.yaml")
backup_dir = Path("/tmp/backups")
backup_dir.mkdir(parents=True, exist_ok=True)

# Backup deployment config
shutil.copy(config, backup_dir / config.name)

# Read backup content
backup_file = backup_dir / config.name
print("Backup content:", backup_file.read_text())

# Delete old temp logs
for log in Path("/tmp/logs").rglob("*.log"):
    log.unlink()
```


### ✅ Summary of Roles in DevOps

| Module       | Role in DevOps Scripts                    |
| ------------ | ----------------------------------------- |
| `os`         | Env vars, basic OS interaction            |
| `sys`        | CLI args, script exit handling            |
| `subprocess` | Run shell commands (kubectl, docker, git) |
| `shutil`     | Copy/move/delete files or directories     |
| `pathlib`    | Handle file paths cleanly and safely      |

---
# Final List of Used Commands
Perfect! Let’s create a **final, consolidated list of the most used Python commands/functions in DevOps scripting** from all five modules (`os`, `sys`, `subprocess`, `shutil`, `pathlib`) that you can rely on for **automation, CI/CD, Kubernetes, Docker, and pipelines**. I’ve structured it by **module → command → purpose → example**.

---

# **1️⃣ OS Module (`os`) – Environment & System**

| Command / Function                 | Purpose                         | Example                                      |
| ---------------------------------- | ------------------------------- | -------------------------------------------- |
| `os.getenv("VAR", default)`        | Read environment variable       | `env = os.getenv("KUBE_CONTEXT", "dev")`     |
| `os.environ["VAR"] = value`        | Set/update env var              | `os.environ["ENV"] = "stage"`                |
| `os.environ.items()`               | List all environment variables  | `for k,v in os.environ.items(): print(k,v)`  |
| `"VAR" in os.environ`              | Check if env var exists         | `if "HOME" in os.environ: ...`               |
| `os.path.exists(path)`             | Check if file/folder exists     | `os.path.exists("/tmp/config.yaml")`         |
| `os.path.join(path1, path2)`       | Safe path join                  | `os.path.join("/tmp","logs")`                |
| `os.makedirs(path, exist_ok=True)` | Create directories recursively  | `os.makedirs("/tmp/backups", exist_ok=True)` |
| `os.remove(path)`                  | Delete a file                   | `os.remove("/tmp/app.log")`                  |
| `os.rename(src,dst)`               | Rename/move file                | `os.rename("old.txt","new.txt")`             |
| `os.listdir(path)`                 | List files/folders in directory | `files = os.listdir("/tmp")`                 |
| `os.system(cmd)`                   | Run simple shell command        | `os.system("ls -l")`                         |
| `os.name` / `os.platform`          | Get OS info                     | `print(os.name)`                             |

---

# **2️⃣ SYS Module (`sys`) – Script Control & Runtime Info**

| Command / Function                 | Purpose                    | Example                              |
| ---------------------------------- | -------------------------- | ------------------------------------ |
| `sys.argv`                         | Command-line arguments     | `env = sys.argv[1]`                  |
| `len(sys.argv)`                    | Count arguments            | `if len(sys.argv)<2: sys.exit()`     |
| `sys.exit([status/message])`       | Exit script                | `sys.exit("Config missing!")`        |
| `sys.platform`                     | OS platform info           | `print(sys.platform)`                |
| `sys.version` / `sys.version_info` | Python version info        | `print(sys.version)`                 |
| `sys.executable`                   | Path to Python interpreter | `print(sys.executable)`              |
| `sys.stdout.write()`               | Print to stdout            | `sys.stdout.write("Deploying...\n")` |
| `sys.stderr.write()`               | Print to stderr            | `sys.stderr.write("Error!\n")`       |

---

# **3️⃣ Subprocess Module (`subprocess`) – Running CLI Commands**

| Command / Function                                     | Purpose                                           | Example                                                                    |                             |
| ------------------------------------------------------ | ------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------- |
| `subprocess.run(args, capture_output=True, text=True)` | Run command and capture output                    | `subprocess.run(["kubectl","get","pods"], capture_output=True, text=True)` |                             |
| `subprocess.check_call(args)`                          | Run command, raise exception if fails             | `subprocess.check_call(["docker","build","."])`                            |                             |
| `subprocess.check_output(args)`                        | Run command, get output, raise exception if fails | `output = subprocess.check_output(["git","status"], text=True)`            |                             |
| `subprocess.Popen(args, stdout=PIPE, stderr=PIPE)`     | Advanced: real-time interaction                   | `proc = subprocess.Popen(["kubectl","logs","my-pod"], stdout=PIPE)`        |                             |
| `env` parameter                                        | Pass environment vars                             | `subprocess.run(["echo","$MY_ENV"], env=os.environ.copy(), shell=True)`    |                             |
| `cwd`                                                  | Run command in specific directory                 | `subprocess.run(["ls"], cwd="/tmp")`                                       |                             |
| `shell=True`                                           | Run shell command with pipes                      | `subprocess.run("kubectl get pods                                          | grep Running", shell=True)` |

---

# **4️⃣ Shutil Module (`shutil`) – File & Directory Operations**

| Command / Function                                 | Purpose                      | Example                                                        |
| -------------------------------------------------- | ---------------------------- | -------------------------------------------------------------- |
| `shutil.copy(src, dst)`                            | Copy a file                  | `shutil.copy("config.yaml","/tmp/config.yaml")`                |
| `shutil.copy2(src,dst)`                            | Copy file + metadata         | `shutil.copy2("config.yaml","/tmp/config.yaml")`               |
| `shutil.copytree(src,dst)`                         | Copy entire directory        | `shutil.copytree("app/","/tmp/app_backup")`                    |
| `shutil.move(src,dst)`                             | Move or rename               | `shutil.move("app.log","/var/logs/app.log")`                   |
| `shutil.rmtree(path)`                              | Delete directory recursively | `shutil.rmtree("/tmp/old_logs")`                               |
| `shutil.make_archive(base_name, format, root_dir)` | Create archive               | `shutil.make_archive("/tmp/deploy","zip","deployment_folder")` |
| `shutil.unpack_archive(filename, extract_dir)`     | Extract archive              | `shutil.unpack_archive("/tmp/deploy.zip","/tmp/restore")`      |
| `shutil.disk_usage(path)`                          | Check disk usage             | `total, used, free = shutil.disk_usage("/")`                   |
| `shutil.which(cmd)`                                | Locate command in PATH       | `shutil.which("docker")`                                       |

---

# **5️⃣ Pathlib Module (`pathlib`) – Modern File Paths**

| Command / Function                                        | Purpose                     | Example                                                |
| --------------------------------------------------------- | --------------------------- | ------------------------------------------------------ |
| `Path("file")`                                            | Create path object          | `config = Path("deployment.yaml")`                     |
| `Path.cwd()`                                              | Current working directory   | `cwd = Path.cwd()`                                     |
| `Path.home()`                                             | Home directory              | `home = Path.home()`                                   |
| `path.exists()`                                           | Check if file/folder exists | `if config.exists(): ...`                              |
| `path.is_file()` / `path.is_dir()`                        | Check type                  | `if config.is_file(): ...`                             |
| `path.mkdir(parents=True, exist_ok=True)`                 | Create directory            | `Path("/tmp/logs").mkdir(parents=True, exist_ok=True)` |
| `path / "subfile"` or `path.joinpath()`                   | Join paths                  | `file_path = Path("/tmp") / "app.log"`                 |
| `path.read_text()` / `path.write_text()`                  | Read/write text file        | `data = config.read_text()`                            |
| `path.stat()`                                             | File metadata               | `size = config.stat().st_size`                         |
| `path.iterdir()`                                          | Iterate folder              | `for f in Path("/tmp").iterdir(): print(f)`            |
| `path.glob("*.yaml")` / `path.rglob("*.log")`             | Find files matching pattern | `for f in Path("/tmp").rglob("*.log"): print(f)`       |
| `path.unlink()`                                           | Delete file                 | `file_path.unlink()`                                   |
| `path.parent` / `path.name` / `path.stem` / `path.suffix` | Path properties             | `print(config.name, config.suffix, config.parent)`     |

---

### ✅ Key Takeaways

* **`os` + `pathlib`** → File system & environment handling
* **`sys`** → Script arguments & runtime control
* **`subprocess`** → Run CLI commands (`kubectl`, `docker`, `git`)
* **`shutil`** → Backup, move, delete, archive files/folders
