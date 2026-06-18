import operator
import re


OPERATORS = {
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
}


STRING_METHODS = {
    "startsWith": lambda value, arg: str(value).startswith(arg),
    "endsWith": lambda value, arg: str(value).endswith(arg),
    "contains": lambda value, arg: arg in str(value),
}

def parse_literal(value):
    value = value.strip()

    # chaîne entre guillemets
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    # booléens
    if value == "true":
        return True

    if value == "false":
        return False

    # entier
    try:
        return int(value)
    except ValueError:
        pass

    # flottant
    try:
        return float(value)
    except ValueError:
        pass

    return value

class FilterExpression:

    OP_RE = re.compile(
        r'^(?P<field>[\w\.]+)\s*(?P<op>==|!=|<=|>=|<|>)\s*(?P<value>.+)$'
    )

    METHOD_RE = re.compile(
        r'^(?P<field>[\w\.]+)\.(?P<method>\w+)\("(?P<arg>.*)"\)$'
    )

    def __init__(self, expression):
        self.expression = expression.strip()

    def evaluate(self, note):

        m = self.OP_RE.match(self.expression)
        if m:
            field = m.group("field")
            op = m.group("op")
            value = parse_literal(m.group("value"))

            left = note.get(field)

            return OPERATORS[op](left, value)

        m = self.METHOD_RE.match(self.expression)
        if m:
            field = m.group("field")
            method = m.group("method")
            arg = m.group("arg")

            left = note.get(field)

            return STRING_METHODS[method](left, arg)

        raise ValueError(f"Unknown filter: {self.expression}")