from enum import Enum

class Choice(Enum):
    ADD_ROOT = 1
    ADD_CHILD = 2
    ADD_SUBCHILD = 3
    DEL_SUBCHILD = 4
    READ_ELEMENT = 5
    CREATE_XML = 6
    XML_FROM_STR = 7
    VALIDATE = 8
    QUIT_APP = 9


