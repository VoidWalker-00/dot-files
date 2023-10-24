import subprocess
import psutil

def get_wifi_state():
    try:
        # Get the SSID and signal strength
        output = subprocess.check_output(["iwconfig", "wlan0"]).decode()
        signal_strength_line = [line for line in output.split("\n") if "Signal level" in line][0]
        signal_strength = int(signal_strength_line.split("Signal level=")[1].split(" dBm")[0])
        # Define Wi-Fi states based on signal strength
        if signal_strength >= -40:
            return f" 󰤨"
        elif signal_strength >= -60:
            return f" 󰤥"
        elif signal_strength >= -70:
            return f" 󰤢"
        else:
            return f" 󰤟"
    except Exception:
        return " 󰤭"

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        return " 󰂄"
    elif battery.percent >= 99.00:
        return " 󱟢"
    elif battery.percent >= 90.00:
        return " 󰂂"
    elif battery.percent >= 70.00:
        return " 󰂀"
    elif battery.percent >= 50.00:
        return " 󰁾"
    elif battery.percent >= 30.00:
        return " 󰁼"
    elif battery.percent >= 10.00:
        return " 󰂃"
    else:
        return "Error"

if __name__ == "__main__":
    battery_info = get_battery_percentage()
    print(battery_info)

