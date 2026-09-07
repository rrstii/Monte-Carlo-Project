# Bank Queue Simulation (Monte Carlo)

A simple simulation of a single-teller bank queue. Customers arrive at random times and wait in line if the teller is busy with someone else.

## How it works
1. Customer arrival gaps and service times are generated randomly using an exponential distribution (common way to model random arrivals/waiting).
2. The simulation processes customers one by one, tracking when each one starts being served and how long they had to wait.
3. The whole simulation is then repeated 200 times (Monte Carlo) to see how the average wait time varies across different random scenarios, instead of relying on just one run.

## Run it
```
pip install matplotlib
python queue_sim.py
```

## Output
- `wait_times.png` - wait time for each customer in a single run
- `monte_carlo_result.png` - distribution of average wait time across 200 simulation runs

## Sample results
- Average wait time: ~4-8 minutes (varies by run since it's random)
- Some customers don't wait at all, some wait a long time if a slow customer is ahead of them

## Notes
Arrival gap and service time averages can be changed at the top of the script (`AVG_ARRIVAL_GAP`, `AVG_SERVICE_TIME`) to simulate busier or quieter scenarios.
