import pandas as pd
import random
import os

# PROJECT 2: REAL ESTATE AUDIT
print(" STARTING PROJECT 2: REAL ESTATE AUDIT ")
file_name = 'properties_2006.csv'

# Ensure the file exists
if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
    data = {
        'Property_ID': [f"Unit_{i:03}" for i in range(1, 201)],
        'Market_Value': [random.randint(150000, 600000) for _ in range(200)],
        'Monthly_Rent': [random.randint(800, 3500) for _ in range(200)]
    }
    pd.DataFrame(data).to_csv(file_name, index=False)

# Load and Audit
df = pd.read_csv(file_name)
YIELD_GOAL = 0.07
df['Yield'] = (df['Monthly_Rent'] * 12) / df['Market_Value']
df['Audit_Status'] = df['Yield'].apply(lambda x: "HIGH YIELD" if x >= YIELD_GOAL else "Standard")

# THIS LINE SHOWS YOU THE RESULTS
print(df.head(10))
