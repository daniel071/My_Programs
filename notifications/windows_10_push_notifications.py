from win10toast import ToastNotifier
import time

toaster = ToastNotifier()


def notify(title, message):
    toaster.show_toast(title,
                       message,
                       icon_path=None,
                       duration=5,
                       threaded=True)

    # Wait for threaded notification to finish
    while toaster.notification_active():
        time.sleep(0.1)



print("0")
notify("Hoi", "lol")
print("1")
notify("Hoi", "lol")
print("2")
