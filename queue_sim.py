import random
import matplotlib.pyplot as plt

# simple simulation of a bank with one teller
# customers arrive randomly and wait in line if the teller is busy

random.seed(3)

NUM_CUSTOMERS = 100
AVG_ARRIVAL_GAP = 4   # minutes between customers on average
AVG_SERVICE_TIME = 3  # minutes to serve one customer on average

arrival_times = []
current_time = 0

for i in range(NUM_CUSTOMERS):
    gap = random.expovariate(1 / AVG_ARRIVAL_GAP)
    current_time += gap
    arrival_times.append(current_time)

service_times = [random.expovariate(1 / AVG_SERVICE_TIME) for i in range(NUM_CUSTOMERS)]

# now simulate the teller, one customer at a time
start_times = []
end_times = []
wait_times = []

teller_free_at = 0

for i in range(NUM_CUSTOMERS):
    arrival = arrival_times[i]

    # customer starts either when they arrive, or when teller is free, whichever is later
    start = max(arrival, teller_free_at)
    end = start + service_times[i]

    wait = start - arrival

    start_times.append(start)
    end_times.append(end)
    wait_times.append(wait)

    teller_free_at = end

avg_wait = sum(wait_times) / len(wait_times)
max_wait = max(wait_times)
num_waited = sum(1 for w in wait_times if w > 0)

print(f"average wait time: {avg_wait:.2f} minutes")
print(f"longest wait: {max_wait:.2f} minutes")
print(f"{num_waited} out of {NUM_CUSTOMERS} customers had to wait")

# quick plot of wait times per customer
plt.figure(figsize=(9,5))
plt.bar(range(NUM_CUSTOMERS), wait_times)
plt.xlabel("customer number")
plt.ylabel("wait time (minutes)")
plt.title("wait time for each customer")
plt.savefig("wait_times.png")
print("saved chart as wait_times.png")

# also try running it a bunch of times to see how avg wait changes
# this is basically the monte carlo part, running the sim many times
all_avg_waits = []

for trial in range(200):
    t_time = 0
    teller_free = 0
    waits = []

    for i in range(NUM_CUSTOMERS):
        gap = random.expovariate(1 / AVG_ARRIVAL_GAP)
        t_time += gap
        service = random.expovariate(1 / AVG_SERVICE_TIME)

        start = max(t_time, teller_free)
        wait = start - t_time
        waits.append(wait)
        teller_free = start + service

    all_avg_waits.append(sum(waits) / len(waits))

print(f"\nran {len(all_avg_waits)} simulations")
print(f"average wait across all simulations: {sum(all_avg_waits)/len(all_avg_waits):.2f} minutes")

plt.figure(figsize=(9,5))
plt.hist(all_avg_waits, bins=20)
plt.xlabel("average wait time (minutes)")
plt.ylabel("number of simulations")
plt.title("distribution of average wait time over 200 simulations")
plt.savefig("monte_carlo_result.png")
print("saved chart as monte_carlo_result.png")
