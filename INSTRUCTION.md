# Option 1: Running NavCanada NOTAM Scraper in Google Colab

This guide explains how to run the Python script in Google Colab to scrape NOTAM data from NavCanada and display the results in a formatted table.

## Step 1: Open Google Colab

1. Visit [Google Colab](https://colab.research.google.com/).
2. If prompted, sign in with your Google account.

## Step 2: Create a New Notebook

1. In Google Colab, click on **File** in the top left corner.
2. Select **New notebook** to create a new Colab notebook.

## Step 3: Add and Run the Script

Google Colab comes with all required libraries pre-installed.

In a new code cell, copy and paste Python script from scraper.py
After adding the code to the Colab notebook, click on the Run button (the play icon on the left side of the code cell).
The script will run, and after a short moment, it will display the total number of records fetched from NavCanada and a well-formatted table with the NOTAM data.

<img width="1405" alt="scraper-on-google-collab" src="https://github.com/user-attachments/assets/b6daee77-8bf0-4a65-a56f-b8ddc21e905e">

---

# Option 2: Running NavCanada NOTAM Scraper on a Local Machine

This guide explains how to run the Python script on your local machine to scrape NOTAM data from NavCanada and display the results in a formatted table.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.6 or above)
- `pip` (Python package manager)
- Required Python libraries:
  - `pandas`
  - `requests`
  - `tabulate`

## Step 1: Install Python

If Python is not already installed, follow these steps:

1. **Download Python**:
   - Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**:
   - Follow the installation instructions, making sure to check the box that says "Add Python to PATH."

3. **Verify Python Installation**:
   - Open a terminal or command prompt and run:
     ```bash
     python --version
     ```
   - You should see the installed Python version.

## Step 2: Install `pip`

`pip` is typically included with Python installations. To check if `pip` is installed, run:
```bash 
pip --version
```

## Step 3: Clone the Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository from GitHub:
   ```bash
   git clone https://github.com/qnamtran/navcanada-notam-scraper.git
   ```
4. Navigate into the cloned repository
    ```bash 
    cd navcanada-notam-scraper
    ```

## Step 4: Install Required Libraries
```bash 
pip install pandas requests tabulate
```

## Step 5: Run The Script
```bash 
python navcanada_scraper.py
```

<img width="1352" alt="scraper-on-visual-studio" src="https://github.com/user-attachments/assets/64ebf43a-cd19-462a-9e62-5d067b0ff5c2">


