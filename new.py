import os
import shutil

id = 1
while True:
    path = f"archived\\{id:03}.md"
    if not os.path.exists(path):
        break
    id += 1

shutil.copyfile("templete", f"{id:03}.md")
