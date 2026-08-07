from langchain.agents.middleware import wrap_tool_call
@wrap_tool_call
def pre_tool_hook(request, handler):
    tool_name = request.tool_call["name"]
    tool_args = request.tool_call["args"]
    
    print(f"[Pre-Tool Hook] About to run tool: '{tool_name}' with arguments: {tool_args}")
    

    if tool_name == "calculate_shipping_cost" and tool_args.get("weight_kg", 0) > 50:
        print("[Pre-Tool Hook] Security Alert: Package weight exceeds maximum allowed limit!")
        return "Error: Shipment blocked. Weight exceeds the 50kg limit."
        

    return handler(request)

@wrap_tool_call
def post_tool_hook(request, handler):
    print(f"[Post-Tool Hook] Executing tool: {request.tool_call["name"]}...")
    

    result = handler(request)
    
    print(f"[Post-Tool Hook] Result received from tool: {result}")

    modified_result = f"{result} [Status: Verified & Logged Successfully]"
    return modified_result