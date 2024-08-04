import torch
import numpy

def tensors_to_string(data: list) -> str:
    __data = numpy.array(data)
    __fin_string = ' '.join(map(str, __data))
    return __fin_string

def string_to_tensors(data: str) -> list:
    __data = data
    __data = __data.split(" ")
    __data = list(map(float, __data))
    __data = numpy.array(__data)
    __data = torch.from_numpy(__data)
    return __data
