import os

from clients.cf_module_client import CFModuleClient
from clients.market_module_client import MarketModuleClient

from cf.cf_models import ConvertSinkOutputModel

import dotenv

from data.cf_data import cf_data


dotenv.load_dotenv()


def use_case():
    market_client = MarketModuleClient(os.getenv("MARKET_HOST"), os.getenv("MARKET_PORT"))
    cf_client = CFModuleClient(os.getenv("CF_HOST"), os.getenv("CF_PORT"))

    result = cf_client.convert_sink(cf_data)

    print(f"{result}")


if __name__ == '__main__':
    use_case()
