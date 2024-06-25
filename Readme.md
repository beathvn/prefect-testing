# Prefect Testing

This repo tests the functionality and the concepts of [prefect](https://www.prefect.io/).

## Explanations
* Flows are the logical combination of Tasks. Tasks and Flows are python functions
* You can run a Flow using .serve -> this will run the flow on your machine in certain intervals (that you define)
* You can also run a Flow on a wok pool. For this you need to create a deployment of your flow and then run it using .deploy

## Running locally
### Setup
Follow this [link](https://docs.prefect.io/latest/ui/cloud-local-environment/)
*  `prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"`
* setting the root for the prefect database using `conda env config vars set PREFECT_HOME=YOUR_DESIRED_FOLDER` (**make sure** to restart the conda environment in order for the changes to take effect!). To check where prefect stores its data:
    * go in the UI into the settings (see below on how to open the UI)
    * in a python script run `import prefect.settings` and `prefect.settings.PREFECT_HOME.value()`

### Using
* `prefect server start` starts up the local server and lets you see the UI.