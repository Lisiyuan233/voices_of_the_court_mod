# 一些常见问题

## 一、没有弹出对话框
该mod需要运行额外后端程序，汉化后端程序下载地址：[https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest)，下载下来的exe文件打开后会自动安装。


## 二、api配置问题
建议使用DeepSeek官方api，在对话模型连接的下拉框中选择`custom(openai-compatible)`页面进行配置：
- Server URL需要填写：`https://api.deepseek.com/beta`
- api key填入自己的apikey，可在[https://platform.deepseek.com](https://platform.deepseek.com)申请。

如果有openai和openrouter，也应该都可以使用。


## 三、安装好后，在后端程序运行的情况下没有弹出对话框
**解决方法**：需要使用汉化mod才行。

安装方法（二选一）：
1. 将下载下来的汉化mod文件解压后，直接覆盖创意工坊中的原mod文件；
2. 将解压后的mod文件夹`voices_of_the_court_mod-1.2.1-beta`放入游戏mod文件夹，然后用记事本在`Documents\Paradox Interactive\Crusader Kings III\mod`文件夹中新建一个`voices_of_the_court_mod-1.2.1-beta.mod`文件，内容如下：
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ 这里是你电脑的用户名 / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

如果安装开启汉化mod后依然不会弹出对话框，可能是CK3 用户文件夹路径设置不正确，或者是游戏处于铁人模式，改mod在铁人模式下不会生效。

## 四、打开聊天窗口时，收到一个带有红色文本的错误"TypeError： Cannot read properties of undedined （reading 'playerID'）"
**解决**：在`Documents\Paradox Interactive\Crusader Kings III`中创建一个名为 `run` 的文件夹，进入创建的文件夹并创建一个名为 `votc.txt` 的文本文件

## 五、和人物对话时读取不到最近的记忆
**解决**：  
1. 原作者后端程序的小bug，下载汉化的后端可解决。  
2. 还可能是memoery tokens限制，在后端程序的setting/设置页面调整max memory tokens/最大记忆令牌数的大小，调整记忆tokens的大小后要同时调大最大新令牌数，最大新令牌数最好大于最大记忆令牌数。

## 六、修改了提示词生成脚本，重新打开后端程序后就还原了
**解决**：  
另存一个放在custom文件夹中。

## 许可证与归属

### 模组信息
- **模组名称**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **许可证**: GNU General Public License v3.0 (GPLv3)
- **支持的CK3版本**: 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### GPLv3声明
本程序是自由软件：您可以根据自由软件基金会发布的GNU通用公共许可证的条款重新分发和/或修改它，许可证版本3或（根据您的选择）任何更高版本。

本程序是希望它有用而分发的，但没有任何保证；甚至没有适销性或特定用途适用性的暗示保证。有关更多详细信息，请参阅GNU通用公共许可证。

您应该已经收到了GNU通用公共许可证的副本以及本程序。如果没有，请参阅<https://www.gnu.org/licenses/>。
