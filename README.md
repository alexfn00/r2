# r2
tool for uploading files into cloudflare storage

# Replace paramters in cloudflare: 
```
ACCESS_KEY_ID = 'xxxxxxx'
SECRET_ACCESS_KEY = 'xxxxxxx'
BUCKET_NAME = 'xxxxxxxx'
ENDPOINT_URL = 'xxxxxxx'
```

# usage
Usage: r2 [options]

Options:
  -h, --help           Show this help message and exit
  -f FILE, --file FILE Specify the file to upload to the cloud
  -p PROXY, --proxy PROXY Specify the proxy server to use

Examples:
r2 -f example.txt
r2 --file=example.txt
r2 --file=example.txt -p http://proxyserver:port

Description:
        This tool allows you to upload files to the cloud
