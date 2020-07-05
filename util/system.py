import platform

class SystemInfo:

    @staticmethod
    def on_wsl() -> bool:
        isOnWSL=False
        
        uname=platform.uname()
        system=uname[0]
        release=uname[2]

        if system.lower() == 'linux' and 'microsoft' in release.lower():
            isOnWSL=True
        return isOnWSL

    @staticmethod
    def getPlatformName() -> str:
        return platform.system().lower()
