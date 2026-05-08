from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.messages import HumanMessage

import sounddevice as sd
from scipy.io.wavfile import write
import base64
import time
from tqdm import tqdm

import base64

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)


agent= create_agent(
    model=model,
    tools=[],
)

# Settings
duration = 5 
sample_rate = 44100
filename = "temp_recording.wav"

print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)

for _ in tqdm(range(duration * 10)):
    time.sleep(0.1)
sd.wait()
print("Done.")

write(filename, sample_rate, audio)

with open(filename, "rb") as wav_file:
    aud_b64 = base64.b64encode(wav_file.read()).decode("utf-8")


multimodal_question = HumanMessage(content=[
    {"type": "text", "text": "Answer the question asked in the audio"},
    {"type": "image", "base64": aud_b64, "mime_type": "audio/wav"}
])

response = agent.invoke(
    {"messages": [multimodal_question]}
)

print(response['messages'][-1].content)
