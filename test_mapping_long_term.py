import json


## Long Term
def gis_module_to_long_term(river_data):
    optimize_network = json.loads(river_data['optimize_network'])
    output = {}

    output['res_sources_sinks'] = optimize_network['res_sources_sinks']
    output['network_solution_edges'] = optimize_network['network_solution_edges']
    output['network_solution_nodes'] = optimize_network['network_solution_nodes']
    output['selected_agents'] = optimize_network['selected_agents']

    return output

def cf_module_to_long_term(river_data):
    convert_source = json.loads(river_data['convert_source'])
    convert_sink = json.loads(river_data['convert_sink'])

    output = {}

    output['all_sources_info'] = convert_source['all_sources_info']
    output['all_sinks_info'] = convert_sink['all_sinks_info']

    return output

def teo_module_to_long_term(river_data):
    build_model = json.loads(river_data['build_model'])

    output = {}

    output['AccumulatedNewCapacity'] = build_model['AccumulatedNewCapacity']
    output['AnnualVariableOperatingCost'] = build_model['VariableOMCost']
    output['ProductionByTechnologyAnnual'] = build_model['ProductionByTechnology']
    output['AnnualTechnologyEmission'] = build_model['AnnualTechnologyEmission']

    return output

def platform_to_long_term(initial_data):
    output = {}

    output['md'] = initial_data['md']
    output['start_datetime'] = initial_data['start_datetime']
    output['util'] = initial_data['util']
    output['horizon_basis'] = initial_data['horizon_basis']
    output['data_profile'] = initial_data['data_profile']
    output['recurrence'] = initial_data['recurrence']

    if output['horizon_basis'] == 'years' and output['recurrence'] > 1:
        output['yearly_demand_rate'] = initial_data['yearly_demand_rate']

    if output['md'] == 'decentralized':
        output['prod_diff_option'] = initial_data['prod_diff_option']

    return output

convertSink = json.load(open('./json/input/convert_sink_output.json', encoding="utf8"))
convertSource = json.load(open('./json/input/convert_source_output.json', encoding="utf8"))
createNetwork = json.load(open('./json/input/create_network_output.json', encoding="utf8"))
optimizeNetwork = json.load(open('./json/input/optimize_network_output.json', encoding="utf8"))
buildModel = json.load(open('./json/input/buildmodel_output.json', encoding="utf8"))
initialData = json.load(open('./json/input/initial_data_long_term.json', encoding="utf8"))


riverData = {}

riverData['convert_sink'] = json.dumps(convertSink)
riverData['convert_source'] = json.dumps(convertSource)
riverData['build_model'] = json.dumps(buildModel)
riverData['create_network'] = json.dumps(createNetwork)
riverData['optimize_network'] = json.dumps(optimizeNetwork)


input_data = {}

input_data['platform'] = platform_to_long_term(initialData)
input_data['gis-module'] = gis_module_to_long_term(riverData)
input_data['cf-module'] = cf_module_to_long_term(riverData)
input_data['teo-module'] = teo_module_to_long_term(riverData)


with open('./json/output/long_term_output.json', 'w') as outfile:
    json.dump(input_data, outfile)
