import pandas as pd
import numpy as np

def generate_data():
    # Center around Milton/Mississauga (Logistics Hub)
    # Lat: 43.5, Lon: -79.8 approx
    n_orders = 50
    n_drivers = 5
    
    # Generate random orders with weights
    orders = pd.DataFrame({
        'order_id': [f'ORD-{i:03d}' for i in range(n_orders)],
        'lat': np.random.uniform(43.50, 43.70, n_orders), # Greater Toronto Area
        'lon': np.random.uniform(-79.90, -79.60, n_orders),
        'weight_kg': np.random.randint(5, 50, n_orders)
    })
    
    orders.to_csv('orders.csv', index=False)
    print(f"Generated {n_orders} orders in orders.csv")

if __name__ == "__main__":
    generate_data()