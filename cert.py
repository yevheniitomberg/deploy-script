import sys
import os

os.system(f'certbot --nginx -d {sys.argv[1]}')