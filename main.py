import psutil
import time
import pygetwindow 
import pyautogui

browsers  = {
    'chrome.exe':'Google Chrome',
    'firefox.exe':'Firefox',
    'msedge.exe':'Edge',
}

blocked_sites = [
    'Facebook', 'YouTube', 'Twitter', 'Instagram', 'Reddit', 'TikTok', 'Snapchat', 'Discord', 'X'
]

def main():
    while True:
        try:
            time.sleep(2)
            processes_running = psutil.process_iter()
            for processes in processes_running:
                process_name = processes.name().lower()
                if process_name in browsers.keys():
                    print(browsers[process_name])
                    windows = pygetwindow.getWindowsWithTitle(browsers[process_name])
                    print(windows)
                    for window in windows:
                        window_title = window.title.lower()
                        print(window_title)
                        for site in blocked_sites:
                            if site.lower() in window_title:
                                print(f'Blocking {site}')
                                print('Don\'t get distracted!')
                                try:
                                    window.maximize()
                                    time.sleep(1)
                                    window.activate()
                                    time.sleep(1)
                                    pyautogui.click(window.center)
                                except:
                                    pass
                                if window.isMaximized:
                                    time.sleep(1)
                                    pyautogui.hotkey('ctrl', 'w')
                                    time.sleep(2)
                                break
        except KeyboardInterrupt:
            break
        except Exception as e:
            pass

if __name__ == '__main__':
    main()