import os

from .count_nout import count_nout

def port(path_in,path_out):
    files_list=[]
    for dirpath, _, files in os.walk(path_in):
        files_list.extend(files)
        dirpath_prune = dirpath.replace(path_in,'').replace("@","at_").replace("-","_")
        depth = 2
        for s in dirpath_prune:
            if s == '\\' or s == '/':
                depth += 1
        dots = '.'*depth
        # print(dirpath_prune)
        # print(dots)

        for f in files:
            if f[-2:] == '.m':
                if os.path.basename(os.path.normpath(dirpath)+".m") in files_list:
                    print(os.path.basename(os.path.normpath(dirpath)))
                    current_folder = os.path.join(path_out,"_"+dirpath_prune[1:])
                else:
                    current_folder = os.path.join(path_out,dirpath_prune[1:])
                # print(path_out)
                # print(dirpath_prune)
                # print(current_folder)

                if not os.path.isdir(current_folder):
                    os.makedirs(current_folder)
                if not os.path.isfile(os.path.join(current_folder,'__init__.py')):
                    with open(os.path.join(current_folder,'__init__.py'),'w') as fout:
                        pass

                nout = count_nout(os.path.join(dirpath,f))
                # print(os.path.join(dirpath,f))

                with open(os.path.join(current_folder,f[:-2]+'.py'),'w') as fout:
                    fout.write(f'def {f[:-2]}(*args,nout={nout},oc=None):\n')
                    fout.write('\tif oc == None:\n')
                    fout.write(f'\t\tfrom {dots}oc_api import oc_matpower\n')
                    fout.write('\toc = oc_matpower()\n')
                    fout.write(f'\treturn oc.{f[:-2]}(*args,nout=nout)\n')