from TwitterAPI import TwitterAPI


consumer_key = '47BxI5lHo8dd4Krq5Ur5AmMGG'
consumer_secret = 'XfBjjOTONN9SCi2CjE0FobOyfzlyvGNfNrmFjX61at2FdNjFzu'
access_token_key = '1958278392-1ef1X83bOIRGzUXOs2JE7sok48HR10Nm0WvJgyj'
access_token_secret = 'tfNOAhuEbB1ztvhZdBx4Fh3KnQC0mANwzd7LEoiPlUz1Q'

file = open("data.txt","a")

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('search/tweets', {'q':'สังเกตุ'})

def __init__(self, csocket):
    self.client_scoket = csocket

for item in r:
    text_encode = item['text'].encode('utf-8')
    text_encode_second = text_encode.encode('cp874')
    text_decode = text_encode_second.decode('cp874')
    file.write('%s\n' %text_decode)