import tkinter as tk
from tkinter import ttk

import GUIAdapter
import SerialAdapter
from Defination import DefinationsEveryting
from LoggerHandler import LoggerHandler
from MainGUIHandler import App

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Utility")

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)
    logger_class = LoggerHandler()
    DefinationsEveryting.myserial = SerialAdapter
    SerialAdapter.serial_init()
    SerialAdapter.serial_config(logger_class.log_serial_data, logger_class.deinit_logger, logger_class.init_logger)
    GUIAdapter.guiadapter_init()
    GUIAdapter.set_log_folder_directory(GUIAdapter.read_stored_file_path())
    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    root.mainloop()
