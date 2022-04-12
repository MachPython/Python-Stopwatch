import time
print('t̾h̾i̾s̾ ̾i̾s̾ ̾y̾o̾u̾r̾ ̾o̾w̾n̾ ̾p̾y̾t̾h̾o̾n̾ ̾s̾t̾o̾p̾w̾a̾t̾c̾h̾ ̾f̾o̾r̾ ̾t̾h̾e̾ ̾p̾e̾o̾p̾l̾e̾ ̾t̾h̾a̾t̾ ̾a̾r̾e̾ ̾a̾b̾o̾v̾e̾ ̾g̾o̾o̾g̾l̾e̾')
time.sleep(2)
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("𝕡𝕣𝕖𝕤𝕤 𝕖𝕟𝕥𝕖𝕣 𝕥𝕠 𝕤𝕥𝕒𝕣𝕥 𝕤𝕥𝕠𝕡𝕨𝕒𝕥𝕔𝕙")
start_time = time.time()
input("𝕡𝕣𝕖𝕤𝕤 𝕖𝕟𝕥𝕖𝕣 𝕥𝕠 𝕤𝕥𝕠𝕡 𝕤𝕥𝕠𝕡𝕨𝕒𝕥𝕔𝕙")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)