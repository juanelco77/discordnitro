"""MIT License

Copyright (c) 2020-2021 LnX - DR34M-M4K3R

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE"""




import os
from time import sleep
import requests
import random
import string
from colorama import Fore


os.system("cls")

print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator made by {Fore.WHITE}LnX{Fore.LIGHTBLACK_EX}, improved by {Fore.WHITE}DR34M-M4K3R{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Original creator: {Fore.WHITE}https://github.com/lnxcz")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Creator of this version : {Fore.WHITE}https://github.com/DR34M-M4K3R")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}See what is new here: {Fore.WHITE}https://github.com/DR34M-M4K3R/nitro-generator/blob/master/README.md#whats-new")
amount = int(input(f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How much codes will be generated: {Fore.WHITE}"))
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Classic Nitro is 16chars and Boost Nitro is 24chars")
nitro = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Boost codes or Classic codes {Fore.WHITE}(boost or classic){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

if "boost" in nitro or "classic" in nitro:
    pass
else:
    print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}or {Fore.WHITE}classic")
    exit()


checker = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Enable Checker {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        proxy = 'https://' + proxy
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")

if checker == "yes":
    scrapep = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If no, every check will be on random proxy.")
    mult = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Multiple checks for proxy {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    if scrapep == "yes":
        scrape()
else:
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If true, before code will be {Fore.WHITE}discord.gift/")
    prefix = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Prefix before codes {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    if "yes" in prefix or "no" in prefix:
        pass
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
        exit()


print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generating {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} codes!")
if checker != "yes":
    sleep(1)

fulla = amount
f = open("codes.txt", "w+", encoding="UTF-8")



def readproxies():
    try:
        p = open("proxies.txt", encoding="UTF-8")
    except FileNotFoundError:
        p = open("proxies.txt", "w+", encoding="UTF-8")
        print(f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
        raise SystemExit



    rproxy = p.read().split('\n')
    for i in rproxy:
        if i == "" or i == " ":
            index = rproxy.index(i)
            del rproxy[index]
    p.close()
    
    return rproxy
    
    
rproxy=readproxies()


if not rproxy:
        print(f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
        raise SystemExit


if checker != "yes":
    while amount > 0:
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        if prefix == "yes":
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
            f.write(f"discord.gift/{code}\n")
        else:
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
            f.write(f"{code}\n")

else:
    while amount > 0:
        f = open(f"working-codes.txt","a", encoding="UTF-8")
        try:
            if not rproxy[0]:
                print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid{Fore.WHITE}")
                
                #Here, when all the proxies are invalid, if the users choosed to auto-scrape proxy, the program is scraping new proxies.
                if scrapep == "yes":
                    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Rescraping Proxies...{Fore.WHITE}")
                    scrape()
                    rproxy=readproxies()
                else:
                    exit()

        except:
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid{Fore.WHITE}")
            if scrapep == "yes":
                print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Rescraping Proxies...{Fore.WHITE}")
                scrape()
                rproxy=readproxies()
            else:
                exit()
        if mult == "yes":
            proxi = rproxy[0]
        else:
            proxi = random.choice(rproxy)
        proxies = {
            "https": proxi
        }
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        try:
            url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", proxies=proxies, timeout=3)
            if url.status_code == 200:
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Working Code {Fore.WHITE}{code}{Fore.WHITE}")
                f.write(f"\ndiscord.gift/{code}")
                f.close()
            elif url.status_code == 404:
                fulla = fulla - 1
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Code {Fore.WHITE}{code}")
            elif url.status_code == 429:
                fulla = fulla - 1
                if mult == "yes":
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited! | Switching proxy")
                else:
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited!")
                index = rproxy.index(proxi)
                del rproxy[index]
            else:
                fulla = fulla - 1
                print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.WHITE}{url.status_code}")
        except:
            index = rproxy.index(proxi)
            del rproxy[index]
            pw = open(f"proxies.txt","w", encoding="UTF-8")
            for i in rproxy:
                pw.write(i + "\n")
            pw.close()
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!")

f.close()
print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Successfully generated {Fore.WHITE}{fulla} {Fore.LIGHTBLACK_EX}codes!{Fore.WHITE}")

input() 
