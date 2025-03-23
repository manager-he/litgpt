import zipfile
import os

def unzip_file(zip_path, extract_to='.'):
    """
    解压指定的 ZIP 文件到指定的目录。

    :param zip_path: ZIP 文件的路径
    :param extract_to: 解压到的目录，默认为当前目录
    """
    if not os.path.exists(zip_path):
        print(f"文件 {zip_path} 不存在。")
        return

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"文件 {zip_path} 已成功解压到 {extract_to}。")

if __name__ == "__main__":

    zip_file_path = 'data/numpy/numpy.zip'
    unzip_file(zip_file_path, extract_to='data/numpy')
