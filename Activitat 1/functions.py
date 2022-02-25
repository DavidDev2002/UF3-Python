def write_file(fname,text):
    f = open(fname, "w")
    f.write(text)
    f.close()

def file_add_st(fname, str):
  f = open(fname, "a+")
  f.write(str)
  f.close()
