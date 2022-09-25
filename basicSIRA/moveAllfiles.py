from pathlib import Path

def move_all_kind(root:str = '.', dest:str = None, ext:str= 'txt'):
    '''
    Moves all same kind files to another directory
    The `src`and `dest` path can be relatives.
    '''
    if not Path(dest).exists():
        raise FileNotFoundError("Must assign a valid path")
    p = Path(src)
    dest_path = Path(dest)

    print(f'root path: {p.resolve()}/n \
        destination path: {dest_path.resolve()}')

    for file_path in p.rglobe(f'*.{ext}'):
        file_path.rename(dest_path/file_path.name)