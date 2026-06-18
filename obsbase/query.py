from .filters import FilterExpression

def build_filter(view):

    expressions = [
        FilterExpression(expr)
        for expr in view.filters.get("and", [])
    ]

    def match(note):
        return all(expr.evaluate(note) for expr in expressions)

    return match