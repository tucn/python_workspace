import argparse
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
from foundation.foundation import Foundation

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the Foundation-based service.")
    parser.add_argument(
        "--service-name", type=str, required=True, help="Name of the service."
    )
    return parser.parse_args()

def main_task(service):
    """Main task for the example."""
    for i in service.progress(range(10), description="Main Task"):
        if i == 5:  # Simulate an error
            raise ValueError("Simulated Error!")
        time.sleep(0.5)

def cleanup():
    """Example cleanup task."""
    print("Cleaning up resources...")

def save_results():
    """Example save results task."""
    print("Saving results...")

if __name__ == "__main__":
    # Create an instance of the Foundation class
    service = Foundation(service_name="example")

    # Add deferred tasks
    service.defer(cleanup)
    service.defer(save_results)

    # Use serve to manage lifecycle
    try:
        service.serve(main_task, service)
    except Exception:
        print("Handled exception gracefully.")