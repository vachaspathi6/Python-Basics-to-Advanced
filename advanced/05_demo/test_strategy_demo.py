from abc import ABC, abstractmethod
import pytest

# Strategy Design
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class TenPercentDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9

class Context:
    def __init__(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def get_final_price(self, price):
        return self._strategy.apply_discount(price)

def test_no_discount():
    ctx = Context(NoDiscount())
    assert ctx.get_final_price(100) == 100

def test_ten_percent_discount():
    ctx = Context(TenPercentDiscount())
    assert ctx.get_final_price(200) == 180

def test_strategy_switch():
    ctx = Context(NoDiscount())
    ctx.set_strategy(TenPercentDiscount())
    assert ctx.get_final_price(50) == 45

def test_integration():
    ctx = Context(NoDiscount())
    prices = [100, 150, 220]
    discounted = [ctx.get_final_price(p) for p in prices]
    assert discounted == prices
    ctx.set_strategy(TenPercentDiscount())
    discounted = [ctx.get_final_price(p) for p in prices]
    assert discounted == [90, 135, 198]
