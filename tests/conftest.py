import subprocess

import grpc
import pytest

from tests.server import calculator_pb2, calculator_pb2_grpc


@pytest.fixture(scope='session')
def start_server():
    # Start grpc server in different process
    subprocess.Popen(['python', './server/server.py'])


@pytest.fixture(scope='session')
def grpc_stuff(start_server):
    channel = grpc.insecure_channel('localhost:50051')
    return calculator_pb2_grpc.CalculatorStub(channel), calculator_pb2, ''
