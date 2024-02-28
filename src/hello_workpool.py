from prefect import flow


@flow(log_prints=True, name="Hello World Print")
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    hello_world.from_source(
        source="https://github.com/beathvn/prefect-testing",
        entrypoint="src/hello_workpool.py:hello_world"
    ).deploy(
        name="workpool-deployment",
        work_pool_name="my-first-workpool",
    )
