import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QFrame, QAction, QMessageBox
)
from PyQt5.QtGui import QIcon, QFont, QDesktopServices
from PyQt5.QtCore import Qt, QUrl, QTimer
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BlackHole QuickTime Manager")
        self.setMinimumSize(600, 400)
        self.init_ui()
        self.check_blackhole_installed()
        self.check_multi_output_device()
        # Timer for recording
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.update_timer)
        self.record_seconds = 0

    def init_ui(self):
        # Central widget
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Header
        header = QHBoxLayout()
        app_label = QLabel("BlackHole QuickTime Manager")
        app_label.setFont(QFont("Arial", 18, QFont.Bold))
        header.addWidget(app_label)
        header.addStretch()
        status_icon = QLabel()
        status_icon.setPixmap(QIcon.fromTheme("dialog-information").pixmap(24, 24))
        header.addWidget(status_icon)
        main_layout.addLayout(header)

        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(divider)

        # Main Control Panel
        control_panel = QHBoxLayout()
        # Audio Routing Section
        audio_routing = QVBoxLayout()
        status_row = QHBoxLayout()
        self.blackhole_status = QLabel("BlackHole: Not detected")
        self.multi_output_status = QLabel("Multi-Output Device: Not configured")
        self.refresh_mod_btn = QPushButton("Refresh")
        self.refresh_mod_btn.setToolTip("Re-check Multi-Output Device status")
        self.refresh_mod_btn.clicked.connect(self.check_multi_output_device)
        # Create BlackHole website button before adding to layout
        self.blackhole_website_btn = QPushButton("Get BlackHole →")
        self.blackhole_website_btn.setVisible(False)
        self.blackhole_website_btn.clicked.connect(self.open_blackhole_website)
        # Create Setup Audio Routing button before adding to layout
        self.setup_audio_btn = QPushButton("Setup Audio Routing")
        self.setup_audio_btn.clicked.connect(self.setup_audio_routing)
        status_row.addWidget(self.multi_output_status)
        status_row.addWidget(self.refresh_mod_btn)
        status_row.addStretch()
        audio_routing.addWidget(self.blackhole_status)
        audio_routing.addWidget(self.blackhole_website_btn)
        audio_routing.addLayout(status_row)
        audio_routing.addWidget(self.setup_audio_btn)
        audio_routing.addStretch()
        control_panel.addLayout(audio_routing)
        # Recording Control Section
        recording_control = QVBoxLayout()
        self.record_btn = QPushButton("Start Recording")
        self.record_btn.setStyleSheet("font-size: 16px; padding: 12px;")
        self.record_btn.clicked.connect(self.handle_record_btn)
        self.timer_label = QLabel("00:00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        recording_control.addWidget(self.record_btn)
        recording_control.addWidget(self.timer_label)
        recording_control.addStretch()
        control_panel.addLayout(recording_control)
        main_layout.addLayout(control_panel)

        # Log / Status Area
        log_label = QLabel("Log / Status:")
        log_label.setFont(QFont("Arial", 10, QFont.Bold))
        main_layout.addWidget(log_label)
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setFont(QFont("Menlo", 10))
        main_layout.addWidget(self.log_area, stretch=1)

        # Settings Menu (gear icon in menu bar)
        settings_action = QAction(QIcon.fromTheme("preferences-system"), "Settings", self)
        settings_action.triggered.connect(self.open_settings)
        self.menuBar().addAction(settings_action)

    def check_blackhole_installed(self):
        try:
            result = subprocess.run([
                "system_profiler", "SPAudioDataType"
            ], capture_output=True, text=True, timeout=5)
            if "BlackHole" in result.stdout:
                self.blackhole_status.setText("BlackHole: Installed ✅")
                self.log_area.append("[INFO] BlackHole detected on system.")
                self.blackhole_website_btn.setVisible(False)
            else:
                self.blackhole_status.setText("BlackHole: Not detected ❌")
                self.log_area.append("[ERROR] BlackHole not found. Please install BlackHole from https://existential.audio/blackhole/.")
                self.blackhole_website_btn.setVisible(True)
        except Exception as e:
            self.blackhole_status.setText("BlackHole: Detection error ❌")
            self.log_area.append(f"[ERROR] Failed to check BlackHole: {e}")
            self.blackhole_website_btn.setVisible(True)

    def open_blackhole_website(self):
        QDesktopServices.openUrl(QUrl("https://existential.audio/blackhole/"))

    def open_settings(self):
        # Placeholder for settings dialog
        self.log_area.append("[INFO] Settings dialog opened (not implemented yet)")

    def check_multi_output_device(self):
        try:
            result = subprocess.run([
                "system_profiler", "SPAudioDataType"
            ], capture_output=True, text=True, timeout=5)
            output = result.stdout
            self.log_area.append("[DEBUG] system_profiler SPAudioDataType output:\n" + output)
            found_mod = False
            mod_name = None
            device_name = None
            output_channels = 0
            candidates = []
            for line in output.splitlines():
                line = line.strip()
                # Detect device name
                if line.endswith(":") and not line.startswith("Input") and not line.startswith("Output") and not line.startswith("Devices") and not line.startswith("Audio"):
                    device_name = line[:-1]
                    output_channels = 0
                # Detect output channels
                if line.startswith("Output Channels:"):
                    try:
                        output_channels = int(line.split(":")[1].strip())
                    except Exception:
                        output_channels = 0
                # If we have a device name and output channels > 0, check if it's a candidate
                if device_name and output_channels > 0:
                    if (
                        device_name != "BlackHole 2ch" and
                        device_name != "MacBook Air Speakers" and
                        not device_name.startswith("AirPods") and
                        not device_name.startswith("Nick's iPhone") and
                        not device_name.startswith("MacBook Air Microphone")
                    ):
                        candidates.append(device_name)
                        # Prefer a device named 'Record_Meeting' if present
                        if device_name == "Record_Meeting":
                            found_mod = True
                            mod_name = device_name
                            break
                    # Reset for next device
                    device_name = None
                    output_channels = 0
            if not found_mod and candidates:
                found_mod = True
                mod_name = candidates[0]
            if found_mod:
                self.multi_output_status.setText(f"Multi-Output Device: {mod_name} ✅")
                self.log_area.append(f"[INFO] Multi-Output Device detected: {mod_name}")
                self.log_area.append(f"[DEBUG] Candidate MODs: {candidates}")
            else:
                self.multi_output_status.setText("Multi-Output Device: Not configured ❌")
                self.log_area.append("[WARN] Multi-Output Device not found. Please set up audio routing.")
        except Exception as e:
            self.multi_output_status.setText("Multi-Output Device: Detection error ❌")
            self.log_area.append(f"[ERROR] Failed to check Multi-Output Device: {e}")

    def setup_audio_routing(self):
        # Try to open Audio MIDI Setup
        try:
            subprocess.run([
                "open", "/Applications/Utilities/Audio MIDI Setup.app"
            ], check=True)
            self.log_area.append("[INFO] Opened Audio MIDI Setup.")
        except Exception as e:
            self.log_area.append(f"[ERROR] Could not open Audio MIDI Setup: {e}")
        self.show_audio_routing_guide()

    def show_audio_routing_guide(self):
        self.log_area.append("""
[GUIDE] To create a Multi-Output Device with BlackHole:
1. In Audio MIDI Setup, click the '+' button at the bottom left and select 'Create Multi-Output Device'.
2. In the right panel, check both 'BlackHole' and your main output device (e.g., MacBook Speakers or Headphones).
3. (Optional) Rename the device to something memorable.
4. Right-click your new Multi-Output Device and select 'Use This Device For Sound Output'.
5. Return to this app and click the 'Refresh' button to re-check.
""")

    def handle_record_btn(self):
        if self.record_btn.text() == "Start Recording":
            self.start_quicktime_recording()
        else:
            self.stop_quicktime_recording()

    def start_quicktime_recording(self):
        self.log_area.append("[INFO] Launching QuickTime Player for audio recording...")
        threading.Thread(target=self._run_quicktime_applescript, daemon=True).start()
        self.record_btn.setText("Stop Recording")
        self.log_area.append("[INFO] Please click the red record button in QuickTime if it does not start automatically.")
        # Start timer
        self.record_seconds = 0
        self.timer_label.setText("00:00:00")
        self.record_timer.start(1000)

    def _run_quicktime_applescript(self):
        script = '''
        tell application "QuickTime Player"
            activate
            delay 1
            try
                close (every window whose name contains "Audio Recording")
            end try
            delay 0.5
            set newRecording to (new audio recording)
        end tell
        '''
        try:
            subprocess.run(["osascript", "-e", script], check=True)
            self.log_area.append("[INFO] QuickTime Player launched and new audio recording window opened. Please click the red record button in QuickTime.")
        except Exception as e:
            self.log_area.append(f"[ERROR] Failed to launch QuickTime Player: {e}\nPlease open QuickTime Player and start a new audio recording manually.")

    def stop_quicktime_recording(self):
        self.log_area.append("[INFO] Please manually stop and save the recording in QuickTime Player. (Full automation coming soon.)")
        self.record_btn.setText("Start Recording")
        # Stop timer
        self.record_timer.stop()
        self.record_seconds = 0
        self.timer_label.setText("00:00:00")

    def update_timer(self):
        self.record_seconds += 1
        hrs = self.record_seconds // 3600
        mins = (self.record_seconds % 3600) // 60
        secs = self.record_seconds % 60
        self.timer_label.setText(f"{hrs:02}:{mins:02}:{secs:02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 