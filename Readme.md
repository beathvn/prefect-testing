# Prefect Testing

This repo tests the functionality and the concepts of [prefect](https://www.prefect.io/).

## Explanations
* Flows are the logical combination of Tasks. Tasks and Flows are python functions
* You can run a Flow using .serve -> this will run the flow on your machine in certain intervals (that you define)
* You can also run a Flow on a wok pool. For this you need to create a deployment of your flow and then run it using .deploy