class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self: 'Television') -> None:
        '''
        Sets the default instance variables
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self: 'Television') -> None:
        '''
        Turns and turns off the TV by changing the boolean value of status
        :return: None
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self: 'Television') -> None:
        '''
        Mutes and unmutes the TV by changing the value of the muted variable
        :return: None
        '''
        if self.__status:
            self.__muted = True

    def channel_up(self: 'Television') -> None:
        '''
        Increases the TV channel when TV is on. If the channel is already the max channel, it stays as it is.
        :return: None
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self: 'Television') -> None:
        '''
        Lowers the TV channel when the TV is on. If the channel is already at the minimum channel, it stays as it is.
        :return: None
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self: 'Television') -> None:
        '''
        Raises the volume of the TV when it is on and unmutes the TV if it is muted. IF the volume is already max, stays
        as it is.
        :return: None
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1


    def volume_down(self: 'Television') -> None:
        '''
        Decreases the volume of the TV when it's on and unmutes the TV if it was muted. If the volume is already at the
        lowest, it stays as is.
        :return: None
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self: 'Television') -> str:
        '''
        Sends a formatted string with the power, channel, and volume variables. If the TV is muted, volume is zero.
        :return: Formatted string of the instance values
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

