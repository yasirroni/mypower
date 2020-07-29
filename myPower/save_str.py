from .api import pretty
def save_str(inp,path=None):
    if path==None:
        import os
        path=os.path.join(os.getcwd(),'mypc.txt')
    with open(path,'w') as text:
        text.write(str(pretty(inp)))