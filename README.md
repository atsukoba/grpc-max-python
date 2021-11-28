# Node for Max Python gRPC

## Setup Environment

versions

- `Python`: 3.9.7
- `Node`: 16.6.0 (bundled in Max)
- `Max`: 8.2.1

after creating virtual env for python runtime, run this

```shell
cd python/
pip install -r requirements.txt
python grpc_code_gen.py
```

init your npm for development (different from Node for Max runtime)

```shell
cd node-max/
npm i
```

When these are done, open Max patcher and init Node for Max runtime by sending the message [script npm install] to [node.script] object

## Run server

```shell
cd python/
python main.py
```
