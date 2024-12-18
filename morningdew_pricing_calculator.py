import pandas as pd
from IPython.display import display

# --- Helper functions ---
def display_dataframe_to_user(name, dataframe):
    """
    Displays a Pandas DataFrame to the user with a title.
    """
    print(f"\n{name}:\n")
    display(dataframe)

# --- Pricing Definitions ---
base_rates = {
    "studio_1_bedroom": 100,
    "2_bedroom": 150,
    "3_bedroom": 200
}

addon_services = {
    "sq_ft_rate": 0.1,   # Cost per sq ft
    "window_rate": 5,    # Cost per window
    "laundry_rate": 10,  # Cost per load of laundry
    "item_rate": 15,     # Cost per item to clean
    "airduct_rate": 20   # Cost per air duct
}

# --- Calculation function ---
def calculate_total(flat_rate, addons, sq_ft, num_windows, num_loads, num_items, num_vents):
    total = flat_rate
    total += addons["sq_ft_rate"] * sq_ft
    total += addons["window_rate"] * num_windows
    total += addons["laundry_rate"] * num_loads
    total += addons["item_rate"] * num_items
    total += addons["airduct_rate"] * num_vents
    return total

# Define property scenarios
scenarios = [
    {
        "Service": "Studio/1-Bedroom Cleaning",
        "Flat Rate": base_rates["studio_1_bedroom"],
        "Sq Ft": 800,
        "Windows": 5,
        "Loads of Laundry": 1,
        "Items to Clean": 2,
        "Air Ducts": 3
    },
    {
        "Service": "2-Bedroom Cleaning",
        "Flat Rate": base_rates["2_bedroom"],
        "Sq Ft": 1200,
        "Windows": 10,
        "Loads of Laundry": 2,
        "Items to Clean": 3,
        "Air Ducts": 4
    },
    {
        "Service": "3-Bedroom Cleaning",
        "Flat Rate": base_rates["3_bedroom"],
        "Sq Ft": 2000,
        "Windows": 15,
        "Loads of Laundry": 3,
        "Items to Clean": 4,
        "Air Ducts": 6
    }
]

# Calculate total cost for each scenario
results = []
for scenario in scenarios:
    try:
        total_cost = calculate_total(
            flat_rate=scenario["Flat Rate"],
            addons=addon_services,
            sq_ft=scenario["Sq Ft"],
            num_windows=scenario["Windows"],
            num_loads=scenario["Loads of Laundry"],
            num_items=scenario["Items to Clean"],
            num_vents=scenario["Air Ducts"]
        )
        results.append({
            "Service": scenario["Service"],
            "Flat Rate": scenario["Flat Rate"],
            "Sq Ft": scenario["Sq Ft"],
            "Windows": scenario["Windows"],
            "Loads of Laundry": scenario["Loads of Laundry"],
            "Items to Clean": scenario["Items to Clean"],
            "Air Ducts": scenario["Air Ducts"],
            "Total Cost (with Add-Ons)": round(total_cost, 2)
        })
    except KeyError as e:
        print(f"KeyError: {e} in scenario: {scenario}")
    except Exception as e:
        print(f"Error: {e} while processing scenario: {scenario}")

# Create a DataFrame to present the updated pricing model
df_refined = pd.DataFrame(results)
display_dataframe_to_user(name="Refined Cleaning Service Pricing Model", dataframe=df_refined)
