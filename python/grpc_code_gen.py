from grpc_tools import protoc

protoc.main((
    '',
    '-I../scheme',
    '--python_out=.',
    '--grpc_python_out=.',
    '../scheme/main.proto',
))
