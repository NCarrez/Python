from win32api import GetFileVersionInfo, LOWORD, HIWORD


def get_file_version(fullfilename):
    try:
        info = GetFileVersionInfo(fullfilename, "\\")
        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]
        return str(
            str(HIWORD(ms))
            + "."
            + str(LOWORD(ms))
            + "."
            + str(HIWORD(ls))
            + "."
            + str(LOWORD(ls))
        )
    except:
        return "Unknown version"
