class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME # integer value of 0
        self.__channel = Television.MIN_CHANNEL # integer value of 0

    def power(self):
        if self.__status: # if tv is already on
            self.__status = False
        else:
            self.__status = True
    def mute(self):
        if self.__status:
            self.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL: #0
                self.__channel = Television.MAX_CHANNEL #3
            else:
                self.__channel -= 1

    def volume_up(self): # max volume is 2
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1


    def volume_down(self): # min volume is 0
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

