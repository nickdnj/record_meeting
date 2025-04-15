# BlackHole QuickTime Manager Specification

## Overview

The **BlackHole QuickTime Manager** is a Python desktop application designed to simplify and automate the process of configuring audio routing using the BlackHole virtual audio driver and managing QuickTime audio recordings on macOS. The goal is to streamline the process for users—especially during Google Meet sessions—by providing an intuitive interface for setting up a Multi-Output Device, starting/stopping recordings, and restoring system audio settings.

## Target Platform

- **Operating System:** macOS (compatible with both Intel and Apple Silicon)
- **Prerequisites:**
  - **BlackHole:** Must be installed. Download from [BlackHole website](https://existential.audio/blackhole/).
  - **QuickTime Player:** Pre-installed on macOS.
  - **Python:** Version 3.8 or higher.

## Goals and Objectives

- **Ease of Use:** Offer a straightforward interface to manage audio routing and recording processes.
- **Automation:** Automate multiple system tasks like launching QuickTime in audio-record mode via AppleScript, creating a Multi-Output Device, and managing output settings.
- **Reliability:** Provide a stable solution for switching audio devices and recording without user hassles.
- **Feedback and Logging:** Display real-time status, provide logs for troubleshooting, and offer clear confirmation on actions.

## Core Functions

1. **Audio Routing Management**
   - **Detect BlackHole Installation:**  
     Automatically check for the presence of BlackHole and prompt installation instructions if missing.
   - **Create Multi-Output Device:**  
     Automate (or guide the user through) the creation of a Multi-Output Device that routes audio to both BlackHole and the user’s chosen output (speakers or headphones).
   - **Set Default Output Device:**  
     Enable the user to set the newly created Multi-Output Device as the system’s default audio output.

2. **QuickTime Recording Control**
   - **Launch QuickTime Player:**  
     Use AppleScript commands to open QuickTime Player in audio recording mode with BlackHole selected as the input.
   - **Start and Stop Recording:**  
     Provide controls to initiate and halt recording sessions, automatically triggering QuickTime’s recording functionality.
   - **Save and Manage Recordings:**  
     Save the recorded audio in a user-specified directory using a customizable filename scheme.
   - **Restore Audio Settings:**  
     Offer a simple mechanism to revert to the previous audio settings after recording is complete.

3. **Session Logging and Notifications**
   - **Activity Logging:**  
     Maintain and display logs of all operations, including setup steps, start/stop times for recordings, and any errors encountered.
   - **Real-Time Status Updates:**  
     Deliver immediate feedback and notifications regarding the current state of audio routing and recording sessions.

4. **Settings and Preferences**
   - **Configuration Panel:**  
     Allow users to modify settings such as:
     - Default audio output device selection.
     - Recording file save location.
     - Naming conventions for saved recordings.
     - Verbosity of logging and notifications.
   - **Automation Preferences:**  
     Enable customization of the level of automation for tasks like Multi-Output Device creation and QuickTime control.

## UI Design

The application will have a modern, simple, and functional interface. Below is the envisioned UI layout and design style.

### Style and Layout

- **Modern and Minimalistic:**  
  The design features a flat, clean, and uncluttered aesthetic with ample white space. Controls and icons are designed to be instantly recognizable and easy to use.

### Main Window Structure

1. **Header**
   - Displays the application name (e.g., "BlackHole QuickTime Manager").
   - Includes a status icon that indicates the overall system state (e.g., a green check for fully configured or an alert icon for issues).

2. **Main Control Panel**
   - **Audio Routing Section:**
     - Displays the current status of BlackHole installation and Multi-Output Device setup.
     - Features a button labeled **"Setup Audio Routing"** to initiate the configuration process.
   - **Recording Control Section:**
     - A large, prominent **"Start Recording"** button that toggles to **"Stop Recording"** when a session is active.
     - A display area showing a live timer of the recording duration.
   
3. **Log / Status Area**
   - A scrollable text window that shows real-time logs and notifications.
   - Uses a clear, monospace font to differentiate system logs from other UI elements.

4. **Settings Menu**
   - Accessible via a gear icon at the top right.
   - Contains configuration options such as:
     - Changing the default directory for saved recordings.
     - Adjusting filename conventions.
     - Toggling auto-restoration of system audio settings.
     - Viewing application info (version, credits, etc.).

### Interactivity and Responsiveness

- **Intuitive Controls:**  
  All buttons and interactive elements will have clear labels and tooltips to ensure user actions are self-explanatory.
  
- **Visual Feedback:**  
  Operations like "Setup Audio Routing" or "Start/Stop Recording" provide immediate visual cues (spinners, progress bars, or confirmation messages) to keep the user informed.
  
- **Responsive Design:**  
  The layout will adjust gracefully to window resizing, ensuring all elements remain accessible regardless of the window dimensions.

## System Architecture

- **UI Layer:**  
  Built using a modern GUI framework such as **PyQt5** (preferred for its modern look and advanced widget set) to create a dynamic and responsive interface.
  
- **Controller Layer:**  
  Orchestrates the overall workflow between the UI and system commands, including verifying BlackHole installation, starting and stopping recordings, and managing system settings.
  
- **Automation Module:**  
  Contains all scripts and AppleScript/`osascript` calls necessary for:
  - Launching QuickTime Player.
  - Configuring audio inputs and outputs.
  
- **Configuration Module:**  
  Uses a configuration file (INI or JSON format) to persist user settings and preferences for future sessions.

## Dependencies

- **Python Libraries:**
  - `subprocess` for executing system commands.
  - `os`, `sys`, and `pathlib` for file system operations.
  - GUI framework library (e.g., `PyQt5`).
  - `configparser` or `json` for configuration management.
- **External Tools:**
  - **BlackHole:** Must be installed separately.
  - **QuickTime Player:** Pre-installed on macOS.

## Open Questions / Clarifications

1. **Preferred GUI Framework:**  
   Based on our discussion, a modern interface using **PyQt5** is preferred for its rich, modern design components.

2. **Automation Scope:**  
   - How much of the Multi-Output Device creation should be automated versus guided with instructions?
   - Should the app handle any advanced QuickTime control features, or simply trigger and monitor the process?

3. **User Permissions:**  
   - Clarification on any required admin privileges for altering system audio settings.
   
4. **File Management Details:**  
   - Specific filename conventions and additional post-processing features for the recorded files if required.
   
5. **Future Expansion:**  
   - Consider if scheduling recordings or additional automation features might be needed later.

## Conclusion

This updated specification outlines all the necessary functions and a modern, simple, yet functional user interface for the BlackHole QuickTime Manager app. With a focus on ease of use, automation, and clear user feedback, this tool is designed to help users efficiently manage audio routing and recording sessions on macOS.

Please review the above details and let me know if there are further refinements or additional functionalities you would like to incorporate.
