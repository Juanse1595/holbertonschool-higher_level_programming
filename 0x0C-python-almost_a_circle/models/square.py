#!/usr/bin/python3
'''
models/square module
Contains:
    Class Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Contains:
        Fields:
        All from Rectangle

        Methods:
        __init__ from Rectangle
        __str__
        getter
        setter
        update
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
