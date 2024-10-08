# 如何安装与配置
### Mac
安装：`brew install --cask squirrel`

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

# 在 Mac 下使用删除自带的 ABC 输入法
关机长按指纹键, 进入恢复模式, 在顶部的菜单栏中的实用工具中找到终端, 输入 csrutil disable, 如果输出下面的表示禁用成功
`Successfully disabled System Integrity Protection. Please restart the machine for the changes to take effect. 
`
修改com.apple.HIToolbox.plist文件, 重启即可
```shell

# 备份plist文件
cp ~/Library/Preferences/com.apple.HIToolbox.plist  ~/Library/Preferences/com.apple.HIToolbox.plist.backup

# 这里使用下面的指令看一下是不是这个样子(第一个Dict的Name是ABC)
# AppleEnabledInputSources = Array {
#         Dict {
#             InputSourceKind = Keyboard Layout
#             KeyboardLayout Name = ABC
#             KeyboardLayout ID = 252
#         }
#         ......
#     }
/usr/libexec/PlistBuddy -c "Print"  ~/Library/Preferences/com.apple.HIToolbox.plist 

# 删除ABC输入法
/usr/libexec/PlistBuddy -c "Delete :AppleEnabledInputSources:0"  ~/Library/Preferences/com.apple.HIToolbox.plist 

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




