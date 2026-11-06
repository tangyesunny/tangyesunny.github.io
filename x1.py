from DrissionPage import ChromiumPage
import time,os,csv

filename='小红书数据'
if os.path.exists(filename):
    pass
else:os.makedirs(filename)
content=input('输入你要的内容：')

page = ChromiumPage()
page.listen.start('https://so.xiaohongshu.com/api/sns/web/v2/search/notes',method='POST')
page.get(f'https://www.xiaohongshu.com/search_result_ai?keyword={content}&source=web_explore_feed')
time.sleep(3)

page.ele('xpath://button[@class="xhs-ai-chat-header__close"]').click()
time.sleep(1)
Data=[]

for i in range(5):
    page.scroll.to_bottom()
    time.sleep(2)
    res=page.listen.wait()
    result=res.response.body
    items=result['data']['items']
    for item in items:
        try:
            liked_count=item['note_card']["interact_info"]['liked_count']
            collected_count = item['note_card']["interact_info"]['collected_count']
            comment_count = item['note_card']["interact_info"]['comment_count']
            shared_count = item['note_card']["interact_info"]['shared_count']
            title=item['note_card']['display_title']
            #print(title,liked_count,collected_count,comment_count,shared_count)
            Data.append([title,liked_count,collected_count,comment_count,shared_count])
            time.sleep(2)
        except Exception as e:
            print('程序错误，原因是：',e)
with open(f'{filename}/小红书数据.csv','w',newline='',encoding='utf-8') as f:
    cf=csv.writer(f)
    cf.writerow('题目','点赞','收藏','评论','分享')
    cf.writerows(Data)
