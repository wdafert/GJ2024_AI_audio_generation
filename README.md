# GJ2024 AI Audio Generation

This project uses the ElevenLabs API to generate sound effects based on text descriptions.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/wdafert/GJ2024_AI_audio_generation.git
   cd GJ2024_AI_audio_generation
   ```

2. Install the required packages:
   ```
   pip install elevenlabs python-dotenv
   ```

3. Create a `.env` file in the project root and add your ElevenLabs API key:
   ```
   ELEVENLABS_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual ElevenLabs API key.

4. Run the script:
   ```
   python sound_effects.py
   ```

## Usage

Modify the `text`, `duration_seconds`, and `prompt_influence` variables in `sound_effects.py` to generate different sound effects.

## Important Note

Never commit your `.env` file to the repository. It contains sensitive information and should be kept private.
