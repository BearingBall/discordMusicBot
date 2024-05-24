import os.path

class PathMannager():
    _instance = None

    def __init__(self):
        self.__configFilePath = "config.json"
        self.__ffmpegExeFilePath = "FFmpegExe/ffmpeg.exe"
        self.__localMusicFolderPath = "LocalMusic"
        self.__downloadedMusicFolderPath = "DownloadedFiles"

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
    
    def GetConfigFilePath(self):
        return self.__configFilePath
    
    def GetFfmpegExeFilePath(self):
        return self.__ffmpegExeFilePath
    
    def GetLocalMusicFolderPath(self):
        return self.__localMusicFolderPath
    
    def GetDownloadedMusicFolderPath(self):
        return self.__downloadedMusicFolderPath
    
