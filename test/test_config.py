


import pytest

class NotInRange(Exception):
    def __init__(self,msg="value not in range"):
        self.msg=msg
        super().__init__(self.msg)
        
def test_fuct():
    a=3
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange