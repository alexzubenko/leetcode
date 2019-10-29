import json

json_to_parse = """
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "area_codes": ["205", "251", "256", "334", "938"]
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "area_codes": ["907"]
    },
    {
      "name": "Arizona",
      "abbreviation": "AZ",
      "area_codes": ["480", "520", "602", "623", "928"]
    }
  ]
}

"""

parsed_dict = json.loads(json_to_parse)

for state in parsed_dict['states']:
    print(state)
    del state['area_codes']
    print(state)