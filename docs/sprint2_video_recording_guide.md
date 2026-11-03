# Sprint 2 Video Recording Guide & Storyboard (2-Minute Working Product)

**Deliverable Reference:** SE Mini-Project Deliverables Part-2, Item 3.b:  
> *"Record a two minute video of the outcome of the second Sprint. [It should be a working product]. Upload it to the repo."*

**Speaker / Presenter:** Hemant Ram Nelapati (PES2UG24CS192)  
**Total Target Duration:** 1 minute 55 seconds – 2 minutes 00 seconds (Strict 2-minute limit)  
**Recording Tool:** Windows Game Bar (`Win + Alt + R`) or OBS Studio / Loom  

---

## 1. Recording Setup & Preparation

1. **Terminal:** Open PowerShell in `H:\Sem-5\SE\Team-10-Voice-Assistant-Multimedia-Controls`.
   Ensure terminal font is large and readable (e.g., 16pt / 18pt font).
2. **Audio:** Ensure your PC speakers or headphones are audible so the synthetic audio tones from VLC can be heard in the recording.
3. **Command to Run:**
   ```powershell
   .\.venv\Scripts\python.exe scripts\demo_media_controller.py --auto
   ```
4. **Second Tab / Window (Optional for Test Proof):**
   ```powershell
   .\.venv\Scripts\python.exe -m pytest -q
   ```

---

## 2. Minute-by-Minute Storyboard & Spoken Script

### [0:00 – 0:18] Introduction & Context
- **Visual:** Terminal showing the clean banner for `scripts/demo_media_controller.py`.
- **Spoken Script:**
  > *"Hello everyone. I am Hemant Ram Nelapati, USN PES2UG24CS192, presenting the Sprint 2 working product demonstration for Team 10: Voice Assistant for Multimedia Controls. In Sprint 2, my focus was on implementing the complete suite of extended media controls, volume boundary clamping, circular playlist navigation, and libVLC exception shielding."*

---

### [0:18 – 0:42] Launch Demo: Play, Pause & Resume Execution
- **Visual:** Terminal executes `demo_media_controller.py --auto`. Step 1 (PLAY), Step 2 (PAUSE), Step 3 (RESUME) execute.
- **Spoken Script:**
  > *"Here I launch our live working product demo. The controller initializes our native libVLC engine and loads our playlist. First, the PLAY intent begins audio streaming of Track 1. Next, the PAUSE intent halts playback while preserving the exact buffer position. When we issue RESUME, playback seamlessly continues from where it left off without re-buffering."*

---

### [0:42 – 1:05] Volume Clamping & Defensive Audio Controls
- **Visual:** Step 4 (VOLUME_UP), Step 5 (VOLUME_UP to 90%), Step 6 (VOLUME_DOWN to 80%).
- **Spoken Script:**
  > *"Next are the volume controls. VOLUME_UP increments playback volume in 10% steps from 70 to 80 and then to 90. VOLUME_DOWN decrements volume cleanly. Crucially, as required by non-functional security specifications, our volume logic enforces strict boundary clamping between 0 and 100 percent, preventing any audio overflow or device driver crashes."*

---

### [1:05 – 1:32] Circular Playlist Navigation & Mute Toggling
- **Visual:** Step 7 (NEXT to Track 2), Step 8 (PREVIOUS back to Track 1), Step 9 (MUTE ON), Step 10 (MUTE OFF).
- **Spoken Script:**
  > *"For playlist navigation, the NEXT intent triggers circular navigation, transitioning smoothly to Track 2. Issuing PREVIOUS returns us circularly to Track 1 with zero index bounds errors. Following this, the MUTE intent toggles the audio stream to silent, and a subsequent MUTE restores audio output with synchronized internal state."*

---

### [1:32 – 1:48] STOP Command & Clean State Reset
- **Visual:** Step 11 (STOP). State shows `Playing=False, Paused=False`.
- **Spoken Script:**
  > *"Finally, the STOP command halts audio playback entirely, releases the media resource, and resets the player state back to initial idle ready for future voice commands."*

---

### [1:48 – 2:00] Automated Test Verification & Freeze Sign-off
- **Visual:** Quickly execute `.\.venv\Scripts\python.exe -m pytest -q` showing `105 passed in 0.32s`.
- **Spoken Script:**
  > *"All 9 voice commands are backed by 39 comprehensive unit tests in our media controller suite, contributing to our project's full 105 passing automated tests. All features have been merged into main via PR #1, and our Sprint 2 development cycle is officially frozen. Thank you!"*

---

## 3. Video File Saving & Submission Checklist

- [ ] Save the video as `Team10_Sprint2_Demo_Hemant.mp4`.
- [ ] Verify video length: **<= 2 minutes (120 seconds)**.
- [ ] Check audio balance: Voice is clear and VLC tones are audible.
- [ ] Store in `docs/demo_video/` or upload to YouTube/Google Drive link per instructor submission instructions.
