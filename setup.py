from setuptools import find_packages, setup

setup(
    name="airbyte-dbt-dagster",
    packages=find_packages(),
    install_requires=[
        "dbt-postgres",
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dagster-airbyte",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)