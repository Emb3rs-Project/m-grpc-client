from typing import Dict, Any

import grpc
import jsonpickle

from cf.cf_models import CharacterizationSinkOutputModel, ConvertSinkOutputModel, ConvertSourceOutputModel, \
    ConvertPinchOutputModel, ConvertOrcOutputModel, CharacterizationSourceOutputModel
from cf.cf_pb2_grpc import CFModuleStub
from cf.cf_pb2 import PlatformOnlyInput, ConvertSourceInput


class CFModuleClient(object):

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

        self.channel = grpc.insecure_channel(
            f"{self.host}:{self.port}"
        )

        self.stub = CFModuleStub(self.channel)

    def convert_sink(self, _input: Dict[str, Any]) -> ConvertSinkOutputModel:
        s_request = PlatformOnlyInput(
            platform=jsonpickle.encode(_input, unpicklable=True)
        )

        response = self.stub.convert_sink(s_request)
        return ConvertSinkOutputModel().from_grpc(response)

    def convert_source(self, group_of_sources: Dict[str, Any]) -> ConvertSourceOutputModel:
        pass

    def convert_pinch(self, _input: Dict[str, Any]) -> ConvertPinchOutputModel:
        pass

    def convert_orc(self, _input: Dict[str, Any]) -> ConvertOrcOutputModel:
        pass

    def char_simple(self, _input: Dict[str, Any]) -> CharacterizationSourceOutputModel:
        pass

    def char_building(self, _input: Dict[str, Any]) -> CharacterizationSinkOutputModel:
        pass

    def char_greenhouse(self, _input: Dict[str, Any]) -> CharacterizationSinkOutputModel:
        pass
