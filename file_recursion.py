import os


def find_files(suffix, path):
    """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
    """
    
    try:
        path_list = []
        
        for sub_path in sorted(os.listdir(path)):
            total_path = os.path.join(path, sub_path)
            
            if os.path.isdir(total_path):
                sub_list = find_files(suffix, total_path)
                
                if sub_list:
                    path_list += sub_list
            elif sub_path.endswith(suffix):
                path_list.append(total_path)
    except:
        return -1

    return path_list

def test():
    # Test case 1: regular file suffix
    paths = find_files("c", "testdir")
    test = ['testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c',
             'testdir/subdir5/a.c', 'testdir/t1.c']
    assert paths == test

    # Test case 2: regular file suffix
    paths = find_files("h", "testdir")
    test = ['testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h',
             'testdir/subdir5/a.h', 'testdir/t1.h']
    assert paths == test

    # Test case 3: path does not exist
    paths = find_files("c", "test")
    assert paths == -1

    # Test case 4: no file with suffix exist
    paths = find_files("exe", "testdir")
    assert paths == []

    # Test case 5: all file paths are listed
    paths = find_files("", "testdir")
    test = ['testdir/subdir1/a.c', 'testdir/subdir1/a.h',
            'testdir/subdir2/.gitkeep', 'testdir/subdir3/subsubdir1/b.c',
            'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir4/.gitkeep',
            'testdir/subdir5/a.c', 'testdir/subdir5/a.h', 'testdir/t1.c',
            'testdir/t1.h']
    assert paths == test

    # Test case 6: no file suffix or directory
    paths = find_files("", "")
    assert paths == -1

    # print("All tests passed")

test()
