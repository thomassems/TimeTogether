from transformers import pipeline

# Load the zero-shot classification pipeline with the desired model
# You can choose different models, like 'facebook/bart-large-mnli' or 'roberta-large-mnli'
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Example class descriptions
class_descriptions = ["business", "surgery", "conference", "anniversary", "interview", "board meeting", "presentation", "medical", "flight", "funeral"]

# Preload model outside the function
def preload_model():
    global classifier
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Preload model
preload_model()

# Batch processing for improved efficiency
def get_scores(input_texts):
    results = classifier(input_texts, class_descriptions, batch_size=len(input_texts))
    return [result["scores"][0] for result in results]

# Example input texts
#input_texts = ["Going to walk a dog", "Attending a business conference", "going to the doctor's office"]

# Get scores for input texts
#print(get_scores(input_texts))