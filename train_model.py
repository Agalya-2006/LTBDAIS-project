import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

np.random.seed(42)

def generate_data(n_samples=2000):
    X = []
    y = []

    for _ in range(n_samples):
        is_fault = np.random.rand() < 0.4

        if not is_fault:
            current = np.random.normal(80, 15)
            voltage = np.random.normal(230, 5)
            frequency = np.random.normal(50, 0.3)
            power_factor = np.random.normal(0.92, 0.04)
            label = 0
        else:
            fault_type = np.random.choice(['overload', 'line_break', 'voltage_sag', 'earth_fault'])

            if fault_type == 'overload':
                current = np.random.normal(210, 20)
                voltage = np.random.normal(220, 10)
                frequency = np.random.normal(50, 0.5)
                power_factor = np.random.normal(0.75, 0.05)
            elif fault_type == 'line_break':
                current = np.random.normal(5, 3)
                voltage = np.random.normal(110, 20)
                frequency = np.random.normal(50, 0.5)
                power_factor = np.random.normal(0.5, 0.1)
            elif fault_type == 'voltage_sag':
                current = np.random.normal(70, 15)
                voltage = np.random.normal(160, 10)
                frequency = np.random.normal(49.5, 0.4)
                power_factor = np.random.normal(0.65, 0.07)
            else:
                current = np.random.normal(95, 20)
                voltage = np.random.normal(200, 15)
                frequency = np.random.normal(49.8, 0.4)
                power_factor = np.random.normal(0.55, 0.08)

            label = 1

        X.append([current, voltage, frequency, power_factor])
        y.append(label)

    return np.array(X), np.array(y)

print("Generating synthetic training data...")
X, y = generate_data(2000)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training RandomForest classifier...")
model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
model.fit(X_train, y_train)

train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)
print(f"Train accuracy: {train_acc:.3f}")
print(f"Test accuracy:  {test_acc:.3f}")

joblib.dump(model, 'fault_model.pkl')
print("Model saved as fault_model.pkl")