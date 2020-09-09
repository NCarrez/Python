import win32api


def get_windows_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split("\000")[:-1]
    return drives
