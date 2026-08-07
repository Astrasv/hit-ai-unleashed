from langchain_core.tools import tool


@tool
def calculate_shipping_cost(weight_kg: float, destination: str) -> str:
    """Calculates shipping cost based on package weight and destination country."""
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    

    base_rate = 10.0
    cost = base_rate + (weight_kg * 5.0)
    return f"The shipping cost to {destination} for a {weight_kg}kg package is ${cost:.2f}."