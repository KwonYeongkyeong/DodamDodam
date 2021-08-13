
#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python quickstart.py
"""


def run_quickstart(ans,ans2, ans3):
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=ans)
    synthesis_input2 = texttospeech.SynthesisInput(text=ans2)
    synthesis_input3 = texttospeech.SynthesisInput(text=ans3)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        name="ko-KR-Wavenet-A",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    response2 = client.synthesize_speech(
        input=synthesis_input2, voice=voice, audio_config=audio_config
    )
    response3 = client.synthesize_speech(
        input=synthesis_input3, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    with open("output2.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response2.audio_content)
        print('Audio content written to file "output2.mp3"')

    with open("output3.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response3.audio_content)
        print('Audio content written to file "output3.mp3"')
    # [END tts_quickstart]

def play(file, switch):
    #For playing audio
    import pygame

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    if switch == True:
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()   


if __name__ == "__main__":
    run_quickstart()