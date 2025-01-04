class Lift_Dir:
    Lift_Up = "Up"
    Lift_Down = "Down"
    Lift_Stop = "Stop"

class Slider_Dir:
    In = 'In'
    Out = 'Out'
    Stop = 'stop'
class AGF_Work_Mode:
    Manual = "Manual"
    Auto = "Auto"

class Pallet_State:
    Pallet_Empty = "Empty"
    Pallet_Full = "Full"
    Pallet_None = "None"

class AGF_Work_Status:
    def __init__(self,agf_id:int):
        self.__agf_id = agf_id
        self.__agf_idle = False
        self.__agf_error = []
        self.__agf_work_mode = AGF_Work_Mode.Manual
        self.__pallet = False
        self.__task_list = []
        self.__task_current = {}
        self.__slider_speed = 0
        self.__slider_dir = Slider_Dir.Stop
        self.__lift_dir = Lift_Dir.Lift_Stop
        self.__lift_pos = 0
        self.__agf_charging = False
        self.__agf_sound_audio = ""
        self.__notices = "AMR Busy"

    
    def get_agf_work_status(self) -> dict:
        status = {
            "agf_id":self.__agf_id,
            "agf_idle":self.__agf_idle,
            "agf_error":self.__agf_error,
            "pallet":self.__pallet,
            "task_list":self.__task_list,
            "task_current":self.__task_current,
            "slider_speed":self.__slider_speed,
            "slider_dir":self.__slider_dir,
            "lift_dir":self.__lift_dir,
            "lift_pos":self.__lift_pos,
            "agf_work_mode":self.__agf_work_mode,
            "notices":self.__notices
        }
        return status
    
    @property
    def agf_id(self) -> int:
        return self.__agf_id
    @agf_id.setter
    def agf_id(self,id:int):
        self.__agf_id = id

    @property
    def agf_idle(self) -> bool:
        return self.__agf_idle
    @agf_idle.setter
    def agf_idle(self,idle:bool):
        self.__agf_idle = idle

    @property
    def agf_error(self) -> list:
        return self.__agf_error
    @agf_error.setter
    def agf_error(self,error:list):
        self.__agf_error = error

    @property
    def pallet(self) -> bool:
        return self.__pallet
    @pallet.setter
    def pallet(self,pallet:bool):
        self.__pallet = pallet
    
    @property
    def task_list(self) -> list:
        return self.__task_list
    @task_list.setter
    def task_list(self,task_list:list):
        self.__task_list = task_list

    @property
    def task_current(self) -> dict:
        return self.__task_current
    @task_current.setter
    def task_current(self,task_current:dict):
        self.__task_current = task_current

    @property
    def agf_work_mode(self) -> str:
        return self.__agf_work_mode
    @agf_work_mode.setter
    def agf_work_mode(self,mode:str):
        self.__agf_work_mode = mode

    @property
    def slider_speed(self):
        return self.__slider_speed
    @slider_speed.setter
    def slider_speed(self,speed:int):
        self.__slider_speed = speed

    @property
    def slider_dir(self):
        return self.slider_dir
    @slider_dir.setter
    def slider_dir(self,dir:int):
        if dir == 1:
            self.__slider_dir = Slider_Dir.In
        if dir == 2:
            self.__slider_dir = Slider_Dir.Out
        if dir == 0:
            self.__slider_dir = Slider_Dir.Stop

    @property
    def lift_dir(self):
        return self.__lift_dir
    @lift_dir.setter
    def lift_dir(self,dir:int):
        if dir == 2:
            self.__lift_dir = Lift_Dir.Lift_Up
        if dir == 1:
            self.__lift_dir = Lift_Dir.Lift_Down
        if dir == 0:
            self.__lift_dir = Lift_Dir.Lift_Stop
    
    @property
    def lift_pos(self):
        return self.__lift_pos
    @lift_pos.setter
    def lift_pos(self,pos:int):
        self.__lift_pos = pos


    @property
    def agf_sound_audio(self):
        return self.__agf_sound_audio
    @agf_sound_audio.setter
    def agf_sound_audio(self,audio:str):
        self.__agf_sound_audio = audio

    @property
    def notices(self):
        return self.__notices
    @notices.setter
    def notices(self,notice:str):
        self.notices = notice