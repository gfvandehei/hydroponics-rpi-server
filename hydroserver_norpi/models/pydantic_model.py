from pydantic import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id: int
    firstname: str
    lastname: str
    username: str
    email: str
    password: str
    salt: str
    admin: bool

class System(BaseModel):
    __tablename__="systems"

    id: int
    name: str
    address: str

class UserPermission(BaseModel):
    __tablename__ = "user_permissions"

    user_id: int
    system: int


class Camera(BaseModel):
    __tablename__ = "cameras"
    
    id: int
    name: str
    index: int
    system_id: int
    camera_store_id: int

class CameraGimbal(BaseModel):
    __tablename__ = "camera_gimbals"

    id: int
    camera_id: int
    x_servo_id: int
    y_servo_id: int


class CameraStore(BaseModel):
    __tablename__= "camera_stores"

    id: int
    name: str
    fs_path: str
    image_save_time: str
    system_id: int

class Servo(BaseModel):
    __tablename__ = "servos"

    id: int
    label: str
    pin: int
    system_id: int

class Pump(BaseModel):
    __tablename__ = "pumps"

    id: int
    label: str
    pin: int
    system_id: int
    time_to_fill: int

class PumpScheduleEntry(BaseModel):
    __tablename__ = "pump_schedule"

    id: int
    action: str
    pump_id: int
    #system_id = Column(Integer, ForeignKey("systems.id")) # this could optimize queries but I dont think it will be a realistic use case subquery will slow enough
    days_active: str #M,T,W,TH,F,S,SU
    times: str # datetime iso string delimited by commas

    
class DHTSensor(BaseModel):
    __tablename__="dht_sensors"

    id: int
    label: str
    pin: int
    dht_type: str
    system_id: int