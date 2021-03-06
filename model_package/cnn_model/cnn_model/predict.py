from cnn_model.cnn_architecture import model
from numpy import argmax
from cnn_model.pipeline import Pipeline

def make_prediction(*, input_image):
    """
    Making a prediction using the inference pipeline
    param input_image: A path to a jpeg image, string
    return: A numpy array that contains a single prediction
    """
    
    pipeline = Pipeline(model)
    resized_image = pipeline.resize_image(input_image)
    prediction = argmax(pipeline.make_prediction(resized_image))
    
    return prediction

print("works")