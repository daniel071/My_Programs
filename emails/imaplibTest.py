def cb(cb_arg_list):
    response, cb_arg, error = cb_arg_list
    typ, data = response
    if not data:
        return
    for field in data:
        if type(field) is not tuple:
            continue
        print('Message %s:\n%s\n'
              % (field[0].split()[0], field[1]))


import imaplib2


M = imaplib2.IMAP4()
M.LOGIN(input("input login"), input("input pass"))
M.SELECT(readonly=True)
typ, data = M.SEARCH(None, 'ALL')
for num in data[0].split():
    M.FETCH(num, '(RFC822)', callback=cb)
M.CLOSE()
M.LOGOUT()