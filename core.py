"""Deterministic planning calculations for fictional SDR scenarios."""
def funnel(dials, rates):
    if dials < 0 or len(rates) != 5 or any(not 0 <= r <= 100 for r in rates):
        raise ValueError('Use non-negative dials and five percentages from 0 to 100.')
    values = [float(dials)]
    for rate in rates:
        values.append(values[-1] * rate / 100)
    return values


def qualification(revenue, checks, stop=False):
    if stop:
        return 'stop'
    if revenue == 'Below $1m':
        return 'review'
    if revenue == 'Unknown' or not all(checks):
        return 'clarify'
    return 'ready'
