# 📈 Simple Linear Regression from Scratch

A beginner-friendly **Simple Linear Regression** project built from scratch using Python.

This project predicts a value of **Y based on X** using the **Ordinary Least Squares (OLS)** method. Instead of using machine-learning libraries such as `scikit-learn`, the regression calculations are implemented manually using Python functions.

## 🚀 Features

* Calculate the mean of X and Y values
* Calculate deviations from the mean
* Calculate squared deviations
* Calculate the product of X and Y deviations
* Calculate regression slope
* Calculate regression intercept
* Predict Y for a given X value
* Input validation for X and Y datasets
* Works completely with built-in Python functionality

## 🧠 How It Works

The program calculates the regression equation:

```text
ŷ = b₀ + b₁x
```

Where:

* `ŷ` = Predicted Y value
* `b₀` = Intercept
* `b₁` = Slope
* `x` = Input X value

### Slope

The slope is calculated using:

```text
b₁ = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
```

### Intercept

```text
b₀ = ȳ - b₁x̄
```

The predicted value is then calculated using:

```text
ŷ = b₀ + b₁x
```

## 📊 Example

### Input

```text
Enter x values data: 1 2 3 4 5
Enter y values data: 2 4 5 4 5

Enter x to find y: 6
```

### Output

```text
Predicted y: 5.8
```

*The output will depend on the dataset provided.*

## 🛠️ Technologies Used

* **Python 3**
* Python Lists
* Functions
* Loops
* Exception Handling
* Basic Statistics
* Linear Regression Mathematics

No external ML libraries are required.

## 📂 Project Structure

```text
Simple-Linear-Regression/
│
├── linear_regression.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/simple-linear-regression.git
```

### 2. Navigate to the project

```bash
cd simple-linear-regression
```

### 3. Run the program

```bash
python linear_regression.py
```

### 4. Enter your data

Provide X and Y values separated by spaces:

```text
1 2 3 4 5
```

Then enter the X value for which you want to predict Y.

## 🎯 Learning Goals

This project was created to understand how **Linear Regression works internally** rather than directly using a machine-learning library.

Through this project, I practiced:

* Mean calculation
* Deviation calculation
* Mathematical formulas
* Functions in Python
* Lists and loops
* Exception handling
* Statistical concepts
* Regression fundamentals

## 🔮 Future Improvements

Some possible improvements for this project:

* [ ] Add R² score calculation
* [ ] Add Mean Squared Error (MSE)
* [ ] Add Root Mean Squared Error (RMSE)
* [ ] Display the regression equation
* [ ] Plot the data and regression line
* [ ] Support multiple regression variables
* [ ] Add a graphical user interface
* [ ] Add CSV dataset support

## 👨‍💻 Author

**Conning**

Built while learning **Python, Statistics, and Machine Learning fundamentals**.

---

⭐ If you find this project useful, consider giving the repository a star!
