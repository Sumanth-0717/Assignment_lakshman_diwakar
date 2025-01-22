Here are two programs designed for different datasets:

1. app.py:
    -This program is designed to work with a dataset downloaded from Kaggle, which does not include a date column but provides annual returns.
    -It calculates monthly, weekly, and daily returns based on the annual returns provided in the dataset.
2. main.py:
    -This program is tailored for a dataset that includes a fund_name and a start_date column.
    -It calculates returns based on the selected period by performing calculations on the start_date column.

Instructions to Run the Programs:
    For app.py:
        -Ensure the app.py file, the dataset, and the templates folder are in the correct directory.
        -Open the terminal, navigate to the directory, and run the following command:
            python3 app.py
    For main.py:
        -Replace the dataset path in the code with the correct path to the dataset containing the start_date column.
        -Open the terminal, navigate to the directory, and run the following command:
            python3 main.py