import json
from urllib.request import urlopen

def read_geojson(input_file):
  """
  Read a geojson file

  Parameters
  ----------
  input_file : str
               The PATH to the data to be read

  Returns
  -------
  gj : dict
       An in memory version of the geojson
  """
  # with open(input_file, 'r') as f:
  #     gj = json.load(f)
  response = urlopen("https://api.myjson.com/bins/4587l").read().decode('utf8')
  gj = json.loads(response)

  return gj
