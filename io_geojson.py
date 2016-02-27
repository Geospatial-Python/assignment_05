import json

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
  with open(input_file, 'r') as f:
      gj = json.load(f)
  return gj
