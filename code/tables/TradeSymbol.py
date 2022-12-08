from tables.SymbolPair import SymbolPair
from dataclasses import dataclass, field
@dataclass
class TradeSymbol():
    _token:str=field(init=False)
    _base_cur:str=field(init=False,repr=False)
    _invest_amount:str=field(init=False)
    _pairs:list=field(init=False,default_factory=list)
    _symbol:str=field(init=False,repr=False)
    _spent:float=0.0
    _tokens:float=0.0
    _war_chest:float=0.0

    def parse_data(self,symbol)->None:
        self._token=symbol['Token']
        self._invest_amount=symbol['InvestAmount']
        self._war_chest=float(self._invest_amount)
        for pair in symbol['SymbolPair']:
            symbol_pair=SymbolPair(
            _base_pair=pair['BaseCur'],
            _upper_limit=pair['UpperLimit'],
            _lower_limit=pair['LowerLimit'],
            _price_step=pair['PriceStep'],
            _buy_amount=pair['BuyAmount'],
            _max_pending_depth=int(pair['MaxPendingDepth']))
            self._pairs.append(symbol_pair)

