from typing import Any, Self

class CLAMP:
    @staticmethod
    def err(err: str) -> str:
        return f"\n !!! CLAMP Error: {err} !!! \n"
    
    def __new__(cls: type, _min_: Any, _mid_: Any, _max_: Any) -> Any:
        
        # Guard clause for banned types...
        for val in [_min_, _mid_, _max_]:
            if isinstance(val, (str, list, dict, set, tuple, complex)):
                return cls.err(f"Cannot use type: {type(val).__name__} for value: {val}.")
         
        # Guard clause to determine if min > max...
        if (_min_ > _max_):
            return cls.err(f"Minimum value cannot be greater than maximum value.")
            
        # Guard clause to determine if min > mid...
        if (_min_ > _mid_):
            return cls.err(f"Minimum value cannot be greater than middle value.")
            
         # Guard clause to determine if mid > max...
        if (_mid_ > _max_):
            return cls.err(f"Middle value cannot be greater than maximum value.")
        
        # Returns either a clamped integer or float depending on values...
        if all(isinstance(val, int) for val in [_min_, _mid_, _max_]):
            return int(max(min(_mid_, _max_), _min_))
        else:
            if (max(min(_mid_, _max_), _min_).is_integer()):
                return int(max(min(_mid_, _max_), _min_))
            return float(max(min(_mid_, _max_), _min_))