# 如何安装与配置
### Mac
安装：`brew install --cask squirrel`

```shell
git clone git@github.com:qujihan/Rime.git ~/Library/Rime
cd ~/Library/Rime/dicts
pip install requests; python download.py
```

配置：将所有文件复制到 `Users/${UserName}/Library/Rime`

### Windows
安装：[下载页面](https://github.com/rime/weasel/releases)

配置：将所有文件复制到 `C:\Users\${UesrName}\AppData\Roaming\Rime`

### Ubuntu
```
sudo apt install ibus-rime
cd ~/.config/ibus
rm -rf rime
git clone https://github.com/qujihan/Rime.git rime
```

# 文档
日后的修改可以参考[文档](https://github.com/LEOYoon-Tsaw/Rime_collections)

# 感谢
- 配置参考: [LufsX/rime](https://github.com/LufsX/rime)
- 词库参考: 
    - [雾凇拼音 rime-ice](https://github.com/iDvel/rime-ice)
    - [白霜词库 rime-frost](https://github.com/gaboolic/rime-frost)
- 字体: 
    - [Lxgw](https://github.com/lxgw)
    - [花园明朝字体](https://glyphwiki.org/hanazono/)




