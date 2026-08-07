from langchain.agents.middleware import before_model
from langchain_core.messages import HumanMessage

BANNED_WORDS = ["exploit", "malware", "hack", "unauthorized"]

@before_model
def banned_words(state, runtime):
    
    messages = state.get("messages", [])
    
    if messages:
        last_message = messages[-1]
        content_lower = getattr(last_message, "content", "").lower()
        
        # Check if any banned word exists in the latest message
        for word in BANNED_WORDS:
            if word in content_lower:
                print(f"[Before Model Hook] Prohibited keyword detected: '{word}'")
                
                if isinstance(last_message, HumanMessage):
                    last_message.content = "I'm sorry, but I cannot process requests containing restricted terms."
                break
                

    return state