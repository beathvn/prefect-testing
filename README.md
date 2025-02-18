# Prefect Testing

This repo tests the functionality and the concepts of [prefect](https://www.prefect.io/).

## Explanations

* Flows are the logical combination of Tasks. Tasks and Flows are python functions
* You can run a Flow using .serve -> this will run the flow on your machine in certain intervals (that you define)
* You can also run a Flow on a wok pool. For this you need to create a deployment of your flow and then run it using .deploy

## Running locally

### Setup

* Configure Prefect to communicate with the server with:

    ```bash
    prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
    ```

* setting the root for the prefect database, by setting the `PREFECT_HOME` environment variable:
  * **virtual env in unix**: run the following command

    ```bash
    export PREFECT_HOME=YOUR_DESIRED_FOLDER
    ```

    for example:

    ```bash
    export PREFECT_HOME=$(pwd)/.prefect
    ```

  * **conda**
    * run the following command

        ```bash
        conda env config vars set PREFECT_HOME=YOUR_DESIRED_FOLDER
        ```

    * make sure to restart the conda environment in order for the changes to take effect!.
  * To check where prefect stores its data:
    * go in the UI into the settings (see below on how to open the UI)
    * in a python script (in terminal type `python`)

    ```python
    import prefect.settings
    prefect.settings.PREFECT_HOME.value()
    ```

### Using

* start up the local server:

    ```bash
    prefect server start
    ```
