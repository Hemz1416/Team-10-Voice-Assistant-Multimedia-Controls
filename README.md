\# Team 10 — Voice Assistant for Multimedia Controls



Software Engineering Mini Project — Voice Assistant for Multimedia Controls.



\## Overview



This project is a voice-controlled multimedia application that uses speech recognition to identify spoken commands and control audio playback through VLC.



The application processes spoken input, detects the intended command, validates it, and executes the corresponding media action.



\## Features



\- Speech recognition using Vosk.

\- Voice command processing and intent detection.

\- Confidence-based command validation.

\- VLC-based media playback control.

\- Support for a playlist containing multiple audio files.

\- Continuous listening for voice commands.

\- Rejection of unsupported commands and low-confidence input.

\- Automated tests for command processing, validation, and integration.



\## Supported Voice Commands



| Command | Action |

|---|---|

| PLAY | Start playback |

| PAUSE | Pause playback |

| RESUME | Resume playback |

| STOP | Stop playback |

| NEXT | Play the next track |

| PREVIOUS | Play the previous track |

| VOLUME\_UP | Increase volume |

| VOLUME\_DOWN | Decrease volume |

| MUTE | Toggle mute |



Example phrases include "play music", "pause music", "resume music", "next song", "previous track", "volume up", "volume down", and "mute".



\## Technology Stack



\- Python 3

\- Vosk speech recognition

\- SoundDevice microphone input

\- VLC media player

\- python-vlc

\- pytest



\## Project Structure



```text

Team-10-Voice-Assistant-Multimedia-Controls/

├── src/

│   ├── command\_service.py

│   ├── command\_validator.py

│   ├── intent\_processor.py

│   ├── integration\_app.py

│   ├── media\_controller.py

│   ├── models.py

│   └── speech\_input.py

├── tests/

│   ├── test\_command\_service.py

│   ├── test\_command\_validator.py

│   ├── test\_intent\_processor.py

│   └── test\_media\_integration.py

├── models/

│   └── vosk-model-small-en-us-0.15/

├── requirements.txt

└── README.md

```



The Vosk model directory is downloaded separately and is not included in the Git repository.



\## Prerequisites



1\. Python 3 installed.

2\. VLC media player installed.

3\. A working microphone.

4\. A Vosk English speech recognition model.

5\. Audio files supported by VLC.



The application has been manually tested in a Windows development environment. Raspberry Pi OS/Linux deployment should be verified on the target hardware.



\## Installation



\### 1. Clone the repository



```cmd

git clone https://github.com/Team10-SE/Team-10-Voice-Assistant-Multimedia-Controls.git

cd Team-10-Voice-Assistant-Multimedia-Controls

```



\### 2. Install Python dependencies



```cmd

python -m pip install -r requirements.txt

```



\### 3. Install VLC



Install VLC media player from the official VideoLAN website:



https://www.videolan.org/vlc/



Ensure VLC and its required libraries are available to python-vlc.



\### 4. Download the Vosk model



Download the small English model named `vosk-model-small-en-us-0.15` from:



https://alphacephei.com/vosk/models



Extract it into the project's `models` directory so the model files are available at:



```text

models/vosk-model-small-en-us-0.15/

```



The directory should contain the extracted model files, including `am`, `conf`, and `graph`.



\## Running the Application



From the repository root, provide one or more audio file paths.



Example on Windows:



```cmd

python -m src.integration\_app "C:\\path\\to\\first-song.mp3" "C:\\path\\to\\second-song.mp3"

```



Replace the example paths with the actual paths to your audio files.



The application starts listening for voice commands. Speak a supported command after the listening prompt.



Press `Ctrl+C` to stop the application.



\## Running Automated Tests



From the repository root, run:



```cmd

python -m pytest tests -v

```



The integration development branch has previously reported 18 passing tests and 9 passing subtests. Run the command again on the current commit to verify the latest result.



\## Privacy and Security



\- Raw audio is processed in memory by the speech recognition component and is not intentionally saved as a recording by that component.

\- Commands are checked against supported intents before execution.

\- Low-confidence and unsupported commands should be rejected.

\- The application should not execute arbitrary shell commands from recognized speech.



Privacy and security behavior should be reverified when components or configurations change.



\## Project Scope



The project focuses on voice-controlled multimedia playback, command validation, and integration with a media player.



Supported actions are limited to the nine commands listed above. Gesture recognition and camera-based control are outside the current scope.



\## Testing and Acceptance Criteria



The project acceptance criteria include:



\- At least 90% intent recognition accuracy.

\- At least 90% of recognized commands completed within 3 seconds.

\- Two-hour operation without a crash.

\- No unintended actions from invalid or low-confidence input.

\- Feedback within 2 seconds when feedback is enabled.

\- No retention of raw voice recordings.

\- Startup within 30 seconds.



These criteria must be verified through documented tests; successful manual playback alone does not establish that every criterion has passed.



\## Contributors



Team 10 — Software Engineering Mini Project.



Refer to the repository's project documentation and issue tracker for component ownership, requirements, architecture, and test planning.



