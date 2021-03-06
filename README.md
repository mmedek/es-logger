# es-logger
Simple package for logging to Elasticsearch. Expected usage is to use this package inside your k8s cluster.

## Installation
```
pip install es-logger
```

## Example of usage
In this example we write 3 messages (1-3) to buffer and after that write to Elasticsearch running on address 127.0.0.   :9200 one-by-one (that should be changed to bulk write). Logger has 4 levels of severity (DEBUG, INFO, WARNING, ERROR) and writes messages in the following format: `appName:default-app-name appName.keyword:default-app-name env:default-env-name env.keyword:default-env-name payload:Hi 3 severity:INFO severity.keyword:INFO timestamp:Jun 30, 2021 @ 18:46:54.620 _index:app-name-logs-default-app-name-30-06-2021 _score: - _type:doc`. 

```
from es_logger import ElasticLogger
mh_logger = ElasticLogger(
    buffer_size=3,
    index='app-name-logs',
    app_name='app_name',
    env='dev',
    port=9200,
    ip_addr='127.0.0.1'
)

mh_logger.info('Hi! 1')
mh_logger.info('Hi! 2')
mh_logger.info('Hi! 3')
mh_logger.info('Hi! 4')
```