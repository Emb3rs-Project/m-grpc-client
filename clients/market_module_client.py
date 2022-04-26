from typing import Dict, Any

import grpc
import jsonpickle

from market.market_models import MarketOutputModel
from market.market_pb2 import MarketInput
from market.market_pb2_grpc import MarketModuleStub


class MarketModuleClient(object):

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

        self.channel = grpc.insecure_channel(
            f"{self.host}:{self.port}"
        )

        self.stub = MarketModuleStub(self.channel)

    def run_short_term(self, _input: Dict[str, Any]) -> MarketOutputModel:
        s_request = MarketInput(
            input=jsonpickle.encode(_input, unpicklable=False)
        )

        response = self.stub.RunShortTermMarket(s_request)
        return MarketOutputModel().from_grpc(response)

    def run_long_term(self, _input: Dict[str, Any]) -> MarketOutputModel:
        s_request = MarketInput(
            input=jsonpickle.encode(_input, unpicklable=False)
        )

        response = self.stub.RunLongTermMarket(s_request)
        return MarketOutputModel().from_grpc(response)
