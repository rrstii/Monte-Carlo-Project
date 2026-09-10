"""Monte Carlo simulation of a single-server bank queue."""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple
import random

import matplotlib.pyplot as plt

RANDOM_SEED = 3
NUM_CUSTOMERS = 100
AVG_ARRIVAL_GAP = 4.0
AVG_SERVICE_TIME = 3.0
NUM_TRIALS = 200
WAIT_TIMES_PLOT = Path("wait_times.png")
MONTE_CARLO_PLOT = Path("monte_carlo_result.png")


@dataclass(frozen=True)
class QueueConfig:
    """Configuration for a queue simulation."""

    num_customers: int = NUM_CUSTOMERS
    avg_arrival_gap: float = AVG_ARRIVAL_GAP
    avg_service_time: float = AVG_SERVICE_TIME

    def validate(self) -> None:
        """Validate simulation parameters."""
        if self.num_customers <= 0:
            raise ValueError("num_customers must be greater than 0")
        if self.avg_arrival_gap <= 0:
            raise ValueError("avg_arrival_gap must be greater than 0")
        if self.avg_service_time <= 0:
            raise ValueError("avg_service_time must be greater than 0")


def generate_arrival_times(config: QueueConfig, rng: random.Random) -> List[float]:
    """Generate cumulative Poisson-process arrival times."""
    current_time = 0.0
    arrivals: List[float] = []

    for _ in range(config.num_customers):
        current_time += rng.expovariate(1 / config.avg_arrival_gap)
        arrivals.append(current_time)

    return arrivals


def simulate_queue(config: QueueConfig, rng: random.Random) -> Tuple[List[float], List[float], List[float]]:
    """Simulate one bank queue and return starts, ends, and waits."""
    config.validate()
    arrivals = generate_arrival_times(config, rng)
    service_times = [rng.expovariate(1 / config.avg_service_time) for _ in arrivals]

    start_times: List[float] = []
    end_times: List[float] = []
    wait_times: List[float] = []
    teller_free_at = 0.0

    for arrival, service_time in zip(arrivals, service_times):
        start = max(arrival, teller_free_at)
        end = start + service_time

        start_times.append(start)
        end_times.append(end)
        wait_times.append(start - arrival)
        teller_free_at = end

    return start_times, end_times, wait_times


def summarize_waits(wait_times: List[float]) -> dict:
    """Return the main waiting-time statistics."""
    if not wait_times:
        raise ValueError("wait_times must not be empty")

    return {
        "average_wait": sum(wait_times) / len(wait_times),
        "max_wait": max(wait_times),
        "num_waited": sum(wait > 0 for wait in wait_times),
    }


def run_monte_carlo(
    config: QueueConfig = QueueConfig(),
    trials: int = NUM_TRIALS,
    seed: int = RANDOM_SEED,
) -> List[float]:
    """Run repeated queue simulations and return the mean wait of each trial."""
    if trials <= 0:
        raise ValueError("trials must be greater than 0")

    rng = random.Random(seed)
    average_waits: List[float] = []

    for _ in range(trials):
        _, _, wait_times = simulate_queue(config, rng)
        average_waits.append(summarize_waits(wait_times)["average_wait"])

    return average_waits


def plot_wait_times(wait_times: List[float], output_path: Path = WAIT_TIMES_PLOT) -> None:
    """Save wait time for each customer."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.bar(range(1, len(wait_times) + 1), wait_times)
    plt.xlabel("Customer number")
    plt.ylabel("Wait time (minutes)")
    plt.title("Customer Wait Times")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_monte_carlo(average_waits: List[float], output_path: Path = MONTE_CARLO_PLOT) -> None:
    """Save the distribution of average wait times across trials."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.hist(average_waits, bins=20)
    plt.xlabel("Average wait time (minutes)")
    plt.ylabel("Number of simulations")
    plt.title(f"Distribution of Average Wait Time Over {len(average_waits)} Simulations")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main() -> None:
    """Run one simulation, generate plots, and run the Monte Carlo experiment."""
    config = QueueConfig()
    _, _, wait_times = simulate_queue(config, random.Random(RANDOM_SEED))
    summary = summarize_waits(wait_times)

    print(f"Average wait time: {summary['average_wait']:.2f} minutes")
    print(f"Longest wait: {summary['max_wait']:.2f} minutes")
    print(f"{summary['num_waited']} out of {config.num_customers} customers had to wait")

    plot_wait_times(wait_times)
    print(f"Saved chart as {WAIT_TIMES_PLOT}")

    average_waits = run_monte_carlo(config)
    overall_average = sum(average_waits) / len(average_waits)
    print(f"\nRan {len(average_waits)} simulations")
    print(f"Average wait across all simulations: {overall_average:.2f} minutes")

    plot_monte_carlo(average_waits)
    print(f"Saved chart as {MONTE_CARLO_PLOT}")


if __name__ == "__main__":
    main()
