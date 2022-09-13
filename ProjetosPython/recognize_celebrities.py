from urllib import response
import boto3
import json

def recognize_celebrities(photo):
    client = boto3.client(
        service_name='rekognition',
        region_name='us-east-1',
        aws_access_key_id='rogercluts',
        aws_secret_access_key='disconnectjunioresdisconnect12ç'
    )
    
    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})
        
    for celebrity in response['CelebrityFaces']:
        print('\nNome: ' + celebrity['Name'])
        print(' Id: ' + celebrity['Id'])
        print('Posição:')
        print('  Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print('  Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print('Info:')
        for url in celebrity['Urls']:
            print('   ' + url)
        print
    return len(response['CelebrityFaces'])

def main():
    photo = input('Digite o local onde está a imagem: ')
    
    celeb_count = recognize_celebrities(photo)
    print('\n Celebridades detectadas: ' + str(celeb_count))
    
if __name__ == "__main__":
    main()