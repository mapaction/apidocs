import csv
import io
import urllib.request
import os

# url = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vQxcNd7W2VNzZFZdub1nVg8EKQowrkrUg97tzEpFr3iNqwHnUpF-TjWFyiwdU4d3ntfIKjNyrsCdhMn/pub?gid=1446133716&single=true&output=csv'
url = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vQxcNd7W2VNzZFZdub1nVg8EKQowrkrUg97tzEpFr3iNqwHnUpF-TjWFyiwdU4d3ntfIKjNyrsCdhMn/pub?gid=454102953&single=true&output=csv'

def format_field_entry(row):
    str_list = []
    
    # Field-name
    # str_list.append('=========================================================================')
    str_list.append('\n\n{0}\n'.format(row[1]))
    str_list.append('-------------------------------------------------------------------------\n\n')
   
    
    # Data-type
    str_list.append('  :Data type: {0}\n'.format(no_paras(row[5])))

    # Description
    str_list.append('  :Description: {0}\n'.format(no_paras(row[6])))

    # Controlled-by
    str_list.append('  :Validation: {0}\n'.format(no_paras(row[8])))

    # Example
    str_list.append('  :Example: {0}\n'.format(format_example_value(row[9])))

    # Changed
    # Comments-on-changes
    
    return ''.join(str_list)

    
def filter_name_space(row):
    if row[0] in ['dataset','ext_versions']:
        return format_field_entry(row)
    else:
        return ""
    
def no_paras(s):
    return s.replace('\n', ' ').replace('\r', '')
    

def format_example_value(s):
    if len(s) < 1:
        return ''
    elif '\n' in s:
        return '\n\n  ::\n\n    {0}'.format(s.replace('\n', '\n    ').replace('\r', ''))
    else:
        return ' ``{0}``\n'.format(s)

    
if __name__ == "__main__":
    webpage = urllib.request.urlopen(url)
    datareader = csv.reader(io.TextIOWrapper(webpage))

    repo_root = os.path.realpath(os.path.dirname(__file__))
    output_path = os.path.join(repo_root, r'src', 'source', 'fields-reference.rst')
    skip_first_row = True
    
    with open(output_path, mode='w', encoding='utf-8') as f:
        f.write('.. title:: Field Reference\n\n')
        f.write('Field Reference\n')
        f.write('=========================================================================')
        #PermissionError: [Errno 13] Permission denied: 'D:\\work\\custom-software-group\\code\\github\\apidocs\\src\\source\\test-all-fields.rst'
         
        for row in datareader:
            if skip_first_row:
                skip_first_row = False
            else:
                f.write(filter_name_space(row))
