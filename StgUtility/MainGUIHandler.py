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
        self.var_3 = tk.IntVar(value=2)
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
        self.readonly_combo = ttk.Combobox(
            self.serialport_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        # Button
        self.button_refresh_port = ttk.Button(self.serialport_frame, text="Refresh")
        self.button_refresh_port.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        # ******** END OF Serial PORT ----------

        # ******** Baud Rate ----------

        self.baudrate_frame = ttk.LabelFrame(self.frame_settings, text="Baud Rate", padding=(20, 10))
        self.baudrate_frame.grid(
            row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
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

        DefinationsEveryting.togglebuttons = ttk.Checkbutton(
            self.frame_settings, text="Open", style="Toggle.TButton", command=GUIAdapter.clicked_rf1
        )
        DefinationsEveryting.togglebuttons.grid(row=4, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        # ******** END OF Connect Button ----------

        # ******** Log File Save Location Bit ----------

        self.log_file_frame = ttk.LabelFrame(self.frame_settings, text="Log File Save Location", padding=(20, 10))
        self.log_file_frame.grid(
            row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Label
        self.label_file_location = ttk.Label(
            self.log_file_frame,
            text="C:\\Users\TR\\PycharmProjects\\loggingTest",
            justify="center",
            font=("-size", 9, "-weight", "normal"),
        )
        self.label_file_location.grid(row=0, column=0, pady=10, columnspan=2)
        # Button
        self.button_select_location = ttk.Button(self.log_file_frame, text="Select")
        self.button_select_location.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        # ******** END OF Log File Save Location ----------
        # ******** Monitoring Data Type Switcher ----------

        self.monitoring_data_frame = ttk.LabelFrame(self.frame_settings, text="Data Visualization Selector", padding=(20, 10))
        self.monitoring_data_frame.grid(
            row=1, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Radiobuttons
        self.radio_raw = ttk.Radiobutton(
            self.monitoring_data_frame, text="Raw Data", variable=self.var_3, value=1
        )
        self.radio_raw.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_split = ttk.Radiobutton(
            self.monitoring_data_frame, text="Split Data", variable=self.var_3, value=2
        )
        self.radio_split.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        # ******** END OF Log Monitoring Data Type Switcher ----------

        # **********************  END OF Serial Settings CONTENTS ************************

        # ********************** Monitoring CONTENTS ************************
        # Create a Frame for the serial connection settings
        self.frame_monitoring = ttk.LabelFrame(self.tab_1, text="Monitoring", padding=(20, 10))
        self.frame_monitoring.grid(
            row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame_monitoring)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.frame_monitoring,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)
        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)
        # Treeview Heading
        self.treeview.heading('#0', text="Speed")
        self.treeview.heading(1, text="Frequency")
        self.treeview.heading(2, text="PWM")

        # Define treeview data
        treeview_data = [
            ("", 1, "Parent", ("Item 1", "Value 1")),
            (1, 2, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 3, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 4, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 5, "Child", ("Subitem 1.4", "Value 1.4")),
            ("", 6, "Parent", ("Item 2", "Value 2")),
            (6, 7, "Child", ("Subitem 2.1", "Value 2.1")),
            (6, 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
            (8, 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
            (8, 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
            (8, 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
            (6, 12, "Child", ("Subitem 2.3", "Value 2.3")),
            (6, 13, "Child", ("Subitem 2.4", "Value 2.4")),
            ("", 14, "Parent", ("Item 3", "Value 3")),
            (14, 15, "Child", ("Subitem 3.1", "Value 3.1")),
            (14, 16, "Child", ("Subitem 3.2", "Value 3.2")),
            (14, 17, "Child", ("Subitem 3.3", "Value 3.3")),
            (14, 18, "Child", ("Subitem 3.4", "Value 3.4")),
            ("", 19, "Parent", ("Item 4", "Value 4")),
            (19, 20, "Child", ("Subitem 4.1", "Value 4.1")),
            (19, 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
            (21, 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
            (21, 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
            (21, 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
            (19, 25, "Child", ("Subitem 4.3", "Value 4.3")),
            ("", 26, "Parent", ("Item 1", "Value 1")),
            (1, 27, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 28, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 29, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 30, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 31, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 32, "Child", ("Subitem 1.3", "Value 1.3")),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                self.treeview.item(item[1], open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set(10)
        self.treeview.see(7)
        # ********************** END OF Monitoring CONTENTS ************************

        # ****************************** END OF Serial TAB CONTENTS ***************************************

        # ****************************** END OF TAB CONTENTS ***************************************
        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


