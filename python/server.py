import json
import time
from concurrent.futures import ThreadPoolExecutor

import grpc

import main_pb2
import main_pb2_grpc

with open("config.json", "r") as f:
    config = json.load(f)


class SampleServicer(main_pb2_grpc.SearchServiceServicer):
    def Search(self, request, context):
        return main_pb2.CandidateResponse(
            memo=f"Hi {request.requester}!",
            candidates=[
                {'name': 'Taro', 'rate': 'GOOD'},
                {'name': 'Jiro', 'rate': 'BAD'}
            ]
        )


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=8))
    main_pb2_grpc.add_SearchServiceServicer_to_server(
        SampleServicer(), server)
    server.add_insecure_port(f"[::]:{config['port']}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    pass
