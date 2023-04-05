
from torch import tensor
class PseudoTensor(tensor):

    def __init__(self, pseudo_data:[], data_str):
        super().__init__(pseudo_data)
        self.data_str=data_str
