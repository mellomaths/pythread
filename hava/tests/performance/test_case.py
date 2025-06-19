from rich import print
from concurrent.futures import ThreadPoolExecutor
from test_result import TestResult


class TestCase:
    
    def __init__(self, name: str, description: str, base_url: str, api_version: str, endpoint: str):
        if not name or not description or not endpoint or not base_url or not api_version:
            raise ValueError("All parameters must be provided and non-empty.")
        self.name = name
        self.description = description
        self.base_url = base_url
        self.api_version = api_version
        self.endpoint = endpoint
        self.log(f"Initialized test case: {self.name} - {self.description}")
    
    @property
    def url(self) -> str:
        return f"{self.base_url}/hava/api/{self.api_version}/{self.endpoint}"
    
    def log(self, message: str):
        print(f"[{self.name}] {message}")

    def log_error(self, message: str):
        print(f"[bold red][{self.name}] {message}[bold red]")
    
    def log_success(self, message: str):
        print(f"[bold green][{self.name}] {message}[bold green]")
    
    def run_single(self) -> TestResult:
        raise NotImplementedError("Subclasses should implement this method.")
    
    def run_multiple(self, iterations: int) -> list[TestResult]:
        results = []
        for i in range(iterations):
            self.log(f"Running iteration {i + 1} of {iterations}")
            result = self.run_single(iterations)
            results.append(result)
        return results
    
    def run_concurrent(self, iterations: int, workers: int) -> list[TestResult]:
        results = []
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(self.run_single) for _ in range(iterations)]
            for future in futures:
                results.append(future.result())
        return results
    
    def __repr__(self):
        return f"TestCase(name={self.name}, description={self.description}, base_url={self.base_url}, api_version={self.api_version}, endpoint={self.endpoint})"