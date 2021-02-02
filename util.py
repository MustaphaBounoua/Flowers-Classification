import os
import shutil
import requests
import time
from functools import wraps
import traceback
from tqdm import tqdm
import tensorflow

# https://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except KeyboardInterrupt as e:
                    raise e
                except ExceptionToCheck as e:
                    print("%s, retrying in %d seconds..." % (str(e), mdelay))
                    traceback.print_exc()
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)
        return f_retry  # true decorator
    return deco_retry



@retry(Exception)
def download_file(url, file_path):
    """Download file

    Args:
        url ([str]): [Url of the file]
        file_path ([File_path]): [Where to save the file]

    Raises:
        Exception: [KeyboardInterrupt or  ExceptionToCheck ]
    """
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length'))
    
    incomplete_download = False
    try:
        with open(file_path, 'wb', buffering=16 * 1024 * 1024) as f:
            for chunk in tqdm(r.iter_content(4 * 1024 * 1024) ):
                f.write(chunk)
    except Exception as e:
        raise e
    finally:
        if os.path.exists(file_path) and os.path.getsize(file_path) != total_size:
            incomplete_download = True
            os.remove(file_path)
    if incomplete_download:
        raise Exception("Incomplete download")