import pytest
import pendulum as pdl
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog


def test_add_session():
    my_session = PendulumWorkSession()
    my_log = OrderedSetWorkLog(client="A", project="1")
    with pytest.raises(ValueError):
        my_log.add_session(my_session)
    my_session.end_session()
    my_log.add_session(my_session)
    assert my_session in my_log


def test_has_session():
    my_session = PendulumWorkSession()
    with pytest.raises(ValueError):
        OrderedSetWorkLog(client="A", project="1", sessions={my_session})
    my_session.end_session()
    my_log = OrderedSetWorkLog(client="A", project="1", sessions={my_session})
    assert my_session in my_log


def test_total_time():
    start = pdl.now()
    my_log = OrderedSetWorkLog(client="A", project="1", sessions=set())
    my_log.add_session(PendulumWorkSession().end_session())
    my_log.add_session(PendulumWorkSession().end_session())
    end = pdl.now()
    assert my_log.total_time(start, end) == 0


def test_get_client():
    my_log = OrderedSetWorkLog(client="A", project="1")
    assert my_log.get_client() == "A"


def test_get_project():
    my_log = OrderedSetWorkLog(client="A", project="1")
    assert my_log.get_project() == "1"


def test_get_work_sessions():

    first = PendulumWorkSession().end_session()
    second = PendulumWorkSession().end_session()
    my_log = OrderedSetWorkLog(client="A", project="1")
    my_log.add_session(first)
    my_log.add_session(second)
    i = 0
    for s in my_log.get_work_sessions():
        assert isinstance(s, PendulumWorkSession)
        if i == 0:
            assert s == first
        if i == 1:
            assert s == second
        i = i + 1