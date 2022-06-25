from tkinter.constants import INSERT

import serial
import serial.tools.list_ports

import GUIAdapter
from Defination import DefinationsEveryting


def serial_init(band=57600, data=8, stop=1):
    # Get Available Serial Ports
    DefinationsEveryting.port_list = list(serial.tools.list_ports.comports())
    # assert (len(self.port_list) != 0), "No Serial Port Available"

    DefinationsEveryting.bandRate = band
    DefinationsEveryting.databit = data
    DefinationsEveryting.stopbit = stop
    # Read and write data
    DefinationsEveryting.read_data = None
    DefinationsEveryting.write_data = None


def serial_config(cc_fnc, deinit_callback, initlog_callback):
    print("serial opeenneed...")
    DefinationsEveryting.click_fnc = cc_fnc
    DefinationsEveryting.deinit_log_callback = deinit_callback
    DefinationsEveryting.init_log_calllback = initlog_callback

def show_port():
    for i in range(0, len(DefinationsEveryting.port_list)):
        print(DefinationsEveryting.port_list[i])


# Return to Serial Port
def get_port():
    DefinationsEveryting.port_list = list(serial.tools.list_ports.comports())
    return DefinationsEveryting.port_list


# Open Serial Port
def open_port(port):
    DefinationsEveryting.port = serial.Serial(port, DefinationsEveryting.bandRate, timeout=.3)


def delete_port():
    if DefinationsEveryting.port is not None:
        DefinationsEveryting.port.close()
        print("Close Serial Port Complete")
    else:
        pass
def read_data_fnc():
    # self.read_data = self.port.read(self.port.in_waiting)  # Read data
    DefinationsEveryting.read_data = DefinationsEveryting.port.readline()  # Read data
    # lines = [x.decode('utf8').strip() for x in f.readlines()]

    # print("ser val: ", self.read_data)
    # return self.read_data.decode("utf-8")
    return DefinationsEveryting.read_data

def write_data_fnc(data):
    if not DefinationsEveryting.port.isOpen():
        print("Serial port open error")
    else:
        DefinationsEveryting.port.write(data.encode("utf-8"))  # Returns the number of bytes written

def listen_serial():
    first_start = True
    while DefinationsEveryting.port.isOpen():
        value = read_data_fnc()
        if value:
            # print("111: ", value)
            if len(value) >= 17:
                if value[0] != ord('?'):
                    print("corrupted Value:", chr(value[0]))
                else:

                    DefinationsEveryting.serial_receive_counter += 1
                    GUIAdapter.set_labl_count_data(DefinationsEveryting.serial_receive_counter)
                    # print("2222: ", value)  # printing the value
                    frq = value[value.find(b':') + 1: value.find(b':', 2)].decode("cp437")
                    frq = frq[:frq.find('\x00')]
                    # print("frq: ", frq[:frq.find('\x00')])
                    spd = value[value.find(b':', 2) + 1: value.find(b':', 8)].decode("cp437")
                    spd = spd[:spd.find('\x00')]
                    # print("spd: ", spd[:spd.find('\x00')] )

                    pwm = value[value.find(b':', 8) + 1: value.find(b'*')].decode("cp437")
                    pwm = pwm[:pwm.find('\x00')]
                    # print("pwm: %s frq: %s spd %s" % (pwm, frq, spd))
                    if frq:
                        DefinationsEveryting.motor_freq = int(frq)
                    if spd:
                        DefinationsEveryting.motor_speed = int(spd)
                    if pwm:
                        DefinationsEveryting.calclted_pwm = int(pwm)
                    # print("f: %d, s: %d, p: %d" % (motorFreq, motorSpeed, pwm))
                    if frq and spd and pwm:
                        DefinationsEveryting.click_fnc(DefinationsEveryting.motor_freq, DefinationsEveryting.motor_speed, DefinationsEveryting.calclted_pwm, next(DefinationsEveryting.iid))
                        first_start = False
                        # label10['text'] = str(DefinationsEveryting.iid)[str(DefinationsEveryting.iid).find('(') + 1:-1]
                    # log_serial_data(motorFreq, motorSpeed, pwm, self.iid)
                    if DefinationsEveryting.serial_receive_counter % 100 == 0:
                        DefinationsEveryting.treeview.insert(
                            parent="", index="end", text=str(value)
                        )
                        DefinationsEveryting.treeview_item_counter += 1

                        if DefinationsEveryting.treeview_item_counter > 15:
                            GUIAdapter.delete()
            else:
                print("corrrrrrrpttttttt")