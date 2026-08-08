from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class InputState(TypedDict):
    customer_request: str
    dimensions: str


class OutputState(TypedDict):
    design_summary: str
    total_price_usd: float

class OverallState(TypedDict):
    customer_request: str
    dimensions: str
    wood_type: str
    material_cost: float
    labor_hours: int
    design_summary: str
    total_price_usd: float

def design_node(state: InputState):
    request = state["customer_request"].lower()
    
    wood = "Premium Oak" if "oak" in request else "Standard Pine"
    cost = 350.0 if "oak" in request else 120.0
    labor = 15 if "table" in request else 8
    
    summary = (
        f"Handcrafted {wood} piece matching request: '{state['customer_request']}'. "
        f"Cut to dimensions {state['dimensions']}."
    )
    
    return {
        "wood_type": wood,
        "material_cost": cost,
        "labor_hours": labor,
        "design_summary": summary
    }

def pricing_node(state: OverallState) -> OutputState:
    hourly_rate = 45.0
    total_labor_cost = state["labor_hours"] * hourly_rate
    final_price = state["material_cost"] + total_labor_cost
    
    return {
        "design_summary": f" Approved Blueprint : {state['design_summary']}",
        "total_price_usd": final_price
    }

graph = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
graph.add_node("design_node", design_node)
graph.add_node("pricing_node", pricing_node)

graph.add_edge(START, "design_node")
graph.add_edge("design_node", "pricing_node")
graph.add_edge("pricing_node", END)

graph = graph.compile()


response = graph.invoke({
    "customer_request": "Rustic dining table made of oak", 
    "dimensions": "72in x 36in x 30in"
})

print("Final Output:")
for key, value in response.items():
    print(f"{key}: {value}")