# Monte Carlo Queue Simulation

A Python simulation project that models customer waiting times in a single-server bank queue and uses repeated random simulations to study the distribution of average waiting time.

## Overview

The simulation models:

- Random customer arrivals using an exponential inter-arrival distribution.
- Random service durations using an exponential distribution.
- A single teller serving one customer at a time.
- Individual waiting times for 100 customers.
- 200 repeated simulation trials to observe variation in average waiting time.

The project is a practical introduction to **Monte Carlo simulation**, queueing systems, and stochastic modeling.

## How It Works

For each customer, the service start time is determined by whichever occurs later:

```text
start_time = max(arrival_time, teller_free_time)
```

The waiting time is then:

```text
wait_time = start_time - arrival_time
```

The script first runs one simulation and then repeats the experiment 200 times to examine how the average waiting time varies between trials.

## Run

```bash
pip install -r requirements.txt
python queue_sim.py
```

## Outputs

The program reports:

- Average waiting time
- Maximum waiting time
- Number of customers who waited
- Average waiting time across 200 simulations

It also generates two visualizations:

- `wait_times.png` — waiting time for each customer in one simulation
- `monte_carlo_result.png` — distribution of average waiting times across 200 simulations

## Project Structure

```text
.
├── queue_sim.py
├── Q_RM.md
├── requirements.txt
├── wait_times.png
├── monte_carlo_result.png
└── README.md
```

## Parameters

The main simulation parameters are configurable in `queue_sim.py`:

- Number of customers: `100`
- Average arrival gap: `4` minutes
- Average service time: `3` minutes
- Monte Carlo trials: `200`

## Tech Stack

Python · Random Simulation · Matplotlib · Monte Carlo Methods · Queueing Systems
