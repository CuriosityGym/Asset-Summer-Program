import boto3

if __name__ == "__main__":

    imageFile='numberplate.jpg'
    client=boto3.client('rekognition','us-west-2')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_text(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    print(response)
