import json


## Short Term
def gis_module_to_short_term(river_data):
    optimize_network = json.loads(river_data['optimize_network'])
    output = {}

    output['res_sources_sinks'] = optimize_network['res_sources_sinks']
    output['network_solution_edges'] = optimize_network['network_solution_edges']
    output['network_solution_nodes'] = optimize_network['network_solution_nodes']
    output['selected_agents'] = optimize_network['selected_agents']

    return output

def cf_module_to_short_term(river_data):
    convert_source = json.loads(river_data['convert_source'])

    output = {}

    output['all_sources_info'] = convert_source['all_sources_info']

    return output

def teo_module_to_short_term(river_data):
    build_model = json.loads(river_data['build_model'])

    output = {}

    output['AccumulatedNewCapacity'] = build_model['AccumulatedNewCapacity']
    output['AnnualVariableOperatingCost'] = build_model['VariableOMCost']
    output['ProductionByTechnologyAnnual'] = build_model['ProductionByTechnology']
    output['AnnualTechnologyEmission'] = build_model['AnnualTechnologyEmission']

    return output

def platform_to_short_term(initial_data):
    output = {}

    output['md'] = initial_data['md']
    output['offer_type'] = initial_data['offer_type']

    output['network'] = initial_data['network']
    output['el_dependent'] = initial_data['el_dependent']
    output['nr_of_hours'] = initial_data['nr_of_hours']

    if output['md'] == 'community':
        output['objective'] = initial_data['objective']
        output['is_in_community'] = initial_data['is_in_community']
        if initial_data['community_settings'] :
            output['community_settings'] = initial_data['community_settings']
        else:
            output['community_settings'] = {
                "g_peak" : None,
                "g_exp" : None,
                "g_imp" : None,
            }

    if output['md'] == 'p2p':
        output['prod_diff'] = initial_data['prod_diff']

    if output['offer_type'] == 'block_offer':
        output['block_offer'] = initial_data['block_offer']

    if output['el_dependent'] is True:
        output['chp_pars'] = initial_data['chp_pars']
        output['el_price'] = initial_data['el_price']

    output['start_datetime'] = initial_data['start_datetime']
    output['util'] = initial_data['util']

    return output


convertSink = json.load(open('./json/input/convert_sink_output.json', encoding="utf8"))
convertSource = json.load(open('./json/input/convert_source_output.json', encoding="utf8"))
createNetwork = json.load(open('./json/input/create_network_output.json', encoding="utf8"))
optimizeNetwork = json.load(open('./json/input/optimize_network_output.json', encoding="utf8"))
buildModel = json.load(open('./json/input/buildmodel_output.json', encoding="utf8"))
initialData = json.load(open('./json/input/initial_data_short_term.json', encoding="utf8"))


riverData = {}

riverData['convert_sink'] = json.dumps(convertSink)
riverData['convert_source'] = json.dumps(convertSource)
riverData['build_model'] = json.dumps(buildModel)
riverData['create_network'] = json.dumps(createNetwork)
riverData['optimize_network'] = json.dumps(optimizeNetwork)



input_data = {}

input_data['platform'] = platform_to_short_term(initialData)
input_data['gis-module'] = gis_module_to_short_term(riverData)
input_data['cf-module'] = cf_module_to_short_term(riverData)
input_data['teo-module'] = teo_module_to_short_term(riverData)


with open('./json/output/short_term_output.json', 'w') as outfile:
    json.dump(input_data, outfile)
