from datetime import datetime


def out():
    exitTime={"Exit":datetime.now()}
    return exitTime
def enter():
    enterTime={"Enter":datetime.now()}
    return enterTime
