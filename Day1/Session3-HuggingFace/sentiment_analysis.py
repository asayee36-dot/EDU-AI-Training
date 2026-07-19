from transformers import pipeline 
 
# Load pretrained sentiment model 
classifier = pipeline("sentiment-analysis") 
 
# Test sentences 
sentences = [ 
    "The training today was excellent and very clear.", 
    "I am tired and the room is too hot.", 
    "Our team will win this exercise!" 
] 
 
for s in sentences: 
    result = classifier(s)[0] 
    print(f"{s} -> {result['label']} ({result['score']:.2f})") 
