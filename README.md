# Human Detection from Drone Footage Using Computer Vision

This project involves the development and implementation of a computer vision algorithm designed to detect humans from a large dataset of drone footage. 


# Linux or MacOS
Retrieving JSON predictions for a local file called YOUR_IMAGE.jpg

base64 YOUR_IMAGE.jpg | curl -d @- \"https://detect.roboflow.com/human-detection-lpfdd/1?api_key=tR99Gj2Sryjbc9MnWPJA"

Inferring on an image hosted elsewhere on the web via its URL (don't forget to URL encode it):

curl -X POST \ 
"https://detect.roboflow.com/human-detection-lpfdd/1?api_key=tR99Gj2Sryjbc9MnWPJA&image=URL_OF_YOUR_IMAGE"

# Windows 
You will need to install curl for Windows and GNU's base64 tool for Windows. The easiest way to do this is to use the git for Windows installer which also includes the curl and base64 command line tools when you select "Use Git and optional Unix tools from the Command Prompt" during installation. Then you can use the same commands as above.







