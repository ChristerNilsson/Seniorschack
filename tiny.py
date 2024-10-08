import os

from fasthtml.common import FastHTML, serve, A, H1, Table,Tr,Td

app = FastHTML()

@app.get("/{fname:path}")
def home(fname:str):
    print('fname',fname)
    # BASE = '.'
    full_path = fname # os.path.join(BASE, fname)
    print('full_path',full_path)
    path = full_path

    if os.path.exists(full_path):
        if os.path.isdir(full_path):
            items = os.listdir(full_path)
            links = []
            for item in items:
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    links.append(Tr(Td(A(item,href=item_path))))
                else:
                    links.append(Tr(Td(A(item,href=item_path))))

            print(len(links))
            return Table(*links)
        elif full_path.endswith('.html'):
            with open(full_path,'r',encoding='utf-8') as f: return f.read()

    return H1(fname)
serve()

