import pytest
from core import funnel, qualification


def test_funnel_denominators_and_default():
    assert funnel(600,[12,65,25,80,75]) == pytest.approx([600,72,46.8,11.7,9.36,7.02])


@pytest.mark.parametrize('rates', [[0]*5,[100]*5,[12,65,25,80,75]])
def test_counts_never_increase_down_funnel(rates):
    values=funnel(600,rates)
    assert all(a>=b for a,b in zip(values,values[1:]))


@pytest.mark.parametrize('dials,rates',[(-1,[0]*5),(600,[101]*5),(600,[-1]*5),(600,[50])])
def test_invalid_model_inputs(dials,rates):
    with pytest.raises(ValueError): funnel(dials,rates)


def test_opt_out_overrides_all_other_fit():
    assert qualification('$1m–$9.9m',[True]*3,True)=='stop'


@pytest.mark.parametrize('revenue,checks,expected', [('Unknown',[True]*3,'clarify'),('Below $1m',[True]*3,'review'),('$1m–$9.9m',[True,False,True],'clarify'),('$1m–$9.9m',[True]*3,'ready')])
def test_qualification(revenue,checks,expected):
    assert qualification(revenue,checks)==expected
