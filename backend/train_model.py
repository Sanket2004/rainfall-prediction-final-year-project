import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
import matplotlib.pyplot as plt

# Function to preprocess data
def preprocess_data(data_path):
    data = pd.read_csv(data_path)
    data.columns = data.columns.str.strip()
    
    # Select features and target
    X = data[['pressure', 'maxtemp', 'temparature', 'mintemp', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed']]
    y = data['rainfall'].apply(lambda x: 1 if x.lower() == 'yes' else 0)

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    # Feature scaling
    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    return X, y

# Function to perform model training and evaluation
def train_and_evaluate(model, param_grid, X_train, y_train, X_test, y_test, model_name, output_file):
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # Best model and evaluation
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"{model_name} Best Parameters: {grid_search.best_params_}")
    print(f"{model_name} Accuracy: {accuracy * 100:.2f}%")
    print(f"{model_name} Classification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Rain", "Rain"])
    disp.plot(cmap=plt.cm.Blues)
    plt.title(f"Confusion Matrix for {model_name}")
    plt.show()

    # Save the model
    joblib.dump(best_model, output_file)
    print(f"{model_name} model saved as '{output_file}'\n")

    return accuracy

# Function to plot comparison of model accuracies
def plot_accuracies(algorithms, accuracies):
    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, accuracies, color=['blue', 'orange', 'green', 'red'])
    plt.ylim(0, 100)
    plt.ylabel('Accuracy (%)')
    plt.title('Comparison of Algorithm Accuracies')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Main script
if __name__ == "__main__":
    # Load and preprocess data
    data_path = "weather_data.csv"
    X, y = preprocess_data(data_path)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Models and parameters
    models = [
        (RandomForestClassifier(random_state=42), {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }, "Random Forest", "rainfall_rf_model.pkl"),

        (SVC(random_state=42), {
            'C': [0.1, 1, 10, 100],
            'kernel': ['linear', 'rbf'],
            'gamma': [1, 0.1, 0.01, 0.001]
        }, "SVM", "rainfall_svm_model.pkl"),

        (GradientBoostingClassifier(random_state=42), {
            'n_estimators': [50, 100, 200],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7]
        }, "Gradient Boosting", "rainfall_gb_model.pkl"),

        (LogisticRegression(max_iter=1000, random_state=42), {
            'C': [0.01, 0.1, 1, 10, 100],
            'penalty': ['l2'],
            'solver': ['lbfgs']
        }, "Logistic Regression", "rainfall_lr_model.pkl")
    ]

    accuracies = []

    for model, param_grid, model_name, output_file in models:
        accuracy = train_and_evaluate(model, param_grid, X_train, y_train, X_test, y_test, model_name, output_file)
        accuracies.append(accuracy * 100)

    # Plot model accuracies
    algorithms = [m[2] for m in models]
    plot_accuracies(algorithms, accuracies)