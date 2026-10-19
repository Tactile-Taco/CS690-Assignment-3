# Implementation-ready specification

## Selected requirement

Requirement ID: R-1 — a reservation becomes releasable once the configured grace period
passes with no check-in and no grace-extension hold in effect.
Evidence trace: E-1 (INT-01:P06), E-3 (INT-01:P04); the unsettled value is tracked as Q-1
(INT-01:P06, INT-01:P12).

## Behavior and scope

Given the whole minutes since a reservation start, the lab's configured grace period, whether
the borrower has checked in, and any recorded hold end time, the system reports exactly one
disposition: `active`, `held`, or `releasable`. The function never chooses the grace value or
the hold duration; both arrive as inputs. Scope is the release decision at the checkout desk,
before pickup. What happens after a reservation is picked up, released, or returned is not
covered.

## Typed interface or function signature

```python
from typing import Literal

Disposition = Literal["active", "held", "releasable"]


def reservation_disposition(
    *,
    minutes_after_start: int,
    grace_minutes: int,
    checked_in: bool,
    staff_hold_until: int | None = None,
) -> Disposition: ...
```

## Preconditions

1. `minutes_after_start` is a whole number of minutes, zero or greater, measured after the
   reservation start.
2. When `checked_in` is true, `minutes_after_start` is measured from the borrower's arrival at
   the desk, not from when the desk finished verifying the ID.
3. `grace_minutes` is a whole number, zero or greater, taken from the lab's configuration
   rather than fixed in code.
4. `staff_hold_until`, when not `None`, is a whole number of minutes after the reservation
   start, zero or greater.
5. A call that violates any of the above raises `ValueError`.

## Postconditions

1. If `checked_in` is `True`, the result is `"active"`.
2. Otherwise, if `staff_hold_until` is not `None` and `minutes_after_start` is less than
   `staff_hold_until`, the result is `"held"`.
3. Otherwise, if `minutes_after_start` is less than `grace_minutes`, the result is `"held"`.
4. Otherwise the result is `"releasable"`.

Note: ordering check-in ahead of a hold is a software default, not established policy.
INT-01 leaves the collision to desk discretion, so this order may be overridden by staff in
practice and is recorded as an open question.

## Invariant

Not applicable: `reservation_disposition` is a pure computation over its arguments and keeps
no stored or repeated state, so there is no state invariant to preserve.

## Edge cases

1. `minutes_after_start` exactly equals `grace_minutes`: the grace test is strict (`<`), so
   the boundary minute is the first releasable one, not the last held one.
2. A borrower checks in after the grace window has passed (`checked_in=True`,
   `minutes_after_start > grace_minutes`): the result is `"active"`, because check-in
   dominates the clock.
3. `staff_hold_until` equals `minutes_after_start`: the hold is no longer in effect, so the
   function falls through to the grace test.
4. A negative `minutes_after_start`, `grace_minutes`, or `staff_hold_until`: `ValueError` is
   raised.
5. `checked_in=True` while a grace-extension hold is still live: the result is `"active"`
   under postcondition 1, but this is the case INT-01 leaves to desk discretion, so the
   software default is not policy.

## Non-goal

This specification does not cover how equipment technicians mark preparation complete or
through what interface; INT-01 could not say and they were never interviewed (Q-2).

## Settled decisions

1. A release may occur once the configured grace period elapses with no check-in and no
   grace-extension hold in effect. (E-1, P06)
2. A checked-in reservation remains active regardless of elapsed time. (E-6, P21)
3. A grace-extension hold keeps the reservation held until its end time. (E-3, P04)
4. The grace value is an input from configuration, not a constant the software fixes.
   (E-1, P06)

## Open questions the implementation agent may not answer

1. The configured grace value: 15 minutes (P06) versus 20 (P12). Do not choose either. (Q-1)
2. Whether that value has changed since, and how staff and borrowers are told when it changes.
   (Q-1)
3. Whether a hold expires automatically at its end time or must be cleared by a person, and
   who clears it.
4. Any numeric threshold for the courtesy rule for a borrower "only a little late". (P07)
5. What disposition applies when a borrower checks in while a grace-extension hold is still
   recorded. INT-01 does not settle the precedence.
6. What ends a reservation — pickup, release, return, or cancellation — and whether a
   reservation is bound to the borrowing instance or to the device.
7. The recipient and channel of the release notification. (P10)

Do not guess any of these. If an implementation decision depends on one of them, stop and ask
rather than choosing a plausible value.
