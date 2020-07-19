from myp_pretty import myp_pretty
def print_log(inp,path=None):
    if path==None:
        import os
        path=os.path.join(os.getcwd(),'log.txt')
    with open(path,'w') as log:
        log.write(str(myp_pretty(inp)))