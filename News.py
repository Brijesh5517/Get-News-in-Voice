# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:19:44 2020

@author: Brijesh
"""
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)
#if __name__=='__main__':
    speak("News for Today   Lets begin")
    url='http://newsapi.org/v2/top-headlines?country=in&apiKey=9e5a1408637b420xxxxxxxxxxcc5b023'
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak('Moving to the next news')
#speak('Thanks for listening')

