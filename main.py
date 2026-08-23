

from recommend.recommender_system import recommend_class
  
def main():

  rec = recommend_class("data/outfit_data.csv")
  print("Recommendation of Red color and Party is :  ")
  print(rec.recommendation(color = "red",ocassion = "party"))
  

if __name__ == "__main__":
  main()
  
