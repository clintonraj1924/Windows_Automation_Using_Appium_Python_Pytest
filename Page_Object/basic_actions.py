import subprocess
import json


def remove_printer_driver_settings(driver_name):
    # PowerShell command to uninstall an app
    remove_driver_cmd = f'Remove-Printer -Name "{driver_name}"'
    # Execute PowerShell command
    try:
        subprocess.run(["powershell", "-Command", remove_driver_cmd])
        print(f"Printer driver '{driver_name}' removed successfully.")

    except Exception as e:
        print(f"An error occurred during the remove +'{driver_name}'+ driver!!!")
        assert False


def uninstall_app(app_name):
    # PowerShell command to uninstall an app
    uninstall_cmd = f'Get-AppxPackage -Name "{app_name}" | Remove-AppxPackage'

    # Execute PowerShell command
    try:
        subprocess.run(["powershell", "-Command", uninstall_cmd])
        print(f"HP Smart app Uninstalled successfully.")
    except Exception as e:
        print(f"An error occurred during HP Smart app uninstall!!!")


def install_app_store(app_id):
    # PowerShell command to uninstall an app
    install_app_cmd = f'winget install -e -i --id="{app_id}" --source=msstore'
    # Execute PowerShell command
    try:
        subprocess.run(["powershell", "-Command", install_app_cmd], capture_output=True, text=True, input="Y",
                       timeout=180)
        print(f"HP Smart App Installed successfully.")

    except Exception as e:
        print(f"An Error occurred during App install!!!")
        assert False


def get_data_from_json(key_data):
    file_path = 'Utilites\\commonData.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[key_data]
