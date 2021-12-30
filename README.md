# movies_recommendation_engine
 This is content based machine learning project that will recommend top similar movies based on user's search
 Not only user can see the recommended movies poster but also can watch their trailer also for getting idea about movies.
 
 similarity is found by using cosine similarity in scikit library.
 IDE used : jupyter notebook and pycharm editor
 Dataset used : TMDB dataset available on kaggle
 
 steps to execute:
 
 1) run jupyter notebook(untitled.ipynb
 2) two pickle file will be generated --> similarity.pkl and movies_dict_df.pkl
 3) copy these files into your pychram project folder along with app.py
 4) run app.py in command terminal of pycharm by writing command "streamlit run app.py"
 NOTE: make sure streamlit is installed in your env. for this write -> "pip install streamlit" in pycharm terminal and make sure to install it in project directory. 
 
 some outputs:
 
 ![image](https://user-images.githubusercontent.com/90515883/147734701-06a6586c-4ecf-41e5-9d82-6f513b94bce3.png)

These are top recommendation for selected movie :

![image](https://user-images.githubusercontent.com/90515883/147734783-00cf8024-a77a-48ea-a1a6-f23ae8ae6905.png)

Followed by their trailers:
![image](https://user-images.githubusercontent.com/90515883/147734841-23dbcb0f-cd96-47e8-ad42-1cc9fbf33dd6.png)

![image](https://user-images.githubusercontent.com/90515883/147734858-a870e7a9-469e-479a-8261-0ca4f6b06f72.png)

and so on!

 
 
