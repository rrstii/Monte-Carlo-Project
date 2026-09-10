# Monte Carlo Queue Simulation

A Python simulation project that models a single-server bank queue and uses repeated Monte Carlo trials to study customer waiting times and their variability.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)

## Project Overview

The simulation models a simple stochastic queue in which customers arrive randomly and are served by one teller. It then repeats the experiment to examine how the average waiting time changes across independent trials.

The model uses:

- Exponential inter-arrival times with a mean gap of 4 minutes.
- Exponential service times with a mean of 3 minutes.
- A single server (bank teller).
- 100 customers per simulation.
- 200 Monte Carlo trials.

## Queue Logic

For each customer, service begins when both the customer has arrived and the teller is available:

```text
start_time = max(arrival_time, teller_free_time)
wait_time  = start_time - arrival_time
```

This produces a sequence of individual waiting times. The repeated simulations are then used to visualize the distribution of the resulting average waiting time.

## Outputs

A single run reports:

- Average waiting time
- Maximum waiting time
- Number of customers who had to wait
- Average waiting time across 200 trials

The program also generates:

| File | Description |
| --- | --- |
| `wait_times.png` | Waiting time for each customer in one simulation |
| `monte_carlo_result.png` | Distribution of average waiting times across 200 trials |

## Installation

```bash
git clone https://github.com/rrstii/Monte-Carlo-Project.git
cd Monte-Carlo-Project
pip install -r requirements.txt
```

## Usage

```bash
python queue_sim.py
```

## Project Structure

```text
Monte-Carlo-Project/
├── queue_sim.py
├── Q_RM.md
├── requirements.txt
├── wait_times.png
├── monte_carlo_result.png
└── README.md
```

## Parameters

The experiment can be adjusted directly in `queue_sim.py`:

| Parameter | Default |
| --- | ---: |
| Customers per run | 100 |
| Average arrival gap | 4 min |
| Average service time | 3 min |
| Monte Carlo trials | 200 |

## Why Monte Carlo?

A single random simulation gives only one possible outcome. Repeating the experiment many times makes it possible to examine the variability of the system and the distribution of average waiting times rather than relying on one run.

## Limitations and Next Steps

The model intentionally represents a simplified queue. Possible extensions include:

- Multiple tellers or servers.
- Different arrival and service distributions.
- Queue capacity limits.
- Server utilization and throughput metrics.
- Confidence intervals for simulation estimates.
- Parameter sweeps and sensitivity analysis.
- Larger numbers of trials for more stable estimates.

## Tech Stack

**Python · Matplotlib · Monte Carlo Simulation · Probability · Queueing Systems · Stochastic Modeling**
