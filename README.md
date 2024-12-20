

# Linear Regression Project - Algerian Forest Data

## Overview
This project explores various linear regression models to predict forest-related variables using the Algerian Forest Data. The models used in this project include:

- **Lasso Regression**  
- **Ridge Regression**  
- **Elastic Net Regression**

The goal is to evaluate the performance of each model and understand how they handle multicollinearity and overfitting in the dataset.

## Project Structure
- `data/`: Folder containing the dataset.
- `models/`: Folder with Python scripts for different regression models (Lasso, Ridge, Elastic Net).
- `notebooks/`: Jupyter notebooks for data exploration, model training, and evaluation.
- `scripts/`: Python scripts for preprocessing the data, training models, and evaluating performance.
- `requirements.txt`: Python dependencies required for the project.

## Installation

To install the required dependencies, create a virtual environment and install the libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Data Description
The dataset consists of various features related to the Algerian forest, including environmental factors and other variables that may influence forest characteristics. The data is used to predict target variables such as forest density, tree height, and biomass.

## Models Used
1. **Lasso Regression**: Implements L1 regularization to handle feature selection and prevent overfitting.
2. **Ridge Regression**: Applies L2 regularization to control model complexity and multicollinearity.
3. **Elastic Net Regression**: Combines both L1 and L2 regularization to take advantage of both Lasso and Ridge.

## Usage
1. **Data Preprocessing**  
   - Clean and preprocess the dataset by handling missing values, encoding categorical variables, and scaling features.
2. **Model Training**  
   - Each model (Lasso, Ridge, Elastic Net) is trained using the training dataset.
3. **Model Evaluation**  
   - Evaluate each model's performance using metrics like Mean Squared Error (MSE) and R².

Run the following script to train and evaluate the models:

```bash
python scripts/train_and_evaluate.py
```

## Results
The models are evaluated based on:
- Training error (MSE)
- Test error (MSE)
- R² score

The evaluation results are stored in `results/` for comparison.

## Conclusion
Based on the results, you will find the model that best fits the data, taking into account the trade-offs between simplicity and accuracy.

## Requirements
- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
