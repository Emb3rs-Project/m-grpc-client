from clients.market_module_client import MarketModuleClient


def use_case():
    client = MarketModuleClient("127.0.0.1", 50051)
    result = client.run_short_term({})

    print(f"{result}")


if __name__ == '__main__':
    use_case()
