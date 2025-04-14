```markdown
# Step 1: Setting Up the Environment

This document outlines the steps to set up the development environment for the Malaysian Dietary Recommendation Application (`akudietla`). All tools and libraries used are free and open-source.

---

## **1.1 Navigate to Your Project Directory**

First, navigate to the directory where your project is located. If you cloned the GitHub repository earlier, use the following command:

```bash
cd akudietla
```

If you haven't cloned the repository yet, you can do so with:

```bash
git clone https://github.com/<your-username>/akudietla.git
cd akudietla
```

---

## **1.2 Create a Virtual Environment**

A virtual environment ensures that all dependencies for your project are isolated and won't conflict with other Python projects on your machine.

Run the following command to create a virtual environment named `venv`:

```bash
python3 -m venv venv
```

This will create a folder called `venv` in your project directory.

---

## **1.3 Activate the Virtual Environment**

To activate the virtual environment, run:

```bash
source venv/bin/activate
```

Once activated, you should see `(venv)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

For example:
```
(venv) your-mac:akudietla yourusername$
```

---

## **1.4 Upgrade `pip` (Optional but Recommended)**

It's a good practice to upgrade `pip` to the latest version within your virtual environment:

```bash
pip install --upgrade pip
```

---

## **1.5 Install Required Libraries**

Install the necessary libraries for the project. Note that `sqlite3` is part of Python's standard library and does not need to be installed via `pip`.

Run the following command to install the required dependencies:

```bash
pip install transformers langchain pandas numpy
```

These libraries include:
- **transformers**: For loading pre-trained language models.
- **langchain**: For integrating LLMs into your application.
- **pandas** and **numpy**: For handling data operations.

---

## **1.6 Verify SQLite3 Installation**

Although `sqlite3` is included in Python's standard library, you can verify its availability by running a test script.

Create a file named `test_sqlite.py` with the following content:

```python
import sqlite3

# Test SQLite3 connection
try:
    conn = sqlite3.connect(':memory:')  # Creates an in-memory database for testing
    print("SQLite3 is working!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
```

Run the script:

```bash
python test_sqlite.py
```

If everything is set up correctly, you should see:

```
SQLite3 is working!
```

---

## **1.7 Initialize `.gitignore`**

To ensure that unnecessary files (like the virtual environment and temporary files) are not committed to GitHub, create a `.gitignore` file in your project directory.

Create a file named `.gitignore` and add the following content:

```
# Ignore virtual environment
venv/

# Ignore Python cache files
__pycache__/

# Ignore macOS-specific files
.DS_Store
```

You can create the `.gitignore` file using VS Code or the terminal:

```bash
echo "venv/\n__pycache__/\n.DS_Store" > .gitignore
```

---

## **1.8 Commit Initial Setup to GitHub**

Let's commit the initial setup to your GitHub repository.

1. **Stage the Changes**:
   ```bash
   git add .
   ```

2. **Commit the Changes**:
   ```bash
   git commit -m "Initial setup: Created virtual environment and added .gitignore"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin main
   ```

---

## **Key Notes**
- All tools and frameworks used in this project are **free and open-source**.
- Development can be done entirely on your local machine without requiring any paid services.
- `sqlite3` is part of Python's standard library and does not need to be installed via `pip`.
```
