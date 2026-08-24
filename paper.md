# RHINO: Robustness under High-Impact Novel Operations

## Abstract

RHINO is an experimental framework for evaluating structural robustness under severe, unfamiliar, and compound perturbations. It measures invariant survival, performance retention, structural damage, shock amplification, graceful failure, and recovery potential.

## 1. Motivation

Robustness to small perturbations does not establish robustness to large or novel ones.

RHINO focuses on the region where the disturbance itself may change the system's operating regime.

## 2. Model

Healthy state:

`x_0`

Shocked state:

`x_1=F(x_0,p)`

Invariant survival:

`S_I=passed/total`

Performance retention:

`R_Q=Q_after/Q_before`

Structural retention:

`R_S=1-normalized_distance(x_1,x_0)`

Shock amplification:

`A=loss/|p|`

Graceful-failure score:

`G=w1*S_I+w2*R_Q`

## 3. Metrics

- invariant survival
- performance retention
- structural retention
- shock amplification
- graceful failure
- recovery potential
- robustness margin

## 4. Baselines

- ordinary stress testing
- chaos engineering
- adversarial robustness metrics
- fault injection
- resilience curves
- failure-domain analysis

## 5. Ablations

- remove invariant scoring
- remove critical weighting
- single-axis shocks only
- seen shocks only
- no recovery-potential estimate
- no structural-retention term

## 6. Falsification

If conventional robustness and stress-testing methods explain held-out high-impact outcomes equally well, RHINO's additional structure is not justified.

## 7. Claim boundary

RHINO evaluates robustness only over tested perturbation families. Passing RHINO does not establish universal resilience.
