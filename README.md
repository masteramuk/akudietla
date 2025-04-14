# A Dietary Recommendation Application for Malaysian Cuisine

# App Name: akudietla
A simple LLM-based application that provides dietary recommendations tailored to Malaysian local cuisine (e.g., Nasi Lemak, Roti Canai) while helping users manage their food intake and achieve their ideal weight based on height.

## **Objective**
To create a simple LLM-based application that provides dietary recommendations tailored to Malaysian local cuisine (e.g., Nasi Lemak, Roti Canai) while helping users manage their food intake and achieve their ideal weight based on height.

---

## **Environment Setup**

### **1. Tools and Technologies**
All tools and technologies used in this project are **free and open-source**, ensuring you can develop the application entirely on your local machine without any licensing costs.
- **IDE**: Visual Studio Code (VS Code) - Free and open-source.
- **Version Control**: GitHub - Free for public repositories.
- **Programming Language**: Python 3.12.2 - Free and open-source.
- **LLM Framework**: Hugging Face Transformers or LangChain - Free and open-source.
- **Database**: SQLite - Free and open-source.
- **API Integration**: Optional integration with external APIs for nutrition data (e.g., USDA FoodData Central or custom datasets). Alternatively, you can use a manually curated dataset stored locally.

### **2. Prerequisites**
- Install Python 3.12.2 (already installed in your environment).
- Install VS Code extensions:
  - Python extension by Microsoft - Free.
  - GitLens for GitHub integration - Free.
- Create a new GitHub repository for version control - Free for public repositories.
- Install required Python libraries (all free and open-source).

---

## **Application Architecture**

### **1. Key Components**
The application will consist of the following components:
1. **User Input Module**:
   - Collect user details: height, current weight, target weight, dietary preferences, and activity level.
2. **Dietary Database**:
   - A dataset containing Malaysian cuisine items (e.g., Nasi Lemak, Roti Canai) with nutritional information (calories, protein, carbs, fat). This dataset will be stored locally in an SQLite database.
3. **LLM-Based Recommendation Engine**:
   - Use a pre-trained language model from Hugging Face Transformers or LangChain to generate personalized dietary advice based on user input and the dietary database.
4. **Output Module**:
   - Display recommendations in a user-friendly format (e.g., daily meal plans, portion sizes, calorie counts).

### **2. Workflow**
1. User inputs their details via a CLI or GUI interface.
2. The application queries the dietary database for suitable food options.
3. The LLM generates personalized recommendations based on the user's profile and preferences.
4. Recommendations are displayed to the user.

---

## **Step-by-Step Implementation Plan**

### **Step 1: Project Initialization**
1. **Create a New GitHub Repository**:
   - Go to GitHub and create a new repository named `MalaysianDietaryApp`. Ensure it is a **public repository** to stay within the free tier.
   - Clone the repository to your local machine using:
     ```bash
     git clone https://github.com/<your-username>/MalaysianDietaryApp.git
     ```
2. **Set Up Virtual Environment**:
   - Navigate to the project directory:
     ```bash
     cd MalaysianDietaryApp
     ```
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Libraries**:
   - Install dependencies (all free and open-source):
     ```bash
     pip install transformers langchain sqlite3 pandas numpy
     ```

4. **Initialize `.gitignore`**:
   - Add the following to `.gitignore` to exclude unnecessary files:
     ```
     venv/
     __pycache__/
     .DS_Store
     ```

---

### **Step 2: Build the Dietary Database**
1. **Collect Malaysian Cuisine Data**:
   - Gather nutritional information for common Malaysian dishes (e.g., Nasi Lemak, Roti Canai). You can use publicly available datasets or manually create one.
   - Example structure:
     ```csv
     dish_name,calories,protein,carbs,fat
     Nasi Lemak,500,8,60,25
     Roti Canai,300,6,45,12
     ...
     ```

2. **Store Data in SQLite**:
   - Create a SQLite database to store the dietary data (SQLite is free and open-source):
     ```python
     import sqlite3
     import pandas as pd

     # Load CSV data
     df = pd.read_csv('malaysian_cuisine.csv')

     # Connect to SQLite database
     conn = sqlite3.connect('dietary.db')
     df.to_sql('cuisine', conn, if_exists='replace', index=False)
     conn.close()
     ```

---

### **Step 3: Develop the Recommendation Engine**
1. **Load Pre-Trained LLM**:
   - Use Hugging Face Transformers to load a pre-trained model (Hugging Face offers free access to many models):
     ```python
     from transformers import pipeline

     # Load a text generation model
     generator = pipeline('text-generation', model='gpt-3.5-turbo')
     ```

2. **Generate Recommendations**:
   - Write a function to query the database and generate recommendations:
     ```python
     def generate_recommendation(user_data):
         # Query SQLite database for suitable dishes
         # Generate personalized advice using the LLM
         prompt = f"Based on the user's height ({user_data['height']}), weight ({user_data['weight']}), and preferences, recommend a daily meal plan using Malaysian cuisine."
         recommendation = generator(prompt, max_length=200)
         return recommendation[0]['generated_text']
     ```

---

### **Step 4: Create the User Interface**
1. **CLI Interface**:
   - Build a simple command-line interface to collect user input:
     ```python
     def get_user_input():
         height = float(input("Enter your height (cm): "))
         weight = float(input("Enter your current weight (kg): "))
         target_weight = float(input("Enter your target weight (kg): "))
         preferences = input("Enter your dietary preferences (comma-separated): ")
         return {
             'height': height,
             'weight': weight,
             'target_weight': target_weight,
             'preferences': preferences
         }
     ```

2. **Display Output**:
   - Print the generated recommendations:
     ```python
     user_data = get_user_input()
     recommendation = generate_recommendation(user_data)
     print("Your personalized dietary recommendation:")
     print(recommendation)
     ```

---

### **Step 5: Test and Debug**
1. Test the application with various user inputs.
2. Debug any issues with database queries or LLM outputs.

---

### **Step 6: Deploy the Application**
1. **Package the Application**:
   - Use `setuptools` to package the app for distribution (free and open-source).
2. **Optional Web Interface**:
   - Use Flask or Streamlit (both free and open-source) to create a web-based interface.

---

## **Next Steps**
1. Follow the steps above to implement the application.
2. Commit your code to GitHub regularly:
   ```bash
   git add .
   git commit -m "Add <description>"
   git push origin main