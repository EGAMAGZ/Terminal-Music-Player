import platform
import getpass

def on_wsl() -> bool:
    isOnWSL=False
    
    uname=platform.uname()
    system=uname[0]
    release=uname[2]

    if system.lower() == 'linux' and 'microsoft' in release.lower():
        isOnWSL=True
    return isOnWSL

def get_platform_name() -> str:
    return platform.system().lower()

def get_user_name() -> str:
    return getpass.getuser()
