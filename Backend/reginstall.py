import winreg
import os
import sys
import ctypes
# Ok, so we have to make a Windows registry install for cascading menus


# Takes the registry path, creates it if it doesn't exist, then sets the value
rootPath = 'Software\\Classes\\Directory\\Background\\shell\\FileSorter'
pyLoc = sys.executable
scriptLoc = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'main.py')  # Location of parser to be called


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def formatCommand(param):
    global pyLoc, scriptLoc
    return '"{}" {}'.format(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\main.exe'), param)


def setValue(path, variable, value):
    registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path, 0,
                                  winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, variable, 0, winreg.REG_SZ, value)
    winreg.CloseKey(registry_key)


def createMenu(path, caption):
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    setValue(path, 'MUIVerb', caption)
    setValue(path, 'subcommands', '')
    path = os.path.join(path, 'shell')
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    return path


def createCommand(path, name, command):
    path = os.path.join(path, name.replace(' ', '_'))
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    setValue(path, '', name)
    path = os.path.join(path, 'command')
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    setValue(path, '', command)


def install():
    global rootPath

    # Creating the original entry
    rootPath = createMenu(rootPath, 'Отсортировать')

    # Adding each option to the context menu

    # Quick sort by type
    typeCommand = formatCommand('--qtype')
    createCommand(rootPath, 'Тип', typeCommand)
    # Extract files
    extractCommand = formatCommand('--extract')
    createCommand(rootPath, 'Извлечь', extractCommand)
    # Quick sort by extension
    extensionCommand = formatCommand('--qextension')
    createCommand(rootPath, 'Расширение', extensionCommand)
    # Setting menu
    settingsCommand = os.path.join('"C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\tuner.exe"')
    createCommand(rootPath, 'Подробнее...', settingsCommand)


if __name__ == "__main__":
    if is_admin():
        install()
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)


# Computer\HKEY_CLASSES_ROOT\Directory\shell
