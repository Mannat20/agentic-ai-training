import os
import signal
from config import agent_id
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
agent_id = agent_id
api_key = os.getenv("917cab1ae6fde892b0e1a440331ce1ca8e719c62b2051af3cfa5c33bb704c24b")
elevenlabs = ElevenLabs(api_key=api_key)

conversation = Conversation(
    # API client and agent ID.
    elevenlabs,
    agent_id,

    # Assume auth is required when API_KEY is set.
    requires_auth=bool(api_key),

    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),

    # Simple callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

    # Uncomment if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),

    # Uncomment if you want to receive audio alignment data with character-level timing.
    # callback_audio_alignment=lambda alignment: print(f"Alignment: {alignment.chars}"),
)

conversation.start_session(
    user_id='mannat43210@gmail.com' # optional field
)
def end_session():
  signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())


conversation_id = conversation.wait_for_session_end()
print(f"Conversation ID: {conversation_id}")
