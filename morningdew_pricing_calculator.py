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
class PricingModel:
    """
    Encapsulates the pricing model and its related calculations
    """

    def __init__(self, base_rates, addon_services):
        self.base_rates = base_rates
        self.addon_services = addon_services

    def calculate_total(self, flat_rate, addons_list, sq_ft, num_windows, num_loads, num_items, num_vents):
        """
         Calculates the total cost based on flat rate and add-on services.
        """
        total = flat_rate
        if 'sq_ft_rate' in addons_list:
            total += self.addon_services["sq_ft_rate"] * sq_ft
        if 'window_rate' in addons_list:
             total += self.addon_services["window_rate"] * num_windows
        if 'laundry_rate' in addons_list:
             total += self.addon_services["laundry_rate"] * num_loads
        if 'item_rate' in addons_list:
             total += self.addon_services["item_rate"] * num_items
        if 'airduct_rate' in addons_list:
            total += self.addon_services["airduct_rate"] * num_vents
        return total
    def add_addon(self, key, rate):
        """
        Adds a new add-on service to the pricing model.
        """
        self.addon_services[key] = rate
        print(f"Added addon {key} with rate {rate}")
    def remove_addon(self, key):
        """
         Removes an add-on service from the pricing model.
        """
        if key in self.addon_services:
            del self.addon_services[key]
        else:
            print(f"Error: Addon {key} not found")


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

# --- Create Pricing Model ---
pricing_model = PricingModel(base_rates, addon_services)


# Define property scenarios
scenarios = [
    {
        "Service": "Studio/1-Bedroom Cleaning",
        "Flat Rate": base_rates["studio_1_bedroom"],
        "Sq Ft": 800,
        "Windows": 5,
        "Loads of Laundry": 1,
        "Items to Clean": 2,
        "Air Ducts": 3,
        "addons":["sq_ft_rate","window_rate","laundry_rate", "item_rate", "airduct_rate"]
    },
    {
        "Service": "2-Bedroom Cleaning",
        "Flat Rate": base_rates["2_bedroom"],
        "Sq Ft": 1200,
        "Windows": 10,
        "Loads of Laundry": 2,
        "Items to Clean": 3,
        "Air Ducts": 4,
         "addons":["sq_ft_rate","window_rate","laundry_rate", "item_rate", "airduct_rate"]
    },
    {
        "Service": "3-Bedroom Cleaning",
        "Flat Rate": base_rates["3_bedroom"],
        "Sq Ft": 2000,
        "Windows": 15,
        "Loads of Laundry": 3,
        "Items to Clean": 4,
        "Air Ducts": 6,
         "addons":["sq_ft_rate","window_rate","laundry_rate", "item_rate", "airduct_rate"]
    }
]

# Calculate total cost for each scenario
results = []
for scenario in scenarios:
    try:
        total_cost = pricing_model.calculate_total(
            flat_rate=scenario["Flat Rate"],
            addons_list=scenario["addons"],
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

#Demonstrate add-on and remove features
pricing_model.add_addon("balcony_rate", 25)
pricing_model.remove_addon("item_rate")

# Calculate total cost for each scenario
results_updated = []
for scenario in scenarios:
    try:
        total_cost = pricing_model.calculate_total(
            flat_rate=scenario["Flat Rate"],
            addons_list=scenario["addons"],
            sq_ft=scenario["Sq Ft"],
            num_windows=scenario["Windows"],
            num_loads=scenario["Loads of Laundry"],
            num_items=scenario["Items to Clean"],
            num_vents=scenario["Air Ducts"]
        )
        results_updated.append({
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
df_updated = pd.DataFrame(results_updated)
display_dataframe_to_user(name="Updated Cleaning Service Pricing Model (after add-on)", dataframe=df_updated)
