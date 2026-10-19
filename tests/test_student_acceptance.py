"""Student acceptance tests for CS 690 Assignment 3.

Exactly three tests, one for each of AC-1, AC-2, and AC-3, calling only the two public
functions from ``reference`` with named arguments. Each expected value comes from the
acceptance criterion, not from reading the reference implementation.
"""

from reference import can_offer_to_waitlist, reservation_disposition

# Configured value: the lab's grace period, injected rather than baked in. The interview
# leaves the exact value open (15 minutes in P06, 20 reported in P12; see Q-1), so the
# tests pass a named constant instead of hard-coding a disputed number.
CONFIGURED_GRACE_MINUTES = 15


def test_ac1_releasable_at_configured_grace() -> None:
    """AC-1 (R-1): no check-in, no hold, at the grace boundary -> releasable."""
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
    )
    assert state == "releasable"


def test_ac2_checked_in_uses_arrival_time() -> None:
    """AC-2 (R-2): check-in is stamped at arrival, so late verification cannot release

    the reservation. Elapsed time is the one recorded at arrival: one minute inside the
    grace window, even though verification itself finished after the window closed.
    """
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES - 1,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=True,
    )
    assert state == "active"


def test_ac3_releasable_unprepared_not_offered() -> None:
    """AC-3 (R-4): releasable, but preparation not recorded complete, so the kit may not

    be offered to the waitlist. The second assertion pins the gate as a conjunction.
    """
    offered = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    assert offered is False
    assert (
        can_offer_to_waitlist(disposition="releasable", preparation_complete=True) is True
    )
