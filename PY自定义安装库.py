#  #//二改请表明作者TG:@Mo_Bai 
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//二改请表明作者TG:@Mo_Bai
#  #//二改请表明作者TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/

#  #English
#  #//Indicate the author if modified TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/ 
#  #//Indicate the author if modified TG:@Mo_Bai
#  #//Indicate the author if modified TG:@Mo_Bai


import subprocess
import sys
import pkg_resources
print('嗨，我是Mo_Bai的小助手，来帮你管理Python库啦！')
print('作者TG:@Mo_Bai')

#  #一个小函数，用来问问用户想不想继续
def ask_user(message):
    while True:
        response = input(message + " (想/不想): ").strip().lower()
        if response in ('想', 'y', 'yes'):
            return True
        elif response in ('不想', 'n', 'no'):
            return False
        else:
            print("嗯？好像没听懂，你再说一遍呗，是想还是不想？")

#  #再来一个函数，检查某个库是不是已经装好了
def is_library_installed(library_name):
    try:
        pkg_resources.get_distribution(library_name)
        return True
    except:
        return False

#  #这个函数负责实际去安装库
def install_library(library_name):
    try:
        #  #调用pip来安装库
        result = subprocess.run([sys.executable, "-m", "pip", "install", library_name],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        #  #安装成功啦！
        return True
    except subprocess.CalledProcessError as e:
        #  #安装出错了，告诉用户咋回事
        print(f"安装{library_name}的时候出错了:\n{e.stderr}", file=sys.stderr)
        return False
    except Exception as e:
        #  #别的啥错误也可能有，都告诉用户
        print(f"安装{library_name}的时候遇到了个奇怪的错误: {e}", file=sys.stderr)
        return False

#  #这些是一些常用的库，你看看需不需要
common_libraries = [
    'requests', 'beautifulsoup4', 'Pillow', 'urllib3', 'gmssl', 'Scrapy', 'pycryptodome',
    'seaborn', 'chardet', 'PyQt5', 'PyQt6'  #  #把PyQt5和PyQt6也加进来
]


#  #检查一下这些库都装了没，没装的话问问用户想不想装
missing_libraries = [lib for lib in common_libraries if not is_library_installed(lib)]
if missing_libraries:
    print(f"我发现你有几个常用的库还没装呢: {', '.join(missing_libraries)}")
    if ask_user("你想不想现在就把这些库装上？"):
        for library in missing_libraries:
            if library.startswith('PyQt'):
                #  #对于PyQt，要特别处理，因为有两个版本
                pyqt_version = library[5:]  #  #提取版本号，比如'5'或'6'
                if ask_user(f"你想安装PyQt的{pyqt_version}版本吗？"):
                    if install_library(library):
                        print(f"「{library}」已经给你装好啦！")
                    else:
                        print(f"「{library}」安装失败，你可能得自己手动装一下了。")
            else:
                if install_library(library):
                    print(f"「{library}」已经给你装好啦！")
                else:
                    print(f"「{library}」安装失败，你可能得自己手动装一下了。")
else:
    print("你常用的库都装好啦，真棒！")
#  #//二改请表明作者TG:@Mo_Bai
#  #如果之前没有安装PyQt，现在再单独问问用户
if 'PyQt5' in missing_libraries or 'PyQt6' in missing_libraries:
    #  #这里不需要再问了，因为上面已经处理过了
    pass
else:
    #  #否则，检查是否安装了任意一个PyQt版本
    pyqt_installed = is_library_installed('PyQt5') or is_library_installed('PyQt6')
    if not pyqt_installed:
        while True:
            pyqt_version = input("你还没有安装PyQt哦，你想装PyQt5还是PyQt6呀？输入5或6告诉我: ").strip()
            if pyqt_version in ('5', '6'):
                pyqt_package = f'PyQt{pyqt_version}'
                if install_library(pyqt_package):
                    print(f"「{pyqt_package}」也给你装上了！")
                    break
                else:
                    print(f"「{pyqt_package}」安装失败，你检查一下Python环境或者手动装一下呗。")
            else:
                print("你输入的不对哦，是5还是6呢？再试一次~")

#  #最后问问用户还有没有别的库想装的
additional_library = input("你还有没有别的库想装的？输入库名就行（如果不想装了，直接按Enter跳过）: ").strip()
if additional_library:
    if install_library(additional_library):
        print(f'「{additional_library}」也给你安装成功啦！')
    else:
        print(f'「{additional_library}」安装失败，你是不是输入错库名了，或者这个库不能用pip装？')

#  #全部搞定
print("好啦，所有的库都给你装好了，祝你用得开心哦！")

#繁體中文
# #//二改請表明作者TG:@Mo_Bai
# #//GitHub:https://github.com/MoBai-Curt/
# #//二改請表明作者TG:@Mo_Bai
# #//二改請表明作者TG:@Mo_Bai
# #//GitHub:https://github.com/MoBai-Curt/

#简体中文
#  #//二改请表明作者TG:@Mo_Bai 
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//二改请表明作者TG:@Mo_Bai
#  #//二改请表明作者TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/

#  #Russian

#  #//Укажите автора при внесении изменений TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//Укажите автора при внесении изменений TG:@Mo_Bai 
#  #//Укажите автора при внесении изменений TG:@Mo_Bai

#  #English

#  #//Indicate the author if modified TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/ 
#  #//Indicate the author if modified TG:@Mo_Bai
#  #//Indicate the author if modified TG:@Mo_Bai

#  #Spanish

#  #//Indique el autor si realiza modificaciones TG:@Mo_Bai 
#  #//GitHub:https://github.com/MoBai-Curt/ 
#  #//Indique el autor si realiza modificaciones TG:@Mo_Bai
#  #//Indique el autor si realiza modificaciones TG:@Mo_Bai

#  #French

#  #//Indiquez l'auteur en cas de modification TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/ 
#  #//Indiquez l'auteur en cas de modification TG:@Mo_Bai
#  #//Indiquez l'auteur en cas de modification TG:@Mo_Bai

#  #German

#  #//Geben Sie den Autor an, falls Sie Änderungen vornehmen TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//Geben Sie den Autor an, falls Sie Änderungen vornehmen TG:@Mo_Bai
#  #//Geben Sie den Autor an, falls Sie Änderungen vornehmen TG:@Mo_Bai

#  #Italian

#  #//Indicate l'autore in caso di modifiche TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//Indicate l'autore in caso di modifiche TG:@Mo_Bai
#  #//Indicate l'autore in caso di modifiche TG:@Mo_Bai

#  #Japanese

#  #//編集時には作者を明示してください TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//編集時には作者を明示してください TG:@Mo_Bai
#  #//編集時には作者を明示してください TG:@Mo_Bai

#  #Korean

#  #//수정할 경우 작성자를 명시하십시오 TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/ 
#  #//수정할 경우 작성자를 명시하십시오 TG:@Mo_Bai
#  #//수정할 경우 작성자를 명시하십시오 TG:@Mo_Bai

#  #Portuguese (Brazil)

#  #//Indique o autor caso faça modificações TG:@Mo_Bai
#  #//GitHub:https://github.com/MoBai-Curt/
#  #//Indique o autor caso faça modificações TG:@Mo_Bai
#  #//Indique o autor caso faça modificações TG:@Mo_Bai
