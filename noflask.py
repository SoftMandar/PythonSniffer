



class Flask:

    def __init__(self, name):
        self.name = name
        self.routes = {}

    def route(self, path, methods=None):
        
        def decorator(f):
            
            self.routes[path] = f

        return decorator


    def get_view(self, path):

        try:
            view = self.routes.get(path,)
            return view()
        except KeyError:
            print("No route defined")


app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index_page():

    return "Hello World"

print(app.get_view('/'))



