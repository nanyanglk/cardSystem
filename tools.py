
card_list = []


#菜单
def menu():
    print('\n\n\n','*' * 50)
    print(' 1：新增名片\n 2：显示全部\n 3：搜索编辑\n \n 0：退出程序')
    print('*' * 50)

#新增名片
def new_card():
    print('-' * 50)
    print('：新增名片')
    name = input('Please enter your name: ')
    phone = input('Please enter your phone number: ')
    wechat = input('Please enter your wechat: ')
    email = input('Please enter your email: ')
    card_dict = {'name':name,
                'phone':phone,
                'wechat':wechat,
                'email':email}
    card_list.append(card_dict)
    print('\n添加{}成功\n'.format(name))


#显示所有名片
def show_all():
    print('-' * 50)
    print('：显示所有名片')

    if len(card_list) == 0:
        print('当前没有任何名片记录，请先添加名片！')
        return

    print('-' * 50)    
    for name in ['姓名', '电话', '微信', '邮箱']:
        print('{}'.format(name), end='\t\t')
    print('\n','-' * 50)
    for card_dict in card_list:
        print('{}\t{}\t{}\t{}'.format(card_dict['name'],
                                                            card_dict['phone'],
                                                            card_dict['wechat'],
                                                            card_dict['email']))


#搜索名片
def search_card():
    print('-' * 50)
    print('：搜索名片')
    find_name = input('请输入要搜索的姓名: ')

    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名\t\t电话\t\t微信\t\t邮箱')
            print('=' * 50)
            print('{}\t{}\t{}\t{}'.format(card_dict['name'],
                                                            card_dict['phone'],
                                                            card_dict['wechat'],
                                                            card_dict['email']))

            deal_card(card_dict)   
            break
    
    else:
        print('抱歉没有找到 {} 信息'.format(find_name))

def deal_card(find_dict):

    action_str = input('\n\n请选择要执行的操作 [1]：修改 [2]：删除 [3]: 清空 [请谨慎操作！！！] [0]：返回上级菜单：')    
    
    if action_str == '1':
        print('\n修改名片: ')
        find_dict['name'] = input_card_info(find_dict['name'], '姓名[回车默认不修改]: ')
        find_dict['phone'] = input_card_info(find_dict['phone'], '电话[回车默认不修改]: ')
        find_dict['wechat'] = input_card_info(find_dict['wechat'], '微信[回车默认不修改]: ')
        find_dict['email'] = input_card_info(find_dict['email'], '邮箱[回车默认不修改]: ')
        print('\n修改成功！')

    elif action_str == '2':
        card_list.remove(find_dict)
        print('\n删除名片')

    elif action_str == '3':
        option = input('\n确认是否清空全部名片！【Y】or【N】：')
        
        if option == 'Y' or option == 'y':
            card_list.clear()
            print('\n清空成功!')
        
        elif option == 'N' or option == 'n':
            print('\n您选择不清空')
            return
        
        else:
            print('\n请按照提示输入')



def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
    
