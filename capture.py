import time
import win32gui, win32ui, win32con, win32api
def window_capture(filename):
  hwnd=0
  hwndDC = win32gui.GetWindowDC(hwnd)
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  saveDC = mfcDC.CreateCompatibleDC()
  saveBitMap = win32ui.CreateBitmap()
  MoniterDev = win32api.EnumDisplayMonitors(None, None)
  w = MoniterDev[0][2][2]
  h = MoniterDev[0][2][3]
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  saveDC.SelectObject(saveBitMap)
  saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
  saveBitMap.SaveBitmapFile(saveDC, filename)
beg = time.time()
for i in range(10):
  window_capture("haha" + str(i) +".jpg")
end = time.time()
print(end - beg)