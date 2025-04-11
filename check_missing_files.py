import pathlib

def check_missing_files(path, count_chapters):
    # path = pathlib.Path("C:\\Users\\raikoben\\Desktop\\Frontier Shangri La")
    absolute_path = pathlib.Path().absolute()
    path = pathlib.Path(f"{absolute_path}\\{path}")

    files = []
    for file in path.iterdir():
        files.append(int(file.name.strip(".docx")))
    
    missing_chapters = []
    files.sort()
    files.append(0)
    for i in range(count_chapters):
        if files[i] != i + 1:
            missing_chapters.append(i + 1)
            print(f"Missing file: {i + 1}")
            files.insert(i, i + 1)
    else:
        print("All files here")
        
    return missing_chapters if len(missing_chapters) > 0 else False