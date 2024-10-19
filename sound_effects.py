import os
import time
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize ElevenLabs client
elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def generate_and_play_sound_effect(text: str, duration_seconds: float, prompt_influence: float):
    print(f"Generating sound effect for: '{text}'")
    
    # Record start time
    start_time = time.time()
    
    # Generate sound effect
    result = elevenlabs.text_to_sound_effects.convert(
        text=text,
        duration_seconds=duration_seconds,
        prompt_influence=prompt_influence
    )
    
    # Get the first chunk and measure latency
    first_chunk = next(result)
    latency = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"Latency to first chunk: {latency:.2f} ms")
    
    # Save audio to a temporary file
    temp_file = "temp_audio.mp3"
    with open(temp_file, "wb") as f:
        f.write(first_chunk)
        for chunk in result:
            f.write(chunk)
    
    # Record total generation time
    total_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"Total generation time: {total_time:.2f} ms")
    
    # Play the audio file using the default system player
    if os.name == 'nt':  # For Windows
        os.system(f'start {temp_file}')
    elif os.name == 'posix':  # For macOS and Linux
        os.system(f'open {temp_file}')
    
    print(f"Playing audio file: {temp_file}")
    print("The audio file will be played using your system's default audio player.")
    print("You can manually delete the temporary file after listening.")

if __name__ == "__main__":
    text = "a retro game sound of a spaceship accelerating"
    duration_seconds = 2
    prompt_influence = 0.3
    
    generate_and_play_sound_effect(text, duration_seconds, prompt_influence)
