import vk_api

def delete_post(post_id):
    vk.wall.delete(post_id=post_id)

login = input('Enter VK login: ')
password = input('Enter VK password: ')
try:
    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
    except vk_api.exceptions.BadPassword:
        print('Bad password!'); exit()
    except vk_api.exceptions.AuthError:
        vk_session = vk_api.VkApi(login, password, auth_handler = lambda: [input('Enter two-factor auth code: '), False])
        vk_session.auth()

    vk = vk_session.get_api()

    while True:
        for post in vk.wall.get()['items']:
            if post['from_id'] == post['owner_id']:
                if post['text'].lower() == 'print \'hello!\'':
                    delete_post(post['id'])
                    print('hello!')
                
                # there you can add you triggers:
                # if post['text'].lower() == '%YOU STRING%': 
                # ....delete_post(post['id']) - for delete post
                # ....%DO SOMETHING%

                if post['text'].lower() == 'turn off':
                    delete_post(post['id'])
                    exit()

    print('Completed!')
except KeyboardInterrupt:
    print('Goodbye :D'); exit()
