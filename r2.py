import getopt
import os.path
import sys

import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'xxxxxxx'
SECRET_ACCESS_KEY = 'xxxxxxx'
BUCKET_NAME = 'xxxxxxxx'
ENDPOINT_URL = 'xxxxxxx'


def print_usage():
    print('Usage: r2 [options]\n')
    print('Options:')
    print('  -h, --help           Show this help message and exit')
    print('  -f FILE, --file FILE Specify the file to upload to the cloud')
    print("  -p PROXY, --proxy PROXY Specify the proxy server to use")

    print('\nExamples:')
    print('r2 -f example.txt')
    print('r2 --file=example.txt')
    print('r2 --file=example.txt -p http://proxyserver:port')
    print('\nDescription:')
    print('\tThis tool allows you to upload files to the cloud')


def main(argv):
    input_file = None
    object_name = None
    proxy = None
    try:
        opts, args = getopt.getopt(argv, "f:hp:", ["file=", "proxy="])
    except getopt.GetoptError as err:
        print(str(err))
        print_usage()
        sys.exit(2)

    if len(opts) == 0:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-f", "--file"):
            input_file = arg
            object_name = os.path.basename(input_file)
        elif opt in ("-p", "--proxy"):
            proxy = arg
        elif opt in ("-h", "--help"):
            print_usage()
            sys.exit(2)
        else:
            print_usage()
            sys.exit(2)

    if proxy is not None:
        config = Config(signature_version='s3v4', proxies={'http': proxy})
    else:
        config = Config(signature_version='s3v4')

    client = boto3.client(
        's3',
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        config=config
    )
    try:
        client.upload_file(input_file, BUCKET_NAME, object_name)
        print('Upload success')
    except Exception as err:
        print('Upload failed: %s' % str(err))


if __name__ == '__main__':
    main(sys.argv[1:])
