
import typer
from rich import print, box
from rich.table import Table

from cases.health_check_test_case import HealthCheckTestCase
    

app = typer.Typer()


@app.command()
def run(
    base_url: str = "http://localhost:8000", 
    workers: int = 10, 
    iterations: int = 10,
    api_version: str = 'v1'
):
    print(f"Running performance test with base URL: {base_url}, workers: {workers}, iterations: {iterations}, API version: {api_version}")
    HealthCheckTestCase(
        base_url=base_url, 
        api_version=api_version
    ).run_concurrent(iterations=iterations, workers=workers)
    
if __name__ == "__main__":
    app()
