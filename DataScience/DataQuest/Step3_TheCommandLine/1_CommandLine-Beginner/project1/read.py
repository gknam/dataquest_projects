from urllib.parse import urlparse
parsed_uri = urlparse( 'bbc.co.uk' )
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
print (domain)
