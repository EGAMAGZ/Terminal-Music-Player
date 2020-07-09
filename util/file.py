from .system import on_wsl,get_platform_name,get_user_name

class File:

    file_path:str
    platform_name:str
    user_name:str

    def __init__(self):
        self.platform_name=get_platform_name()
        self.user_name=get_user_name()
        self.file_path=self.__get_default_path()

    def set_file_path(self,file_path:str):
        self.file_path=file_path

    def get_file_path(self,file_path=None) -> str:
        return self.file_path

    def __get_default_path(self) -> str:
        if not on_wsl():
            if self.platform_name == "linux":
                file_path="/home/{}/Music/".format(self.user_name)
            elif self.platform_name == "windows":
                file_path="C:\\Users\\{}\\Music".format(self.user_name)
        else:
            file_path="/mnt/c/Users/{}/Music".format(self.user_name)

        return file_path

    def get_music_list(self):
        pass
