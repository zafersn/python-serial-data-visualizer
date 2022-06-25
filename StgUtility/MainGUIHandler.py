import tkinter as tk
from tkinter import ttk

from Defination import DefinationsEveryting
import GUIAdapter


class App(DefinationsEveryting, ttk.Frame):

    def __init__(self, parents):
        ttk.Frame.__init__(self)

        # Make the app responsive
        self.notebook = None
        self.tab_1 = None
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        DefinationsEveryting.var_3 = tk.IntVar(value=3)
        DefinationsEveryting.var_clr = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)
        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Panedwindow **************************************************************
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=0, pady=(25, 5), sticky="nsew", rowspan=3, columnspan=3)

        # Notebook, pane #2 **************************************************************
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Notebook, pane #2 **************************************************************
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # ************************** TAB Definations **********************************************
        self.tab_1 = ttk.Frame(self.notebook)
        # for index in [0, 1]:
        #     self.tab_1.columnconfigure(index=index, weight=1)
        #     self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Serial")

        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Tab 2")

        # Tab #3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Tab 3")
        # **************************** END OF TAB Definations **********************************************

        # ****************************** TAB CONTENTS ***************************************

        # ****************************** Serial TAB CONTENTS ***************************************
        # ********************** Settings CONTENTS ************************
        # Create a Frame for the serial connection settings
        self.frame_settings = ttk.LabelFrame(self.tab_1, text="Settings", padding=(20, 10))
        self.frame_settings.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # ******** Serial PORT ----------

        self.serialport_frame = ttk.LabelFrame(self.frame_settings, text="Serial Port", padding=(20, 10))
        self.serialport_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        self.readonly_combo_list = ["None", "Item 1", "Item 2"]
        DefinationsEveryting.serialport_cmbbox = ttk.Combobox(
            self.serialport_frame, state="readonly", values=self.readonly_combo_list
        )
        DefinationsEveryting.serialport_cmbbox.current(0)
        DefinationsEveryting.serialport_cmbbox.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        # Button
        self.button_refresh_port = ttk.Button(self.serialport_frame, text="Refresh", command=GUIAdapter.button_refrsh_click)
        self.button_refresh_port.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        # ******** END OF Serial PORT ----------

        # ******** Baud Rate ----------

        self.baudrate_frame = ttk.LabelFrame(self.frame_settings, text="Baud Rate", padding=(20, 10))
        self.baudrate_frame.grid(
            row=1, column=0, rowspan=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        self.readonly_combo_list = ["4800", "9600", "14400", "19200", "38400", "57600",
                                    "115200"]
        self.readonly_combo = ttk.Combobox(
            self.baudrate_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(5)
        self.readonly_combo.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        # ********  END OF Baud Rate ----------

        # ******** Data Bits ----------

        self.data_bits_frame = ttk.LabelFrame(self.frame_settings, text="Data Bits", padding=(20, 10))
        self.data_bits_frame.grid(
            row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        self.readonly_combo_list = ["8", "9", "0"]
        self.readonly_combo = ttk.Combobox(
            self.data_bits_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        # ******** END OF Data Bits ----------

        # ******** Stop Bit ----------

        self.stop_bit_frame = ttk.LabelFrame(self.frame_settings, text="Stop Bit", padding=(20, 10))
        self.stop_bit_frame.grid(
            row=3, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        self.readonly_combo_list = ["1", "0"]
        self.readonly_combo = ttk.Combobox(
            self.stop_bit_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        # ******** END OF Stop Bit ----------


        # ******** Connect Button ----------

        DefinationsEveryting.serial_c_open_buttons = ttk.Checkbutton(
            self.frame_settings, text="Open", style="Toggle.TButton", command=GUIAdapter.clicked_serialopen
        )
        DefinationsEveryting.serial_c_open_buttons.grid(row=4, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        # ******** END OF Connect Button ----------

        # ******** Log File Save Location Bit ----------

        self.log_file_frame = ttk.LabelFrame(self.frame_settings, text="Log File Save Location", padding=(20, 10))
        self.log_file_frame.grid(
            row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Label
        DefinationsEveryting.label_file_location = ttk.Label(
            self.log_file_frame,
            text="C:\\Users\TR\\PycharmProjects\\loggingTest",
            justify="center",
            font=("-size", 9, "-weight", "normal"),
        )
        DefinationsEveryting.label_file_location.grid(row=0, column=0, pady=10, columnspan=2)
        # Button
        self.button_select_location = ttk.Button(self.log_file_frame, text="Select", command=GUIAdapter.open_file)
        self.button_select_location.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        # ******** END OF Log File Save Location ----------
        # ******** Monitoring Data Type Switcher ----------

        self.monitoring_data_frame = ttk.LabelFrame(self.frame_settings, text="Data Visualization Selector", padding=(20, 10))
        self.monitoring_data_frame.grid(
            row=1, column=1, rowspan=2, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Radiobuttons
        DefinationsEveryting.radio_raw = ttk.Radiobutton(
            self.monitoring_data_frame, text="Raw Data", variable=DefinationsEveryting.var_3, value=3, command=GUIAdapter.radio_raw_click
        )
        DefinationsEveryting.radio_raw.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        DefinationsEveryting.radio_split = ttk.Radiobutton(
            self.monitoring_data_frame, text="Split Data", variable=DefinationsEveryting.var_3, value=2, command=GUIAdapter.radio_split_click
        )
        DefinationsEveryting.radio_split.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        DefinationsEveryting.radio_both = ttk.Radiobutton(
            self.monitoring_data_frame, text="Both Data", variable=DefinationsEveryting.var_3, value=1,
            command=GUIAdapter.radio_split_click
        )
        DefinationsEveryting.radio_both.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        # ******** END OF Log Monitoring Data Type Switcher ----------
        # ******** Clear monitoring data Settings----------

        self.frame_clear_screen_data = ttk.LabelFrame(self.frame_settings, text="Clear screen when serial is open ",
                                                    padding=(20, 10))
        self.frame_clear_screen_data.grid(
            row=3, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Switch
        DefinationsEveryting.radio_clear_receivedta = ttk.Checkbutton(
            self.frame_clear_screen_data, text="Clear", style="Switch.TCheckbutton"
        )
        DefinationsEveryting.radio_clear_receivedta.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")
        # ******** END OF Clear monitoring data Settings ----------
        # **********************  END OF Serial Settings CONTENTS ************************

        # ********************** Monitoring CONTENTS ************************
        # Create a Frame for the serial connection settings
        DefinationsEveryting.frame_monitoring = ttk.LabelFrame(self.tab_1, text="Monitoring", padding=(20, 10))
        DefinationsEveryting.frame_monitoring.grid(
            row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        DefinationsEveryting.frame_monitoringdata = ttk.LabelFrame(DefinationsEveryting.frame_monitoring, text="Data", padding=(20, 10))
        DefinationsEveryting.frame_monitoringdata.grid(
            row=0, column=0, rowspan=6, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Scrollbar
        DefinationsEveryting.scrollbar = ttk.Scrollbar(DefinationsEveryting.frame_monitoringdata)
        DefinationsEveryting.scrollbar.pack(side="right", fill="y")
        # Define treeview data
        DefinationsEveryting.treeview = ttk.Treeview(
            DefinationsEveryting.frame_monitoringdata,
            selectmode="browse",
            yscrollcommand=DefinationsEveryting.scrollbar.set,
            height=10,
        )

        GUIAdapter.treeview_usb_data_init()
        # Create a Frame for the serial connection settings
        self.frame_nmbr_data = ttk.LabelFrame(DefinationsEveryting.frame_monitoring, text="Total Number of Data", padding=(20, 10))
        self.frame_nmbr_data.grid(
            row=6, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Label
        DefinationsEveryting.label_count_data = ttk.Label(
            self.frame_nmbr_data,
            text="0",
            justify="center",
            font=("-size", 9, "-weight", "normal"),
        )
        DefinationsEveryting.label_count_data.grid(row=3, column=0, pady=10, columnspan=2)

        # ********************** END OF Monitoring CONTENTS ************************

        # ****************************** END OF Serial TAB CONTENTS ***************************************

        # ****************************** END OF TAB CONTENTS ***************************************
        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


