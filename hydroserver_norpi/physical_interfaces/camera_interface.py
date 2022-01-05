from hydroserver.physical_interfaces.camera_controller import CameraController
from hydroserver.physical_interfaces.camera_storage import CameraStore
from hydroserver.physical_interfaces.camera_streamer import CameraStreamer
import hydroserver_norpi.models.pydantic_model as Model
import numpy as np

class NoServiceCameraController(CameraController):

    def __init__(self, camera_store: CameraStore, camera_stream: CameraStreamer, camera_db_object: Model.Camera):
        self.image_store = camera_store
        self.image_stream = camera_stream
        self.camera_index = camera_db_object.index
        self.camera_db_obj = camera_db_object
        #self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        self.camera = None
        self.most_recent_image = None
        self._refresh_rate = 1

        frame = np.zeros(shape=(1920, 1080, 3))
        self.image_stream.add_new_image(frame)
        self.image_store.save_image(frame)

    def json(self):
        return self.camera_db_obj.json()