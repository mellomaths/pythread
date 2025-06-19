from test_case import TestCase
from test_result import TestResult
import requests
import time


class HealthCheckTestCase(TestCase):
    
    def __init__(self, base_url: str, api_version: str):
        super().__init__(
            name="HealthCheckTestCase", 
            description="Health check test case to verify the health endpoint of the API.", 
            base_url=base_url, 
            api_version=api_version, 
            endpoint="health")
    
    def run_single(self) -> TestResult:
        self.log("Starting...")
        self.log(f"URL: {self.url}")
        start = time.time()
        response = requests.get(self.url, timeout=1)
        end = time.time()
        response_time = end - start
        self.log(f"Response time: {response_time:.2f} seconds")
        self.log(f"Status code: {response.status_code}")
        self.log(f"Response: {response.json()}")
        if response.status_code != 200:
            self.log_error(f"Failed with status code: {response.status_code}")
            return TestResult(
                url=self.url,
                status_code=response.status_code,
                response_time=response_time,
                success=False
            )
        if not response.json().get('success') and not response.json().get('up', {}).get('database'):
            self.log_error("Failed - 'success' key not found in response")
            return TestResult(
                url=self.url,
                status_code=response.status_code,
                response_time=response_time,
                success=False
            )
        self.log_success("Health check passed!")
        return TestResult(
            url=self.url,
            status_code=response.status_code,
            response_time=response_time,
            success=True
        )