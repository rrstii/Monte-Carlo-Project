import random

import pytest

from queue_sim import QueueConfig, run_monte_carlo, simulate_queue, summarize_waits


def test_simulation_returns_one_record_per_customer():
    config = QueueConfig(num_customers=25)
    starts, ends, waits = simulate_queue(config, random.Random(10))

    assert len(starts) == 25
    assert len(ends) == 25
    assert len(waits) == 25
    assert all(wait >= 0 for wait in waits)
    assert all(end >= start for start, end in zip(starts, ends))


def test_wait_summary_is_consistent():
    summary = summarize_waits([0.0, 2.0, 4.0])

    assert summary["average_wait"] == pytest.approx(2.0)
    assert summary["max_wait"] == pytest.approx(4.0)
    assert summary["num_waited"] == 2


def test_monte_carlo_is_reproducible():
    first = run_monte_carlo(QueueConfig(num_customers=20), trials=10, seed=5)
    second = run_monte_carlo(QueueConfig(num_customers=20), trials=10, seed=5)

    assert first == second


def test_invalid_configuration_is_rejected():
    with pytest.raises(ValueError):
        QueueConfig(num_customers=0).validate()

    with pytest.raises(ValueError):
        run_monte_carlo(trials=0)
