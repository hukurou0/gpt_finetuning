import sys
import funcs


options = {'-m': True,'-train': True, '-val': False, '-model': False}
args = {'m': 'f', 'train': '', 'val': '', 'model':'gpt-3.5-turbo-instruct'}  # デフォルト値

for key in options.keys():
    if key in sys.argv:
        idx = sys.argv.index(key)
        if options[key]:
            value = sys.argv[idx+1]
            if value.startswith('-'):
                raise ValueError(f'option {key} must have a value.')
            args[key[1:]] = value
            del sys.argv[idx:idx+2]
        else:
            args[key[1:]] = True
            del sys.argv[idx]

#モードによる動作制御
if args['m'] == 'help':
      with open('help.txt', encoding='utf-8') as f:
            print()
            print(f.read())
elif args['m'] == 'history':
      with open('history.txt', encoding='utf-8') as f:
            print()
            print(f.read())
elif args['m'] == 'up':
      if args['train']:
            funcs.upload_file_train(args['train'])
      if args['val']:
            funcs.upload_file_val(args['val'])
elif args['m'] == 'fine':
      if args['val']:
            funcs.fine_train_val(args['train'],args['val'])
      else:
            funcs.fine_train(args['train'])
elif args['m'] == 'up-fine':
      pass