![Logo](logo.png)
# Proxy & DNS Switcher

## Description
The Proxy & DNS Switcher is a user-friendly Python application designed to simplify the management of DNS settings and proxy configurations on Windows systems. Built using PyQt5 for its graphical interface, this tool allows users to effortlessly switch between predefined or custom DNS servers and launch the V2RayN proxy application with just a few clicks. The application automatically elevates privileges when needed to ensure seamless system-level changes.

This tool is particularly useful for users who frequently change their network configurations or rely on specific DNS providers for enhanced privacy, security, or access to geo-restricted content. Additionally, it streamlines the process of managing proxy settings by directly integrating with the V2RayN application.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Proxy & DNS Switcher is a Python-based application that allows users to easily switch between different DNS servers and toggle a V2RayN proxy on and off. The application is built using PyQt5 for the graphical user interface and includes functionality for managing DNS settings and proxy configurations on a Windows system.

## Features
### DNS Management
- Select from predefined DNS servers.
- Add custom DNS servers.
- View descriptions and server details for each DNS option.
- Apply selected DNS settings to the network interface.

### Proxy Management
- Open the V2RayN proxy application directly from the app.
- Automatically elevate privileges to ensure the application has the necessary permissions to modify system settings.

*Note: In the updated version, the "Enable/Disable Proxy" functionality has been replaced with a single button to open the V2RayN application.*

## Requirements
- **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **PyQt5**: Install PyQt5 using pip:
  ```sh
  pip install pyqt5
  ```
- **Windows Operating System**: The application is designed for Windows and requires administrative privileges to modify DNS and proxy settings.
- **V2RayN Application**: Download and install V2RayN from [GitHub](https://github.com/2dust/v2rayN/releases). Update the path in the script to match the location of your `v2rayn.exe`.

## Installation
### Clone the Repository
Obtain the source code by cloning the repository:
```sh
git clone https://github.com/yourusername/proxy-dns-switcher.git
cd proxy-dns-switcher
```

### Set V2RayN Path
Ensure the path to `v2rayn.exe` in the script matches the installation location on your system. Update the `v2rayn_path` variable in the `main.py` file accordingly.

## Usage
### Run the Application
Execute the script using Python:
```sh
python /d:/ProxySwitch/codes/main.py
```

### Use the Graphical Interface
- Use the dropdown menu to select a DNS provider and click "Set DNS" to apply the settings.
- Add custom DNS entries by entering a name and server addresses, then clicking "Add DNS."
- Click "Open V2RayN" to launch the V2RayN application.

*To enable the V2RayN app, ensure you update the script with the correct directory path based on your V2RayN installation.*

### Create an Executable
To create a standalone executable for the application, use PyInstaller:
```sh
pyinstaller --onefile --windowed --icon=logo.ico --hidden-import=resources_rc main.py
```
This will generate a single executable file that you can run without needing to install Python or any dependencies.

## Configuration
The application loads DNS configurations from a JSON file located at `../Config/config.json`. Ensure this file exists and contains the necessary DNS entries. Here’s an example structure:
```json
{
  "dns": {
    "Google Public DNS": {
      "servers": ["8.8.8.8", "8.8.4.4"],
      "description": "Google's public DNS servers"
    },
    "Cloudflare DNS": {
      "servers": ["1.1.1.1", "1.0.0.1"],
      "description": "Cloudflare's public DNS servers"
    }
  }
  .
  .
  .
}
```
You can add or modify entries in this file to include additional DNS providers.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

