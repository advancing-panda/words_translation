import json
from urllib.parse import urlencode
from urllib.request import urlopen
 
def translate(word):
    #从有道获取翻译的HTML

    #编辑并发送请求
    query = {'q': "".join(word)} 
    url = 'https://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + urlencode(query)
    try:
        response = urlopen(url, timeout=3)
    except:#连接错误
        print("**网络连接错误**")
        return "**网络连接错误**"
    word_json = response.read().decode('utf-8')

    #将json转换成所需字符
    word_dict = json.loads(word_json)    #将对象转换为字典
    if word_dict.get('errorCode') == 0: #判断是否出错
        if word_dict['translation'][0] != word_dict['query']:   #判断是否查询到翻译
            explains = word_dict.get('basic').get('explains')   #储存各条翻译
            # print(explains) 测试所用代码
            reasult = ''
            for explain in explains:    #编辑翻译结果字符串
                reasult = reasult + '  ' + explain
            reasult = reasult[2:]
            print('已翻译：' + word + ':' + reasult)
        else:
            reasult = '**未找到翻译**'
            print(reasult)
    else:
            reasult = '**翻译错误**'
            print(reasult)

    return reasult

if __name__ == '__main__':
    #获取所需要翻译的单词
    word_file = open('in.txt')
    words = word_file.readlines()
    for i, word in enumerate(words):
        words[i] = word.rsplit('\n')[0]
    word_file.close()

    #翻译并写入文件
    reasult_file = open('out.txt', mode = 'w', encoding = 'utf8')
    print("**开始翻译**")
    for word in words:
        reasult_r = word + '\t' + translate(word) + '\n'
        reasult_file.write(reasult_r)
        # print(reasult_r) 测试所用代码

    reasult_file.close()
    # input('**翻译结束**\n**按回车关闭**') #可选语句