# WinTracker

WinTracker is a Python program designed to log usage statistics for applications and provide insights into how Windows is used. It records the active window's title and logs the time spent using each application.

## Features

- Tracks active window usage in real-time.
- Logs the time spent on each application.
- Outputs usage statistics to a JSON file.

## Requirements

- Python 3.x
- `psutil` library
- `pywin32` library (only required on Windows systems)

## Installation

Before running WinTracker, ensure you have the necessary dependencies installed. You can install them using pip:

```bash
pip install psutil pywin32
```

## Usage

To start logging application usage:

```bash
python wintracker.py
```

The program will log the active window's title and the time spent on each application until you stop it by pressing `Ctrl + C`. The usage statistics will be saved to a file named `usage_stats.json`.

## Notes

- The program relies on the `win32gui` module, which is part of the `pywin32` package, to get the active window title. It is necessary to run this on a Windows system.
- The default logging interval is set to 60 seconds. You can modify this by changing the `interval` parameter in the `log_application_usage` method.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.