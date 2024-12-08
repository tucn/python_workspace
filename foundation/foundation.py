import logging
import time
import traceback
from tqdm import tqdm

class Foundation:
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.start_time = None
        self.end_time = None
        self.logger = self.setup_logger()
        self.defer_tasks = []  # Holds functions to execute at the end

    def setup_logger(self) -> logging.Logger:
        """Set up logging with a specific format and file."""
        logger = logging.getLogger(self.service_name)
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def start(self):
        """Mark the start time of the service and defer the duration calculation."""
        self.start_time = time.time()
        self.logger.info(f"Service '{self.service_name}' started.")
        # Defer duration calculation
        self.defer(self.log_duration)

    def end(self):
        """Run deferred tasks."""
        self.end_time = time.time()
        self.run_deferred_tasks()

    def serve(self, main_task, *args, **kwargs):
        """
        Serve function to manage the lifecycle of the service.

        Args:
            main_task (callable): The main task to execute.
            *args: Positional arguments for the main task.
            **kwargs: Keyword arguments for the main task.
        """
        try:
            self.start()
            main_task(*args, **kwargs)
        except Exception as e:
            self.logger.error(f"An error occurred in the main task: {e}")
            self.logger.debug(traceback.format_exc())
            raise
        finally:
            # Ensure deferred tasks run even if there's an exception
            self.end()

    def progress(self, iterable, description: str = "Processing"):
        """Provide a progress bar for an iterable."""
        return tqdm(iterable, desc=description)

    def handle_error(self, func):
        """Decorator for error handling with stack trace logging."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f"An error occurred: {e}")
                self.logger.debug(traceback.format_exc())
                raise
        return wrapper

    def defer(self, task, *args, **kwargs):
        """
        Add a deferred task to the queue.

        Args:
            task (callable): A function to run later.
            *args: Positional arguments for the task.
            **kwargs: Keyword arguments for the task.
        """
        self.defer_tasks.append((task, args, kwargs))
        self.logger.debug(f"Deferred task added: {task.__name__}")

    def run_deferred_tasks(self):
        """Execute all deferred tasks in reverse order."""
        self.logger.info("Running deferred tasks...")
        while self.defer_tasks:
            task, args, kwargs = self.defer_tasks.pop()
            try:
                task(*args, **kwargs)
                self.logger.debug(f"Deferred task executed: {task.__name__}")
            except Exception as e:
                self.logger.error(f"Error during deferred task: {e}")
                self.logger.debug(traceback.format_exc())

    def log_duration(self):
        """Log the duration of the service."""
        if self.start_time is None or self.end_time is None:
            self.logger.warning("Cannot calculate duration; start or end time is missing.")
            return
        duration = self.end_time - self.start_time
        self.logger.info(
            f"Service '{self.service_name}' ran from {time.ctime(self.start_time)} "
            f"to {time.ctime(self.end_time)}, lasting {duration:.2f} seconds."
        )
