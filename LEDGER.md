# Provenance ledger

## What this file has to satisfy

The course syllabus, under **Academic Integrity and the Use of AI Tools**, states:

> "On every assignment, students must record and submit a **provenance log: which tools were
> used, what prompts were issued (summary form acceptable for long sessions), and what review
> actions were taken on the generated output**. Submitting AI-generated code without review is
> a form of misrepresentation and will be treated as a violation."

and, in the same section:

> "Violations, including submitting unreviewed AI output, **fabricating provenance logs**, or
> representing teammates' work as one's own, are referred to the Dean of Graduate Studies…"

`HANDOUT.md` additionally fixes the seven-field format used below. The two are compatible; this
table shows where each syllabus element is answered:

| Syllabus requirement | Field carrying it | Extra evidence |
| --- | --- | --- |
| which tools were used | `tool:` — product, model, version, date | — |
| what prompts were issued (summary acceptable) | `prompts:` — one-line summary plus the verbatim file under `prompts/` | verbatim files exceed the "summary form" allowance |
| what review actions were taken on the generated output | `review:` — what was read, changed, rejected, and why | `DECISIONS.md` holds all 52 item-level rulings |

Every entry also carries the handout's remaining fields: `artifact:`, `checks:`, `evidence:`,
`risk:`.

**Nothing in this file asserts a review that did not happen.** Where work was proposed by the
assistant and ruled on by the student, both facts are stated; the ruling itself is in
`DECISIONS.md`, keyed by decision ID.

---

## Entry 1
artifact:  results/ambiguity_audit.md — the one required Part 6 AI ambiguity audit, run once over transcripts/interview.txt, plus the adjudication of its findings in Part 6 of the report.
tool:      omp chat assistant; model bifrost/opencode-go/deepseek-v4-flash; audit run 2026-10-13, adjudication 2026-10-18.
prompts:   prompts/ambiguity_audit_prompt.txt (unmodified, the prompt mandated by the handout) — "Audit the attached interview transcript as a requirements reviewer. Find ambiguity, incompleteness, and direct contradictions…"; the verbatim text used is saved as prompts/ambiguity_audit_prompt_used.txt.
review:    The student classified all eight findings individually, one per turn, each shown beside the paragraphs it cites (DECISIONS.md D-037..D-044). Six are true positives and two are false positives: finding 7 asserts a ten-minute grace period that no speaker states — P08 is an interviewer question and the only "ten minutes" in the transcript is P13 describing the interview starting late; finding 8 asserts students already use a running-late button, but P15 is counterfactual ("If there were"). Changes made during review: finding 1 was first ruled a false positive and reversed to true positive once its conflict with the Part 2 contradiction row was pointed out; finding 2 was qualified because "a little late" may be bounded by the grace period itself, which in turn forced a revision of evidence entry A-2.
checks:    Full-text search of transcripts/interview.txt for "ten" and "10" (single hit, P13); re-read of P06, P08, P12, P13, P15, P19 and P21 against each verdict; `python -m pytest -q` -> 4 passed.
evidence:  E-1, E-2, A-2, Q-1, Q-2.
risk:      The audit is a single model sample and is not exhaustive; a defect it did not mention may still be present. Findings 1 and 2 rest on judgement calls made by the student, recorded in DECISIONS.md D-037 and D-038.

## Entry 2
artifact:  evidence/evidence_log.md, spec/spec_template.md, traceability/template.csv and the Part 2/3/4 prose in the report.
tool:      omp chat assistant; drafted 2026-10-13, rebuilt 2026-10-18 from the student's rulings.
prompts:   prompts/draft_artifacts_prompt.txt — "You are helping me complete CS 690 Assignment 3 … using ONLY the case material …" (items 1-6 of that prompt cover the evidence log, the audit table, the four slices, the three criteria, the spec and the traceability/ledger fields).
review:    Every artifact was rebuilt from DECISIONS.md rather than carried over. The student ruled on each of the 30 items in Parts 1-4 after being shown the referenced interview paragraphs. Substantive rejections and changes: E-1 was rejected for overstating P06 — calling 15 minutes "the current policy" states a disputed value as settled — and reworded to attribute the rule to Jordan; E-2's owner was changed from the technicians to the coordinator who asserts the desk's practice; E-4 was found to be missing P13's closing sentence about the email, call history and paper list each showing only part of the sequence; A-2 was rewritten to record the ambiguity between two readings of "only a little late" instead of asserting that no value exists; R-1 was corrected twice — it had to name the reservation start, and it had to stop resolving check-in versus staff-hold precedence, after checking the transcript showed no such precedence is established (P13 never says the waitlisted student received the kit); R-2 gained the arrival-timestamp rule and the separation of a grace-extension hold from a servicing hold; the INVEST check records R-1 and R-4 both failing on I.
checks:    Mechanical verification that all ten entries cite paragraphs that exist in transcripts/interview.txt and that no entry cites SYN-01; full-text re-reads of P02, P04, P06, P07, P09, P10, P12, P13, P15, P17, P19 and P21; `python -m pytest -q` -> 4 passed.
evidence:  E-1..E-6, A-1, A-2, Q-1, Q-2; R-1..R-4; AC-1..AC-3.
risk:      The assistant proposed every draft; the student ruled on each, but a ruling is not independent authoring. The arrival-timestamp rule in R-2 is a design decision, not evidence, and is deliberately excluded from Settled decisions for that reason.

## Entry 3
artifact:  tests/test_student_acceptance.py — three acceptance tests, one per AC-1, AC-2 and AC-3.
tool:      omp chat assistant; drafted 2026-10-13, rebuilt 2026-10-18.
prompts:   prompts/draft_artifacts_prompt.txt (items 4 and 6 only — the acceptance criteria and the three tests).
review:    The student ruled on each test. Test 2 was changed from testing "checked in beats the clock" (elapsed time well past the window) to testing the arrival timestamp (elapsed time one minute inside the window with checked_in true), because the first version would have passed even if arrival stamping were never implemented. Test 3 gained a positive-case assertion so the waitlist gate is pinned as a conjunction rather than a single check. reference/ and tests/test_reference_smoke.py were left unmodified, verified by diff against the starter commit.
checks:    `python -m pytest -q` -> 4 passed in 0.01s, run in the submitted repository immediately before committing.
evidence:  AC-1 -> R-1 (E-1, E-3); AC-2 -> R-2 (E-6); AC-3 -> R-4 (E-2, E-5, E-6), per traceability/template.csv.
risk:      CONFIGURED_GRACE_MINUTES = 15 is a configured value, not the confirmed policy (Q-1 open). AC-2's arrival-timestamp scenario is exercised through the specification's preconditions rather than through any parameter of the reference function, so the test models the caller's obligation rather than the function enforcing it.

## Entry 4
artifact:  the submitted PDF report (name, commit SHA, Parts 1-7, final pytest output) and the repository carrying the artifacts.
tool:      omp chat assistant; packaged 2026-10-18.
prompts:   prompts/draft_artifacts_prompt.txt (report assembly only).
review:    The PDF was assembled from DECISIONS.md and then checked element by element for the student's name, the commit SHA, Parts 1 through 7 and the raw `python -m pytest -q` output. The report source lives outside the repository, so re-stamping the SHA requires re-rendering the PDF rather than a new commit.
checks:    `git rev-parse HEAD`; `python -m pytest -q`; rendered-PDF text extraction confirming each required element is present, and that the SHA in the PDF equals the repository HEAD.
evidence:  R-1..R-4, AC-1..AC-3, and the tests test_ac1_releasable_at_configured_grace, test_ac2_checked_in_uses_arrival_time, test_ac3_releasable_unprepared_not_offered.
risk:      The stamped SHA is valid only while the repository is unchanged; any later commit invalidates it and the PDF must be re-rendered.

## Entry 5
artifact:  the rebuild itself — DECISIONS.md and every file derived from it, replacing the previous submission.
tool:      omp chat assistant; 2026-10-17 to 2026-10-18.
prompts:   none beyond those above.
review:    The student found that the previous ledger asserted review work that had not been performed, and required instead that every judgement be presented for an explicit ruling before being recorded. This rebuild does that: 52 decision items were presented one at a time, each with the referenced interview content and a proposed answer, and each recorded in DECISIONS.md with what was offered, what was recommended, what the student corrected, and what they ruled. Where a correction contradicted an earlier ruling, the earlier item was amended rather than quietly kept — A-2 (D-038) and finding 1 (D-037) were both revised in place.
checks:    `python -m pytest -q` -> 4 passed; mechanical check that every cited paragraph exists in transcripts/interview.txt; grep confirming SYN-01 is cited nowhere as evidence.
evidence:  affects the whole submission; no requirement, criterion or test survived unchanged by review.
risk:      DECISIONS.md is the only record of the rulings and lives in the repository alongside the artifacts it justifies. If the two ever diverge, DECISIONS.md is authoritative and the artifacts are wrong.
