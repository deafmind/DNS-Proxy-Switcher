import sys
import json
import subprocess
import ctypes
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QListWidget,
    QComboBox,
    QMessageBox,
    QFileDialog,
)


# Function to check for admin privileges and elevate if necessary
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()


# Function to set DNS on Windows
def set_dns(interface_name, dns_servers):
    try:
        # Clear existing DNS settings
        subprocess.run(
            [
                "netsh",
                "interface",
                "ip",
                "set",
                "dns",
                interface_name,
                "static",
                "none",
            ],
            check=True,
        )
        # Set new DNS servers
        for i, dns in enumerate(dns_servers, start=1):
            subprocess.run(
                [
                    "netsh",
                    "interface",
                    "ip",
                    "add",
                    "dns",
                    interface_name,
                    dns,
                    f"index={i}",
                ],
                check=True,
            )
        return True
    except Exception as e:
        print(f"Error setting DNS: {e}")
        return False


# Main Application Class
class ProxySwitcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proxy & DNS Switcher")
        self.setGeometry(100, 100, 400, 300)
        # Load configurations
        self.config_file = "../Config/config.json"
        self.load_config()
        # Layout
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # DNS Section
        self.dns_label = QLabel("Select DNS:")
        self.dns_combo = QComboBox()
        self.dns_combo.addItems(self.config["dns"].keys())
        self.dns_combo.currentTextChanged.connect(self.update_dns_description)
        self.dns_button = QPushButton("Set DNS")
        self.dns_button.clicked.connect(self.set_selected_dns)
        layout.addWidget(self.dns_label)
        layout.addWidget(self.dns_combo)
        layout.addWidget(self.dns_button)
        # Proxy Section
        self.proxy_label = QLabel("Open V2RayN:")
        self.proxy_button_open = QPushButton("Open V2RayN")
        self.proxy_button_open.clicked.connect(self.open_v2rayn)
        layout.addWidget(self.proxy_label)
        layout.addWidget(self.proxy_button_open)
        # Add DNS Section
        self.add_dns_label = QLabel("Add Custom DNS:")
        self.add_dns_name = QLineEdit(placeholderText="DNS Name")
        self.add_dns_server = QLineEdit(placeholderText="DNS Server (comma-separated)")
        self.add_dns_button = QPushButton("Add DNS")
        self.add_dns_button.clicked.connect(self.add_custom_dns)
        layout.addWidget(self.add_dns_label)
        layout.addWidget(self.add_dns_name)
        layout.addWidget(self.add_dns_server)
        layout.addWidget(self.add_dns_button)

    def load_config(self):
        try:
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {"dns": {}}

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def update_dns_description(self, dns_name):
        dns_info = self.config["dns"].get(dns_name, {})
        msg = f"Description: {dns_info.get('description', 'N/A')}\nServers: {', '.join(dns_info.get('servers', []))}"
        QMessageBox.information(self, "DNS Info", msg)

    def set_selected_dns(self):
        dns_name = self.dns_combo.currentText()
        dns_servers = self.config["dns"].get(dns_name, {}).get("servers", [])
        if dns_servers:
            if set_dns(
                "Wi-Fi", dns_servers
            ):  # Replace "Wi-Fi" with your network interface name
                QMessageBox.information(self, "Success", f"DNS set to {dns_name}")
            else:
                QMessageBox.warning(self, "Error", "Failed to set DNS")

    def open_v2rayn(self):
        try:
            v2rayn_path = r"D:\v2rayN-windows-64\v2rayn.exe"  # Full path to v2rayn.exe
            subprocess.Popen([v2rayn_path])  # Open V2RayN app
            QMessageBox.information(self, "Success", "V2RayN opened successfully.")
        except Exception as e:
            print(f"Error opening V2RayN: {e}")
            QMessageBox.warning(self, "Error", "Failed to open V2RayN")

    def add_custom_dns(self):
        dns_name = self.add_dns_name.text().strip()
        dns_servers = [
            s.strip() for s in self.add_dns_server.text().split(",") if s.strip()
        ]
        if dns_name and dns_servers:
            self.config["dns"][dns_name] = {
                "servers": dns_servers,
                "description": "Custom DNS",
            }
            self.save_config()
            self.dns_combo.addItem(dns_name)
            QMessageBox.information(self, "Success", "Custom DNS added")
        else:
            QMessageBox.warning(self, "Error", "Invalid DNS name or servers")


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProxySwitcher()
    window.show()
    sys.exit(app.exec_())
