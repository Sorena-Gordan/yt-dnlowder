import os
import time
try:
    from pytube import YouTube
    from colorama import Fore
except : 
    print(Fore.RED + " [!]  ERROR  "+ Fore.RED +"==> in your system , dont have a pakage !  ")
    os.system('pip install pytube')
    os.system('pip install colorama')
try:
    try:
        os.system('clear')
    except:
        os.system('cls')
    print(Fore.GREEN +
        """
    =====================================================
    
    ██╗██████╗░░░░███╗░░██╗░█████╗░███████╗░█████╗░███████╗
    ██║██╔══██╗░░░████╗░██║██╔══██╗██╔════╝██╔══██╗╚════██║
    ██║██████╔╝░░░██╔██╗██║██║░░██║█████╗░░██║░░██║░░███╔═╝
    ██║██╔══██╗░░░██║╚████║██║░░██║██╔══╝░░██║░░██║██╔══╝░░
    ██║██║░░██║██╗██║░╚███║╚█████╔╝██║░░░░░╚█████╔╝███████╗
    ╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░░╚════╝░╚══════╝

                    developer : Sorena Gordan
                    discord id : ✡ Sorena ᵍᵒʳᵈᵃᶰ#2939
    ======================================================
        """
    )
    print(Fore.YELLOW + " [*] Enter your youtube link")
    link = input("? "+Fore.LIGHTBLUE_EX +">")
    yt = YouTube(link)

    print(Fore.RED+"==========================================")
    print("Title: ",yt.title)
    print("views: ",yt.views)
    print("Length of video: ",yt.length)
    print(Fore.RED+"==========================================")
    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download()
    print("Download completed!!")
except Exception:
    try:
        os.system('clear')
    except:
        os.system('cls')
    print("[!] ERROR : in parametr input is in error")
    time.sleep(2)
    try:
        os.system('python3 main.py')
    except:
        os.system('python main.py')