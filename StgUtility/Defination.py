from itertools import count


class DefinationsEveryting:
    # ****************** GUI Adapter items *****************
    serial_c_open_buttons = None
    serialport_cmbbox = None
    radio_split = None
    radio_raw = None
    t1 = None
    treeview = None
    var_3 = None
    var_clr = None
    scrollbar = None
    frame_monitoring = None
    label_count_data = None
    label_file_location = None
    # ****************** END OF GUI Adapter items *****************

    # ****************** Serial Adapter items *****************
    myserial = None
    port = None
    bandRate = None
    databit = None
    stopbit = None
    read_data = None
    write_data = None
    port_list = None
    motor_freq = None
    motor_speed = None
    calclted_pwm = None
    click_fnc = None
    deinit_log_callback = None
    init_log_calllback = None
    pth = None
    iid = count()
    treeview_item_counter = 0
    serial_receive_counter = 0
    # ****************** END OF SerialAdapter items *****************

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
    val = b'?:1666\x00:3696\x00:30\x00\x00\x00*\x17\r\n'.decode('UTF-8').replace('\x00', '')
    val = val[:val.find('*') + 1]
    print(val, val.find('0'))
    treeview_rawdata = [
        ("", 1, val, ("Item 1", "Value 1")),
        (1, 2, val, ("Subitem 1.1", "Value 1.1")),
    ]

    def __init__(self, parents):
        # self.togglebutton = None
        self.adapter = None
        self.app = None

    def testfnc(self):
        pass
