# md2doc

markdown文档整理工具

## 主要流程

- 输入：
    - 一系列markdown文件；
    - markdown文件夹路径；
    - html包输出路径；
    - 主题；
- 输出：
    - 制作好的html包；
    
## 执行流程

- prepare
    - 对输入进行规范性检查
    - 将文件拷入项目内指定位置
    - 根据输入调整设置

- build
    - 识别markdown的摆放结构
    - 用rst文件代替文件夹，生成一系列rst文件用于管理
    - 启动sphinx引擎构建html包

- clean
    - 将包输出到指定位置
    - 清理环境