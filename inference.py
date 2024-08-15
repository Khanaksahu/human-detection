# import the inference-sdk
from inference_sdk import InferenceHTTPClient

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="tR99Gj2Sryjbc9MnWPJA"
)

# infer on a local image
result = CLIENT.infer("YOUR_IMAGE.jpg", model_id="human-detection-lpfdd/1")
