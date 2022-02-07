from .pretty import pretty

def save_txt(inp,path_file=None):
    if path_file==None:
        import os
        path_file=os.path.join(os.getcwd(),'mypc.txt')
    with open(path_file,'w') as text:
        text.write(str(pretty(inp)))