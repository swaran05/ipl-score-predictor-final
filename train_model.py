import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os, sys

data_path = os.path.join("data", "ipl_matches.csv")
if not os.path.exists(data_path):
    print("Data file not found:", data_path)
    sys.exit(1)

df = pd.read_csv(data_path)
X = df[["overs","wickets","runs_so_far","venue_factor"]]
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
print(f"Trained RandomForestRegressor. Test MSE: {mse:.2f}")
joblib.dump(model, "model.pkl")
print("Saved model to model.pkl")
