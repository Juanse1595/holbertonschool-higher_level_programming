#!/usr/bin/python3
'''
models/rectangle module
Contains:
    Class:
    +Rectangule
'''
from models.base import Base


class Rectangle(Base):
    '''
    Contains:
        Fields:
        __width
        __height
        __x
        __y

        Methods:
        __init__
        area
        display
        __str__
        update
        to_dictionary
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''instantation of every object'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''find the area of self'''
        return (self.__width * self.__height)

    def display(self):
        '''display the figure with # chars'''
        if self.__y > 0:
            print('\n' * self.__y, end='')
        print('\n'.join([(' ' * self.__x) + ('#' * self.__width)
                         for row in range(self.__height)]))

    def __str__(self):
        '''str representation of the object'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''update the object with new attributes'''
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            try:
                self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.__x = kwargs['x']
            except KeyError:
                pass
            try:
                self.__y = kwargs['y']
            except KeyError:
                pass
            try:
                self.__width = kwargs['width']
            except KeyError:
                pass
            try:
                self.__height = kwargs['height']
            except KeyError:
                pass

    def to_dictionary(self):
        '''return a dictionary representation of the object'''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
