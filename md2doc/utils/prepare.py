""" 准备工作
"""
import os
import shutil
from .static import SOURCE_DIR_PATH


hints_dict = {
    'not_dir': 'Your path may not a directory.',
    'no_md': 'No .md file detected in your directory.',
    'inner': 'Some trouble happened inside. To avoid further error, try to install again.'
}


def is_path_valid(dir_path):
    """ 检查路径是否合法 """
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(hints_dict['not_dir'])
    for _, _, file_list in os.walk(dir_path):
        is_markdown = lambda s: True if s.endswith('.md') else False
        if not any([is_markdown(each) for each in file_list]):
            raise FileNotFoundError(hints_dict['no_md'])
    else:
        return True


def copy_res_dir(ori_res_path):
    """ 拷贝markdown到指定位置 """
    if not os.path.split(SOURCE_DIR_PATH)[1] == 'markdown_files':
        raise FileExistsError(hints_dict['inner'])
    if os.path.exists(SOURCE_DIR_PATH):
        shutil.rmtree(SOURCE_DIR_PATH)
    shutil.copytree(ori_res_path, SOURCE_DIR_PATH)


def apply_conf():
    """ 根据设置调整conf.py """
    # TODO: 修改 项目名 作者名 主题类型 主题对应的css
    pass


def start_prepare(input_path):
    is_path_valid(input_path)
    copy_res_dir(input_path)
    apply_conf()


__all__ = [start_prepare]
