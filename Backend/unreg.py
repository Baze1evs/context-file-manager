import winreg
import os
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def list_keys(path: str, hive=winreg.HKEY_CURRENT_USER) -> 'List of keys':
    """
    Returns a list of all the keys at a given registry path.
    """

    open_key = winreg.OpenKey(hive, path)
    key_amt = winreg.QueryInfoKey(open_key)[0]
    keys = []

    for count in range(key_amt):
        subkey = winreg.EnumKey(open_key, count)
        keys.append(subkey)

    return keys


def delete_key(path: str, hive=winreg.HKEY_CURRENT_USER):
    """
    Deletes the desired key and all other subkeys at the given path.
    """
    open_key = winreg.OpenKey(hive, path)
    subkeys = list_keys(path)

    if len(subkeys) > 0:
        for key in subkeys:
            delete_key(path + '\\' + key)
    winreg.DeleteKey(open_key, "")


def remove_menu(name: str, type: str):
    """
    Removes a context menu from the windows registry.
    """
    # run_admin()
    menu_path = os.path.join(type, name)
    delete_key(menu_path)


if __name__ == "__main__":
    if is_admin():
        remove_menu('FileSorter', 'Software\\Classes\\Directory\\Background\\shell')
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)
