# Outcome taxonomy v0.1

MergerLedger does not store a single editorial `winner` field. It separates adjudication from what happened to the transaction.

## Legal result

- `FTC_PREVAILED`
- `PARTIES_PREVAILED`
- `SETTLED`
- `NO_ADJUDICATION`
- `MIXED`
- `PENDING`
- `UNKNOWN`

## Transaction result

- `BLOCKED`
- `ABANDONED`
- `UNWOUND`
- `COMPLETED_WITH_STRUCTURAL_REMEDY`
- `COMPLETED_WITH_BEHAVIORAL_REMEDY`
- `COMPLETED_RESTRUCTURED`
- `COMPLETED_UNCONDITIONALLY`
- `PENDING`
- `UNKNOWN`

## MergerLedger outcome

- `FTC_BLOCKED`
- `FTC_INDUCED_ABANDONMENT`
- `FTC_OBTAINED_DIVESTITURE`
- `FTC_OBTAINED_OTHER_REMEDY`
- `PARTIES_DEFEATED_CHALLENGE`
- `PARTIES_COMPLETED_WITHOUT_REMEDY`
- `NEGOTIATED_RESOLUTION`
- `MIXED`
- `PENDING`
- `INDETERMINATE`

## Required provenance

Every derived outcome must carry:

- classification rule ID
- classification version
- supporting primary-source URL(s)
- supporting fact/event
- confidence
- review status
- classification timestamp

## v0.1 rule sketches

These are hypotheses to test during M0, not production rules.

1. Challenge filed + parties terminate transaction after challenge → candidate `FTC_INDUCED_ABANDONMENT`; verify causality/timing from primary sources.
2. Injunction granted + transaction cannot proceed → candidate `FTC_BLOCKED`.
3. Final consent/order requires divestiture → candidate `FTC_OBTAINED_DIVESTITURE`.
4. FTC challenge fails in adjudication + transaction closes without FTC remedy → candidate `PARTIES_DEFEATED_CHALLENGE`.
5. Conflicting proceedings, partial remedies, subsequent appeals, or unclear transaction disposition → `MIXED` or `INDETERMINATE` and manual review.

No rule may classify solely from an FTC action-type label when the claimed outcome requires additional facts.
