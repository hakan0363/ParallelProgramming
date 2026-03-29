custom_power = lambda x=0 , / , e=1 : x **e

def custom_equation(x: int=0, y: int=0, /, a: int=1, b: int=1, *, c: int=1) -> float:
    """
    This function does something

    :param x: positional only argument,       defaults to 0
    :type  x: int 
    :param y: poisitonal only argument,       defaults to 0
    :type  y: int
    :param a: positional or keyword argument, defaults to 1
    :type  a: int
    :param b: positional or keyword argument, defaults to 1
    :type  b: int
    :param c: keyword only argument,          defaults to 1
    :type  c: int
    :return: the result of division by c the sum of x to the power of a and y to the power of b 
    :rtype : float
    """
    return (x**a + y **b) / c

_count = 0
def fn_w_counter() -> (int, dict[str, int]):
    global _count
    _count += 1
    return _count, {__name__: _count} 