#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google Assistant GRPC recognizer."""

import os

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat

def main():
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()
    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text, audio = assistant.recognize()
        if text is not None:
          if text == 'goodbye':
            print('Bye!')
            os._exit(0)
          print('You said "', text, '"')
        if audio is not None:
          aiy.audio.play_audio(audio)


if __name__ == '__main__':
    main()