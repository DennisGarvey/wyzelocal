import os
import cv2
import wyzecam

assert os.environ["WYZE_EMAIL"], "missing WYZE_EMAIL"
assert os.environ["WYZE_PASSWORD"], "missing WYZE_PASSWORD"

def initIOTC(channels):
    iotc = wyzecam.WyzeIOTC(max_num_av_channels = channels)
    iotc.initialize()
    return iotc

def createImageGenerators(iotc, account, camera):
    print("Creating generator for camera: " + camera.nickname)
    session = iotc.connect_and_auth(account, camera)
    session._connect()
    session._auth()
    return session.recv_video_frame_ndarray_with_stats()
    #return session.recv_video_frame_ndarray()
    #return session.recv_video_frame()

def createRawImageGenerators(iotc, account, camera):
    print("Creating generator for camera: " + camera.nickname)
    session = iotc.connect_and_auth(account, camera)
    session._connect()
    session._auth()
    return session.recv_video_data()

def displayCam(camID):
    gen = generators[camID]
    for (frame, frame_info) in gen:
        cv2.imshow("Video Feed "+str(camID), frame)
        cv2.waitKey(1)

def getGenerators():
    print("authenticating")
    auth_info = wyzecam.login(os.environ["WYZE_EMAIL"], os.environ["WYZE_PASSWORD"])
    account = wyzecam.get_user_info(auth_info)
    cameras = wyzecam.get_camera_list(auth_info)
    iotc = initIOTC(channels = len(cameras) )
    generators = []
    for i in range(len(cameras)):
        generators.append(createImageGenerators(iotc, account, cameras[i]))
    return generators
    
def getRawGenerators():
    print("authenticating")
    auth_info = wyzecam.login(os.environ["WYZE_EMAIL"], os.environ["WYZE_PASSWORD"])
    account = wyzecam.get_user_info(auth_info)
    cameras = wyzecam.get_camera_list(auth_info)
    iotc = initIOTC(channels = len(cameras) )
    generators = []
    for i in range(len(cameras)):
        generators.append(createRawImageGenerators(iotc, account, cameras[i]))
    return generators