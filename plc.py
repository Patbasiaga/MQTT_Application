import snap7
import snap7.types
from snap7.util import *
from snap7.types import *
from config import PLC_CONFIG


class PLC:

    IP = PLC_CONFIG.IP
    RACK = PLC_CONFIG.RACK
    SLOT = PLC_CONFIG.SLOT

    def __init__(self):
        self.state = ''
        self.plc_client = snap7.client.Client()
        self.datatype = S7WLDWord

    def connect_to_plc(self):
        self.plc_client.connect(PLC.IP, PLC.RACK, PLC.SLOT)
        self.state = self.plc_client.get_cpu_state()
        print(f'State {self.state}')

    def is_running(self):
        if self.state == "S7CpuStatusRun":
            return True

    def read_memory_block(self, db_number, start, size):
        result = self.plc_client.read_area(snap7.types.Areas.DB, db_number, start, size)
        #Add conversion to different type
        if True:
            return get_byte(result, 0)

    def write_memory_block(self, db_number, start, size, value):
        result = self.plc_client.read_area(snap7.types.Areas.DB, db_number, start, size)
        print(self.datatype)
        set_byte(result, 0, value)
        self.plc_client.write_area(snap7.types.Areas.DB, db_number, start, result)


