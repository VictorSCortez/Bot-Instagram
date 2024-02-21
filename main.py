import os
import requests
import tweepy
from instabot import Bot

#login no X
consumer_key = "SuaConsumerKey"
consumer_secret = "SeuConsumerSecret"
access_token = "SeuAccessToken"
access_token_secret = "SeuAccessTokenSecret"

#login no insta
username = "seu_nome"
password = "sua_senha"
perfil_instagram = "o_perfil"

bot_instagram = Bot()
bot_instagram.login(username=username, password=password)

#obter os posts recentes
posts = bot_instagram.get_user_medias(perfil_instagram, filtration=False)

print(posts)
if posts:
    #obter a URL da última foto
    ultimo_post = posts[0]["url"]
    
    #baixar a foto
    post_filename = "ultimo_post_instagram.jpg"
    with open(post_filename, 'wb') as f:
        f.write(requests.get(ultimo_post).content)
    
    #configure a autenticação do X
    auth = tweepy.OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #fazer o upload do post para o X
    api.update_with_media(post_filename, status="Confira o último post do Instagram!")
    
    #excluir o post
    os.remove(post_filename)
else:
    print("nenhum post encontrada no perfil do Instagram.")

#sair do Instagram
bot_instagram.logout()
