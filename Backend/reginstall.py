import winreg
import os
import ctypes


rootPath = 'Software\\Classes\\Directory\\Background\\shell\\FileSorter'


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def format_command(param):
    return '"{}" {}'.format(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\main.exe'), param)


def set_value(path, variable, value):
    registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, variable, 0, winreg.REG_SZ, value)
    winreg.CloseKey(registry_key)


def create_menu(path, caption):
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    set_value(path, 'MUIVerb', caption)
    set_value(path, 'subcommands', '')
    path = os.path.join(path, 'shell')
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    return path


def create_command(path, name, command):
    path = os.path.join(path, name.replace(' ', '_'))
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    set_value(path, '', name)
    path = os.path.join(path, 'command')
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, path)
    set_value(path, '', command)


def install():
    global rootPath

    rootPath = create_menu(rootPath, 'Отсортировать')

    qtype_command = format_command('--qtype')
    create_command(rootPath, 'Тип', qtype_command)

    extract_command = format_command('--extract')
    create_command(rootPath, 'Извлечь', extract_command)

    qext_command = format_command('--qextension')
    create_command(rootPath, 'Расширение', qext_command)

    tuner_command = os.path.join('"C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\tuner.exe"')
    create_command(rootPath, 'Подробнее...', tuner_command)


if __name__ == "__main__":
    if is_admin():
        install()
