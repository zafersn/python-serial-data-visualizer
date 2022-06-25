import pickle
import time
from itertools import count
from pathlib import Path
from threading import Thread
from tkinter import ttk, filedialog

import SerialAdapter
from Defination import DefinationsEveryting
from LoggerHandler import LoggerHandler

logger_class = LoggerHandler()


def guiadapter_init():
    DefinationsEveryting.t1 = Thread(target=SerialAdapter.listen_serial)

def clicked_serialopen():
    if DefinationsEveryting.serial_c_open_buttons['text'] == "Open":
        DefinationsEveryting.serial_c_open_buttons.configure(text="Close")
        '''
               @ Serial Open Function
               :return:
               '''
        if DefinationsEveryting.port == None or DefinationsEveryting.port.isOpen() == False:
            DefinationsEveryting.myserial.open_port(DefinationsEveryting.serialport_cmbbox.get())
            if not DefinationsEveryting.t1.is_alive():
                DefinationsEveryting.t1 = None
                DefinationsEveryting.t1 = Thread(target=SerialAdapter.listen_serial)
                DefinationsEveryting.t1.start()
                DefinationsEveryting.init_log_calllback()
                # logger_class.init_logger()
            # else:
            #     self.t1.join()
            # print("Successfully opened serial port")
        else:
            pass
    else:
        DefinationsEveryting.serial_c_open_buttons.configure(text="Open")
        DefinationsEveryting.myserial.delete_port()
        DefinationsEveryting.t1.join()
        DefinationsEveryting.deinit_log_callback()
        # logger_class.deinit_logger()
        DefinationsEveryting.iid = count()

        print("Successfully closed serial port")

def get_all_children(tree, item=""):
    children = tree.get_children(item)
    numberOfChlid = 0
    for child in children:
        # children += get_all_children(tree, child)
        numberOfChlid = numberOfChlid + 1
    return numberOfChlid

def set_labl_count_data(text):
    DefinationsEveryting.label_count_data['text'] = text

def radio_raw_click():
    print("rawwwww")
    treeview_usb_data_init('v')

def radio_split_click():
    print("splittttt")
    treeview_usb_data_init('v')

def button_refrsh_click():
    DefinationsEveryting.myserial.show_port()
    port_list = DefinationsEveryting.myserial.get_port()
    port_str_list = []  # Used to store cut serial numbers
    print("list p: ", port_list)
    if not port_list:
        DefinationsEveryting.serialport_cmbbox["value"] = ('None')
        DefinationsEveryting.serialport_cmbbox.current(0)  # Select 0 by default
    else:
        for i in range(len(port_list)):
            # Cut out serial number
            lines = str(port_list[i])
            str_list = lines.split(" ")
            port_str_list.append(str_list[0])
        DefinationsEveryting.serialport_cmbbox["value"] = port_str_list
        DefinationsEveryting.serialport_cmbbox.current(0)  # Select 0 by default
    print("Successfully Refresh serial port")

def delete():
    # print( "selection", DefinationsEveryting.treeview.get_children(""))
    selected_item = DefinationsEveryting.treeview.get_children()[0] ## get selected item
    DefinationsEveryting.treeview.delete(selected_item)

def treeview_usb_data_init(x=None):
    if DefinationsEveryting.var_3.get() == 2:
        # Treeview
        DefinationsEveryting.treeview['columns'] = (1, 2)
        DefinationsEveryting.treeview.pack(expand=True, fill="both")
        DefinationsEveryting.scrollbar.config(command=DefinationsEveryting.treeview.yview)
        # Treeview columns
        DefinationsEveryting.treeview.column("#0", anchor="w")
        DefinationsEveryting.treeview.column(1, anchor="w")
        DefinationsEveryting.treeview.column(2, anchor="w")
        # Treeview Heading
        DefinationsEveryting.treeview.heading('#0', text="Speed")
        DefinationsEveryting.treeview.heading(1, text="Frequency")
        DefinationsEveryting.treeview.heading(2, text="PWM")
        # Insert treeview data
        # if x != 'v':
        #     for item in DefinationsEveryting.treeview_data:
        #         DefinationsEveryting.treeview.insert(
        #             parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
        #         )
        #         if item[0] == "" or item[1] in {8, 21}:
        #             DefinationsEveryting.treeview.item(item[1], open=True)  # Open parents
        #     # Select and scroll
        #     DefinationsEveryting.treeview.selection_set(10)
        #     DefinationsEveryting.treeview.see(7)
    elif DefinationsEveryting.var_3.get() == 3:
        DefinationsEveryting.treeview['columns'] = ''
        DefinationsEveryting.treeview.pack(expand=True, fill="both")
        DefinationsEveryting.scrollbar.config(command=DefinationsEveryting.treeview.yview)
        # Treeview columns
        DefinationsEveryting.treeview.column("#0", anchor="w", width=300)
        # Treeview Heading
        DefinationsEveryting.treeview.heading('#0', text="Raw")
        # if x != 'v':
        #     for item in DefinationsEveryting.treeview_rawdata:
        #         DefinationsEveryting.treeview.insert(
        #             parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
        #         )
        #         if item[0] == "" or item[1] in {8, 21}:
        #             DefinationsEveryting.treeview.item(item[1], open=True)  # Open parents
        #             # Select and scroll
        #     DefinationsEveryting.treeview.selection_set(2)
        #     DefinationsEveryting.treeview.see(2)
def open_file():
    # file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
    file = filedialog.askdirectory()
    if file:
        store_file_path(file + "/")
    else:
        return
    if file:
        logPath = str(file) + "/"
        DefinationsEveryting.label_file_location['text'] = logPath
        set_log_folder_directory(logPath)

        # self.main_class_obj.set_log_save_path(self.logPath)
        # timeFilename = time.strftime("%Y%m%d-%H%M%S") + '_log.txt'
        # pth = logPath + timeFilename
        # Label(win, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()
def set_log_folder_directory( path):
    log_path = path
    # print(".......: ", self.log_path)
    time_file_name = time.strftime("%Y%m%d-%H%M%S") + '_log.txt'
    DefinationsEveryting.pth = log_path + time_file_name
    print("new path: ", DefinationsEveryting.pth)

def store_file_path(file):
    dataset = [file]
    outputFile = 'pathstored.data'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()

def read_stored_file_path():
    inputFile = './pathstored.data'
    my_file = Path(inputFile)
    if my_file.exists():
        fd = open(inputFile, 'rb')
        dataset = pickle.load(fd)
        print(dataset)
        return dataset[0]
    else:
        return './'