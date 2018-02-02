Taffrail Server: A Kubernetes Metric Aggregation API
===================================================


[Taffrail] is a python package that automatically discovers metrics providers in a Kubernetes cluster and exposes them via a simple interface.

Taffrail Server lets you easily run Taffrail behind a RESTful API inside your Kubernetes cluster.

Usage
-----

```
$ kubectl create -f kubernetes
```

## API

 Endpoint           | Method      | Description                         |
| ------------------| ----------- | ------------------------------------|
| /                 | GET         | See a friendly status               |
| /metrics          | GET         | Gets metrics from all sources       |
| /metrics?source=  | GET         | Get metrics from a specific source  |
| /sources          | GET         | Get all available metrics sources   |

[Taffrail]: https://github.com/taffrailmetrics/taffrail