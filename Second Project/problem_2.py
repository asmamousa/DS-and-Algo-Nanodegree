import os

def find_files(suffix, path, out_list=[]):
    if suffix is None or suffix=='':
        raise Exception("Specify a suffix for the needed files")
    if path is None or not (os.path.exists(path)):
        raise Exception("Invalid path")

    file_dir_list = os.listdir(path)

    if len(file_dir_list) == 0:
        return

    for file_dir in file_dir_list:
        file_dir_path = os.path.join(path, '/', file_dir)
        if os.path.isfile(file_dir_path):
            if file_dir.endswith(suffix):
                out_list.append(file_dir_path)

        elif os.path.isdir(file_dir_path):
            temp_list = find_files(suffix, file_dir_path, out_list)

    return out_list



final_output = find_files('.c', '.')
print (final_output)
# returns ['./subdir1/a.c', './subdir3/subsubdir1/b.c', './subdir5/a.c', './t1.c']


final_output = find_files('', '.')
print (final_output
# raises an exception with the message "Specify a suffix for the needed files"

final_output2 = find_files('.c', '')
print (final_output)
#raises an exception with the message Invalid path

