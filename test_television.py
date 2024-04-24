import pytest
from television import *



def test_init():
    TV = Television()
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"




def test_power():
    TV = Television()
    TV.power()
    assert str(TV) == "Power = True, Channel = 0, Volume = 0"
    TV.power()
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"




def test_mute(): #New mute does not set volume to zero btw
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up():
    TV = Television()
    TV.channel_up()
    assert str(TV) == "Power = False, Channel = 1, Volume = 0"
    TV.power()
    TV.channel_up()
    assert str(TV) == "Power = True, Channel = 1, Volume = 0"

    TV.channel_up()
    assert str(TV) == "Power = True, Channel = 2, Volume = 0"

    TV.channel_up()
    assert str(TV) == "Power = True, Channel = 3, Volume = 0"


    TV.channel_up()
    assert str(TV) == "Power = True, Channel = 3, Volume = 0"


def test_channel_down():
    TV = Television()
    TV.channel_down()
    assert str(TV) == "Power = False, Channel = 3, Volume = 0"
    TV.power()
    TV.channel_down()
    assert str(TV) == "Power = True, Channel = 2, Volume = 0"
    TV.channel_down()
    assert str(TV) == "Power = True, Channel = 1, Volume = 0"
    TV.channel_down()
    assert str(TV) == "Power = True, Channel = 0, Volume = 0"
    TV.channel_down()
    assert str(TV) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up():



    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"


    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down(): #MIn volume = 0
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"




    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()


    assert str(tv) == "Power = True, Channel = 0, Volume = 0"