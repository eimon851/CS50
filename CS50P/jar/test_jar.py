from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(1) == 1
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(11)



def test_withdraw():
   jar = Jar()
   jar.deposit(1)
   jar.withdraw(1)
   jar.size == 0
   jar.deposit(10)
   jar.withdraw(1)
   jar.size == 9
   with pytest.raises(ValueError):
      jar.withdraw(10)

