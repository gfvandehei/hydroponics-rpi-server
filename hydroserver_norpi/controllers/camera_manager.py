from typing import List
from hydroserver.controllers.camera_manager import CameraManager
import hydroserver_norpi.models.pydantic_model as Model

class LocalOnlyDevCameraManager(CameraManager):

    def __init__(self, database=None, camera_store_manager=None, system_id=0, cameras_list: List[Model.Camera]=[]):
        super().__init__(database, camera_store_manager, system_id)
        self.camera_list = cameras_list
    
    def populate_from_database(self):
        # we are not actually reaching out to the database here,
        #  the we are just reading camera_list and placing it into the right object
        for camera in self.camera_list:
            self.cameras[]
        #return super().populate_from_database()