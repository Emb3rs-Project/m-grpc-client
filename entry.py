from clients.market_module_client import MarketModuleClient


def use_case():
    market_client = MarketModuleClient("127.0.0.1", 50051)

    input_dict = {  # 'sim_name': 'test_pool',
        'md': 'pool',  # other options are  'p2p' or 'community'
        'nr_of_hours': 12,
        'offer_type': 'simple',
        'prod_diff': 'noPref',
        'network': 'none',
        'el_dependent': 'false',  # can be false or true
        'el_price': 'none',
        'agent_ids': ["prosumer_1",
                      "prosumer_2", "consumer_1", "producer_1"],
        'agent_types': ["prosumer", "prosumer", "consumer", "producer"],
        'objective': 'none',  # objective for community
        'community_settings': {'g_peak': 'none', 'g_exp': 'none', 'g_imp': 'none'},
        'gmin': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                 [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                 [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        'gmax': [[1, 2, 0, 5], [3, 4, 0, 4], [1, 5, 0, 3], [0, 0, 0, 0], [1, 1, 0, 1],
                 [2, 3, 0, 1], [4, 2, 0, 5], [3, 4, 0, 4], [1, 5, 0, 3],
                 [0, 0, 0, 0], [1, 1, 0, 1], [2, 3, 0, 1]],
        'lmin': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                 [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                 [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        'lmax': [[2, 2, 1, 0], [2, 1, 0, 0], [1, 2, 1, 0], [3, 0, 2, 0], [1, 1, 4, 0],
                 [2, 3, 3, 0], [4, 2, 1, 0], [3, 4, 2, 0], [1, 5, 3, 0], [0, 0, 5, 0],
                 [1, 1, 3, 0], [2, 3, 1, 0]],
        'cost': [[24, 25, 45, 30], [31, 24, 0, 24], [18, 19, 0, 32], [0, 0, 0, 0],
                 [20, 25, 0, 18], [25, 31, 0, 19], [24, 27, 0, 22], [32, 31, 0, 19],
                 [15, 25, 0, 31], [0, 0, 0, 0], [19, 20, 0, 21], [22, 33, 0, 17]],
        'util': [[40, 42, 35, 0], [45, 50, 40, 0], [55, 36, 45, 0], [44, 34, 43, 0],
                 [34, 44, 55, 0], [29, 33, 45, 0], [40, 55, 33, 0],
                 [33, 42, 38, 0], [24, 55, 35, 0], [25, 35, 51, 0], [19, 43, 45, 0], [34, 55, 19, 0]],
        'co2_emissions': 'none',  # allowed values are 'none' or array of size (nr_of_agents)
        'is_in_community': 'none',  # allowed values are 'none' or boolean array of size (nr_of_agents)
        'block_offer': 'none',
        'is_chp': 'none',  # allowed values are 'none' or a list with ids of agents that are CHPs
        'chp_pars': 'none',
        'gis_data':
            {'from_to': ['(0, 1)', '(1, 2)', '(1, 3)'],
             'losses_total': [22969.228855, 24122.603833, 18138.588662],
             'length': [1855.232413, 1989.471069, 1446.688900],
             'total_costs': [1.848387e+06, 1.934302e+06, 1.488082e+06]},
        'nodes': ["prosumer_1", "prosumer_2", "consumer_1", "producer_1"],
        'edges': [("producer_1", "consumer_1"), ("producer_1", "prosumer_1"),
                  ("prosumer_1", "prosumer_2"), ]
    }

    result = market_client.run_short_term(input_dict)

    print(f"{result}")


if __name__ == '__main__':
    use_case()
