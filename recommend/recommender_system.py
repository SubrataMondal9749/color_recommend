

import pandas as pd
class recommend_class:

  def __init__(self,file_data):
    self.data = pd.read_csv(file_data)

  def recommendation(self,color = None,ocassion = None):

    result = self.data

    if color:
      result = result[result['color'].str.lower() == color.lower()]
      
    if ocassion:
      result = result[result['ocassion'].str.lower() == ocassion.lower()]

      return result['outfits'].tolist()

    