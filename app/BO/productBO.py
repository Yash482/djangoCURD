

from datetime import date
from typing import List

class ItemBO:
    id : int
    product_name : str
    extra_name : List[str]
    weight_info : str
    packaging_info : str
    packaging_type : str
    expired_on : date
    is_frozen : bool
    active : bool
    created_on : str
    updated_on : str
