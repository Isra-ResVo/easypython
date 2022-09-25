# Libraries

from requests_html import AsyncHTMLSession
import requests

# Session and request
def down_zip_async(url:str, path_dir:str = '/data', url_file:str = None)->None:
    '''
    This function dowload all the zip files from a web page,
    the links must to finish in zip extention to be recognized.
    '''
    AsyncHTMLSession()
    r = await asession.get(url)
    await r.html.arender(sleep=1) # The sleep arg is necessary I don't know why...
    r.close()

    # Processing and saving to a file the links

    links = r.html.links

    dir_path = path_dir
    path_file = dir_path + url_file 

    with  open(path_file, mode='w') as url_files:
        for link in links:
            if link.split('.')[-1] == 'zip':
                url_files.write(link + '\n')

    # Download data

    with open(path_file, mode='r') as url_file:
        for link in url_file:
            link = link[0:-1] # rid the \n character
            response = requests.get(link)
            file_name = link.split('/')[-1]
            with open(dir_path + file_name, mode='wb') as zipfile:
                zipfile.write(response.content)
            print(f'succcesful downloaded file: {file_name}')

def main():
    # example of use
    url = 'https://somepage.com'
    path_dir = "data/"
    urls_file = "url_files.txt" 



if __name__=='__main__':
    main()