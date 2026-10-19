# DECISIONS.md — the record of your rulings

Every item the AI proposes is recorded here only after you rule on it. This file is the
source the provenance ledger gets written from. Nothing here is inferred.

---

## D-001 · 2026-10-17 · Part 1, entry E-1

**Item:** `E-1`, source `INT-01:P06` — the 15-minute grace rule and the configured-value instruction.

**Referenced content supplied for review:** every paragraph bearing on the grace period,
paired with its question — P03/P04, P05/P06/P07, P11/P12, P16/P17, P20/P21 (15 paragraphs
found by topic search; P13 and P15 excluded as adjacent and named as excluded).

**Options offered:**

| | Option |
| --- | --- |
| A | Attributed, both halves |
| B | Configuration constraint only (15 vs 20 lives solely in A-1/Q-1) |
| C | Plain restatement of P06 |
| D | Split into two entries (11 total, over the 8–10 cap) |

**AI recommendation:** A.

**Prior draft rejected by the student**, reason given: *"draft overstates the source"* — the
rejected wording opened "The current policy is a 15-minute grace period", which states the
disputed value as settled policy and collides with `RUBRIC.md:11`.

**Student's ruling: A — attributed, both halves.**

**Resulting entry:**

```
Entry ID:  E-1
Source:    INT-01:P06
Claim:     Jordan states the release rule as 15 minutes after the reservation
           start: at 15 minutes, with no check-in and no recorded hold, the
           kit can be released, and the grace value is to come from the lab's
           configuration rather than be fixed in the software.
Status:    Stated
Owner:     Media lab manager
```

**Consequences:** the log stays at 10 entries; `15` appears only as something Jordan states,
so A-1 and Q-1 continue to carry the conflict; R-1 can still trace to `E-1` for the
configured-grace-period half.

---

## D-002 · 2026-10-18 · Part 1, entry E-2

**Item:** `E-2`, source `INT-01:P09` — releasing a reservation is not the same as the kit
being physically ready.

**Referenced content supplied for review:** the two pairs new to this item (`P01/P02`, the
normal flow including the preparation step; `P08/P09`, the direct source), plus pointers to
`P16/P17` and `P20/P21` already shown under D-001. `P04` and `P13` named as excluded
(E-3's and E-4's sources).

**Options offered:**

| | Option |
| --- | --- |
| A | As drafted (Owner: equipment technicians) |
| B | Same claim and Status, Owner changed to the media lab coordinator |
| C | Split the two assertions (11 entries, over the cap) |
| D | Claim or Status wrong |

**AI recommendation:** A.

**Student's ruling: B — same claim and Status, Owner changed to the media lab coordinator**
(Jordan asserted the desk's no-promise practice; the technicians perform the check).

**Resulting entry:**

```
Entry ID:  E-2
Source:    INT-01:P09
Claim:     Releasing a reservation does not mean the kit is physically ready:
           technicians may move it back, replace a missing battery, or
           confirm the accessories match, and the desk will not promise the
           next person until that check is done.
Status:    Stated
Owner:     Media lab coordinator
```

**Consequences:** the readiness claim is owned by the party who stated it; Q-2 already
carries the technicians' unanswered signal question, so their voice is represented in the
log by an open question rather than by ownership of E-2. Log stays at 10 entries.

---

## D-003 · 2026-10-18 · Part 1, entry E-3

**Item:** `E-3`, source `INT-01:P04` — the camera kit held under a paper note and collected
at 2:22.

**Referenced content supplied:** the direct pair `P03/P04`, plus pointers to `P06/P07`,
`P16/P17`, `P18/P19`, `P20/P21`, `P12`, all already shown under D-001.

**Options offered:** A as drafted · B Owner as a role · C trim the causal clause · D claim
or Status wrong.

**AI recommendation:** A.

**Student's ruling: A — as drafted.**

**Resulting entry:**

```
Entry ID:  E-3
Source:    INT-01:P04
Claim:     On the last late pickup, a camera kit reserved for 2:00 had a paper
           note "hold until 2:25"; the kit stayed on the shelf and the
           borrower completed pickup at 2:22 because the phone call was
           recorded.
Status:    Observed
Owner:     Jordan Lee
```

---

## D-004 · 2026-10-18 · Part 1, entry E-4

**Item:** `E-4`, source `INT-01:P13` — Priya's Thursday account of a released reservation and
a kit that was not ready.

**Referenced content supplied:** the direct pair `P11/P13`, plus pointers to `P12`,
`P16/P17`, `P21` already shown under D-001.

**Options offered:** A as drafted · B add the record-fragmentation detail · C B plus naming
Priya · D B plus the resolution.

**AI recommendation:** B, after the student identified the omission — *"Missing detail about
the paper list being disaggregated."*

**Student's ruling: B — add the record-fragmentation detail.**

**Resulting entry:**

```
Entry ID:  E-4
Source:    INT-01:P13
Claim:     On the last Thursday event, a lighting kit booked for 3:00 was
           already released when the borrower reached the desk at 3:16, the
           kit was still behind the counter because a light stand was being
           checked, and she waited until 3:38 and began the interview about
           ten minutes late. The confirmation email, call history, and paper
           list each showed only part of the sequence.
Status:    Observed
Owner:     Priya Shah
```

**Consequences:** the entry now records that no single artefact held the whole sequence
(email, call history, paper list each partial), which is the observed cost that P19's
requested fields answer.

---

## D-005 · 2026-10-18 · Part 1, entry E-5

**Item:** `E-5`, source `INT-01:P19` — the fields the coordinator wants preserved.

**Referenced content supplied:** the direct pair `P18/P19`, plus pointers to `P04`, `P17`,
and `P13`'s closing sentence (now in E-4).

**Options offered:** A as drafted · B Owner as a role · C add the stated justification ·
D claim or Status wrong.

**AI recommendation:** A.

**Student's ruling: A — as drafted.**

**Resulting entry:**

```
Entry ID:  E-5
Source:    INT-01:P19
Claim:     The coordinator wants the system to preserve the reservation start
           time, whether the student checked in, any temporary hold and its
           end, when the reservation became releasable, whether the kit is
           ready for the next checkout, and the reason for a manual hold.
Status:    Stated
Owner:     Jordan Lee
```

---

## D-006 · 2026-10-18 · Part 1, entry E-6

**Item:** `E-6`, source `INT-01:P21` — three assertions: checked-in stays active, staff
extend after contact, waitlist sees only ready equipment.

**Referenced content supplied:** the direct pair `P20/P21`, plus pointers to `P06/P07`,
`P09`, `P17`.

**Options offered:** A as drafted (bundled) · B Owner as a role · C add the stated principle
("the software should not invent policy") · D split into three (12 entries, over the cap).

**AI recommendation:** A.

**Student's ruling: A — as drafted.**

**Resulting entry:**

```
Entry ID:  E-6
Source:    INT-01:P21
Claim:     A checked-in reservation should remain active; staff sometimes
           extend a reservation after a student contacts them; the waitlist
           should only see equipment that is actually ready.
Status:    Stated
Owner:     Jordan Lee
```

**Consequences:** the split option was declined, so the log stays at 10 entries and three
P21 assertions share one ID. R-2 and R-4 both trace to this entry.

---

## D-007 · 2026-10-18 · Part 1, entry A-1

**Item:** `A-1`, source `INT-01:P12` — the disputed 20-minute figure, logged as uncertainty.

**Referenced content supplied:** the direct pair `P11/P12`.

**Options offered:** A as drafted · B Owner simplified · C make the unestablished part
explicit · D claim or Status wrong.

**AI recommendation:** A.

**Student's ruling: B — Owner simplified.** The parenthetical `(student hearsay, P12)` is
removed; the source already appears in the Source column.

**Resulting entry:**

```
Entry ID:  A-1
Source:    INT-01:P12
Claim:     The grace period is 20 minutes.
Status:    Assumption
Owner:     Media lab manager
```

**Note on the label:** `A` is deliberate. Priya did say this, but the claim as written — that
the configured period is 20 minutes — is contradicted by P06 and confirmed by no staff
member. `RUBRIC.md:11` requires the conflicting fact to sit in an A or Q entry, and this is
that entry.

---

## D-008 · 2026-10-18 · Part 1, entry A-2

**Item:** `A-2`, source `INT-01:P07` — the courtesy intent for a borrower "only a little
late", with no stated threshold.

**Referenced content supplied:** the direct pair `P05/P07` (P07 continues the answer to
Dana's P05 question), plus pointers to `P06` and `P13`.

**Options offered:** A as drafted · B make the unstated part the subject · C relabel as E
(9 entries) · D claim or Status wrong.

**AI recommendation:** A.

**Student's ruling: B — make the unstated part the subject.**

**Resulting entry:**

```
Entry ID:  A-2
Source:    INT-01:P07
Claim:     No value is stated for the courtesy rule: the interview records
           the intent ("only a little late") but gives no number, so any
           threshold would be invented.
Status:    Assumption
Owner:     Media lab manager
```

**Consequences:** the entry now asserts the absence of a value rather than the existence of a
threshold, which is the thing the interview actually fails to establish. Log stays at 10
entries.

---

## D-009 · 2026-10-18 · Part 1, entry Q-1

**Item:** `Q-1`, sources `INT-01:P06`, `INT-01:P12` — the disputed grace value.

**Referenced content supplied:** the P06, P12 and P21 excerpts that raise the conflict.

**Options offered:** A as drafted · B drop who-confirms · C add mutability · D claim or
Status wrong.

**AI recommendation:** A.

**Student's correction:** *"Not only should the mutability concern be added, but also how are
all parties informed of the policy and its changes?"*

**Student's ruling: A (revised) — value, currency, and dissemination.**

**Resulting entry:**

```
Entry ID:  Q-1
Source:    INT-01:P06, INT-01:P12, INT-01:P21
Claim:     Which grace value is actually configured - Jordan states 15 minutes
           (P06) while Priya reports 20 (P12); has it changed since, given P21
           says the grace value can change; and how are staff and borrowers
           informed when it does, given students are still hearing 20?
Status:    Open
Owner:     Media lab manager
```

**Consequences:** the entry now carries three linked uncertainties rather than one. Because it
remains a single entry, the log stays at 10. The dissemination half is grounded in P12 —
Priya still hears 20 while P06 states 15 — so it stands regardless of which value turns out
to be current.

---

## D-010 · 2026-10-18 · Part 1, entry Q-2

**Item:** `Q-2`, source `INT-01:P19` — how the technicians signal that preparation is
complete.

**Referenced content supplied:** the direct pair `P18/P19`, plus pointers to `P02`, `P09`,
`P13`.

**Options offered:** A as drafted · B add the not-asked fact · C add role and failure path ·
D claim or Status wrong.

**AI recommendation:** A.

**Student's ruling: A — as drafted.**

**Resulting entry:**

```
Entry ID:  Q-2
Source:    INT-01:P19
Claim:     How do the equipment technicians signal that preparation is
           complete, and through what interface? The coordinator could not
           say.
Status:    Open
Owner:     Equipment technicians
```

**Part 1 closed.** All ten entries ruled: six E, two A, two Q — inside the 8–10 cap. The
final evidence log text is assembled from these rulings at rebuild time, not hand-written.

---

## D-011 · 2026-10-18 · Part 2, row 1 of 7 — the contradiction

**Referenced content supplied:** `P06`, `P12`, `P21`, `P07` excerpts.

**Options offered:** A as drafted · B name the speakers · C reword the why · D row wrong,
then two rounds of correction driven by the student.

**Student's corrections, in order:**

1. The contradiction indicates a need for a **publicly checkable source of truth**; the value
   is already configurable and changes, so setting 15 does not settle the root cause.
2. "Neither value can be implemented" was unfaithful — the **initial configuration can be set
   to 15**, the manager's declared value; what a default does not do is remove the drift.
3. The evidence **cannot be reduced to "one publicly checkable home"** — the full interaction
   creating drift is undisclosed, there may be **intentional** drift, a configurable period
   affords future intentional drift, **visibility** into the period determines suitable bounds
   and limitations on its modulation, and change too frequent to track **and adjust to**
   produces friction.

**Student's ruling: A — full reading, corrected.**

**Resulting row:**

```
Item:            Contradiction
Location:        P06, P12
Classification:  Direct factual contradiction, unresolved (15 vs 20 minutes)
Why it matters:  The contradiction is a visible symptom of a change process
                 the interview never discloses, so drift may be unintended or
                 deliberate, and making the value configurable keeps both
                 possible. Requirements therefore need visibility into the
                 current value and bounds on how often it may change, since a
                 grace period that shifts faster than staff and students can
                 track and adjust to produces friction.
```

**Consequences:** the row no longer decides a winner and stays inside the two-sentence limit,
so both the "does not decide which speaker is right" (2 pts) and the "at most two sentences"
(5 pts) rubric items hold. The drift framing also carries forward into R-1, which takes the
grace value as a configured input rather than a constant.

---

## D-012 · 2026-10-18 · Part 2, row 2 of 7 — ambiguity 1

**Referenced content supplied:** the `P05/P07` pair.

**Options offered:** A as drafted · B tie to testability · C connect to A-2 · D row wrong.

**AI recommendation:** A.

**Student's ruling: A — as drafted.**

```
Item:            Ambiguity 1 (vague amount/time)
Location:        P07
Classification:  Vague quantity ("only a little late")
Why it matters:  No number bounds "a little late", so any courtesy hold period
                 would have to be invented.
```

---

## D-013 · 2026-10-18 · Part 2, row 3 of 7 — ambiguity 2

**Referenced content supplied:** the `P09/P10` pair at first, then the fuller `P08`–`P11`
release thread plus `P16/P17` after the student asked for more context.

**Options offered:** A as drafted · B name the antecedent · C reword around the channel ·
D row wrong.

**AI recommendation:** A.

**Student's ruling: A — as drafted.**

```
Item:            Ambiguity 2 (unclear who/what)
Location:        P10
Classification:  Unclear referent ("They should get a message")
Why it matters:  It is unclear whether "they" is the current borrower or the
                 waitlist person, and the channel is unstated, so a notification
                 requirement would be guessed.
```

---

## D-014 · 2026-10-18 · Part 2, row 4 of 7 — missing stakeholder

**Referenced content supplied:** `P02`, `P09`, `P13`, `P17`, `P19` excerpts.

**Options offered:** A as drafted · B add P17 · C reword the why · D row wrong.

**AI recommendation:** B.

**Student's ruling: A — as drafted** (locations P02, P09, P13, P19; P17 not added).

```
Item:            Missing stakeholder
Location:        P02, P09, P13, P19
Classification:  Missing stakeholder (equipment technicians)
Why it matters:  The preparation-and-readiness step the handoff depends on is
                 owned by a group that was never interviewed (P19: "We have not
                 asked them yet"), so their workflow cannot be specified.
```

---

## D-015 · 2026-10-18 · Part 2, row 5 of 7 — the compliment

**Judgment call surfaced:** `HANDOUT.md` asks for "the compliment", but P14 praises a feature
that does not exist, so it reads as a wish. It is the only positive-affect statement in the
transcript.

**Referenced content supplied:** the `P14` line, with `P13`, `P15`, `P17` as neighbouring
context.

**Options offered:** A as drafted · B classify precisely as a wish · C reword the why ·
D row wrong.

**AI recommendation:** A.

**Student's ruling: B — classify as a wish.**

```
Item:            Compliment
Location:        P14
Classification:  Wish about a hypothetical feature (the closest thing to a
                 compliment in the transcript)
Why it matters:  "would be amazing" praises a dashboard that does not exist,
                 so it reports no behaviour and cannot justify a requirement.
```

---

## D-016 · 2026-10-18 · Part 2, row 6 of 7 — prediction about future use

**Referenced content supplied:** the `P15` line and `P13`'s call-attempt detail.

**Options offered:** A as drafted · B name the counterfactual · C connect to P13 · D row
wrong.

**AI recommendation:** C.

**Student's ruling: C — connect to P13.**

```
Item:            Prediction about future use
Location:        P15
Classification:  Prediction, not evidence of current behavior
Why it matters:  Taken as demand, it would justify building a button; the only
                 behaviour actually observed is calling the desk and finding the
                 line busy (P13).
```

---

## D-017 · 2026-10-18 · Part 2, row 7 of 7 — strongest past event

**Referenced content supplied:** `P04` and `P13` in full, so the choice between them is
visible.

**Options offered:** A as drafted (P13) · B A plus the comparison to P04 · C nominate P04 ·
D row wrong.

**AI recommendation:** B.

**Student's ruling: B — P13 plus the comparison.**

```
Item:            Strongest past event
Location:        P13
Classification:  Strongest specific past event (observed evidence)
Why it matters:  The fully detailed Thursday sequence shows release before the
                 contact resolves, kit not physically ready, waitlist person
                 already at the counter - the firmest evidence for the release
                 and readiness requirements. P04 is also a specific past event
                 with timestamps, but it records a case that went right, whereas
                 P13 records three failures at once.
```

**Part 2 closed.** All seven rows ruled. Row 5 is classified as a wish rather than a
compliment (the transcript has no compliment), and row 7 now names P13 over P04 explicitly.
Batch 1 is complete: 17 of 17 items ruled.

---

## D-018 · 2026-10-18 · Part 3, requirement slice R-1

**Student's corrections, in order:**

1. The "exhaustively testable" wording lost clarity about what "the start" means — it must
   be the reservation start.
2. Borrower check-in and staff hold are **not mutually exclusive**; if a late borrower checks
   in while a hold is in effect, the correct disposition is ambiguous.
3. There is also **no clear end state**: what happens to the reservation when the kit is
   returned or released, and is a reservation bound to the borrowing instance or to the
   device?

**Options offered:** A explicit precedence · B precedence left open too · C narrow to release
only · D wrong.

**AI recommendation:** A.

**Student's ruling: B — precedence left open as well.** Both the check-in-during-hold
disposition and the reservation end state become open questions in Part 4.

**Resulting slice:**

```
R-1
Story:        As a media lab checkout coordinator, I want an unclaimed
              reservation to become releasable once the configured grace period
              passes with no check-in and no recorded hold, so that I can give
              equipment to the waitlist without deciding by hand each time.
Requirement:  The system reports a reservation as releasable when, and only
              when, the borrower has not checked in, no staff hold is in effect,
              and at least the configured grace period has elapsed since the
              reservation start.
Trace:        E-1 (P06), E-3 (P04)
```

**Part 4 open questions this creates:**

```
- What disposition applies when a borrower checks in while a staff hold is
  still recorded? The interview does not settle the precedence.
- What ends a reservation - pickup, release, return, or cancellation - and is a
  reservation bound to the borrowing instance or to the device?
```

**Consequences:** R-1 no longer asserts a precedence the interview does not state, which
means R-2 and later slices must also avoid resolving it implicitly. The phrase "when, and
only when" keeps the releasable case testable without settling active or held.

---

## D-019 · 2026-10-18 · Part 3, requirement slice R-2

**Student's corrections, in order:**

1. B was right in scope but left open what happens when a borrower **calls the desk** to
   extend the window while on their way — unless that is what "check-in" means.
2. Looking up and verifying an ID **takes time**, and the grace period must not expire during
   it: check-in must be **backwards time-stamped to the moment the borrower arrives** at the
   service desk.
3. Merging the call path into a single "staff hold" **conflates two mechanisms**: holds for
   **technicians servicing the device** (P09, P19) and holds that **extend the grace period**
   (P04).

**Options offered:** A arrival-timestamped check-in · B A plus the call path as a distinct
grace-extension hold · C A plus both hold kinds named without settling interaction · D wrong.

**AI recommendation:** A.

**Student's ruling: B.**

**Resulting slice:**

```
R-2
Story:        As a student borrower, I want a reservation I have already checked
              in at the desk to stay active, so that passing the clock cannot
              take equipment I have claimed.
Requirement:  The grace window applies only to borrowers who have not checked in.
              Check-in is recorded against the moment the borrower arrives at the
              service desk, not the moment the desk finishes looking up the name
              and verifying the ID, so the grace period cannot expire while that
              verification is in progress. Once checked in, elapsed time alone
              never makes the reservation releasable. A call or message before
              arrival is not a check-in; it may create a grace-extension hold - a
              hold on the reservation's release deadline - which is a different
              mechanism from a servicing hold that keeps a kit with the
              technicians while it is prepared.
Trace:        E-6 (P21), E-3 (P04)
```

**Consequences:** the two hold kinds are now named and kept apart, so R-3 covers the
grace-extension hold and R-4's readiness gate covers servicing. The arrival timestamp also
means R-1's elapsed-time input must be measured from arrival where a check-in occurred.

---

## D-020 · 2026-10-18 · Part 3, requirement slice R-3

**Options offered:** A scope to the grace-extension hold · B add the control · C add the
unresolved duration · D wrong.

**AI recommendation:** B.

**Student's ruling: B — add the control.**

**Resulting slice:**

```
R-3
Story:        As a media lab checkout coordinator, I want a recorded
              grace-extension hold to keep a reservation held until its end time,
              so that a borrower who has contacted us is not treated as a
              no-show.
Requirement:  While a grace-extension hold is recorded and its end time has not
              passed, the reservation is held, even after the configured grace
              period has elapsed. Staff record the hold before the grace period
              expires, in response to the borrower signalling that they are on
              their way. The hold carries an end time; the interview gives no
              rule for its length.
Trace:        E-3 (P04), E-5 (P19)
```

---

## D-021 · 2026-10-18 · Part 3, requirement slice R-4

**Options offered:** A as drafted · B preparation as input · C B plus INVEST failure
recorded · D wrong.

**AI recommendation:** C.

**Student's ruling: C — preparation as input, with the INVEST failure kept visible.**

**Resulting slice:**

```
R-4
Story:        As a media lab checkout coordinator, I want the waitlist to be
              offered equipment only when it is physically ready, so that the
              next person is not sent to the desk for a kit still being repacked.
Requirement:  The system offers equipment to the waitlist only when the
              reservation is releasable and preparation is recorded complete.
              How completion is signalled is not specified here; the interview
              could not say what the technicians use (Q-2), so this requirement
              consumes that signal rather than defining it.
Trace:        E-2 (P09), E-5 (P19), E-6 (P21)
INVEST:       I = fail - couples the waitlist offer to the equipment
              technicians' preparation workflow, owned by a stakeholder who was
              never interviewed.
```

---

## D-022 · 2026-10-18 · Part 3, INVEST check

**Options offered:** A only R-4 fails on I · B R-1 also fails on I · C note the R-1 coupling
without marking fail · D table wrong.

**AI recommendation:** A.

**Student's ruling: B — R-1 and R-4 both fail on I.**

```
| Req | I    | N    | V    | E    | S    | T    | Named problem for any fail |
| R-1 | fail | pass | pass | pass | pass | pass | Depends on the hold mechanism R-3
                                                       defines: releasability cannot be decided
                                                       without knowing what counts as a hold in
                                                       effect, so the slices cannot be delivered
                                                       independently. |
| R-2 | pass | pass | pass | pass | pass | pass | - |
| R-3 | pass | pass | pass | pass | pass | pass | - |
| R-4 | fail | pass | pass | pass | pass | pass | Couples the waitlist offer to the equipment
                                                       technicians' preparation workflow, owned by
                                                       a stakeholder who was never interviewed. |
```

---

## D-023 · 2026-10-18 · Part 3, acceptance criterion AC-1

**Options offered:** A as drafted · B at least G · C pin the boundary · D wrong.

**AI recommendation:** C.

**Student's ruling: C — pin the boundary.**

```
AC-1 (traces R-1)
Given   the lab's configured grace period is G minutes, the borrower has not
        checked in, and no staff hold is recorded
When    exactly G minutes have passed since the reservation start - the first
        minute at which release becomes possible
Then    the reservation is releasable
```

---

## D-024 · 2026-10-18 · Part 3, acceptance criterion AC-2

**Options offered:** A as drafted · B test arrival timestamp · C B stated as outcome ·
D wrong.

**AI recommendation:** C.

**Student's ruling: C — arrival timestamp, stated as the observable outcome.**

```
AC-2 (traces R-2)
Given   the borrower arrived at the desk one minute before the configured grace
        period elapsed, and verification took longer than that
When    the check-in is recorded
Then    the reservation is active, not releasable
```

---

## D-025 · 2026-10-18 · Part 3, acceptance criterion AC-3

**Options offered:** A as drafted · B preparation as input · C positive case · D wrong.

**AI recommendation:** B.

**Student's ruling: B — preparation as a recorded input.**

```
AC-3 (traces R-4)
Given   the reservation is releasable and preparation is not recorded complete
When    the desk asks whether the kit may be offered to the waitlist
Then    the kit may not be offered
```

**Part 3 closed.** Four slices, six INVEST marks each, three criteria on three different
requirements (R-1, R-2, R-4).

---

## D-026 · 2026-10-18 · Part 4, typed interface

**Options offered:** A signature plus arrival rule · B signature only · C defer the arrival
rule to Preconditions · D wrong.

**AI recommendation:** C.

**Student's ruling: C — signature only here; the arrival rule goes in Preconditions.**

**Resulting interface:**

```
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

**Noted constraint:** the signature carries one hold parameter, so it can express a hold's end
time but not which kind of hold it is. The grace-extension versus servicing distinction from
D-019 therefore cannot be represented in this interface.

---

## D-027 · 2026-10-18 · Part 4, preconditions

**Options offered:** A with arrival rule · B name the hold kind · C omit arrival rule ·
D wrong.

**AI recommendation:** A.

**Student's ruling: A.**

```
1. minutes_after_start is a whole number of minutes, zero or greater, measured
   after the reservation start.
2. When checked_in is true, minutes_after_start is measured from the borrower's
   arrival at the desk, not from when the desk finished verifying the ID.
3. grace_minutes is a whole number, zero or greater, taken from the lab's
   configuration rather than fixed in code.
4. staff_hold_until, when not None, is a whole number of minutes after the
   reservation start, zero or greater.
5. A call that violates any of the above raises ValueError.
```

---

## D-028 · 2026-10-18 · Part 4, postconditions

**Tension surfaced:** R-1 (D-018) leaves the check-in-versus-hold case to desk discretion, but
postconditions must be deterministic.

**Options offered:** A reference order plus note · B reference order only · C leave the
collision unresolved · D wrong.

**AI recommendation:** A.

**Student's ruling: A — reference order with the collision named as a software default.**

```
1. If checked_in is True, the result is "active".
2. Otherwise, if staff_hold_until is not None and minutes_after_start is less
   than staff_hold_until, the result is "held".
3. Otherwise, if minutes_after_start is less than grace_minutes, the result is
   "held".
4. Otherwise the result is "releasable".

Note: ordering check-in ahead of a hold is a software default, not established
policy. INT-01 leaves the collision to desk discretion, so this order may be
overridden by staff in practice and is recorded as an open question.
```

---

## D-029 · 2026-10-18 · Part 4, invariant

**Options offered:** A not applicable · B value invariant · C hold invariant · D wrong.

**AI recommendation:** A.

**Student's ruling: A — not applicable.**

```
Not applicable: reservation_disposition is a pure computation over its arguments
and keeps no stored or repeated state, so there is no state invariant to
preserve.
```

---

## D-030 · 2026-10-18 · Part 4, edge cases

**Options offered:** A the four drafted · B add the collision · C add degenerate values ·
D wrong.

**AI recommendation:** B.

**Student's ruling: B — add the discretionary collision.**

```
1. minutes_after_start exactly equals grace_minutes: the grace test is strict
   (<), so the boundary minute is the first releasable one, not the last held one.
2. A borrower checks in after the grace window has passed
   (checked_in=True, minutes_after_start > grace_minutes): the result is
   "active", because check-in dominates the clock.
3. staff_hold_until equals minutes_after_start: the hold is no longer in effect,
   so the function falls through to the grace test.
4. A negative minutes_after_start, grace_minutes, or staff_hold_until:
   ValueError is raised.
5. checked_in=True while a grace-extension hold is still live: the result is
   "active" under postcondition 1, but this is the case INT-01 leaves to desk
   discretion, so the software default is not policy.
```

---

## D-031 · 2026-10-18 · Part 4, non-goal

**Options offered:** A notifications · B reservation end state · C preparation workflow ·
D wrong.

**AI recommendation:** A.

**Student's ruling: C — the technicians' preparation workflow.**

```
This specification does not cover how equipment technicians mark preparation
complete or through what interface; INT-01 could not say and they were never
interviewed (Q-2).
```

**Consequences:** notifications and the reservation end state remain open questions rather
than being excluded by the non-goal, so the spec still has to carry them as unsettled.

---

## D-032 · 2026-10-18 · Part 4, settled decisions

**Options offered:** A five items with the timestamp labelled as design · B four
evidence-backed items · C drop the timestamp · D wrong.

**AI recommendation:** B.

**Student's ruling: B — four evidence-backed items only.**

```
1. A release may occur once the configured grace period elapses with no check-in
   and no grace-extension hold in effect. (E-1, P06)
2. A checked-in reservation remains active regardless of elapsed time.
   (E-6, P21)
3. A grace-extension hold keeps the reservation held until its end time.
   (E-3, P04)
4. The grace value is an input from configuration, not a constant the software
   fixes. (E-1, P06)
```

**Consequences:** the arrival-timestamp rule lives in R-2 and the preconditions but is not
claimed as a settled decision, so the "settled decisions are supported by evidence" rubric
item is not exposed.

---

## D-033 · 2026-10-18 · Part 4, open questions

**Options offered:** A seven plus instruction · B seven only · C four original · D wrong.

**AI recommendation:** A.

**Student's ruling: A — seven unsettled policies plus the instruction not to guess.**

```
1. The configured grace value: 15 minutes (P06) versus 20 (P12). Do not choose
   either. (Q-1)
2. Whether that value has changed since, and how staff and borrowers are told
   when it changes. (Q-1)
3. Whether a hold expires automatically at its end time or must be cleared by a
   person, and who clears it.
4. Any numeric threshold for the courtesy rule for a borrower "only a little
   late". (P07)
5. What disposition applies when a borrower checks in while a grace-extension
   hold is still recorded. INT-01 does not settle the precedence.
6. What ends a reservation - pickup, release, return, or cancellation - and
   whether a reservation is bound to the borrowing instance or to the device.
7. The recipient and channel of the release notification. (P10)

Do not guess any of these. If an implementation decision depends on one of them,
stop and ask rather than choosing a plausible value.
```

**Part 4 closed.** Items 5 and 6 exist because of the corrections made to R-1 and R-2.

---

## D-034 · 2026-10-18 · Part 5, test 1 (AC-1)

**Options offered:** A as drafted · B add just-before contrast · C parametrize over several G
values · D wrong.

**AI recommendation:** A.

**Student's ruling: A.**

```
CONFIGURED_GRACE_MINUTES = 15   # configured value, not a policy claim (Q-1 open)

def test_ac1_releasable_at_configured_grace() -> None:
    """AC-1 (R-1): no check-in, no hold, at the grace boundary -> releasable."""
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
    )
    assert state == "releasable"
```

---

## D-035 · 2026-10-18 · Part 5, test 2 (AC-2)

**Options offered:** A arrival timestamp · B clock only · C both · D wrong.

**AI recommendation:** A.

**Student's ruling: A — arrival timestamp.**

```
def test_ac2_checked_in_uses_arrival_time() -> None:
    """AC-2 (R-2): check-in is stamped at arrival, so late verification cannot
    release the reservation."""
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES - 1,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=True,
    )
    assert state == "active"
```

---

## D-036 · 2026-10-18 · Part 5, test 3 (AC-3)

**Options offered:** A as drafted · B add positive case · C identity assert · D wrong.

**AI recommendation:** A.

**Student's ruling: B — add the positive case.**

```
def test_ac3_releasable_unprepared_not_offered() -> None:
    """AC-3 (R-4): releasable, but preparation not recorded complete, so the
    kit may not be offered to the waitlist."""
    offered = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    assert offered is False
    # the gate is the conjunction: preparation complete is required as well
    assert can_offer_to_waitlist(
        disposition="releasable", preparation_complete=True
    ) is True
```

**Part 5 closed.** Three tests, one per criterion, calling only the two public reference
functions with named arguments and a named configured grace value.

---

## D-037 · 2026-10-18 · Part 6, audit finding 1 of 8

**Finding as returned:** "Conflicting grace period", P06 and P12, direct contradiction, "the
release threshold cannot be set…".

**First ruling: false positive**, which conflicted with the Part 2 contradiction row already
ruled in D-011 (which classifies the same two paragraphs as a direct factual contradiction).

**Conflict surfaced:** Part 2 says the contradiction exists; Part 6 would say the model
invented it. Priya does state a fact about the same rule — "The desk's rule is 20 minutes… 20
is the number students hear" — against P06's "The current policy is 15 minutes". Her being a
student explains why the *resolution* is uncertain, not why the contradiction is absent.

**Student's revised ruling: true positive.**

```
Finding 1 - Conflicting grace period - TRUE POSITIVE
Paragraphs: P06, P12
Reason: Jordan states 15 minutes and Priya reports 20 for the same rule; the
        transcript does not say which is current.
```

---

## D-038 · 2026-10-18 · Part 6, audit finding 2 of 8 (and an A-2 amendment)

**Finding as returned:** "Undefined courtesy window", P07, vague quantity, "no number bounds
'a little late', so any courtesy hold duration would be invented."

**Student's reading:** it is unclear whether "a little late" is late to the reservation start
or late but still inside the grace period. On the second reading P07 is describing the grace
period itself as the courtesy allowance, so the rule is bounded by the configured value and
the model's claim is wrong; on the first it has no bound. Either way the finding has no
immediate use.

**Student's ruling: true positive, qualified.**

```
Finding 2 - Undefined courtesy window - TRUE POSITIVE (qualified)
Paragraphs: P07
Reason: the phrase has no stated bound, but the missing bound may be the grace
        period itself: if "a little late" means late but inside the window, P07 is
        bounded by the configured value. The two readings are not distinguished.
```

**Amendment to A-2 (supersedes D-008's wording):**

```
Entry ID:  A-2
Source:    INT-01:P07
Claim:     The interview does not say whether "only a little late" means late to
           the reservation start or late but still inside the grace period. On
           the second reading the rule is bounded by the configured grace value;
           on the first it has no stated bound.
Status:    Assumption
Owner:     Media lab manager
```

**Why amended:** D-008 recorded A-2 as asserting that no value is stated. That is only true
under one of the two readings, so the entry now records the ambiguity rather than pre-deciding
it.

---

## D-039 · 2026-10-18 · Part 6, audit finding 3 of 8

**Finding as returned:** "Unclear recipient of the release message", P10, unclear referent,
"'They' could be the current borrower or the waitlist person…".

**Options offered:** true positive · false positive · partly right.

**AI recommendation:** true positive.

**Student's ruling: true positive.**

```
Finding 3 - Unclear recipient of the release message - TRUE POSITIVE
Paragraphs: P10
Reason: the antecedent of "They" and the channel are never stated; P09 ends on
        the waitlist person while P17 shows the borrower also expecting to be
        told, so both readings survive.
```

---

## D-040 · 2026-10-18 · Part 6, audit finding 4 of 8

**Finding as returned:** "Missing stakeholder: equipment technicians", P02/P09/P19,
incompleteness / missing stakeholder.

**Options offered:** true positive · false positive · partly right.

**AI recommendation:** true positive.

**Student's ruling: true positive.**

```
Finding 4 - Missing stakeholder: equipment technicians - TRUE POSITIVE
Paragraphs: P02, P09, P19
Reason: P19 states outright that they were not asked, and their preparation step
        is what the readiness requirement depends on.
```

---

## D-041 · 2026-10-18 · Part 6, audit finding 5 of 8

**Finding as returned:** "Hold end behavior unspecified", P04/P19, incomplete policy.

**Options offered:** true positive · false positive · partly right.

**AI recommendation:** true positive.

**Student's ruling: true positive.**

```
Finding 5 - Hold end behavior unspecified - TRUE POSITIVE
Paragraphs: P04, P19
Reason: neither paragraph says whether a hold lapses at its end time or must be
        cleared by a person; carried as open question 3 in the spec.
```

---

## D-042 · 2026-10-18 · Part 6, audit finding 6 of 8

**Finding as returned:** "Readiness signal undefined", P19, incompleteness / missing
interface.

**Options offered:** true positive · false positive · partly right.

**AI recommendation:** true positive.

**Student's ruling: true positive.**

```
Finding 6 - Readiness signal undefined - TRUE POSITIVE
Paragraphs: P19
Reason: P19 says the coordinator cannot tell you what screen or workflow would
        work, and P17 says she does not know the signal either.
```

---

## D-043 · 2026-10-18 · Part 6, audit finding 7 of 8

**Finding as returned:** "Grace period is ten minutes", P08, policy value, "the release
threshold should be specified as ten minutes…".

**Verification:** P08 is Dana's question ("What happens when you do release a kit?"). The only
"ten"/"10" in the whole transcript is P13's "We began the interview about ten minutes late",
which concerns the interview, not the grace period. The only figures attached to the grace
period are 15 (P06) and 20 (P12).

**Student's ruling: false positive.**

```
Finding 7 - Grace period is ten minutes - FALSE POSITIVE
Paragraphs: P08
Reason: no speaker states a ten-minute grace period. P08 is an interviewer question
        and the only "ten minutes" in the transcript (P13) describes the interview
        starting late.
```

---

## D-044 · 2026-10-18 · Part 6, audit finding 8 of 8

**Finding as returned:** "Students already use the running-late button", P15, existing
behaviour.

**Student's ruling: false positive.**

```
Finding 8 - Students already use the "running late" button - FALSE POSITIVE
Paragraphs: P15
Reason: P15 is counterfactual ("If there were"), so no button exists and no student
        uses one; the behaviour actually described is calling the desk, which P13
        records as sometimes busy.
```

**Part 6 adjudication complete: 6 true positives (1-6), 2 false positives (7, 8).**

---

## D-045 · 2026-10-18 · Part 6, synthetic claim 1 of 6

**Student's correction:** P15 is a **wish**, not a prediction about a hypothetical button, and
the motive is a more reliable, streamlined way to signal — not less staff contact.

**Student's ruling: A — revised rationale.**

```
Claim:  "A likely student borrower wants the media lab reservation process to
        require as little staff contact as possible."
Why not established: P15 is a wish - she would use a button because it is easier
        than calling when the line is busy - and P13 shows the call itself
        failing, twice. The motivation the transcript supports is a more
        reliable, streamlined way to signal lateness, not a reduction in staff
        contact; no speaker states that avoiding staff is a goal.
```

---

## D-046 · 2026-10-18 · Part 6, synthetic claim 2 of 6

**Student's ruling: include in the critique.**

```
Claim:  "Students probably prefer text-message alerts over email because they are
        moving between classes."
Why not established: P10 names phone, email and the desk as channels staff
        juggle, not as options anyone prefers; P17 says she wants to know her
        status but names no channel; no speaker mentions moving between classes.
```

---

## D-047 · 2026-10-18 · Part 6, synthetic claim 3 of 6

**Student's ruling: include in the critique.**

```
Claim:  "A 10-minute grace period would likely feel fair for late arrivals."
Why not established: the only figures attached to the grace period are 15 (P06)
        and 20 (P12); the sole "ten minutes" in the transcript is P13 describing
        the interview starting late, and no speaker evaluates how a window feels.
```

---

## D-048 · 2026-10-18 · Part 6, synthetic claim 4 of 6

**Student's ruling: include in the critique.**

```
Claim:  "The strongest feature would be a QR-code self-check-in so a borrower can
        preserve a reservation without waiting for a desk worker."
Why not established: check-in is a desk interaction with the university ID
        verified (P02, P04), described as routine when the student is on time. No
        QR code or self-check-in appears, and P13's wait was for a replacement
        kit rather than for a desk worker.
```

---

## D-049 · 2026-10-18 · Part 6, synthetic claim 5 of 6

**Student's ruling: include in the critique.**

```
Claim:  "Students who lose a reservation are likely willing to accept a different
        brand of camera or light automatically, as long as the general equipment
        category is the same."
Why not established: one substitution happened, under time pressure after a
        22-minute wait (P13), and the paragraph does not say what the replacement
        kit was or whether it differed in brand. The claim turns that single event
        into a standing willingness and adds "automatically" and an
        equipment-category condition, neither of which appears anywhere.
```

---

## D-050 · 2026-10-18 · Part 6, synthetic claim 6 of 6

**Student's ruling: include in the critique, on grounds of invented numbers and mechanism.**

```
Claim:  "Equipment technicians would probably prefer to receive one batch of
        released-reservation updates every 30 minutes instead of individual
        updates."
Why not established: the 30-minute cadence is a specific invented quantity, and
        the batching-versus-individual split is a design decision nobody raised.
        The technicians were never interviewed at all, as P19 states.
```

---

## D-051 · 2026-10-18 · Part 6, closing paragraph of SYN-01

**Referenced content supplied:** SYN-01 in full, the mapping of the six ruled claims onto its
first two paragraphs, and a support map for each of the five elements the closing paragraph
names.

**Student's ruling: exclude from the critique.** All five elements (late arrival,
staff-recorded holds, checked-in reservations, equipment preparation, waitlist handoff) are
supported by INT-01, and the paragraph itself defers to the transcript before treating them as
requirements. Listing it would cost the "does not list a claim the transcript actually
supports" point.

**Part 6 closed.** Six synthetic claims listed as unsupported; the closing paragraph excluded.

---

## D-052 · 2026-10-18 · Part 7, traceability matrix

**Question raised by the student:** why C (AC-2 also tracing E-3) was not recommended.

**Answer given:** E-3 (P04) records check-in as a desk act with ID verification, but says
nothing about verification outrunning the grace window — in P04 the student arrived at 2:22
against a hold to 2:25, so the situation AC-2 exercises never arises. Citing E-3 for the
arrival-timestamp rule would also contradict D-032, which deliberately kept that rule out of
Settled decisions because INT-01 does not establish it.

**Student's ruling: A — derived from the rulings.**

```
evidence_id,requirement_id,acceptance_criterion_id,test_name
E-1;E-3,R-1,AC-1,test_ac1_releasable_at_configured_grace
E-6,R-2,AC-2,test_ac2_checked_in_uses_arrival_time
E-2;E-5;E-6,R-4,AC-3,test_ac3_releasable_unprepared_not_offered
```

**All decision items closed. 52 items ruled.** Rebuild proceeds from this file.
