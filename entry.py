import json
from pydantic import Field
import dotenv
import grpc

from teo.teo_pb2_grpc import TEOModuleStub
from teo.teo_pb2 import BuildModelInput
from teo.teo_models import BuildModelOutputModel

from test_mapping_long_term import input_data


dotenv.load_dotenv()

## CF MODULE
CF_HOST = "vali.pantherify.dev"
CF_PORT = 50051

## GIS MODULE
GIS_HOST = "vali.pantherify.dev"
GIS_PORT = 50052

## TEO MODULE
TEO_HOST = "172.17.0.2"
TEO_PORT = 50053

## MM MODULE
MM_HOST = "localhost"
MM_PORT = 50054

## BM MODULE
BM_HOST = "vali.pantherify.dev"
BM_PORT = 50055

def use_case():
    # cf_channel = grpc.insecure_channel(f"{CF_HOST}:{CF_PORT}")
    # cf_module = CFModuleStub(cf_channel)

    # market_channel = grpc.insecure_channel(f"{MM_HOST}:{MM_PORT}")
    # market_module = MarketModuleStub(market_channel)

    teo_channel = grpc.insecure_channel(f"{TEO_HOST}:{TEO_PORT}")
    teo_module = TEOModuleStub(teo_channel)

    # input_file = open('./json/teo_input.json')
    # input_data = json.load(input_file)


    teo_input = BuildModelInput(
        platform = json.dumps(input_data['platform']),
        cf_module = json.dumps(input_data['cf-module']),
        gis_module = json.dumps(input_data['gis-module'])
    )

    result = teo_module.buildmodel(teo_input)
    processed = BuildModelOutputModel().from_grpc(result)

    with open('teo_ouput.json', 'w') as outfile:
        json.dump(processed.dict(), outfile)
    
    

if __name__ == '__main__':
    use_case()
