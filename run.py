# 处理&接受外界传入的一系列设置 开始运行
INPUT_PATH = '/Users/fengzhangchi/Downloads/md2doc/test/input'
OUTPUT_PATH = '/Users/fengzhangchi/Downloads/md2doc/test/output'


from md2doc.utils.prepare import start_prepare


if __name__ == '__main__':
    start_prepare(INPUT_PATH)