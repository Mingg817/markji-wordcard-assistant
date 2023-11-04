import os
import tempfile

import dotenv
import elevenlabs

dotenv.load_dotenv()


def tts(text: str):
    elevenlabs.set_api_key(os.getenv("ELEVEN_API_KEY"))
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as file:
        b = elevenlabs.generate(
            text=text,
            voice="Adam",
            # voice=elevenlabs.Voice(
            #     voice_id='pNInz6obpgDQGcFmaJgB',
            #     name="Adam",
            #     settings=elevenlabs.VoiceSettings(
            #         stability=0.5,
            #         similarity_boost=0.75,
            #         style=0,
            #         use_speaker_boost=True,
            #     )
            # ),
            model="eleven_multilingual_v2",
        )

        file.write(b)
    print(file)
    return file.name


if __name__ == '__main__':
    print(tts("He barely touched his food and left the restaurant.."))
