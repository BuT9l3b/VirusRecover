from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import subprocess
import tkinter
import winreg
import ctypes
import admin
import sys
vers = '1.001'
programmer = 'BuT9l3b'
bg_col = 'gray17'


def theme_color():
    try:
        key_path = r"Software\VirusRecover"  # Проверяем наличие пути HKEY_CURRENT_USER\Software\VirusRecover
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        value_name = "theme"  # Проверяем наличие значения theme
        theme_value, _ = winreg.QueryValueEx(key, value_name)
        value_name1 = 'color'
        theme_value1, _ = winreg.QueryValueEx(key, value_name1)
        winreg.CloseKey(key)  # Закрываем ключ реестра
    except FileNotFoundError:
        key_path = r"Software\VirusRecover"  # Создаем папку VirusRecover
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        value_name = "theme"  # Устанавливаем значение theme равным "dark"
        theme_value = "dark"
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, theme_value)
        value_name1 = 'color'
        theme_value1 = 'blue'
        winreg.SetValueEx(key, value_name1, 0, winreg.REG_SZ, theme_value1)
        winreg.CloseKey(key)  # Закрываем ключ реестра
    return theme_value, theme_value1


class App:
    def __init__(self):
        self.theme, self.color = theme_color()
        self.window = ctk.CTk()
        self.window_settings()
        self.window_interface()
        self.window.mainloop()

    def window_settings(self):
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        ctk.set_appearance_mode(self.theme)
        ctk.set_default_color_theme(self.color)
        self.window.title('VirusRecover')
        self.window.geometry('500x180+600+360')
        global bg_col
        if self.theme == 'dark': bg_col = 'gray17'
        else: bg_col = 'gray86'
        self.window.resizable(False, False)

    def window_interface(self):
        ctk.CTkFrame(self.window, width=460, height=140).place(x=20, y=20)

        but1 = ctk.CTkButton(self.window, text='Разблокировка', width=200, height=38, font=('Arial', 20),
                             command=lambda: Root(self.window, 'Unlock', '520x190+600+360', 'unl'))
        but1.place(x=40, y=40)

        but2 = ctk.CTkButton(self.window, text='Диспетчер задач', width=200, height=38, font=('Arial', 20),
                             command=lambda: subprocess.Popen('Taskmgr.exe'))
        but2.place(x=260, y=40)

        but3 = ctk.CTkButton(self.window, text='Настройки', height=38, width=200, font=('Arial', 20),
                             command=lambda: Root(self.window, 'Settings', '500x180+600+360', 'set', but1))
        but3.place(x=40, y=100)

        but4 = ctk.CTkButton(self.window, text='О программе', height=38, width=200, font=('Arial', 20),
                             command=lambda: Root(self.window, 'Info', '300x200+600+360', 'inf'))
        but4.place(x=260, y=100)

        # ctk.CTkLabel(self.window, text=f"Разработчик: {programmer}").place(x=40, y=160)
        # ctk.CTkLabel(self.window, text=f"Версия: {vers}").place(x=260, y=160)

    def change_theme(self, selection):
        ctk.set_default_color_theme('green')
        pass


class Root:
    ret_icon = Image.open('res\\return56784.png')
    ret_icon = ctk.CTkImage(ret_icon, size=(30, 30))
    off_icon = Image.open('res\\off1767564.png')
    off_icon = ctk.CTkImage(off_icon, size=(30, 30))

    def __init__(self, win, title, resize,
                 com=None, but1=None, but2=None, but3=None, but4=None):
        self.title = title
        self.resize = resize
        self.win = win
        self.com = com

        self.but1 = but1
        self.but2 = but2
        self.but3 = but3
        self.but4 = but4

        self.win.withdraw()
        self.root = ctk.CTkToplevel(self.win)
        self.root_settings()
        self.boot_theme()
        if com == 'unl':
            self.unl()
        if com == 'inf':
            self.inf()
        if com == 'set':
            self.set()
        self.root.mainloop()

    def root_settings(self):
        self.root.title(self.title)
        self.root.geometry(self.resize)
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.ret)

    def boot_theme(self):
        but1 = ctk.CTkButton(self.win, text='Разблокировка', width=200, height=38, font=('Arial', 20),
                             command=lambda: Root(self.win, 'Unlock', '520x190+600+360', 'unl'))
        but1.place(x=40, y=40)
        but2 = ctk.CTkButton(self.win, text='Диспетчер задач', width=200, height=38, font=('Arial', 20),
                             command=lambda: subprocess.Popen('Taskmgr.exe'))
        but2.place(x=260, y=40)

        but3 = ctk.CTkButton(self.win, text='Настройки', height=38, width=200, font=('Arial', 20),
                             command=lambda: Root(self.win, 'Settings', '500x180+600+360', 'set', but1))
        but3.place(x=40, y=100)

        but4 = ctk.CTkButton(self.win, text='О программе', height=38, width=200, font=('Arial', 20),
                             command=lambda: Root(self.win, 'Info', '300x200+600+360', 'inf'))
        but4.place(x=260, y=100)

    def unl(self):
        frame = ctk.CTkFrame(self.root, width=440, height=170).place(x=60, y=10)
        but1 = ctk.CTkButton(self.root, text='', width=30, height=30, image=self.ret_icon, command=self.ret)
        but1.place(x=7, y=10)
        but2 = ctk.CTkButton(self.root, text='', width=30, height=30, image=self.off_icon, command=lambda: sys.exit(0))
        but2.place(x=7, y=60)
        ctk.CTkButton(self.root, text='Разблокировать regedit', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_regedit).place(x=70, y=20)
        ctk.CTkButton(self.root, text='Разблокировать диспетчер задач', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_taskmgr).place(x=290, y=20)
        ctk.CTkButton(self.root, text='Разблокировать кнопки питания', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_power_buttons).place(x=70, y=60)
        ctk.CTkButton(self.root, text='Разблокировать настройки', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_settings).place(x=290, y=60)
        ctk.CTkButton(self.root, text='Разблокировать сочетания клавиш', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_shortcut).place(x=70, y=100)
        ctk.CTkButton(self.root, text='Восстановить explorer', width=200, height=30, font=('Arial', 11),
                      command=Func.recover_explorer).place(x=290, y=100)
        ctk.CTkButton(self.root, text='Разблокировать клавишу win', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_win_button).place(x=70, y=140)
        ctk.CTkButton(self.root, text='Разблокировать диски', width=200, height=30, font=('Arial', 11),
                      command=Func.unblock_disks).place(x=290, y=140)

    def inf(self):
        frame = ctk.CTkFrame(self.root, width=280, height=180).place(x=10, y=10)
        but1 = ctk.CTkButton(self.root, text='', width=30, height=30, image=self.ret_icon, command=self.ret)
        but1.place(x=10, y=10)
        but2 = ctk.CTkButton(self.root, text='', width=30, height=30, image=self.off_icon, command=lambda: sys.exit(0))
        but2.place(x=244, y=10)
        ctk.CTkLabel(self.root, text='VirusRecover', bg_color=bg_col, font=('Arial', 20)).place(x=85, y=20)
        ctk.CTkLabel(self.root, text='Разработчик:', bg_color=bg_col, font=('Arial', 20)).place(x=20, y=80)
        ctk.CTkLabel(self.root, text='Версия:', bg_color=bg_col, font=('Arial', 20)).place(x=20, y=140)
        ctk.CTkLabel(self.root, text=programmer, bg_color=bg_col, font=('Arial', 20)).place(x=180, y=80)
        ctk.CTkLabel(self.root, text=vers, bg_color=bg_col, font=('Arial', 20)).place(x=180, y=140)

    def set(self):
        frame = ctk.CTkFrame(self.root, width=430, height=160).place(x=60, y=10)
        but1 = ctk.CTkButton(self.root, text='', width=30, height=30, image=self.ret_icon, command=self.ret)
        but1.place(x=7, y=10)
        but2 = ctk.CTkButton(self.root, text='', width=30, height=30, image=self.off_icon, command=lambda: sys.exit(0))
        but2.place(x=7, y=60)
        ctk.CTkLabel(self.root, text='Тема: ', bg_color=bg_col, font=('Arial', 20)).place(x=70, y=20)
        q = tkinter.StringVar(self.root)
        q.set('Выберите тему:')
        val = ['Тёмная-синяя', 'Тёмная-зелёная', 'Светлая-синяя', 'Светлая-зелёная']
        ctk.CTkOptionMenu(self.root, variable=q, values=val, width=220, font=('Arial', 20), command=self.change_theme).place(x=180, y=20)

    def change_theme(self, selection):
        global bg_col
        if selection == 'Тёмная-синяя' or selection == 'Тёмная-зелёная':
            theme = 'dark'
            bg_col = 'gray17'
        if selection == 'Светлая-синяя' or selection == 'Светлая-зелёная':
            theme = 'light'
            bg_col = 'gray86'
        if selection == 'Тёмная-синяя' or selection == 'Светлая-синяя':
            color = 'blue'
        if selection == 'Тёмная-зелёная' or selection == 'Светлая-зелёная':
            color = 'green'
        ctk.set_appearance_mode(theme)
        ctk.set_default_color_theme(color)

        key_path = r"Software\VirusRecover"  # Создаем папку VirusRecover
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, "theme", 0, winreg.REG_SZ, theme)
        winreg.SetValueEx(key, 'color', 0, winreg.REG_SZ, color)
        winreg.CloseKey(key)  # Закрываем ключ реестра

        self.root.destroy()
        Root(self.win, self.title, self.resize, self.com)

    def ret(self):
        self.win.deiconify()
        self.root.destroy()


class Func:
    @staticmethod
    def taskmgr():
        try:
            key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\System'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "DisableRegistryTools", 0, winreg.REG_DWORD, 0)
            subprocess.Popen('Taskmgr.exe')
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_regedit(mode: int = 1 | 0):
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "DisableRegistryTools", 0, winreg.REG_DWORD, 0)
            if mode == 1:
                messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            if mode == 1:
                messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_taskmgr():
        try:
            key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\System'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 0)
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_power_buttons():
        try:
            key_path1 = r'SOFTWARE\Microsoft\PolicyManager\default\Start\HideSleep'
            key_path2 = r'SOFTWARE\Microsoft\PolicyManager\default\Start\HideRestart'
            key_path3 = r'SOFTWARE\Microsoft\PolicyManager\default\Start\HideShutDown'
            key_path4 = r'SOFTWARE\Microsoft\PolicyManager\default\Start\HideHibernate'
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path1, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "value", 0, winreg.REG_DWORD, 0)
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path2, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "value", 0, winreg.REG_DWORD, 0)
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path3, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "value", 0, winreg.REG_DWORD, 0)
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path4, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "value", 0, winreg.REG_DWORD, 0)
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_settings():
        try:
            key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\Explorer'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "NoControlPanel", 0, winreg.REG_DWORD, 0)
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_shortcut():
        try:
            key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\Explorer'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "NoWinKeys", 0, winreg.REG_DWORD, 0)
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_win_button():
        try:
            key_path = r'SYSTEM\CurrentControlSet\Control\Keyboard Layout'
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "Scancode Map", 0, winreg.REG_DWORD, 0)
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def recover_explorer():
        try:
            subprocess.Popen('explorer.exe')
            key_path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, 'Shell', 0, winreg.REG_SZ, "explorer.exe")
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")

    @staticmethod
    def unblock_disks():
        try:
            Func.unblock_regedit(0)
            key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer'
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, 'NoDrives', 0, winreg.REG_DWORD, 0)
            messagebox.showinfo("Успех", "Операция выполнена успешно!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении операции: {e}")


if __name__ == '__main__':
    admin.run()
    app = App()
