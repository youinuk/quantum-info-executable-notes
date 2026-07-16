# Mathematical conventions

These conventions are normative for the app-to-manuscript pipeline.

## State vectors

- One-qubit basis order: `|0>`, `|1>`.
- Two-qubit basis order: `|00>`, `|01>`, `|10>`, `|11>`.
- State vectors are column vectors.
- The first qubit is the left bit in `|q0 q1>`.
- For two qubits, index order is `2*q0 + q1`.

## Gates and circuit order

- Circuit diagrams are read from left to right.
- Matrix products act on state vectors from right to left.
- Written gate sequences must explicitly state which convention is being used.
- `H-Z-H` in prose means: start with the state, apply `H`, then `Z`, then `H`.

## Measurement

- `Z` measurement means computational-basis measurement.
- `X` measurement is implemented conceptually as `H` on each measured qubit followed by `Z` measurement.
- Counts use labels in the fixed order `00`, `01`, `10`, `11`.
- A single shot is an outcome, not a distribution.
- Repeated statistics assume repeated preparation of the same intended state.

## Phase

- Global phase is not treated as an observable state difference.
- Relative phase is retained whenever amplitudes may later interfere.
- Introductory sign examples are special cases of a general complex relative phase.

## Randomness and reproducibility

- Interactive use may use an unspecified seed.
- Publication figures and tables must use an explicit recorded seed.
- The seed does not replace reporting the theoretical distribution.
- Every stochastic figure must show the shot count.

## Numerical tolerances

- Probability normalization tolerance: `1e-10` unless a stricter test is justified.
- Tiny negative probabilities caused by floating-point error may be clipped only after a documented tolerance check.
- Publication tables should not imply more precision than the simulation or experiment supports.

## Oracle convention

- Deutsch functions are `f: {0,1} -> {0,1}`.
- Oracle action: `U_f |x,y> = |x, y xor f(x)>`.
- The standard circuit starts in `|0>|1>`.
- Query count refers to calls to `U_f`, not to the total number of elementary gates.

## Noise terminology

- The public Level 8 implementation is described as a symmetric outcome-flip or readout-error toy model.
- It must not be described as a complete physical decoherence model.
- Sampling fluctuation, readout error, state noise, and gate noise are kept conceptually distinct.
