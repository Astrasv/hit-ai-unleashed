
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.middleware import after_model

from dotenv import load_dotenv

load_dotenv()


rewriter_llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

@after_model
def llm_humanizer_hook(state, runtime):
    """Uses a secondary LLM to rewrite the primary model's output into a warm, casual tone."""
    messages = state.get("messages", [])
    
    if messages:
        last_message = messages[-1]
        
        if isinstance(last_message, AIMessage) and last_message.content:
            original_text = last_message.content

            print(f"[Post-LLM Hook] Original response: {original_text}")
            
            # Construct a prompt for the rewriter LLM
            prompt = (
                "Rewrite the following text to sound warm, friendly, and conversational, "
                "while keeping all factual details intact:\n\n"
                f"{original_text}"
            )
            
            print("[Post-LLM Hook] Invoking secondary LLM to humanize response...")
            rewritten_response = rewriter_llm.invoke(prompt)
            
            # Replace the original response content with the humanized version
            last_message.content = rewritten_response.content
                
    return state