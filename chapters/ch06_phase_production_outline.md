# Chapter 6 production outline — Phase

## Chapter title

**Phase: Information Hidden from a Direct Measurement**

## App sources

- Level 4: Interference
- Level 11: Interference in Greater Depth
- Related bridge: Level 7, Deutsch algorithm

## Core narrative

The chapter must show why probabilities alone are not enough to describe a qubit.
The reader first sees two experiments that look the same under direct measurement,
then sees that a later gate can reveal a difference. This motivates relative phase
without beginning with complex numbers.

## Section plan

### 6.1 Opening question

Can two quantum states give the same measurement statistics and still behave differently later?

### 6.2 Try it first: H-H and H-Z-H

Use `EXP-I01`.

Show:

- start in `|0>`
- apply `H`
- either apply nothing or apply `Z`
- apply final `H`
- measure

Target conclusion:

- `H-H` returns `|0>`
- `H-Z-H` returns `|1>`
- the middle states have the same Z-basis probabilities but different relative signs

### 6.3 Why the middle measurement would miss the difference

Explain:

- after the first H, Z-basis measurement gives 0/1 with equal probability
- after H then Z, Z-basis measurement also gives 0/1 with equal probability
- therefore the difference is not visible in that measurement alone

### 6.4 Amplitudes before probabilities

Introduce the table:

| state | amplitude for 0 | amplitude for 1 | P(0) | P(1) |
|---|---:|---:|---:|---:|
| `|+>` | `+1/sqrt(2)` | `+1/sqrt(2)` | `1/2` | `1/2` |
| `|->` | `+1/sqrt(2)` | `-1/sqrt(2)` | `1/2` | `1/2` |

### 6.5 Relative sign as a first form of phase

Keep this section sign-based first.

Main wording:

> In this first example, phase appears as a sign. Later, the sign will become a direction on a circle.

### 6.6 Recombination: why the final H matters

Explain H as a recombination step:

- for `|+>`, the amplitudes add for 0 and cancel for 1
- for `|->`, the amplitudes cancel for 0 and add for 1

### 6.7 Phase sweep: bright and dark outputs

Use `EXP-I03`.

Show:

\[
P(\mathrm{bright})=\frac{1+\cos(\Delta\phi)}{2}.
\]

Introduce the formula only after the 0°, 90°, 180°, 270° cases are already shown visually.

### 6.8 What this is not saying

Misconception box:

- It does not mean that both outputs are literally printed at once.
- It does not mean that phase is directly visible in every measurement.
- It does not mean that water waves and quantum states are identical.
- It does not mean that probabilities can be ignored.

### 6.9 Bridge to algorithms

Explain:

- quantum algorithms do not merely create many possibilities
- useful circuits arrange phases so that wrong patterns cancel and useful patterns remain
- Deutsch is the next complete example

### 6.10 Going deeper

Optional:

\[
\ket{\psi}
=
\alpha\ket{0}+\beta\ket{1}
\]

\[
\ket{\psi}
=
\cos\frac{\theta}{2}\ket{0}
+
e^{i\phi}\sin\frac{\theta}{2}\ket{1}
\]

Keep this as optional. The core chapter should remain readable if skipped.

## Figure list

- `fig_exp_i01_hh_hzh.pdf`
- `fig_exp_i02_amplitude_table.pdf`
- `fig_exp_i03_phase_sweep.pdf`
- `fig_ch06_recombination.pdf`
- `fig_ch06_algorithm_bridge.pdf`

## Exercise plan

### Basic exercises

1. Predict the result of `H-H` on `|0>`.
2. Predict the result of `H-Z-H` on `|0>`.
3. Explain why `|+>` and `|->` have the same direct Z-basis probabilities.
4. Fill in a small amplitude table.
5. Decide whether a difference is a probability difference or a phase difference.
6. Interpret a bright/dark histogram.

### Deeper exercises

1. Verify `H|+>=|0>` and `H|->=|1>`.
2. Use the phase-sweep formula for 0°, 90°, 180°, and 270°.
3. Explain why a global minus sign does not change measurement probabilities.

## Writing constraints

- Main text: high-school math level.
- Complex numbers: optional box only.
- Do not say: "the qubit is 0 and 1 at the same time" without qualification.
- Do not say: "quantum computers try all answers and read the right one."
