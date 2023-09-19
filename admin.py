import ctypes
import sys


def run_as_admin():
    if sys.platform.startswith('win'):
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except:
            sys.exit(1)
    else:
        print("Запрос прав администратора доступен только в Windows.")
        sys.exit(1)


def run():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        run_as_admin()
        sys.exit(0)  # Закрыть текущее приложение, так как оно будет перезапущено от имени администратора
