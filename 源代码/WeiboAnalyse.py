from weibopy import WeiboOauth2, WeiboClient
import webbrowser

client_key = '262607354'                            # 你的 app key
client_secret = '5345921237fa4ebe8d555a471f5a8da1'  # 你的 app secret
redirect_url = 'https://api.weibo.com/oauth2/default.html'

auth = WeiboOauth2(client_key, client_secret, redirect_url)
# 获取认证 code
webbrowser.open_new(auth.authorize_url)

# 在打开的浏览器中完成操作
# 最终会跳转到一个显示 「微博 OAuth2.0」字样的页面
# 从这个页面的 URL 中复制 code= 后的字符串
# URL 类似这样 https://api.weibo.com/oauth2/default.html?code=9c88ff5051d273522700a6b0261f21e6

code = input('输入 code:')

# 使用 code 获取 token
token = auth.auth_access(code)

print(token)

# token 是刚刚获得的 token，可以一直使用
client = WeiboClient(token['access_token'])

# suffix 指定 API 的名称，parmas 是参数，在文档中有详细描述
result = client.get(suffix='comments/show.json',
                    params={'id': 4416407817336332, 'count': 200, 'page': 10})

print(result)
