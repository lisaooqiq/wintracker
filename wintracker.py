import psutil
import time
import json
from datetime import datetime

class WinTracker:
    def __init__(self):
        self.usage_data = {}

    def log_application_usage(self, interval=60):
        """
        Logs the active window usage statistics every 'interval' seconds.
        """
        print("Starting WinTracker...")
        try:
            while True:
                active_window = self.get_active_window()
                if active_window:
                    self.record_usage(active_window)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopping WinTracker...")
            self.save_usage_stats()

    def get_active_window(self):
        """
        Retrieves the title of the currently active window.
        """
        # This functionality is platform dependent; here we use Windows API
        try:
            import win32gui
            window = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window)
            return window_title
        except ImportError:
            print("win32gui module is required on Windows systems.")
            return None

    def record_usage(self, window_title):
        """
        Records the usage time for the given window title.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if window_title not in self.usage_data:
            self.usage_data[window_title] = []
        self.usage_data[window_title].append(current_time)
        print(f"Window: {window_title} | Time: {current_time}")

    def save_usage_stats(self, filename='usage_stats.json'):
        """
        Saves the logged usage data to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump(self.usage_data, file, indent=4)
        print(f"Usage statistics saved to {filename}")

if __name__ == "__main__":
    tracker = WinTracker()
    tracker.log_application_usage()