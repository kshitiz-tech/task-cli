import re

def error_message(command):
    return f'invalid-format for {command}'


def format_validator(command , arg):
  
    command_patterns = {
        'add' :r'[\'"]([^"\']+)[\'"]$',
        'update':r'[\'"]([^"\']+)[\'"]\s(\d)$',
        'delete':r'(\d)$',
        'mark-in-progress':r'(\d)$',
        'list': r'(\S+)$'
    }

    checker = re.match(command_patterns[command],arg)
    match command:


        case 'add':

            if checker:

                return True, checker.group(1)
            return False, error_message(command)
        
        case 'update':

            if checker:

                task, id = checker.group(1), int(checker.group(2))
                return True, task, id
            
            else:
                return False, error_message(command),id
            
        case 'delete' | 'mark-in-progress' | 'mark-todo' | 'mark-done':

            if checker:
                id = int(checker.group(0))
                return True, id
            
            else:
                return False, error_message(command)
        
        case 'list':

            if arg == '':
                return True, None
            
            else:
                
                if checker:
                    return True, checker.group(0)
                
                else:
                    return False, f"{error_message(command)} with status"  

if __name__ == '__main__':
    format_validator()