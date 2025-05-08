import pickle
import pandas as pd

# Load the similarity model
with open('course_similarity_model.pkl', 'rb') as f:
    sim_df = pickle.load(f)

def recommend_course(course_name, top_n=5):
    if course_name not in sim_df.columns:
        return f"'{course_name}' not found in course list."
    
    sim_scores = sim_df[course_name].sort_values(ascending=False)
    return sim_scores[1:top_n+1]  # Skip the course itsel