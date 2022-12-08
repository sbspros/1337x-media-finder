from dataclasses import dataclass,field
import uuid

@dataclass
class TvShow():
    _show_name:str
    _current_season:str=field(init=False,default="")
    _current_episode:str=field(init=False,default="")
